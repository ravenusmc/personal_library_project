<template>
    <div class="no-books-container">
      <div class="icon">
        📚
      </div>
      <h2 class="message">Oops! No books found</h2>
      <p class="suggestion">Try searching with a different term or explore our categories.</p>
    </div>
  </template>
  
  <script>
  export default {
    name: "NoBooks",
  };
  </script>
  
  <style scoped>
  .no-books-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 2rem;
    text-align: center;
    border: 2px dashed #d3d3d3;
    border-radius: 10px;
    background-color: #f9f9f9;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    font-family: 'Arial', sans-serif;
    color: #555;
  }
  
  .icon {
    font-size: 3rem;
    margin-bottom: 1rem;
  }
  
  .message {
    font-size: 1.5rem;
    font-weight: bold;
    margin-bottom: 0.5rem;
    color: #333;
  }
  
  .suggestion {
    font-size: 1rem;
    color: #777;
  }
  </style>
  