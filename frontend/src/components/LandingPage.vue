<!-- filepath: frontend/src/components/LandingPage.vue -->
<template>
    <div class="landing">
      <img class="logo" :src="logo" alt="Code Red Logo" />
      <h1>Code Red</h1>
      <p class="slogan">Justice Made Accessible</p>
      <blockquote>“Right to Free Legal Aid for All”</blockquote>
      <button @click="authenticate">Get Started</button>
    </div>
  </template>
  
  <script>
  import logo from '@/assets/logo.png'
  
  export default {
    name: 'LandingPage',
    data() {
      return {
        logo
      }
    },
    methods: {
      authenticate() {
        // Use absolute URL to target Django backend (port 8000)
      window.location.href = 'http://localhost:8000/accounts/google/login/';
      }
    }
  }
  </script>
  
  <style scoped>
  .landing {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    background-color: #f8f9fa;
    text-align: center;
    padding: 0 20px;
  }
  .logo {
    width: 120px;
    margin-bottom: 20px;
  }
  .slogan {
    font-size: 1.5em;
    color: #007bff;
  }
  blockquote {
    font-style: italic;
    color: #555;
    margin: 20px 0;
  }
  button {
    padding: 12px 24px;
    font-size: 1em;
    font-weight: bold;
    color: #fff;
    background-color: #007bff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }
  button:hover {
    background-color: #0056b3;
  }
  </style>