<template>
  <div class="home-page">
    <HeaderNav />
    <div class="main-content">
      <!-- CasesTab replaces the old left section -->
      <div class="cases-section">
        <CasesTab />
      </div>
    </div>
  </div>
</template>

<script>
import HeaderNav from '@/components/HeaderNav.vue'
import CasesTab from '@/components/CasesTab.vue'

export default {
  name: 'HomePage',
  components: {
    HeaderNav,
    CasesTab
  },
  data() {
    return {
      // Removed userCity as it's no longer used by LawyersList
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

.main-content {
  flex: 1;
  display: flex;
  justify-content: center; /* Center the cases section */
  padding: 20px;
}

.cases-section {
  width: 100%;
  max-width: 800px; /* Adjust the maximum width as needed */
}
</style>
