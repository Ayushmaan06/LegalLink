<template>
  <div class="cases-tab card">
    <div class="header">
      <h2>Your Cases</h2>
      <button class="add-case-btn" @click="openAddCaseModal">+</button>
    </div>

    <!-- Tabs -->
    <div class="tabs">
      <button :class="{ active: activeTab === 'active' }" @click="activeTab = 'active'">Active Cases</button>
      <button :class="{ active: activeTab === 'closed' }" @click="activeTab = 'closed'">Past Cases</button>
    </div>

    <!-- Case Lists -->
    <div class="cases-list">
      <div v-if="activeTab === 'active'">
        <div v-if="activeCases.length">
          <div class="case-item" v-for="caseItem in activeCases" :key="caseItem.id" @click="openCaseDetail(caseItem)">
            <h3>{{ caseItem.title }}</h3>
            <p>
              Charges:
              <span v-if="caseItem.charges?.length">{{ caseItem.charges.join(', ') }}</span>
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
          <div class="case-item" v-for="caseItem in closedCases" :key="caseItem.id" @click="openCaseDetail(caseItem)">
            <h3>{{ caseItem.title }}</h3>
            <p>
              Charges:
              <span v-if="caseItem.charges?.length">{{ caseItem.charges.join(', ') }}</span>
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
    const router = useRouter()
    const activeTab = ref('active')
    const activeCases = ref([])
    const closedCases = ref([])

    const fetchCases = async () => {
      try {
        const response = await axios.get('http://localhost:8000/api/user-cases/', { withCredentials: true })
        activeCases.value = response.data.active || []
        closedCases.value = response.data.closed || []
      } catch (err) {
        console.error('Error fetching cases:', err)
      }
    }

    const openAddCaseModal = () => {
      router.push({ name: 'case-modal' })
    }

    const openCaseDetail = (caseItem) => {
      console.log('Open case detail for:', caseItem)
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
/* Neumorphic card style applied */
.card.cases-tab {
  padding: 24px;
  background: #212121;
  border-radius: 30px;
  box-shadow:  0 0 10px rgba(255, 204, 0, 0.2),
    0 0 20px rgba(255, 204, 0, 0.15),
    0 0 30px rgba(255, 204, 0, 0.1);
  color: #f0f0f0;
  max-width: 900px;
  margin: 32px auto;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

/* Header section */
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
}

.header h2 {
  font-size: 24px;
  font-weight: 600;
  color: #ffcc00;
}

.add-case-btn {
  background-color: #ffcc00;
  color: #212121;
  border: none;
  font-size: 24px;
  border-radius: 50%;
  width: 42px;
  height: 42px;
  cursor: pointer;
  transition: transform 0.2s ease, background-color 0.3s;
  box-shadow: 0 2px 6px rgba(255, 255, 255, 0.05);
  margin-top: 12px;
}

.add-case-btn:hover {
  background-color: #e6b800;
  transform: scale(1.1);
}

/* Tabs */
.tabs {
  margin-top: 24px;
  display: flex;
  gap: 16px;
  flex-wrap: wrap;
}

.tabs button {
  background: none;
  border: none;
  padding: 10px 16px;
  font-size: 16px;
  font-weight: 500;
  cursor: pointer;
  color: #ccc;
  border-bottom: 2px solid transparent;
  transition: color 0.2s, border-color 0.2s;
}

.tabs button:hover {
  color: #fff;
}

.tabs button.active {
  color: #ffcc00;
  border-bottom: 3px solid #ffcc00;
}

/* Case list */
.cases-list {
  margin-top: 24px;
}

.case-item {
  background-color: #2b2b2b;
  padding: 16px;
  margin-bottom: 12px;
  border-radius: 20px;
  cursor: pointer;
  transition: box-shadow 0.2s, transform 0.2s;
  border: 1px solid #333;
}

.case-item:hover {
  box-shadow: 0 4px 12px rgba(255, 255, 255, 0.08);
  transform: translateY(-2px);
}

.case-item h3 {
  margin: 0 0 6px;
  font-size: 18px;
  font-weight: 600;
  color: #ffcc00;
}

.case-item p {
  margin: 0;
  font-size: 14px;
  color: #bbb;
}

.empty-state {
  text-align: center;
  margin-top: 32px;
  font-style: italic;
  color: #666;
  font-size: 15px;
}

/* Responsive tweaks */
@media (max-width: 768px) {
  .header {
    flex-direction: column;
    align-items: flex-start;
    gap: 12px;
  }

  .add-case-btn {
    width: 36px;
    height: 36px;
    font-size: 20px;
  }
}

@media (max-width: 480px) {
  .card.cases-tab {
    padding: 16px;
  }

  .add-case-btn {
    width: 32px;
    height: 32px;
    font-size: 18px;
  }

  .case-item {
    padding: 12px;
  }

  .case-item h3 {
    font-size: 15px;
  }

  .case-item p {
    font-size: 12px;
  }
}
</style>
