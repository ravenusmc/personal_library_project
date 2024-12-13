<template>
  <div>
    <div v-for="(book, index) in books" :key="index" class="book">
      <div class="outer-book-div">
        <!-- Outside drawer content -->
        <div 
          class="outside-drawer-div"
          @click="toggleDrawer(index)"
        >
          <h3>Book {{ index + 1 }}:</h3>
          <p><strong>Title:</strong> {{ book[1] }}</p>
          <p><strong>Author:</strong> {{ book[2] }} {{ book[3] }}</p>
          <p><strong>Location:</strong> {{ book[10] }}</p>
        </div>

        <!-- Hidden drawer content -->
        <transition name="slide">
          <div 
            v-if="openDrawerIndex === index" 
            class="drawer-div"
          >
            <p><strong>Call Number:</strong> {{ book[4] }}</p>
            <p><strong>Published Date:</strong> {{ new Date(book[5]).toLocaleDateString() }}</p>
            <p><strong>Publisher:</strong> {{ book[6] }}</p>
            <p><strong>Subject:</strong> {{ book[7] }}</p>
            <p><strong>Pages:</strong> {{ book[8] }}</p>
            <p><strong>Link:</strong> <a :href="book[9]" target="_blank">View Book</a></p>
          </div>
        </transition>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "BookResults",
  data() {
    return {
      openDrawerIndex: null, // Tracks which book's drawer is open
    };
  },
  computed: {
    ...mapGetters("library", [
      "books",
    ]),
  },
  methods: {
    toggleDrawer(index) {
      // Toggle the drawer for the clicked index
      this.openDrawerIndex = this.openDrawerIndex === index ? null : index;
    },
  },
};
</script>

<style>
.book {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.outer-book-div {
  margin-bottom: 1rem;
  width: 45%;
}

.outside-drawer-div {
  background-color: #fefefe; /* Light background for readability */
  border: 1px solid #ddd; /* Subtle border */
  border-radius: 8px; /* Rounded corners */
  padding: 1rem; /* Add some spacing inside */
  margin-bottom: 1rem; /* Space between each card */
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); /* Soft shadow */
  transition: transform 0.2s ease, box-shadow 0.2s ease; /* Smooth transition */
  cursor: pointer; /* Pointer cursor to indicate clickability */
}

.outside-drawer-div h3 {
  margin-top: 0; /* Remove default top margin */
  font-size: 1.2rem; /* Slightly larger font for the title */
  color: #333; /* Dark text for contrast */
}

.outside-drawer-div p {
  margin: 0.5rem 0; /* Add spacing between paragraphs */
  font-size: 0.9rem; /* Slightly smaller font for content */
  color: #555; /* Softer text color */
}

.outside-drawer-div:hover {
  transform: scale(1.02); /* Slightly enlarge on hover */
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2); /* Enhance shadow on hover */
}

.outside-drawer-div:active {
  transform: scale(0.98); /* Slight shrink effect on click */
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); /* Reset shadow on click */
}


.drawer-div {
  padding: 1rem;
  background: #f9f9f9;
  border: 2px solid #ccc;
  margin-top: 0.5rem;
}

.slide-enter-active, .slide-leave-active {
  transition: all 0.3s ease;
}

.slide-enter {
  max-height: 0;
  opacity: 0;
}

.slide-leave-to {
  max-height: 0;
  opacity: 0;
}
</style>
