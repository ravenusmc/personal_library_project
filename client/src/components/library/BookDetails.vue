<template>
    <div v-if="book">
      <div class="book-details" style="max-width: 600px; margin: 20px auto; padding: 20px; border: 1px solid #ddd; border-radius: 10px; background-color: #f9f9f9; font-family: Arial, sans-serif; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
        <h1 style="color: #333; font-size: 1.8rem; margin-bottom: 10px;">{{ book[1] }}</h1>
        <p style="margin: 5px 0;"><strong>Author:</strong> {{ book[2] }} {{ book[3] }}</p>
        <p style="margin: 5px 0;"><strong>Location:</strong> {{ book[10] }}</p>
        <p style="margin: 5px 0;"><strong>Description:</strong> {{ book[11] }}</p>
        <p style="margin: 5px 0;"><strong>Call Number:</strong> {{ book[4] }}</p>
        <p style="margin: 5px 0;"><strong>Published Date:</strong> {{ new Date(book[5]).toLocaleDateString() }}</p>
        <p style="margin: 5px 0;"><strong>Publisher:</strong> {{ book[6] }}</p>
        <p style="margin: 5px 0;"><strong>Subject:</strong> {{ book[7] }}</p>
        <p style="margin: 5px 0;"><strong>Pages:</strong> {{ book[8] }}</p>
        <p style="margin: 5px 0;"><strong>Link:</strong> 
          <a :href="book[9]" target="_blank" style="color: #007bff; text-decoration: none;">View Book</a>
        </p>
      </div>
  
      <!-- Update form -->
      <div class="form-container">
        <h3>Update Book Information</h3>
        <form @submit.prevent="updateBook">
          <div class="form-group">
            <label for="author">Author First Name:</label>
            <input
              :placeholder="updatedBook.firstName"
              v-model.lazy="updatedBook.firstName"
              id="author"
              type="text"
            />
          </div>
          <div class="form-group">
            <label for="author">Author Last Name:</label>
            <input
              :placeholder="updatedBook.lastName"
              v-model.lazy="updatedBook.lastName"
              id="author"
              type="text"
            />
          </div>
          <div class="form-group">
            <label for="location">Location:</label>
            <input 
              :placeholder="updatedBook.location"
              v-model="updatedBook.location" 
              id="location" 
              type="text" 
            />
          </div>
          <div class="form-group">
            <label for="publisher">Publisher:</label>
            <input 
              :placeholder="updatedBook.publisher"
              v-model="updatedBook.publisher" 
              id="publisher" 
              type="text" 
            />
          </div>
          <button class="submit-btn" type="submit">Update</button>
        </form>
      </div>
    </div>
  
    <div v-else>
      <p>Book not found.</p>
    </div>
  </template>
  
<script>
  import { mapGetters, mapActions } from "vuex";
  
  export default {
    name: "BookDetails",
    data() {
      return {
        updatedBook: {
          author: "",
          location: "",
          publisher: "",
        },
      };
    },
    computed: {
      ...mapGetters("library", ["bookById"]),
      book() {
        return this.bookById(this.$route.params.id);
      },
    },
    methods: {
      ...mapActions("library", ["updateBookData"]),
      // Initialize the form with existing book data when the component is created
      initUpdateForm() {
        const book = this.book;
        if (book) {
          this.updatedBook = {
            id: book[0],
            firstName: book[2], 
            lastName: book[3],
            // author: `${book[2]} ${book[3]}`,
            location: book[10],
            publisher: book[6],
          };
        }
      },
      updateBook() {
        const payload = {
          updateData: this.updatedBook,
        };
        this.updateBookData({ payload });
      },
    },
    watch: {
      book: "initUpdateForm",
    },
    created() {
      this.initUpdateForm();
    },
  };
</script>

<style scoped> 
.book-details {
  max-width: 600px;
  margin: 20px auto;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 10px;
  background-color: #f9f9f9;
  font-family: Arial, sans-serif;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.book-details h1 {
  color: #333;
  font-size: 1.8rem;
  margin-bottom: 10px;
}

.book-details p {
  margin: 5px 0;
}

.book-details a {
  color: #007bff;
  text-decoration: none;
}

.book-details a:hover {
  text-decoration: underline;
}


/* CSS Code for form */
/* General container styling */
.form-container {
  max-width: 400px;
  margin: 20px auto;
  padding: 40px;
  border: 1px solid #ccc;
  border-radius: 10px;
  background-color: #f9f9f9;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  font-family: Arial, sans-serif;
}

/* Header styling */
.form-container h3 {
  text-align: center;
  color: #333;
  margin-bottom: 20px;
  font-size: 1.5em;
}

/* Group styling */
.form-group {
  margin-bottom: 15px;
}

/* Label styling */
.form-group label {
  display: block;
  font-weight: bold;
  margin-bottom: 5px;
  color: #555;
}

/* Input field styling */
.form-group input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 1em;
  transition: border-color 0.3s;
}

/* Input hover and focus states */
.form-group input:hover {
  border-color: #999;
}

.form-group input:focus {
  border-color: #007BFF;
  outline: none;
  box-shadow: 0 0 3px #007BFF;
}

/* Submit button styling */
.submit-btn {
  width: 100%;
  padding: 10px;
  font-size: 1em;
  font-weight: bold;
  color: #fff;
  background-color: #007BFF;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
}

/* Submit button hover state */
.submit-btn:hover {
  background-color: #0056b3;
}

/* Add responsive design */
@media (max-width: 600px) {
  .form-container {
    padding: 15px;
  }

  .form-container h3 {
    font-size: 1.2em;
  }

  .form-group input {
    font-size: 0.9em;
  }

  .submit-btn {
    font-size: 0.9em;
  }
}

</style>
  
  