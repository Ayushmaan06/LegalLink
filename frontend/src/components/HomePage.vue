<template>
  <div class="home-page">
    <HeaderNav />
    <div class="main-content">
      <!-- Left column: CasesTab -->
      <div class="cases-section">
        <CasesTab />
      </div>
      <!-- Right column: CommunityHelper -->
      <div class="community-section">
        <!-- Pass activeCase prop as needed (e.g., based on a computed property or hardcoded for now) -->
        <CommunityHelper :activeCase="hasActiveCase" />
      </div>
    </div>
  </div>
</template>

<script>
import HeaderNav from '@/components/HeaderNav.vue'
import CasesTab from '@/components/CasesTab.vue'
import CommunityHelper from '@/components/CommunityHelper.vue'

export default {
  name: 'HomePage',
  components: {
    HeaderNav,
    CasesTab,
    CommunityHelper
  },
  data() {
    return {
      // For demonstration, set activeCase to true.
      // You can change this based on your application logic.
      hasActiveCase: true,
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
  gap: 20px;   /* Add some gap between columns */
  padding: 20px;
  justify-content: center;
}
.cases-section {
  flex: 2;
  max-width: 800px; /* Adjust the maximum width as needed */
}
.community-section {
  flex: 1;
  max-width: 300px; /* Adjust as needed */
  background-color: #fff;
  border-radius: 8px;
  padding: 16px;
  color: #222;
}
</style>