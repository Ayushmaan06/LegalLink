<template>
  <div class="profile-page">
    <HeaderNav />
    <div class="profile-container">
      <!-- Sidebar -->
      <aside class="sidebar">
        <div class="avatar-container">
          <img :src="avatarPreview || defaultAvatar" alt="User Avatar" class="avatar" />
          <input type="file" @change="onFileChange" accept="image/*" />
          <button v-if="newAvatar" @click="uploadAvatar">Upload Avatar</button>
        </div>

        <div class="helper-toggle checkbox-wrapper-46">
  <label class="cbx">
    <input type="checkbox" class="inp-cbx" v-model="user.is_helper" />
    <span class="checkbox-icon">
      <svg viewBox="0 0 12 10" height="10px" width="12px">
        <polyline points="1.5 6 4.5 9 10.5 1" />
      </svg>
    </span>
    <span class="checkbox-label">Wanna be a Community Helper?</span>
  </label>
</div>

        <div class="karma-info">
          <p>Karma: {{ user.karma }}</p>
        </div>

        <div class="contact-info">
          <label>
            Public Contact Info:
            <input type="text" v-model="user.contact_info" placeholder="e.g., Twitter: @user" />
          </label>
          <span class="tooltip">
            ?
            <span class="tooltiptext">
              Enter in the format "communication media : contact id"
            </span>
          </span>
        </div>
      </aside>

      <!-- Main Content -->
      <section class="main-content">
        <h2>User Information</h2>
        <form @submit.prevent="updateProfile">
          <div class="form-group">
            <label>Username:</label>
            <span>{{ user.username }}</span>
          </div>
          <div class="form-group">
            <label>First Name:</label>
            <span>{{ user.first_name }}</span>
          </div>
          <div class="form-group">
            <label>Last Name:</label>
            <span>{{ user.last_name }}</span>
          </div>
          <div class="form-group">
            <label>Age:</label>
            <input type="number" v-model="user.age" />
          </div>
          <div class="form-group">
            <label>Gender:</label>
            <select v-model="user.gender">
              <option value="male">Male</option>
              <option value="female">Female</option>
              <option value="other">Other</option>
            </select>
          </div>
          <div class="form-group">
            <label>City:</label>
            <input type="text" v-model="user.city" />
          </div>
          <div class="form-group">
            <label>State:</label>
            <input type="text" v-model="user.state" />
          </div>
          <button type="submit">Save Changes</button>
        </form>
      </section>
    </div>
  </div>
</template>

<script>
import HeaderNav from '@/components/HeaderNav.vue'
import { getUserProfile, updateUserProfile } from '@/services/api.js'
import axios from 'axios'

export default {
  name: 'ProfilePage',
  components: { HeaderNav },
  data() {
    return {
      defaultAvatar: require('@/assets/user-icon.png') || 'https://via.placeholder.com/200',
      loading: true,
      error: '',
      newAvatar: null,
      avatarPreview: '',
      user: {
        username: '',
        first_name: '',
        last_name: '',
        age: null,
        gender: '',
        city: '',
        state: '',
        is_helper: false,
        karma: 0,
        contact_info: '',
        avatar: ''
      }
    }
  },
  mounted() {
    this.fetchProfile()
  },
  methods: {
    async fetchProfile() {
      try {
        const response = await getUserProfile()
        const data = response.data
        this.user = { ...data }
        this.avatarPreview = data.avatar || this.defaultAvatar
      } catch (err) {
        this.error = err.message
      } finally {
        this.loading = false
      }
    },
    async updateProfile() {
      const payload = {
        age: this.user.age,
        gender: this.user.gender,
        city: this.user.city,
        state: this.user.state,
        is_helper: this.user.is_helper,
        contact_info: this.user.contact_info
      }
      try {
        const response = await updateUserProfile(payload)
        if (response.data.status === 'ok') {
          alert('Profile updated successfully!')
          this.fetchProfile()
        }
      } catch (err) {
        alert(err.message)
      }
    },
    onFileChange(event) {
      const file = event.target.files[0]
      if (file) {
        this.newAvatar = file
        this.avatarPreview = URL.createObjectURL(file)
      }
    },
    async uploadAvatar() {
      if (!this.newAvatar) return
      const formData = new FormData()
      formData.append('avatar', this.newAvatar)
      try {
        const response = await axios.post('http://localhost:8000/api/update-avatar/', formData, {
          headers: { 'Content-Type': 'multipart/form-data' },
          withCredentials: true
        })
        if (response.data.status === 'ok') {
          alert('Avatar updated successfully!')
          const newUrl = response.data.avatar
            ? response.data.avatar + '?t=' + new Date().getTime()
            : this.avatarPreview
          this.avatarPreview = newUrl
          this.user.avatar = newUrl
          this.newAvatar = null
        }
      } catch (err) {
        alert(err.message)
      }
    }
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');

.profile-page {
  background-color: #111;
  color: #fff;
  min-height: 100vh;
  font-family: 'Inter', 'Segoe UI', sans-serif;
}

.profile-container {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  margin: 20px auto;
  max-width: 1200px;
  padding: 0 16px;
}

.sidebar {
  flex: 0 0 280px;
  background: rgba(0, 0, 0, 0.7);
  backdrop-filter: blur(10px);
  border: 1px solid #444;
  border-radius: 16px;
  padding: 20px;
  box-shadow: 0 0 12px #FFD700;
}

.avatar-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;
  margin-bottom: 24px;
}

.avatar {
  width: 160px;
  height: 160px;
  object-fit: cover;
  border-radius: 50%;
  border: 4px solid #FFD700;
}

.avatar-container input[type="file"] {
  background: transparent;
  border: 1px solid #FFD700;
  color: #FFD700;
  padding: 8px;
  width: 100%;
  font-size: 14px;
  border-radius: 6px;
  text-align: center;
}

.avatar-container button {
  background-color: #FFD700;
  color: #111;
  border: none;
  padding: 10px 20px;
  border-radius: 6px;
  font-weight: 600;
  cursor: pointer;
  font-size: 15px;
  transition: background 0.3s ease;
}
.avatar-container button:hover {
  background-color: #ffe94d;
}

.karma-info,
.contact-info {
  margin: 16px 0;
}

.contact-info input {
  margin-top: 6px;
  padding: 8px;
  border: 1px solid #555;
  border-radius: 6px;
  background-color: #111;
  color: #fff;
  width: 100%;
  font-size: 14px;
  text-align: center;
}

.tooltip {
  display: inline-block;
  background-color: #FFD700;
  color: #111;
  border-radius: 50%;
  padding: 0 6px;
  margin-left: 5px;
  position: relative;
  cursor: pointer;
}

.tooltip .tooltiptext {
  visibility: hidden;
  opacity: 0;
  transition: opacity 0.3s ease;
  width: 240px;
  background-color: #FFD700;
  color: #111;
  text-align: center;
  border-radius: 6px;
  padding: 8px;
  position: absolute;
  z-index: 1;
  top: 30px;
  left: -20px;
  box-shadow: 0 0 6px rgba(255, 215, 0, 0.5);
}
.tooltip:hover .tooltiptext {
  visibility: visible;
  opacity: 1;
}

.main-content {
  flex: 1;
  min-width: 0;
  background: rgba(0, 0, 0, 0.7);
  border: 1px solid #444;
  backdrop-filter: blur(8px);
  padding: 24px;
  border-radius: 16px;
  box-shadow: 0 0 12px #FFD700;
}

.main-content h2 {
  font-size: 26px;
  margin-bottom: 24px;
  font-weight: 600;
  text-align: center;
}

.form-group {
  margin-bottom: 16px;
  text-align: left;
}

.form-group label {
  display: block;
  margin-bottom: 6px;
  font-weight: 500;
  font-size: 15px;
  color: #FFD700;
}

.form-group input,
.form-group select {
  width: 100%;
  padding: 10px;
  border: 1px solid #555;
  border-radius: 6px;
  background-color: #111;
  color: #fff;
  font-size: 14px;
}

button[type="submit"] {
  margin-top: 24px;
  background-color: #FFD700;
  color: #111;
  padding: 12px 24px;
  border: none;
  border-radius: 6px;
  font-weight: 600;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}
button[type="submit"]:hover {
  background-color: #ffe94d;
}

@media (max-width: 768px) {
  .profile-container {
    flex-direction: column;
  }
  .sidebar,
  .main-content {
    flex: 1 1 100%;
  }
  .avatar {
    width: 140px;
    height: 140px;
  }
}

/* ✅ Checkbox wrapper-46 styles with gold accent */
.checkbox-wrapper-46 input[type='checkbox'] {
  display: none;
  visibility: hidden;
}
.checkbox-wrapper-46 .cbx {
  display: flex;
  align-items: center;
  cursor: pointer;
  user-select: none;
}

.checkbox-wrapper-46 .cbx input[type='checkbox'] {
  display: none;
}

.checkbox-wrapper-46 .checkbox-icon {
  position: relative;
  width: 18px;
  height: 18px;
  border-radius: 3px;
  border: 1px solid #FFD700;
  margin-right: 8px;
  transition: all 0.2s ease;
}

.checkbox-wrapper-46 .checkbox-icon svg {
  position: absolute;
  top: 3px;
  left: 2px;
  fill: none;
  stroke: #111;
  stroke-width: 2;
  stroke-linecap: round;
  stroke-linejoin: round;
  stroke-dasharray: 16px;
  stroke-dashoffset: 16px;
  transition: all 0.3s ease;
  transition-delay: 0.1s;
}

.checkbox-wrapper-46 .inp-cbx:checked + .checkbox-icon {
  background: #FFD700;
  border-color: #FFD700;
  animation: wave-46 0.4s ease;
}

.checkbox-wrapper-46 .inp-cbx:checked + .checkbox-icon svg {
  stroke-dashoffset: 0;
}

.checkbox-wrapper-46 .checkbox-label {
  color: #fff;
  font-size: 14px;
}
</style>