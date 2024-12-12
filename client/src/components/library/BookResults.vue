<template>
    <div>
    <!-- Loop through each book array -->
    <div v-for="(book, index) in books" :key="index" class="book">
      <h3>Book {{ index + 1 }}:</h3>
      <p><strong>Title:</strong> {{ book[1] }}</p>
      <p><strong>Author:</strong> {{ book[2] }} {{ book[3] }}</p>
      <p><strong>Call Number:</strong> {{ book[4] }}</p>
      <p><strong>Published Date:</strong> {{ new Date(book[5]).toLocaleDateString() }}</p>
      <p><strong>Publisher:</strong> {{ book[6] }}</p>
      <p><strong>Category:</strong> {{ book[7] }}</p>
      <p><strong>Pages:</strong> {{ book[8] }}</p>
      <p><strong>Link:</strong> <a :href="book[9]" target="_blank">View Book</a></p>
      <p><strong>Shelf:</strong> {{ book[10] }}</p>
    </div>
    </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "BookResults",
  computed: {
    ...mapGetters("library", [
      "books",
    ]),
  },
};
</script>

<style>

</style>