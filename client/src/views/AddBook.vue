<template>
    <div class="form-container">
      <form @submit.prevent="addBookToDatabase" class="form">
        <div class="form-group">
          <label for="title">Title</label>
          <input type="text" id="title" v-model="book.title" placeholder="Enter the book title" />
        </div>
        
        <div class="form-group">
          <label for="firstName">First Name</label>
          <input type="text" id="firstName" v-model="book.firstName" placeholder="Enter the author's first name" />
        </div>
        
        <div class="form-group">
          <label for="lastName">Last Name</label>
          <input type="text" id="lastName" v-model="book.lastName" placeholder="Enter the author's last name" />
        </div>
        
        <div class="form-group">
          <label for="lcClassifications">LC Classifications</label>
          <input type="text" id="lcClassifications" v-model="book.lcClassifications" placeholder="Enter LC classifications" />
        </div>
        
        <div class="form-group">
          <label for="publishDate">Publish Date</label>
          <input type="date" id="publishDate" v-model="book.publishDate" />
        </div>
        
        <div class="form-group">
          <label for="publisher">Publisher</label>
          <input type="text" id="publisher" v-model="book.publisher" placeholder="Enter the publisher's name" />
        </div>
        
        <div class="form-group">
          <label for="subjects">Subjects</label>
          <input type="text" id="subjects" v-model="book.subjects" placeholder="Enter subjects" />
        </div>
        
        <div class="form-group">
          <label for="pages">Pages</label>
          <input type="number" id="pages" v-model="book.pages" placeholder="Enter the number of pages" />
        </div>
        
        <div class="form-group">
          <label for="infoUrl">Info URL</label>
          <input type="url" id="infoUrl" v-model="book.infoUrl" placeholder="Enter the information URL" />
        </div>
        
        <div class="form-group">
          <label for="location">Location</label>
          <input type="text" id="location" v-model="book.location" placeholder="Enter the location" />
        </div>
        
        <button type="submit" class="submit-btn">Add Book</button>
      </form>
    </div>
  </template>
  
  <script>
  import { mapActions } from "vuex";

  export default {
    name: "AddBook",
    data() {
      return {
        book: {
          title: "",
          firstName: "",
          lastName: "",
          lcClassifications: "",
          publishDate: "",
          publisher: "",
          subjects: "",
          pages: "",
          infoUrl: "",
          location: ""
        }
      };
    },
    methods: {
      ...mapActions("library", ["addBook"]),
      addBookToDatabase() {
        console.log("Form submitted with data:", this.book);
        const payload = {
          book: this.book
        };
        this.addBook({ payload });
      }
    }
  };
  </script>
  
  <style scoped>
  .form-container {
    max-width: 600px;
    margin: 2rem auto;
    padding: 1.5rem;
    background: #f9f9f9;
    border: 1px solid #ddd;
    border-radius: 8px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  }
  
  .form {
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }
  
  .form-group {
    display: flex;
    flex-direction: column;
  }
  
  label {
    font-size: 0.9rem;
    color: #333;
    margin-bottom: 0.5rem;
  }
  
  input {
    padding: 0.75rem;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 1rem;
  }
  
  input:focus {
    border-color: #007bff;
    outline: none;
    box-shadow: 0 0 3px rgba(0, 123, 255, 0.5);
  }
  
  .submit-btn {
    padding: 0.75rem;
    background: #007bff;
    color: #fff;
    border: none;
    border-radius: 4px;
    font-size: 1rem;
    cursor: pointer;
  }
  
  .submit-btn:hover {
    background: #0056b3;
  }
  </style>
  