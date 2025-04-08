<!--
  AddTodo.vue - Component for adding a new to-do item
  
  This component provides a form for users to add new to-do items.
  It includes an input field and a submit button.
-->
<script setup>
import { ref } from 'vue';

// Define emits that this component can trigger
const emit = defineEmits(['add-todo']);

// Reactive reference for the new todo title
const newTodoTitle = ref('');

// Function to handle form submission
const addTodo = () => {
  // Validate that the title is not empty
  if (newTodoTitle.value.trim()) {
    // Emit the add-todo event with the new title
    emit('add-todo', newTodoTitle.value);
    // Clear the input field after submission
    newTodoTitle.value = '';
  }
};
</script>

<template>
  <div class="mb-6">
    <h2 class="text-xl font-bold mb-3">Add New Task</h2>
    
    <!-- Form for adding new todos -->
    <form @submit.prevent="addTodo" class="flex gap-2">
      <!-- Input field for the new todo title -->
      <input
        v-model="newTodoTitle"
        type="text"
        placeholder="Enter a new task..."
        class="input flex-grow"
        required
      />
      
      <!-- Submit button -->
      <button 
        type="submit" 
        class="btn btn-primary"
        :disabled="!newTodoTitle.trim()"
      >
        Add Task
      </button>
    </form>
  </div>
</template>
