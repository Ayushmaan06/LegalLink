<template>
  <div class="community-helpers">
    <!-- Top Community Helpers Section -->
    <div class="section">
      <h3>Top Community Helpers</h3>
      <div v-if="helpers.length">
        <div v-for="helper in helpers" :key="helper.id" class="helper-item">
          <img :src="helper.avatar ? helper.avatar : defaultAvatar" alt="Helper Avatar" class="avatar">
          <div class="helper-info">
            <span class="helper-title">{{ helper.username }}</span>
            <p>Karma: {{ helper.karma }}</p>
            <p v-if="helper.contact_info"> {{ helper.contact_info }}</p>
          </div>
          <button class="upvote-btn" @click="upvoteHelper(helper)">Upvote</button>
        </div>
      </div>
      <div v-else class="empty-state">
        <p>No community helpers available at the moment.</p>
      </div>
    </div>

    <!-- Recommended Community Helper (only if user has an active case) -->
    <div class="section" v-if="activeCase">
      <h3>Recommended Community Helper</h3>
      <div v-if="recommendedHelper.length">
        <div v-for="helper in recommendedHelper" :key="helper.id" class="helper-item">
          <img :src="helper.avatar ? helper.avatar : defaultAvatar" alt="Helper Avatar" class="avatar">
          <div class="helper-info">
            <span class="helper-title">{{ helper.username }}</span>
            <p>Karma: {{ helper.karma }}</p>
            <p v-if="helper.contact_info">{{ helper.contact_info }}</p>
          </div>
          <button class="upvote-btn" @click="upvoteHelper(helper)">Upvote</button>
        </div>
      </div>
      <div v-else class="empty-state">
        <p>No recommended helper right now.</p>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import defaultIcon from '@/assets/user-icon.png'

export default {
  name: 'CommunityHelper',
  props: {
    activeCase: {
      type: Boolean,
      default: false
    }
  },
  setup(props) {
    const helpers = ref([])
    const recommendedHelper = ref([])
    const defaultAvatar = defaultIcon

    const mockHelpers = [
      { id: 1, username: 'Ayushmaan', karma: 20, avatar: '', contact_info: 'tele:@snas' },
      { id: 2, username: 'Shubham', karma: 16, avatar: '', contact_info: 'tele:@shubh' },
      { id: 3, username: 'Sanket', karma: 12, avatar: '', contact_info: 'tele:@sank' }
    ]

    const mockRecommended = [
      { id: 2, username: 'Shubham', karma: 16, avatar: '', contact_info: 'tele:@shubh' },
      { id: 4, username: 'Ayush', karma: 9, avatar: '', contact_info: 'tele:@serief' }
    ]

    const fetchCommunityHelpers = async () => {
      try {
        const response = await axios.get('http://localhost:8000/api/community-helpers/', { withCredentials: true })
        helpers.value = response.data.helpers || mockHelpers
      } catch (error) {
        console.error('Error fetching community helpers:', error)
        helpers.value = mockHelpers
      }
    }

    const fetchRecommendedHelper = async () => {
      try {
        const response = await axios.get('http://localhost:8000/api/recommended-community-helper/', { withCredentials: true })
        recommendedHelper.value = response.data.helpers || mockRecommended
      } catch (error) {
        console.error('Error fetching recommended community helper:', error)
        recommendedHelper.value = mockRecommended
      }
    }

const upvoteHelper = async (helper) => {
// const originalKarma = helper.karma
  helper.karma += 1

  try {
    const response = await axios.post(
      'http://localhost:8000/api/upvote-user/',
      { target_id: helper.id },
      { withCredentials: true }
    )

    if (response.data.status === 'ok') {
      // Sync with backend value
      helper.karma = response.data.new_karma
    } else {
      console.error(response.data.message)
      // helper.karma = originalKarma // Revert on error
    }
  } catch (error) {
    console.error('Error upvoting:', error)
    // helper.karma = originalKarma // Revert on failure
  }
}

    onMounted(() => {
      fetchCommunityHelpers()
      if (props.activeCase) {
        fetchRecommendedHelper()
      }
    })

    return {
      helpers,
      recommendedHelper,
      defaultAvatar,
      upvoteHelper
    }
  }
}
</script>

<style scoped>
.community-helpers {
  padding: 24px;
  background-color: transparent;
  border-radius: 12px;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  color: #fefefe;
}

.section {
  margin-bottom: 24px;
}

.section h3 {
  margin-bottom: 12px;
  font-size: 18px;
  font-weight: 600;
  color: #facc15;
}

.helper-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 14px;
  border-radius: 10px;
  background-color: #2a2a2a;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
  margin-bottom: 10px;
}

.helper-info {
  flex: 1;
  margin-left: 10px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: center;
}

.avatar {
  width: 25px;
  height: 25px;
  object-fit: cover;
}

.helper-title {
  font-size: 15px;
}

.helper-info p {
  font-size: 12px;
  margin: 1px 0;
  color: #d1d5db;
}

.upvote-btn {
  flex-shrink: 0;
  background-color: #facc15;
  color: #1a1a1a;
  border: none;
  padding: 6px 10px;
  border-radius: 6px;
  font-size: 13px;
  font-weight: 500;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

.upvote-btn:hover {
  background-color: #fde047;
}

@media (max-width: 600px) {
  .helper-item {
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: flex-start;
  }

  .upvote-btn {
    margin-top: 6px;
  }
}
</style>
