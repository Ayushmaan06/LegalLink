<template>
  <div class="home-page">
    <HeaderNav />
    <div class="main-content">
      <div class="cases-section">
        <CasesTab />
      </div>
      <div class="community-section">
        <div class="card">
          <CommunityHelper :activeCase="hasActiveCase" />
        </div>
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
      hasActiveCase: true,
    }
  }
}
</script>

<style scoped>
.home-page {
  background-color: var(--bg-black);
  color: var(--highlight-yellow);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.main-content {
  flex: 1;
  display: flex;
  gap: 20px;
  padding: 20px;
  justify-content: center;
  flex-wrap: wrap;
}

.cases-section {
  flex: 2;
  max-width: 800px;
  width: 100%;
}

.community-section {
  flex: 1;
  max-width: 300px;
  width: 100%;
  display: flex;
  justify-content: center;
  margin-left: 20px; /* Add space between sections */
}


/* Reuse your dark glassy card style */
.card {
  width: 100%;
  padding: 16px;
  border-radius: 30px;
  background: #212121;
  box-shadow:
    0 0 10px rgba(255, 204, 0, 0.2),
    0 0 20px rgba(255, 204, 0, 0.15),
    0 0 30px rgba(255, 204, 0, 0.1);
}


/* Optional: make sure CommunityHelper content fits well */
.card :deep(.community-helpers) {
  color: #fefefe;
}

/* Responsive fix */
@media (max-width: 768px) {
  .main-content {
    flex-direction: column;
    align-items: center;
  }
}
</style>
