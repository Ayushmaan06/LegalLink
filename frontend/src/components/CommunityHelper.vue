<template>
    <div class="community-helpers">
      <!-- Top Community Helpers Section -->
      <div class="section">
        <h3>Top Community Helpers</h3>
        <div v-if="helpers.length">
          <div v-for="helper in helpers" :key="helper.id" class="helper-item">
            <img :src="helper.avatar ? helper.avatar : defaultAvatar" alt="Helper Avatar" class="avatar">
            <div class="helper-info">
              <h4>{{ helper.username }}</h4>
              <p>Karma: {{ helper.karma }}</p>
              <p v-if="helper.contact_info">Contact: {{ helper.contact_info }}</p>
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
        <div v-if="recommendedHelper">
          <div class="helper-item">
            <img :src="recommendedHelper.avatar ? recommendedHelper.avatar : defaultAvatar" alt="Helper Avatar" class="avatar">
            <div class="helper-info">
              <h4>{{ recommendedHelper.username }}</h4>
              <p>Karma: {{ recommendedHelper.karma }}</p>
              <p v-if="recommendedHelper.contact_info">Contact: {{ recommendedHelper.contact_info }}</p>
            </div>
            <button class="upvote-btn" @click="upvoteHelper(recommendedHelper)">Upvote</button>
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
  import defaultIcon from '@/assets/user-icon.png' // Use user-icon.png from assets
  
  export default {
    name: 'CommunityHelper',
    props: {
      // Indicates whether the current user has an active case.
      activeCase: {
        type: Boolean,
        default: false
      }
    },
    setup(props) {
      const helpers = ref([])
      const recommendedHelper = ref(null)
      const defaultAvatar = defaultIcon
  
      // Fetch the top community helpers (e.g., top 5 sorted by karma) from the backend
      const fetchCommunityHelpers = async () => {
        try {
          const response = await axios.get('http://localhost:8000/api/community-helpers/', { withCredentials: true })
          // Expected structure: { helpers: [ { id, username, karma, avatar, contact_info } ] }
          // Assume backend limits it to top 5.
          helpers.value = response.data.helpers || []
        } catch (error) {
          console.error('Error fetching community helpers:', error)
        }
      }
  
      // If the user has an active case, fetch a recommended helper
      const fetchRecommendedHelper = async () => {
        try {
          const response = await axios.get('http://localhost:8000/api/recommended-community-helper/', { withCredentials: true })
          // Expected structure: { helper: { id, username, karma, avatar, contact_info } }
          recommendedHelper.value = response.data.helper || null
        } catch (error) {
          console.error('Error fetching recommended community helper:', error)
        }
      }
  
      // Upvote a helper. Only one upvote per (voter, voted) is allowed.
      const upvoteHelper = async (helper) => {
        try {
          const response = await axios.post('http://localhost:8000/api/upvote-user/', { target_id: helper.id }, { withCredentials: true })
          if (response.data.status === 'ok') {
            // Update the helper's karma to the new value returned.
            helper.karma = response.data.new_karma
          } else {
            console.error(response.data.message)
          }
        } catch (error) {
          console.error('Error upvoting:', error)
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
    padding: 16px;
    background-color: #fff;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  }
  .section {
    margin-bottom: 24px;
  }
  .section h3 {
    margin-bottom: 12px;
    color: #222;
  }
  .helper-item {
    display: flex;
    align-items: center;
    margin-bottom: 12px;
  }
  .avatar {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    object-fit: cover;
    margin-right: 12px;
  }
  .helper-info {
    flex: 1;
  }
  .helper-info h4 {
    margin: 0;
    font-size: 18px;
    color: #222;
  }
  .helper-info p {
    margin: 2px 0;
    font-size: 14px;
    color: #555;
  }
  .upvote-btn {
    background-color: gold;
    border: none;
    color: #222;
    padding: 6px 12px;
    border-radius: 4px;
    cursor: pointer;
  }
  .empty-state {
    text-align: center;
    font-style: italic;
    color: #888;
  }
  </style>
 