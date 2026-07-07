# Guess the Number Game - Flask Application

A fun and interactive Flask web application that implements a number guessing game. The application demonstrates Flask URL routing and dynamic content rendering.

## Project Overview

This is a simple game where the server randomly generates a number between 0 and 9, and users try to guess it. Based on their guess, they receive feedback (too high, too low, or correct) with playful animated GIFs.

## Features

- **Random Number Generation**: Server generates a random number between 0-9 on startup
- **URL-based Guessing**: Users guess by entering a number in the URL
- **Instant Feedback**: 
  - Correct guess: Victory page with celebratory GIF
  - Too high: Notification with playful "too high" GIF
  - Too low: Notification with playful "too low" GIF
- **Interactive UI**: HTML pages with embedded GIFs for better user experience

## Project Structure

```
Day 55 - Flask - Guess the number/
├── main.py                 # Flask application entry point
├── requirements.txt        # Project dependencies
├── README.md              # This file
├── templates/             # HTML templates
│   ├── home.html         # Welcome/home page
│   ├── winner.html       # Success page
│   ├── upper.html        # "Too high" feedback page
│   └── lower.html        # "Too low" feedback page
└── practice/             # Practice directory (optional)
```

## Requirements

- Python 3.x
- Flask 3.1.3
- Jinja2 (for template rendering)

See `requirements.txt` for full dependency list.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd "Day 55 - Flask - Guess the number"
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the Flask application:
   ```bash
   python main.py
   ```

2. Open your browser and navigate to:
   ```
   http://localhost:5000/
   ```

3. You'll see the welcome page with instructions

4. To make a guess, navigate to:
   ```
   http://localhost:5000/{number}
   ```
   Replace `{number}` with your guess (0-9)

5. The application will respond with:
   - **Winner page**: If your guess matches the secret number
   - **Too High**: If your guess is higher than the secret number
   - **Too Low**: If your guess is lower than the secret number

## Key Concepts Demonstrated

- **Flask Routing**: Using `@app.route()` decorator with URL parameters
- **URL Parsing**: Extracting and converting URL parameters using `<int:num>`
- **Template Rendering**: Using `render_template()` to serve HTML files
- **Dynamic Content**: Serving different responses based on user input

## Learning Outcome

This project is part of a 100 Days coding challenge and demonstrates fundamental Flask concepts including:
- Route definition and parameter passing
- Template rendering
- Basic conditional logic
- URL-based parameter handling

## Author

Created as part of the 100 Days Coding Challenge (Day 55)
