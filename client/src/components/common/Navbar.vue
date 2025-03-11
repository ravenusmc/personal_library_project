<template>
    <div>
      <nav class="navbar">
        <div class="navlinks-left">
          <a class="navlink"><router-link class="link-style" to="/">Home</router-link></a>
          <a v-if="loginFlag" class="navlink"><router-link class="link-style" to="/library">The Library</router-link></a>
          <a v-if="loginFlag" class="navlink"><router-link class="link-style" to="/addbook">Add Book</router-link></a>
          <a class="navlink"><router-link class="link-style" to="/about">About</router-link></a>
        </div>
        <div class="navlinks-right">
          <a v-if="!loginFlag" class="navlink"><router-link class="link-style" to="/login">Login</router-link></a>
          <a v-if="!loginFlag" class="navlink"><router-link class="link-style" to="/signup">Sign Up</router-link></a>
          <a v-if="loginFlag" class="navlink" @click.prevent="logout"><router-link class="link-style" to="/">Log Out</router-link></a>
        </div>
      </nav>
    </div>
  </template>
  
  <script>
  import { mapGetters, mapActions } from "vuex";
  
  export default {
    name: "navbar",
    computed: {
      ...mapGetters("user", ["passwordNoMatch"]),
    },
    methods: {
      ...mapActions(["user/logout"]),
      logout: function () {
        this.$store.dispatch("user/logout");
      },
    },
  };
  </script>
  
  <style scoped>
  .navbar {
    background-color: #2c3e50;
    height: 50px;
    display: flex; 
    justify-content: space-between;
    align-items: center;
    padding: 0 15px;
  }
  
  a {
    text-decoration: none;
  }
  
  .link-style {
    color: white;
  }
  
  .navlink {
    color: white;
    font-size: 1.5rem;
    margin: 10px 15px;
  }
  
  .navlinks-left, .navlinks-right {
    display: flex;
    align-items: center;
  }
  
  </style>