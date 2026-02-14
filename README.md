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


Added recipes 

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

[Add more endpoints as needed...]

---

### For Mobile Apps:

#### App Flow Diagram

![App Flow](docs/app-flow.png)
*Explain the user flow through your application*

#### Installation Guide

**For Android (APK):**
1. Download the APK from [Release Link]
2. Enable "Install from Unknown Sources" in your device settings:
   - Go to Settings > Security
   - Enable "Unknown Sources"
3. Open the downloaded APK file
4. Follow the installation prompts
5. Open the app and enjoy!

**For iOS (IPA) - TestFlight:**
1. Download TestFlight from the App Store
2. Open this TestFlight link: [Your TestFlight Link]
3. Click "Install" or "Accept"
4. Wait for the app to install
5. Open the app from your home screen

**Building from Source:**
```bash
# For Android
flutter build apk
# or
./gradlew assembleDebug

# For iOS
flutter build ios
# or
xcodebuild -workspace App.xcworkspace -scheme App -configuration Debug
```

---

### For Hardware Projects:

#### Bill of Materials (BOM)

| Component | Quantity | Specifications | Price | Link/Source |
|-----------|----------|----------------|-------|-------------|
| Arduino Uno | 1 | ATmega328P, 16MHz | ₹450 | [Link] |
| LED | 5 | Red, 5mm, 20mA | ₹5 each | [Link] |
| Resistor | 5 | 220Ω, 1/4W | ₹1 each | [Link] |
| Breadboard | 1 | 830 points | ₹100 | [Link] |
| Jumper Wires | 20 | Male-to-Male | ₹50 | [Link] |
| [Add more...] | | | | |

**Total Estimated Cost:** ₹[Amount]

#### Assembly Instructions

**Step 1: Prepare Components**
1. Gather all components listed in the BOM
2. Check component specifications
3. Prepare your workspace
![Step 1](images/assembly-step1.jpg)
*Caption: All components laid out*

**Step 2: Build the Power Supply**
1. Connect the power rails on the breadboard
2. Connect Arduino 5V to breadboard positive rail
3. Connect Arduino GND to breadboard negative rail
![Step 2](images/assembly-step2.jpg)
*Caption: Power connections completed*

**Step 3: Add Components**
1. Place LEDs on breadboard
2. Connect resistors in series with LEDs
3. Connect LED cathodes to GND
4. Connect LED anodes to Arduino digital pins (2-6)
![Step 3](images/assembly-step3.jpg)
*Caption: LED circuit assembled*

**Step 4: [Continue for all steps...]**

**Final Assembly:**
![Final Build](images/final-build.jpg)
*Caption: Completed project ready for testing*

---

### For Scripts/CLI Tools:

#### Command Reference

**Basic Usage:**
```bash
python script.py [options] [arguments]
```

**Available Commands:**
- `command1 [args]` - Description of what command1 does
- `command2 [args]` - Description of what command2 does
- `command3 [args]` - Description of what command3 does

**Options:**
- `-h, --help` - Show help message and exit
- `-v, --verbose` - Enable verbose output
- `-o, --output FILE` - Specify output file path
- `-c, --config FILE` - Specify configuration file
- `--version` - Show version information

**Examples:**

```bash
# Example 1: Basic usage
python script.py input.txt

# Example 2: With verbose output
python script.py -v input.txt

# Example 3: Specify output file
python script.py -o output.txt input.txt

# Example 4: Using configuration
python script.py -c config.json --verbose input.txt
```

#### Demo Output

**Example 1: Basic Processing**

**Input:**
```
This is a sample input file
with multiple lines of text
for demonstration purposes
```

**Command:**
```bash
python script.py sample.txt
```

**Output:**
```
Processing: sample.txt
Lines processed: 3
Characters counted: 86
Status: Success
Output saved to: output.txt
```

**Example 2: Advanced Usage**

**Input:**
```json
{
  "name": "test",
  "value": 123
}
```

**Command:**
```bash
python script.py -v --format json data.json
```

**Output:**
```
[VERBOSE] Loading configuration...
[VERBOSE] Parsing JSON input...
[VERBOSE] Processing data...
{
  "status": "success",
  "processed": true,
  "result": {
    "name": "test",
    "value": 123,
    "timestamp": "2024-02-07T10:30:00"
  }
}
[VERBOSE] Operation completed in 0.23s
```

---

## Project Demo

### Video
[Add your demo video link here - YouTube, Google Drive, etc.]

*Explain what the video demonstrates - key features, user flow, technical highlights*

### Additional Demos
[Add any extra demo materials/links - Live site, APK download, online demo, etc.]

---

## AI Tools Used (Optional - For Transparency Bonus)

If you used AI tools during development, document them here for transparency:

**Tool Used:** [e.g., GitHub Copilot, v0.dev, Cursor, ChatGPT, Claude]

**Purpose:** [What you used it for]
- Example: "Generated boilerplate React components"
- Example: "Debugging assistance for async functions"
- Example: "Code review and optimization suggestions"

**Key Prompts Used:**
- "Create a REST API endpoint for user authentication"
- "Debug this async function that's causing race conditions"
- "Optimize this database query for better performance"

**Percentage of AI-generated code:** [Approximately X%]

**Human Contributions:**
- Architecture design and planning
- Custom business logic implementation
- Integration and testing
- UI/UX design decisions

*Note: Proper documentation of AI usage demonstrates transparency and earns bonus points in evaluation!*

---

## Team Contributions

- [Name 1]: [Specific contributions - e.g., Frontend development, API integration, etc.]
- [Name 2]: [Specific contributions - e.g., Backend development, Database design, etc.]
- [Name 3]: [Specific contributions - e.g., UI/UX design, Testing, Documentation, etc.]

---

## License

This project is licensed under the [LICENSE_NAME] License - see the [LICENSE](LICENSE) file for details.

**Common License Options:**
- MIT License (Permissive, widely used)
- Apache 2.0 (Permissive with patent grant)
- GPL v3 (Copyleft, requires derivative works to be open source)

---

Made with ❤️ at TinkerHub
