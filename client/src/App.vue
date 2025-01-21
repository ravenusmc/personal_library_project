<template>
  <div id="app" class="layout">
    <header>
      <Navbar/>
    </header>
    <main class="content">
      <router-view/>
    </main>
    <footer>
      <Footer/>
    </footer>
  </div>
</template>

<script>
import Navbar from "@/components/common/Navbar.vue";
import Footer from "@/components/common/Footer.vue";

export default {
  components: {
    Navbar,
    Footer,
  },
};
</script>

<style>
/* Ensure no margin or padding disturbs the layout */
body, html {
  margin: 0;
  padding: 0;
  height: 100%; /* Ensure the height covers the full viewport */
}

.layout {
  display: flex;
  flex-direction: column;
  min-height: 100vh; /* Full viewport height */
}

header {
  flex-shrink: 0; /* Prevent shrinking of the header */
}

.content {
  flex: 1; /* Grow to fill available space */
  padding: 20px; /* Optional: Add some spacing for content */
}

footer {
  flex-shrink: 0; /* Prevent shrinking of the footer */
  background-color: #f8f9fa; /* Example footer styling */
  text-align: center;
}
</style>

