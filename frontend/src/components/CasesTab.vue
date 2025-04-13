<template>
    <div class="cases-tab">
      <div class="header">
        <h2>Your Cases</h2>
        <button class="add-case-btn" @click="openAddCaseModal">+</button>
      </div>
  
      <!-- Tabs for Active and Closed Cases -->
      <div class="tabs">
        <button :class="{active: activeTab === 'active'}" @click="activeTab = 'active'">
          Active Cases
        </button>
        <button :class="{active: activeTab === 'closed'}" @click="activeTab = 'closed'">
          Past Cases
        </button>
      </div>
  
      <!-- Cases list -->
      <div class="cases-list">
        <div v-if="activeTab === 'active'">
          <div v-if="activeCases.length">
            <div
              class="case-item"
              v-for="caseItem in activeCases"
              :key="caseItem.id"
              @click="openCaseDetail(caseItem)"
            >
              <h3>{{ caseItem.title }}</h3>
              <p>
                Charges:
                <span v-if="caseItem.charges && caseItem.charges.length">
                  {{ caseItem.charges.join(', ') }}
                </span>
                <span v-else>None</span>
              </p>
            </div>
          </div>
          <div v-else class="empty-state">
            <p>No active cases. Looks like you're enjoying a peaceful day!</p>
          </div>
        </div>
  
        <div v-if="activeTab === 'closed'">
          <div v-if="closedCases.length">
            <div
              class="case-item"
              v-for="caseItem in closedCases"
              :key="caseItem.id"
              @click="openCaseDetail(caseItem)"
            >
              <h3>{{ caseItem.title }}</h3>
              <p>
                Charges:
                <span v-if="caseItem.charges && caseItem.charges.length">
                  {{ caseItem.charges.join(', ') }}
                </span>
                <span v-else>None</span>
              </p>
            </div>
          </div>
          <div v-else class="empty-state">
            <p>No past cases yet. All clear – justice is swift!</p>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import { ref, onMounted } from 'vue'
  import { useRouter } from 'vue-router'
  import axios from 'axios'
  
  export default {
    name: 'CasesTab',
    setup() {
      const router = useRouter()  // import the router
      const activeTab = ref('active')
      const activeCases = ref([])
      const closedCases = ref([])
  
      // Fetch cases for the current user from Django
      const fetchCases = async () => {
        try {
          const response = await axios.get('http://localhost:8000/api/user-cases/', { withCredentials: true })
          // Expected response structure: { active: [...], closed: [...] }
          activeCases.value = response.data.active || []
          closedCases.value = response.data.closed || []
        } catch (err) {
          console.error('Error fetching cases:', err)
        }
      }
  
      // Redirect to the CaseModal route when clicking the plus button
      const openAddCaseModal = () => {
        router.push({ name: 'case-modal' })
      }
  
      const openCaseDetail = (caseItem) => {
        console.log('Open case detail for:', caseItem)
        // Future implementation: open a modal/page with the case details and todo list.
      }
  
      onMounted(fetchCases)
  
      return {
        activeTab,
        activeCases,
        closedCases,
        openAddCaseModal,
        openCaseDetail
      }
    }
  }
  </script>
  
  <style scoped>
  .cases-tab {
    padding: 20px;
    background-color: #f5f5f5;
    border-radius: 8px;
  }
  
  .header {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  
  .add-case-btn {
    background-color: gold;
    color: #222;
    border: none;
    font-size: 24px;
    border-radius: 50%;
    width: 40px;
    height: 40px;
    cursor: pointer;
  }
  
  .tabs {
    margin-top: 20px;
  }
  
  .tabs button {
    background: none;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
  }
  
  .tabs button.active {
    border-bottom: 2px solid gold;
  }
  
  .cases-list {
    margin-top: 20px;
  }
  
  .case-item {
    background-color: white;
    padding: 10px;
    margin-bottom: 10px;
    border-radius: 4px;
    cursor: pointer;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  }
  
  .empty-state {
    text-align: center;
    margin-top: 20px;
    font-style: italic;
    color: #888;
  }
  </style>