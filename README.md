<p align="center">
  <img src="./img.png" alt="Project Banner" width="100%">
</p>

# RBook 🎯

## Basic Details

### Team Name: Asrterix

### Team Members
- Member 1: Aleen Rose - Jyothi Engineering College
- Member 2: Agnes Joseph - Jyothi Engineering College

### Hosted Project Link
[mention your project hosted link here]

### Project Description
RBooK is a dual-purpose web platform designed to modernize the cooking experience. It functions as both a social recipe repository where users can document and share their own culinary creations, and an AI-powered kitchen assistant. By leveraging the Gemini 1.5 Flash API, the platform provides users with an interactive "Sous-Chef" that can generate recipes on the fly, suggest substitutions, and provide nutritional guidance.

### The Problem statement
Standard recipe websites are static. If a user wants to substitute an ingredient (e.g., "I don't have eggs, what can I use?") or adjust a recipe for a specific diet, they have to leave the site and search elsewhere. There is no centralized platform that combines community-driven content (user-added recipes) with real-time intelligent assistance.

### The Solution
Our platform turns the traditional recipe website into a personal kitchen assistant. By combining a community-driven collection with a smart chatbot, we allow users to share their own recipes and get instant, tailored cooking help. Instead of scrolling through endless search results, you can simply chat with the site to find meals based on what is in your fridge or get quick ideas for dietary swaps. It simplifies meal planning and reduces food waste by turning a basic search into an easy, helpful conversation, making cooking simple for everyone.

---

## Technical Details

### Technologies/Components Used

**For Software:**
- Languages used: Python,Html,css
- Frameworks used: Flask
- Libraries used: Pandas,
- Tools used: VS code,Figma,Git Hub

---

## Features

List the key features of your project:
- Feature 1: Community Recipe Hub – A dedicated space where users can upload, store, and share their own personal recipes, building a collective digital cookbook for everyone to enjoy.

- Feature 2: AI Sous-Chef Chatbot – An intelligent assistant that provides instant cooking advice, answers culinary questions, and offers helpful tips just like a professional chef.
  
- Feature 4: Interactive Substitutions & Scaling – A flexible system that lets users instantly find ingredient alternatives or adjust serving sizes to fit their specific dietary needs or guest list.

---

## Implementation

### For Software:

#### Installation
```bash
pip install -r requirements.txt
pip install google-generativeai python-dotenv flask
```

#### Run
```bash
python app.py
```



---

## Project Documentation

### For Software:

#### Screenshots (Add at least 3)
https://github.com/AleenCyriac/tink-her-hack-temp/blob/main/s1.jpeg
Front page of our website

https://github.com/AleenCyriac/tink-her-hack-temp/blob/main/s2.png
AI chat bot for asking recipes 

https://github.com/AleenCyriac/tink-her-hack-temp/blob/main/s3.jpeg
users can add their own recipes by form

https://github.com/AleenCyriac/tink-her-hack-temp/blob/main/s5.jpeg
seraching recipes 

https://github.com/AleenCyriac/tink-her-hack-temp/blob/main/s6.jpeg
showing recipes 

https://github.com/AleenCyriac/tink-her-hack-temp/blob/main/s7.jpeg
login/sign page

#### Diagrams

**System Architecture:**
![Architecture Flow](https://github.com/AleenCyriac/tink-her-hack-temp/blob/main/architure%20flow.png)

1.The Core Components (The Team)
The Frontend (The Waiter): This is your HTML. It’s the face of the website. It takes your order (ingredients) and shows you the final dish (the recipe).

The Backend (The Kitchen Manager): This is Flask (Python). It sits in the middle. It doesn't cook the food itself, but it takes the order from the waiter and sends it to the right place.

The AI Engine (The Master Chef): This is Gemini. It’s the "brain" that knows every recipe in the world. It takes the random ingredients you gave it and turns them into a professional cooking plan.

The Database (The Pantry): This is where you store recipes that users have created. If you want to see a friend's recipe instead of an AI one, the Kitchen Manager looks here.

2. Tech Stack Interaction (How they talk)
Even though these are different tools, they work as one team:

HTML sends a message to Python saying, "Hey, the user has chicken and rice."

Python looks at its secret Environment File (.env) to get the key to talk to the AI.

Gemini AI receives the message, "thinks" for a second, and sends back a perfectly written recipe.

Python catches that recipe and hands it back to the HTML to display on your screen.

3. Application Workflow (The Step-by-Step)
Caption: The workflow starts when a user types in their ingredients. The system passes this information to the AI "Chef," which instantly creates a custom recipe and sends it back to the user’s screen in an easy-to-read format.

---


## Additional Documentation

### For Web Projects with Backend:

#### API Documentation

**Base URL:** `https://api.yourproject.com`

##### Endpoints

**GET /api/endpoint**
- **Description:** [What it does]
- **Parameters:**
  - `param1` (string): [Description]
  - `param2` (integer): [Description]
- **Response:**
```json
{
  "status": "success",
  "data": {}
}
```

**POST /api/endpoint**
- **Description:** [What it does]
- **Request Body:**
```json
{
  "field1": "value1",
  "field2": "value2"
}
```
- **Response:**
```json
{
  "status": "success",
  "message": "Operation completed"
}
```



## Project Demo

### Video
https://drive.google.com/file/d/1AFaNDytA9gCGtj26NwBNnJGJDdJNHaq2/view?usp=drive_link



Made with ❤️ at TinkerHub
