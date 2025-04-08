<!--
  index.vue - Main page component for the to-do list application
  
  This is the main page that brings together all components and handles
  the application logic, including API communication with the backend.
-->
<script setup>
import { ref, onMounted } from 'vue';
import AddTodo from '~/components/AddTodo.vue';
import TodoItem from '~/components/TodoItem.vue';

// Reactive references
const todos = ref([]);
const loading = ref(true);
const error = ref(null);

// API base URL from runtime config
const config = useRuntimeConfig();
const apiBaseUrl = config.public.apiBaseUrl;

// Fetch all todos from the API
const fetchTodos = async () => {
  loading.value = true;
  error.value = null;
  
  try {
    const response = await fetch(`${apiBaseUrl}/todos`);
    if (!response.ok) {
      throw new Error(`API error: ${response.status}`);
    }
    todos.value = await response.json();
  } catch (err) {
    console.error('Error fetching todos:', err);
    error.value = 'Failed to load tasks. Please try again later.';
  } finally {
    loading.value = false;
  }
};

// Add a new todo
const addTodo = async (title) => {
  loading.value = true;
  error.value = null;
  
  try {
    const response = await fetch(`${apiBaseUrl}/todos`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ title }),
    });
    
    if (!response.ok) {
      throw new Error(`API error: ${response.status}`);
    }
    
    const newTodo = await response.json();
    todos.value.push(newTodo);
  } catch (err) {
    console.error('Error adding todo:', err);
    error.value = 'Failed to add task. Please try again.';
  } finally {
    loading.value = false;
  }
};

// Toggle the completed status of a todo
const toggleComplete = async (todo) => {
  loading.value = true;
  error.value = null;
  
  try {
    const updatedTodo = { ...todo, completed: !todo.completed };
    
    const response = await fetch(`${apiBaseUrl}/todos/${todo.id}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(updatedTodo),
    });
    
    if (!response.ok) {
      throw new Error(`API error: ${response.status}`);
    }
    
    // Update the local state
    const index = todos.value.findIndex(t => t.id === todo.id);
    if (index !== -1) {
      todos.value[index] = await response.json();
    }
  } catch (err) {
    console.error('Error updating todo:', err);
    error.value = 'Failed to update task. Please try again.';
    // Revert the local change
    await fetchTodos();
  } finally {
    loading.value = false;
  }
};

// Delete a todo
const deleteTodo = async (id) => {
  loading.value = true;
  error.value = null;
  
  try {
    const response = await fetch(`${apiBaseUrl}/todos/${id}`, {
      method: 'DELETE',
    });
    
    if (!response.ok) {
      throw new Error(`API error: ${response.status}`);
    }
    
    // Remove the todo from the local state
    todos.value = todos.value.filter(todo => todo.id !== id);
  } catch (err) {
    console.error('Error deleting todo:', err);
    error.value = 'Failed to delete task. Please try again.';
  } finally {
    loading.value = false;
  }
};

// Fetch todos when the component is mounted
onMounted(fetchTodos);
</script>

<template>
  <div class="min-h-screen bg-gray-50 py-8">
    <div class="max-w-2xl mx-auto px-4 sm:px-6 lg:px-8">
      <!-- App Header -->
      <header class="mb-8 text-center">
        <h1 class="text-3xl font-bold text-primary mb-2">To-Do List App</h1>
        <p class="text-gray-600">A simple to-do list application built with Nuxt.js and Flask</p>
      </header>
      
      <!-- Main Content -->
      <main class="bg-white p-6 rounded-lg shadow-md">
        <!-- Add Todo Form -->
        <AddTodo @add-todo="addTodo" />
        
        <!-- Divider -->
        <div class="border-t border-gray-200 my-6"></div>
        
        <!-- Todo List Section -->
        <div>
          <h2 class="text-xl font-bold mb-4">Your Tasks</h2>
          
          <!-- Loading State -->
          <div v-if="loading" class="py-4 text-center text-gray-500">
            Loading tasks...
          </div>
          
          <!-- Error State -->
          <div v-else-if="error" class="py-4 text-center text-danger">
            {{ error }}
          </div>
          
          <!-- Empty State -->
          <div v-else-if="todos.length === 0" class="py-4 text-center text-gray-500">
            No tasks yet. Add one above!
          </div>
          
          <!-- Todo List -->
          <div v-else class="space-y-2">
            <TodoItem
              v-for="todo in todos"
              :key="todo.id"
              :todo="todo"
              @toggle-complete="toggleComplete"
              @delete-todo="deleteTodo"
            />
          </div>
        </div>
      </main>
      
      <!-- Footer -->
      <footer class="mt-8 text-center text-gray-500 text-sm">
        <p>Built with Nuxt.js, Tailwind CSS, and Flask</p>
      </footer>
    </div>
  </div>
</template>
