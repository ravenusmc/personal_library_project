<template>
    <div v-if="book">
      <h1>{{ book[1] }}</h1>
      <p><strong>Author:</strong> {{ book[2] }} {{ book[3] }}</p>
      <p><strong>Location:</strong> {{ book[10] }}</p>
      <p><strong>Description:</strong> {{ book[11] }}</p>
      <p><strong>Call Number:</strong> {{ book[4] }}</p>
      <p><strong>Published Date:</strong> {{ new Date(book[5]).toLocaleDateString() }}</p>
      <p><strong>Publisher:</strong> {{ book[6] }}</p>
      <p><strong>Subject:</strong> {{ book[7] }}</p>
      <p><strong>Pages:</strong> {{ book[8] }}</p>
      <p><strong>Link:</strong> <a :href="book[9]" target="_blank">View Book</a></p>
  
      <!-- Update form -->
      <div>
        <h3>Update Book Information</h3>
        <form @submit.prevent="updateBook">
          <div>
            <label for="author">Author:</label>
            <input v-model="updatedBook.author" id="author" type="text" />
          </div>
          <div>
            <label for="location">Location:</label>
            <input v-model="updatedBook.location" id="location" type="text" />
          </div>
          <div>
            <label for="description">Description:</label>
            <textarea v-model="updatedBook.description" id="description"></textarea>
          </div>
          <div>
            <label for="callNumber">Call Number:</label>
            <input v-model="updatedBook.callNumber" id="callNumber" type="text" />
          </div>
          <div>
            <label for="publisher">Publisher:</label>
            <input v-model="updatedBook.publisher" id="publisher" type="text" />
          </div>
          <div>
            <label for="pages">Pages:</label>
            <input v-model="updatedBook.pages" id="pages" type="number" />
          </div>
          <div>
            <label for="link">Link:</label>
            <input v-model="updatedBook.link" id="link" type="url" />
          </div>
          <button type="submit">Update</button>
        </form>
      </div>
    </div>
  
    <div v-else>
      <p>Book not found.</p>
    </div>
  </template>
  
  <script>
  import { mapGetters } from "vuex";
  
  export default {
    name: "BookDetails",
    data() {
      return {
        updatedBook: {
          author: "",
          location: "",
          description: "",
          callNumber: "",
          publisher: "",
          pages: null,
          link: "",
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
      // Initialize the form with existing book data when the component is created
      initUpdateForm() {
        const book = this.book;
        if (book) {
          this.updatedBook = {
            author: `${book[2]} ${book[3]}`,
            location: book[10],
            description: book[11],
            callNumber: book[4],
            publisher: book[6],
            pages: book[8],
            link: book[9],
          };
        }
      },
      updateBook() {
        // Implement the update logic here, such as making an API call or committing to Vuex
        console.log("Updated book data:", this.updatedBook);
        // Example: this.$store.dispatch("updateBook", this.updatedBook);
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
  
  