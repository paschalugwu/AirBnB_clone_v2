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
4. [AirBnB Clone Deployment](#airbnb-clone-deployment)
5. [Contributing](#contributing)
6. [License](#license)

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

## AirBnB Clone Deployment

This repository contains scripts and configurations for deploying the AirBnB Clone project. Below you'll find information about the project, its requirements, and how to use the provided scripts.

### Project Overview

This project focuses on deploying the AirBnB Clone project using Fabric for Python3. The deployment involves setting up web servers, compressing files, distributing archives, and managing Nginx configurations.

#### Concepts

- Continuous Integration/Continuous Deployment (CI/CD)
- AirBnB clone
- Fabric for Python3
- Nginx configuration

### Background Context

In this deployment project, you will deploy your web_static work using Fabric, a Python library for streamlining SSH usage for deployment tasks. This involves setting up Nginx, creating necessary directories, and configuring Nginx to serve the content properly.

### Requirements

- Python Scripts
  - PEP 8 style
  - Fabric3 version 1.14.post1
  - Executable files with proper shebang
  - Documentation for all functions and classes
- Bash Scripts
  - Pass Shellcheck without errors
  - Executable files with proper shebang
  - Documentation for scripts

### Installation

To install Fabric for Python 3, follow these steps:

```bash
$ pip3 uninstall Fabric
$ sudo apt-get install libffi-dev
$ sudo apt-get install libssl-dev
$ sudo apt-get install build-essential
$ sudo apt-get install python3.4-dev
$ sudo apt-get install libpython3-dev
$ pip3 install pyparsing
$ pip3 install appdirs
$ pip3 install setuptools==40.1.0
$ pip3 install cryptography==2.8
$ pip3 install bcrypt==3.1.7
$ pip3 install PyNaCl==1.3.0
$ pip3 install Fabric3==1.14.post1
```

### Usage

#### 0. Prepare your web servers

Run the provided Bash script to set up your web servers for the deployment of web_static:

```bash
$ sudo ./0-setup_web_static.sh
```

#### 1. Compress before sending

Generate a .tgz archive from the contents of the web_static folder of your AirBnB Clone repo using the provided Fabric script:

```bash
$ fab -f 1-pack_web_static.py do_pack
```

#### 2. Deploy archive!

Distribute the archive to your web servers using the provided Fabric script:

```bash
$ fab -f 2-do_deploy_web_static.py do_deploy:archive_path=<archive_path>
```

#### 3. Full deployment

Create and distribute an archive to your web servers using the provided Fabric script:

```bash
$ fab -f 3-deploy_web_static.py deploy
```

#### 4. Keep it clean!

Delete out-of-date archives using the provided Fabric script:

```bash
$ fab -f 100-clean_web_static.py do_clean:number=<number>
```

#### 5. Puppet for setup

Redo the setup task using Puppet:

```bash
$ puppet apply 101-setup_web_static.pp
```

## Contributing



Contributions are welcome! Feel free to open issues or submit pull requests to help improve this project.

## License

This project is licensed under the [MIT License](LICENSE).
