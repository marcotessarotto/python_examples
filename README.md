# python_examples


## Web-Interactive Python Script with Flask and WebSockets

This project demonstrates how to run a Python script that interacts with the user over the web using Flask and WebSockets. The script collects 10 inputs from the user and then displays the total number of characters from all the inputs.

### Prerequisites

Ensure you have the following installed:

    Python 3
    Flask
    Flask-SocketIO
    Eventlet

You can install the required packages using:

pip install flask flask-socketio eventlet

### Project Structure

    app.py: This is the main Flask application file that sets up the WebSocket routes and handles the interaction with the Python script.
    user_input_collector.py: Contains the UserInputCollector class that manages the state of the Python script across WebSocket interactions.
    templates/index.html: The HTML frontend that allows users to input data and view the script's output.

### How It Works

    The user accesses the web page and is prompted to enter input.
    Each input is sent to the server via WebSockets.
    The server processes the input and either asks for the next input or, after 10 inputs, displays the total number of characters.
    The user sees real-time feedback on the web page without any page reloads.

### Running the Project

    Start the Flask application:

    python app.py

    Open a web browser and navigate to http://127.0.0.1:5000.

    Enter the requested inputs. After 10 entries, the total character count will be displayed.

