<template>
    <div class="lawyers-search-container">
      <!-- City Input + Button -->
      <div class="search-bar">
        <input
          v-model="searchCity"
          type="text"
          placeholder="Enter city, e.g. Nagpur"
          @keyup.enter="fetchLawyers"
        />
        <button @click="fetchLawyers">Go</button>
      </div>
  
      <!-- Lawyer Cards -->
      <div class="lawyers-list">
        <h2>Lawyers in {{ currentCity }}</h2>
        <div
          class="lawyer-card"
          v-for="(lawyer, index) in lawyers"
          :key="index"
        >
          <!-- Contact Icon on the left -->
          <a
            :href="lawyer.contact_link"
            target="_blank"
            class="contact-icon"
          >
            <img
              src="@/assets/contact-icon.png"
              alt="Contact Lawyer"
              class="icon"
            />
          </a>
          <!-- Lawyer Info -->
          <div class="lawyer-info">
            <div class="lawyer-name">{{ lawyer.name }}</div>
            <div class="lawyer-address">{{ lawyer.address }}</div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  
  export default {
    name: 'LawyersList',
    data() {
      return {
        searchCity: 'Nagpur', // default city
        currentCity: 'Nagpur',
        lawyers: []
      }
    },
    mounted() {
      // Fetch lawyers for the default city on mount
      this.fetchLawyers()
    },
    methods: {
      fetchLawyers() {
        // Use the user-provided city. If it's blank, default to 'Nagpur'.
        const city = this.searchCity ? this.searchCity.trim() : 'Nagpur'
        // Update currentCity to reflect what we’re showing
        this.currentCity = city
  
        const url = `http://localhost:8000/api/lawyers/${city}/`
        axios.get(url)
          .then(response => {
            this.lawyers = response.data
          })
          .catch(error => {
            console.error('Error fetching lawyers:', error)
            this.lawyers = []
          })
      }
    }
  }
  </script>
  
  <style scoped>
  .lawyers-search-container {
    width: 100%;
    max-width: 300px;
    background-color: rgb(55, 55, 71);
    color: gold;
    padding: 20px;
    display: flex;
    flex-direction: column;
    gap: 15px;
  }
  
  .search-bar {
    display: flex;
    gap: 5px;
  }
  
  .search-bar input {
    flex: 1;
    padding: 5px 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  
  .search-bar button {
    background-color: #333;
    color: gold;
    padding: 6px 12px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  .lawyers-list h2 {
    margin-bottom: 10px;
  }
  
  .lawyer-card {
    display: flex;
    align-items: flex-start;
    background-color: #333;
    margin-bottom: 10px;
    padding: 10px;
    border-radius: 6px;
  }
  
  .contact-icon {
    margin-right: 10px;
  }
  
  .icon {
    width: 28px;
    height: 28px;
  }
  
  .lawyer-info {
    display: flex;
    flex-direction: column;
  }
  
  .lawyer-name {
    font-weight: bold;
    margin-bottom: 4px;
  }
  
  .lawyer-address {
    font-size: 0.9rem;
  }
  </style>