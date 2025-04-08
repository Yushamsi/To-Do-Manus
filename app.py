"""
Flask Backend for To-Do List Application

This module implements a simple REST API for a to-do list application using Flask.
It provides endpoints to create, read, update, and delete to-do items.
Data is stored in-memory using a Python list.
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import uuid
import os

# Initialize Flask application
app = Flask(__name__)

# Enable CORS to allow frontend to communicate with backend
# This is necessary for the frontend to make requests to the backend
CORS(app)

# In-memory storage for to-do items
# Each item is a dictionary with id, title, and completed status
todos = []

@app.route('/todos', methods=['GET'])
def get_todos():
    """
    GET /todos endpoint
    
    Returns all to-do items from the in-memory storage.
    
    Returns:
        JSON: A list of all to-do items
    """
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_todo():
    """
    POST /todos endpoint
    
    Adds a new to-do item to the in-memory storage.
    
    Request body should contain:
        title (str): The title/description of the to-do item
    
    Returns:
        JSON: The newly created to-do item
    """
    # Get the request data
    data = request.get_json()
    
    # Validate that the request contains a title
    if not data or 'title' not in data:
        return jsonify({"error": "Title is required"}), 400
    
    # Create a new to-do item with a unique ID
    new_todo = {
        'id': str(uuid.uuid4()),  # Generate a unique ID
        'title': data['title'],
        'completed': False  # New items are not completed by default
    }
    
    # Add the new item to our in-memory storage
    todos.append(new_todo)
    
    # Return the newly created item
    return jsonify(new_todo), 201

@app.route('/todos/<id>', methods=['PUT'])
def update_todo(id):
    """
    PUT /todos/<id> endpoint
    
    Updates an existing to-do item by ID.
    Can update the title and/or completed status.
    
    Path parameters:
        id (str): The ID of the to-do item to update
    
    Request body may contain:
        title (str, optional): The new title
        completed (bool, optional): The new completed status
    
    Returns:
        JSON: The updated to-do item or an error message
    """
    # Get the request data
    data = request.get_json()
    
    # Find the to-do item with the given ID
    for todo in todos:
        if todo['id'] == id:
            # Update the title if provided
            if data and 'title' in data:
                todo['title'] = data['title']
            
            # Update the completed status if provided
            if data and 'completed' in data:
                todo['completed'] = data['completed']
            
            # Return the updated item
            return jsonify(todo)
    
    # If no item with the given ID was found, return an error
    return jsonify({"error": "Todo not found"}), 404

@app.route('/todos/<id>', methods=['DELETE'])
def delete_todo(id):
    """
    DELETE /todos/<id> endpoint
    
    Deletes a to-do item by ID.
    
    Path parameters:
        id (str): The ID of the to-do item to delete
    
    Returns:
        JSON: A success message or an error message
    """
    # Find the index of the to-do item with the given ID
    for index, todo in enumerate(todos):
        if todo['id'] == id:
            # Remove the item from our in-memory storage
            del todos[index]
            # Return a success message
            return jsonify({"message": "Todo deleted successfully"})
    
    # If no item with the given ID was found, return an error
    return jsonify({"error": "Todo not found"}), 404

# Add some sample to-do items for testing
def add_sample_todos():
    """
    Adds some sample to-do items to the in-memory storage for testing purposes.
    """
    sample_todos = [
        {
            'id': str(uuid.uuid4()),
            'title': 'Learn Flask',
            'completed': True
        },
        {
            'id': str(uuid.uuid4()),
            'title': 'Build a to-do app',
            'completed': False
        },
        {
            'id': str(uuid.uuid4()),
            'title': 'Learn Nuxt.js',
            'completed': False
        }
    ]
    todos.extend(sample_todos)

# Add sample to-do items when the application starts
add_sample_todos()

if __name__ == '__main__':
    """
    Run the Flask application when this script is executed directly.
    
    The application will run on the port specified by the PORT environment variable,
    or on port 5000 by default.
    """
    port = int(os.environ.get("PORT", 5000))
    print(f"Starting Flask backend for To-Do List application on port {port}...")
    app.run(host='0.0.0.0', port=port)
