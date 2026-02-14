

from flask import Flask, render_template, request, redirect, send_from_directory, session, flash
import os
import sqlite3
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import pandas as pd
from flask import jsonify
from chat import get_chat_response



app = Flask(__name__)
app.secret_key = "super_secret_key_change_this"

# -----------------------
# CONFIG
# -----------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "recipes.db")
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)





def import_dataset(csv_path):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    df = pd.read_csv(csv_path)

    for _, row in df.iterrows():
        c.execute('''
            INSERT INTO dataset_recipes (
                title, description, number_of_steps, directions,
                ingredients, cuisine, tastes, cook_speed,
                est_cook_time, difficulty, dietary_profile,
                healthnum, health_flags, health_level
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            row['recipe_title'],
            row['description'],
            row['num_steps'],
            row['combined_text'],
            row['ingredients_raw'],
            row['cuisine_list'],
            row['tastes'],
            row['cook_speed'],
            row['est_cook_time_min'],
            row['difficulty'],
            row['dietary_profile'],
            row['healthiness_score'],
            row['health_flags'],
            row['health_level']
        ))

    conn.commit()
    conn.close()
    print("Dataset Imported Successfully!")







# -----------------------
# DATABASE INIT
# -----------------------
def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # USERS TABLE
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    # RECIPES TABLE (UNCHANGED)
    c.execute('''
        CREATE TABLE IF NOT EXISTS recipes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            title TEXT,
            description TEXT,
            ingredients TEXT,
            directions TEXT,
            number_of_steps INTEGER,
            cuisine TEXT,
            tastes TEXT,
            cook_speed TEXT,
            est_cook_time TEXT,
            difficulty TEXT,
            dietary_profile TEXT,
            healthnum INTEGER,
            health_flags TEXT,
            health_level TEXT,
            image_filename TEXT
        )
    ''')
    
    #new-recipie-dataset
    # DATASET RECIPES TABLE
    c.execute('''
        CREATE TABLE IF NOT EXISTS dataset_recipes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        description TEXT,
        number_of_steps INTEGER,
        directions TEXT,
        ingredients TEXT,
        cuisine TEXT,
        tastes TEXT,
        cook_speed TEXT,
        est_cook_time TEXT,
        difficulty TEXT,
        dietary_profile TEXT,
        healthnum INTEGER,
        health_flags TEXT,
        health_level TEXT
       )
    ''')


    conn.commit()
    conn.close()
    print("Database initialized.")


# -----------------------
# REGISTER
# -----------------------
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        full_name = request.form.get('full_name')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        if password != confirm_password:
            flash("Passwords do not match.")
            return redirect('/register')

        hashed_password = generate_password_hash(password)

        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()

        try:
            c.execute('''
                INSERT INTO users (full_name, email, password)
                VALUES (?, ?, ?)
            ''', (full_name, email, hashed_password))
            conn.commit()
        except sqlite3.IntegrityError:
            flash("Email already exists.")
            conn.close()
            return redirect('/register')

        conn.close()
        return redirect('/login')

    return render_template('register.html')


# -----------------------
# LOGIN
# -----------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE email=?", (email,))
        user = c.fetchone()
        conn.close()

        if user and check_password_hash(user[3], password):
            session['user_id'] = user[0]
            session['user_name'] = user[1]
            return redirect('/')
        else:
            flash("Invalid email or password.")
            return redirect('/login')

    return render_template('login.html')


# -----------------------
# LOGOUT
# -----------------------
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')


# -----------------------
# HOME ROUTE (PRIVATE RECIPES)
# -----------------------
@app.route("/", methods=["GET"])
def home():
    search = request.args.get("search", "")
    page = int(request.args.get("page", 1))
    limit = 10
    offset = (page - 1) * limit

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    recipes = []
    has_next = False

    if search:
        # fetch 1 extra to check if next page exists
        c.execute("""
            SELECT id, title, cuisine, difficulty
            FROM dataset_recipes
            WHERE title LIKE ?
            LIMIT ? OFFSET ?
        """, (f"%{search}%", limit + 1, offset))

        rows = c.fetchall()

        if len(rows) > limit:
            has_next = True
            recipes = rows[:limit]
        else:
            recipes = rows

    conn.close()

    return render_template(
        "home.html",
        recipes=recipes,
        search=search,
        page=page,
        has_next=has_next
    )





@app.route('/recipe/<int:recipe_id>')
def recipe_detail(recipe_id):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    # First: try dataset recipes
    c.execute("SELECT * FROM dataset_recipes WHERE id=?", (recipe_id,))
    recipe = c.fetchone()

    # If not found, try user's own recipes
    if recipe is None:
        c.execute("SELECT * FROM recipes WHERE id=?", (recipe_id,))
        recipe = c.fetchone()

    conn.close()

    if recipe is None:
        return "Recipe not found", 404

    return render_template("recipe_detail.html", recipe=recipe)










# -----------------------
# ADD RECIPE
# -----------------------
@app.route('/add', methods=['GET', 'POST'])
def add_recipe():
    if 'user_id' not in session:
        return redirect('/login')

    if request.method == 'POST':

        form = request.form
        image = request.files.get('image')
        image_filename = None

        if image and image.filename:
            filename = str(uuid.uuid4()) + "_" + secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            image_filename = filename

        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()

        c.execute('''
            INSERT INTO recipes (
                user_id, title, description, ingredients, directions,
                number_of_steps, cuisine, tastes, cook_speed,
                est_cook_time, difficulty, dietary_profile,
                healthnum, health_flags, health_level, image_filename
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            session['user_id'],
            form.get('title'),
            form.get('description'),
            form.get('ingredients'),
            form.get('directions'),
            form.get('number_of_steps'),
            form.get('cuisine'),
            form.get('tastes'),
            form.get('cook_speed'),
            form.get('est_cook_time'),
            form.get('difficulty'),
            form.get('dietary_profile'),
            form.get('healthnum'),
            form.get('health_flags'),
            form.get('health_level'),
            image_filename
        ))

        conn.commit()
        conn.close()

        return redirect('/my-recipes')

    return render_template('add_recipe.html')





# -----------------------
# EDIT RECIPE
# -----------------------
@app.route('/edit/<int:recipe_id>', methods=['GET', 'POST'])
def edit_recipe(recipe_id):
    if 'user_id' not in session:
        return redirect('/login')

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    if request.method == 'POST':

        form = request.form
        image = request.files.get('image')

        if image and image.filename:
            filename = str(uuid.uuid4()) + "_" + secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            c.execute("""
                UPDATE recipes
                SET title=?, description=?, ingredients=?, directions=?,
                    number_of_steps=?, cuisine=?, tastes=?, cook_speed=?,
                    est_cook_time=?, difficulty=?, dietary_profile=?,
                    healthnum=?, health_flags=?, health_level=?, image_filename=?
                WHERE id=? AND user_id=?
            """, (
                form.get('title'),
                form.get('description'),
                form.get('ingredients'),
                form.get('directions'),
                form.get('number_of_steps'),
                form.get('cuisine'),
                form.get('tastes'),
                form.get('cook_speed'),
                form.get('est_cook_time'),
                form.get('difficulty'),
                form.get('dietary_profile'),
                form.get('healthnum'),
                form.get('health_flags'),
                form.get('health_level'),
                filename,
                recipe_id,
                session['user_id']
            ))
        else:
            c.execute("""
                UPDATE recipes
                SET title=?, description=?, ingredients=?, directions=?,
                    number_of_steps=?, cuisine=?, tastes=?, cook_speed=?,
                    est_cook_time=?, difficulty=?, dietary_profile=?,
                    healthnum=?, health_flags=?, health_level=?
                WHERE id=? AND user_id=?
            """, (
                form.get('title'),
                form.get('description'),
                form.get('ingredients'),
                form.get('directions'),
                form.get('number_of_steps'),
                form.get('cuisine'),
                form.get('tastes'),
                form.get('cook_speed'),
                form.get('est_cook_time'),
                form.get('difficulty'),
                form.get('dietary_profile'),
                form.get('healthnum'),
                form.get('health_flags'),
                form.get('health_level'),
                recipe_id,
                session['user_id']
            ))

        conn.commit()
        conn.close()
        return redirect('/my-recipes')

    c.execute("SELECT * FROM recipes WHERE id=? AND user_id=?", (recipe_id, session['user_id']))
    recipe = c.fetchone()
    conn.close()

    return render_template('edit_recipe.html', recipe=recipe)


# -----------------------
# DELETE RECIPE
# -----------------------
@app.route('/delete/<int:recipe_id>', methods=['POST'])
def delete_recipe(recipe_id):
    if 'user_id' not in session:
        return redirect('/login')

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("SELECT image_filename FROM recipes WHERE id=? AND user_id=?",
              (recipe_id, session['user_id']))
    image = c.fetchone()

    if image and image[0]:
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], image[0])
        if os.path.exists(image_path):
            os.remove(image_path)

    c.execute("DELETE FROM recipes WHERE id=? AND user_id=?",
              (recipe_id, session['user_id']))

    conn.commit()
    conn.close()

    return redirect('/my-recipes')


#search bar index route
@app.route("/my-recipes", methods=["GET"])
def my_recipes():
    search = request.args.get("search", "")
    user_id = session["user_id"]

    conn = sqlite3.connect("recipes.db")
    cursor = conn.cursor()

    if search:
        cursor.execute("""
            SELECT * FROM recipes
            WHERE user_id = ?
              AND title LIKE ?
        """, (user_id, f"%{search}%"))
    else:
        cursor.execute("""
            SELECT * FROM recipes
            WHERE user_id = ?
        """, (user_id,))

    recipes = cursor.fetchall()
    conn.close()

    return render_template("index.html", recipes=recipes)


# -----------------------
# SERVE UPLOADED IMAGES
# -----------------------
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


# -----------------------
# CHATBOT API
# -----------------------
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message")

    bot_response = get_chat_response(user_message)

    return jsonify({"response": bot_response})

# -----------------------
# CHAT PAGE
# -----------------------
@app.route("/ask-ai")
def ask_ai():
    if 'user_id' not in session:
        return redirect('/login')
    return render_template("chat.html")




# -----------------------
# RUN
# -----------------------
if __name__ == '__main__':
    init_db()
    import_dataset("recipes_dataset.csv")
    app.run(debug=True)

