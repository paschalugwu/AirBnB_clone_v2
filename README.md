# AirBnB Clone Project

This project aims to create a clone of the popular accommodation rental platform Airbnb. The project is implemented using Python and SQLAlchemy for managing the database, and it includes various tasks to develop different features and functionalities.

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Tasks](#tasks)
   - [Task 0: Set up Environment](#task-0-set-up-environment)
   - [Task 1: Create BaseModel](#task-1-create-base-model)
   - [Task 2: Create User Model](#task-2-create-user-model)
   - [Task 3: Console Command Interpreter](#task-3-console-command-interpreter)
   - [Task 4: Create Place Model](#task-4-create-place-model)
   - [Task 5: Advanced Console Commands](#task-5-advanced-console-commands)
   - [Task 6: File Storage](#task-6-file-storage)
   - [Task 7: Database Storage - User](#task-7-database-storage-user)
   - [Task 8: Database Storage - Place](#task-8-database-storage-place)
   - [Task 9: Database Storage - Review](#task-9-database-storage-review)
   - [Task 10: Database Storage - Amenity](#task-10-database-storage-amenity)
4. [Contributing](#contributing)
5. [License](#license)

## Introduction

Airbnb Clone Project is a comprehensive endeavor to replicate the core functionalities of the Airbnb platform. It involves creating models for users, places, reviews, amenities, and implementing features like database storage, console command interpreter, and file storage. Each task builds upon the previous one, gradually enhancing the functionality and usability of the application.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```bash
   cd AirBnB_clone_v2
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```bash
   # For MySQL database
   sudo apt-get install mysql-server
   sudo mysql_secure_installation
   ```

5. Run the application:
   ```bash
   # For database storage
   HBNB_ENV=test HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
   ```

## Tasks

### Task 0: Set up Environment

- Set up the development environment with Python, SQLAlchemy, and Flask.

### Task 1: Create BaseModel

- Define a base model class with common attributes/methods for all other classes.

### Task 2: Create User Model

- Implement a User model with attributes like email, password, first name, and last name.

### Task 3: Console Command Interpreter

- Develop a command-line interpreter to interact with the application.

### Task 4: Create Place Model

- Create a Place model with various attributes representing rental properties.

### Task 5: Advanced Console Commands

- Enhance the console commands to support advanced functionalities.

### Task 6: File Storage

- Implement file storage to store application data.

### Task 7: Database Storage - User

- Set up database storage for the User model.

### Task 8: Database Storage - Place

- Configure database storage for the Place model with relationships to other models.

### Task 9: Database Storage - Review

- Implement database storage for the Review model with foreign key relationships.

### Task 10: Database Storage - Amenity

- Establish a many-to-many relationship between Place and Amenity models using a separate table.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to help improve this project.
