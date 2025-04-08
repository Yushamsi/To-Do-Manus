# To-Do List Application Backend

This is the backend for a simple to-do list application built with Flask.

## Features

- RESTful API with the following endpoints:
  - GET /todos – retrieve all to-do items
  - POST /todos – add a new to-do item
  - PUT /todos/<id> – mark an item as complete or update it
  - DELETE /todos/<id> – delete a to-do item
- In-memory storage (no database required)
- CORS enabled for frontend communication

## Requirements

- Python 3.6+
- Flask
- flask-cors

## Setup Instructions

1. Install the required packages:
```
pip install flask flask-cors
```

2. Run the application:
```
python app.py
```

The backend will be available at http://localhost:5000
