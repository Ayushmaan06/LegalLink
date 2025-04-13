<template>
    <header class="header-nav">
      <!-- Logo on the left -->
      <div class="logo" @click="goHome">
        <img 
          src="@/assets/logo.png" 
          alt="App Logo" 
          class="logo-img" 
        />
      </div>
  
      <!-- Nav Links -->
      <nav class="nav-links">
        <!-- LLM -->
        <div class="nav-item" @click="goToLLM">
          <img
            src="@/assets/llm-icon.png"
            alt="LLM Icon"
            class="icon"
          />
          <span>LLM</span>
        </div>
  
        <!-- eVault -->
        <div class="nav-item" @click="goToEVault">
          <img
            src="@/assets/vault-icon.png"
            alt="eVault Icon"
            class="icon"
          />
          <span>eVault</span>
        </div>
  
        <!-- Library -->
        <div class="nav-item" @click="goToLibrary">
          <img
            src="@/assets/library-icon.png"
            alt="Library Icon"
            class="icon"
          />
          <span>Library</span>
        </div>
  
        <!-- Legal Document Summarizer -->
        <div class="nav-item" @click="goToSummarizer">
          <img
            src="@/assets/summarizer-icon.png"
            alt="Summarizer Icon"
            class="icon"
          />
          <span>Summarizer</span>
        </div>
      </nav>
  
      <!-- User Profile -->
      <div class="profile-btn" @click="goToProfile">
        <img
          src="@/assets/user-icon.png"
          alt="User Profile"
          class="icon"
        />
        <span>Profile</span>
      </div>
    </header>
  </template>
  
  <script>
  export default {
    name: 'HeaderNav',
    methods: {
      goHome() {
        this.$router.push({ name: 'homepage' })
      },
      goToLLM() {
        window.open('http://localhost:8501', '_blank')
      },
      goToEVault() {
        this.$router.push({ path: '/evault' })
      },
      goToLibrary() {
        window.open('https://nalsa.gov.in/library', '_blank')
      },
      // goToSummarizer() {
      //   this.$router.push({ path: '/summarizer' })
      // },
      goToProfile() {
        this.$router.push({ path: '/profile' })
      }
    }
  }
  </script>
  
  <style scoped>
  .header-nav {
    display: flex;
    align-items: center;
    justify-content: space-between;
    background-color: rgb(55, 55, 71);
    padding: 0 20px;       /* Remove vertical padding to cover white space */
    color: gold;
    position: sticky;
    top: 0;
    z-index: 1000;
    min-height: 70px;      /* Increase header height */
    margin: 0;             /* Ensure no extra space around header */
  }
  
  .logo {
    cursor: pointer;
  }
  
  .logo-img {
    height: 60px;          /* Larger logo */
  }
  
  .nav-links {
    display: flex;
    gap: 30px;             /* Increase spacing between items */
    font-weight: bold;
  }
  
  .nav-item {
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 8px;
  }
  
  .profile-btn {
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 8px;
    font-weight: bold;
  }
  
  .icon {
    width: 28px;           /* Slightly larger icons for clarity */
    height: 28px;
  }
  </style>