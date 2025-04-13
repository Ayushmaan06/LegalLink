<template>
    <div class="home-page">
      <HeaderNav />
  
      <div class="main-content">
        <!-- Left section: Lawyers list -->
        <div class="left-section">
          <LawyersList :city="userCity" />
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import HeaderNav from '@/components/HeaderNav.vue'
  import LawyersList from '@/components/LawyersList.vue'
  
  export default {
    name: 'HomePage',
    components: {
      HeaderNav,
      LawyersList
    },
    data() {
      return {
        // default city is Nagpur; user can change this
        userCity: 'Nagpur'
      }
    }
  }
  </script>
  
  <style scoped>
  .home-page {
    background-color: #222; /* Dark mode background */
    color: gold;            /* Dark mode text color */
    min-height: 100vh;
    display: flex;
    flex-direction: column;
  }
  
  /* Main content container */
  .main-content {
    flex: 1;
    display: flex;
  }
  
  /* Left section for lawyers */
  .left-section {
    width: 25%;
    padding: 20px;
  }
  </style>