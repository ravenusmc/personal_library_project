<template>
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
  
        <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        email: "",
        password: "",
        errorMessage: "",
      };
    },
    methods: {
      handleLogin() {
        if (!this.email.includes("@")) {
          this.errorMessage = "Please enter a valid email.";
          return;
        }
  
        if (this.password.length < 6) {
          this.errorMessage = "Password must be at least 6 characters long.";
          return;
        }
  
        this.errorMessage = "";
        alert("Login successful!");
        // Here you can add authentication logic
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
  
  /* Login Container */
  .login-container {
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(10px);
    padding: 30px;
    border-radius: 15px;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
    text-align: center;
    width: 320px;
  }
  
  /* Heading */
  h2 {
    color: #fff;
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
    border: none;
    font-size: 16px;
    background: rgba(255, 255, 255, 0.2);
    color: white;
    outline: none;
    transition: 0.3s;
  }
  
  input::placeholder {
    color: rgba(255, 255, 255, 0.7);
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
  