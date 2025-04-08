<!--
  TodoItem.vue - Component for displaying a single to-do item
  
  This component displays a single to-do item with its title and status.
  It provides buttons to mark the item as complete or delete it.
-->
<script setup>
// Define props that this component accepts
const props = defineProps({
  // The to-do item object containing id, title, and completed status
  todo: {
    type: Object,
    required: true
  }
});

// Define emits that this component can trigger
const emit = defineEmits(['toggle-complete', 'delete-todo']);

// Function to toggle the completed status of a to-do item
const toggleComplete = () => {
  emit('toggle-complete', props.todo);
};

// Function to delete a to-do item
const deleteTodo = () => {
  emit('delete-todo', props.todo.id);
};
</script>

<template>
  <!-- 
    The todo-item class is defined in tailwind.css
    We conditionally add the 'completed' class if the todo is marked as completed
  -->
  <div :class="['todo-item', { 'completed': todo.completed }]">
    <!-- Left side: Checkbox and todo text -->
    <div class="flex items-center gap-3">
      <!-- Checkbox for marking todo as complete -->
      <input 
        type="checkbox" 
        :checked="todo.completed" 
        @change="toggleComplete" 
        class="h-5 w-5 rounded border-gray-300 text-primary focus:ring-primary"
      />
      
      <!-- Todo text with conditional styling -->
      <span :class="['todo-text', { 'line-through text-gray-500': todo.completed }]">
        {{ todo.title }}
      </span>
    </div>
    
    <!-- Right side: Delete button -->
    <button 
      @click="deleteTodo" 
      class="btn btn-danger text-sm"
      aria-label="Delete todo"
    >
      Delete
    </button>
  </div>
</template>
