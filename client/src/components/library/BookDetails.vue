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
    </div>
    <div v-else>
      <p>Book not found.</p>
    </div>
  </template>
  
  <script>
  import { mapGetters } from "vuex";
  
  export default {
    name: "BookDetails",
    computed: {
      ...mapGetters("library", ["bookById"]),
      book() {
        return this.bookById(this.$route.params.id);
      },
    },
  };
  </script>
  