# Flask Web Application - AirBnB Clone

This repository contains a Flask web application for an AirBnB clone project. The application is built using Python and Flask, and it interfaces with a MySQL database to manage data related to states, cities, amenities, and places.

## Installation

To run the application, follow these steps:

1. Clone this repository to your local machine.
2. Make sure you have Python and Flask installed. If not, you can install Flask using pip:

```bash
pip install Flask
```

3. Set up a MySQL database for the application.
4. Make sure you have a valid `setup_mysql_dev.sql` script in your `AirBnB_clone_v2` repository. This script is used to set up the necessary tables in the database.
5. Run the `setup_mysql_dev.sql` script to create the required tables in the database.
6. Import the provided SQL dump files for each task to have sample data in your database.
7. Run the Flask application script corresponding to the task you want to test.

## Tasks Overview

### 0. Hello Flask!

- Simple Flask application that returns "Hello HBNB!" when accessed.

### 1. HBNB

- Improved Flask application with more routes and HTML responses.

### 2. C is fun!

- Displays "C is fun!" when accessed at `/c`.

### 3. Python is cool!

- Displays "Python is cool!" when accessed at `/python`.

### 4. Route that displays a number

- Displays a given integer when accessed at `/number/<n>`.

### 5. Route that displays a number with a default value

- Displays a default integer value when accessed at `/number`.

### 6. Odd or even?

- Displays whether a given integer is odd or even when accessed at `/number_odd_or_even/<n>`.

### 7. Improve engines

- Update the web application to support both file storage and database storage.

### 8. List of states

- Display a list of all State objects stored in the database.

### 9. States and State

- Display information about states and cities stored in the database.

### 10. HBNB filters

- Display a HTML page similar to the AirBnB clone project's index page with filtering options.

### 11. HBNB is alive!

- Display a HTML page similar to the AirBnB clone project's index page with additional features.

### 12. HBNB is alive!

- Enhanced version of the web application with more features and improved UI.

## Running the Application

To run the Flask application for a specific task, navigate to the `web_flask` directory and execute the corresponding Python script:

```bash
python3 -m <script_name>
```

Make sure to replace `<script_name>` with the name of the Python script for the task you want to run.

## Contributors

- Guillaume, Holberton School Student
- John, Holberton School Student

Feel free to contribute by opening issues or pull requests!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
