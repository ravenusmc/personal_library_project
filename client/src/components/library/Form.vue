<template>
  <div>
    <div class="form-div">
      <form @submit.prevent="SubmitSearchQuery">
        <div>
          <label for="search">Enter Author, Subject, or Title:</label>
          <input v-model="search" id="search" type="text" placeholder="Type your query here..." />
        </div>

        <div class="form-group">
          <label>
            <input type="radio" v-model="searchType" value="Author" /> Author
          </label>
          <label>
            <input type="radio" v-model="searchType" value="Title" /> Title
          </label>
          <label>
            <input type="radio" v-model="searchType" value="Subject" /> Subject
          </label>
          <label>
            <input type="radio" v-model="searchType" value="Location" /> Location
          </label>
        </div>

        <div class="form-group">
          <p>Show Description: (May take longer)</p>
          <label>
            <input type="radio" v-model="showDescription" value="Yes" /> Yes
          </label>
          <label>
            <input type="radio" v-model="showDescription" value="No" /> No
          </label>
        </div>

        <div class="form-group">
          <button class="styled-button" type="submit">Search</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import { mapActions } from "vuex";

export default {
  name: "Form",
  data() {
    return {
      search: "",
      searchType: "Author", 
      showDescription: "No", 
    };
  },
  methods: {
    ...mapActions("library", ["submitSearchQueryToServer"]),
    SubmitSearchQuery() {
      if (!this.search.trim()) {
        alert("Please enter a search query.");
        return;
      }
      if (this.showDescription === 'Yes') {
        this.showDescription = true
      } else {
        this.showDescription = false
      }
      const payload = {
        query: this.search,
        type: this.searchType,
        description: this.showDescription,
      };
      this.submitSearchQueryToServer({ payload });
    },
  },
};
</script>

<style>

.form-div {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.form-group {
  margin: 10px 0;
}

.styled-button {
  background-color: #007bff;
  color: #fff;
  border: none;
  padding: 8px 15px;
  cursor: pointer;
  border-radius: 4px;
}

.styled-button:hover {
  background-color: #0056b3;
}

input[type="radio"] {
  margin-right: 5px;
}
</style>
