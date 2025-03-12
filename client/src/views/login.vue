<template>
  <div>
    <div class="outer-div">
        <div class="login-container">
          <form @submit.prevent="handleLogin">
            <h2>Login</h2>
      
            <div class="input-group">
              <input 
                type="email" 
                v-model="email" 
                placeholder="Email" 
                required
              />
            </div>
      
            <div class="input-group">
              <input 
                type="password" 
                v-model="password" 
                placeholder="Password" 
                required
              />
            </div>
      
            <button type="submit">Login</button>
            <!-- error handling -->
            <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
            <p v-if="!loginFlag">Hello</p>
          </form>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import { mapGetters, mapActions } from "vuex";
  
  export default {
    data() {
      return {
        email: "",
        password: "",
        errorMessage: "",
      };
    },
    computed: {
      ...mapGetters("user", ["loginFlag"]),
    },
    methods: {
      ...mapActions("user", ["loginUser"]),
      handleLogin() {
        //Error handling
        if (!this.email.includes("@")) {
          this.errorMessage = "Please enter a valid email.";
          return;
        }
  
        if (this.password.length < 6) {
          this.errorMessage = "Password must be at least 6 characters long.";
          return;
        }

        const payload = {
          email: this.email,
          password: this.password,
        };
  
        this.errorMessage = "";
        this.loginUser({ payload });
      },
    },
  };
  </script>
  
  <style scoped>
  /* Background */
  body {
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background: url('https://source.unsplash.com/random/1600x900') no-repeat center center/cover;
  }

  .outer-div {
    display: flex;
    justify-content: center;
  }
  
  /* Login Container */
  .login-container {
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(10px);
    padding: 50px;
    border-radius: 15px;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
    text-align: center;
    width: 320px;
    margin-top: 100px;
  }
  
  /* Heading */
  h2 {
    margin-bottom: 20px;
  }
  
  /* Input Group */
  .input-group {
    margin-bottom: 15px;
  }
  
  input {
    width: 100%;
    padding: 12px;
    border-radius: 5px;
    font-size: 16px;
    background: rgba(255, 255, 255, 0.2);
    outline: none;
    transition: 0.3s;
    border: 2px solid black;
  }
  
  input::placeholder {
    color: rgba(27, 24, 205, 0.7);
  }
  
  input:focus {
    background: rgba(255, 255, 255, 0.4);
  }
  
  /* Button */
  button {
    width: 100%;
    padding: 12px;
    background: linear-gradient(45deg, #ff416c, #ff4b2b);
    border: none;
    border-radius: 5px;
    color: white;
    font-size: 18px;
    cursor: pointer;
    transition: 0.3s;
  }
  
  button:hover {
    background: linear-gradient(45deg, #ff4b2b, #ff416c);
  }
  
  /* Error Message */
  .error {
    margin-top: 10px;
    color: #ff4b2b;
    font-size: 14px;
  }
  </style>
  