<template>
    <div class="profile-page">
      <!-- Header -->
      <HeaderNav />
  
      <div class="profile-container">
        <!-- Left Sidebar -->
        <aside class="sidebar">
          <div class="avatar-container">
          <!-- Use defaultAvatar if avatarPreview is empty -->
          <img :src="avatarPreview || defaultAvatar" alt="User Avatar" class="avatar">
          <input type="file" @change="onFileChange" accept="image/*">
          <button v-if="newAvatar" @click="uploadAvatar">Upload Avatar</button>
        </div>
  
          <div class="helper-toggle">
            <label>
              <input type="checkbox" v-model="user.is_helper">
              Wanna be a Community Helper?
            </label>
          </div>
  
          <div class="karma-info">
            <p>Karma: {{ user.karma }}</p>
          </div>
  
          <div class="contact-info">
            <label>
              Public Contact Info:
              <input type="text" v-model="user.contact_info" placeholder="e.g., Twitter: @user">
            </label>
            <span class="tooltip">
              ?
              <span class="tooltiptext">
                Enter in the format "communication media : contact id"
              </span>
            </span>
          </div>
        </aside>
  
        <!-- Middle Section: User Information -->
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
              <input type="number" v-model="user.age">
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
              <input type="text" v-model="user.city">
            </div>
            <div class="form-group">
              <label>State:</label>
              <input type="text" v-model="user.state">
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
        // Store file when user selects a new avatar.
        newAvatar: null,
        avatarPreview: '', 
        user: {
          username: "",
          first_name: "",
          last_name: "",
          age: null,
          gender: "",
          city: "",
          state: "",
          is_helper: false,
          karma: 0,
          contact_info: "",
          avatar: ""
        }
      }
    },
    mounted() {
      this.fetchProfile();
    },
    methods: {
      async fetchProfile() {
        try {
          const response = await getUserProfile();
          const data = response.data;
          console.log("Fetched profile avatar:", data.avatar); // Debug: log returned avatar URL
          this.user = {
            username: data.username,
            first_name: data.first_name,
            last_name: data.last_name,
            age: data.age,
            gender: data.gender,
            city: data.city,
            state: data.state,
            is_helper: data.is_helper,
            karma: data.karma,
            contact_info: data.contact_info,
            avatar: data.avatar
          };
          this.avatarPreview = data.avatar || this.defaultAvatar;
        } catch (err) {
          this.error = err.message;
        } finally {
          this.loading = false;
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
        };
        try {
          const response = await updateUserProfile(payload);
          if (response.data.status === "ok") {
            alert("Profile updated successfully!");
            this.fetchProfile();
          }
        } catch (err) {
          alert(err.message);
        }
      },
      onFileChange(event) {
        const file = event.target.files[0];
        if (file) {
          this.newAvatar = file;
          this.avatarPreview = URL.createObjectURL(file);
        }
      },
      async uploadAvatar() {
        if (!this.newAvatar) return;
        const formData = new FormData();
        formData.append("avatar", this.newAvatar);
        try {
            const response = await axios.post('http://localhost:8000/api/update-avatar/', formData, {
            headers: {
                'Content-Type': 'multipart/form-data'
            },
            withCredentials: true
            });
            if (response.data.status === 'ok') {
            alert("Avatar updated successfully!");
            // Update the avatarPreview with the URL returned from the backend
            const newUrl = response.data.avatar 
        ? response.data.avatar + "?t=" + new Date().getTime() 
        : this.avatarPreview;
      this.avatarPreview = newUrl;
      this.user.avatar = newUrl;
      this.newAvatar = null;
            }
        } catch (err) {
            alert(err.message);
        }
        }
    }
  }
  </script>
  
  <style scoped>
  .profile-page {
    background-color: #222;
    color: gold;
    min-height: 100vh;
    padding: 20px;
  }
  
  .profile-container {
    display: flex;
    gap: 20px;
  }
  
  /* Sidebar Styles */
  .sidebar {
    flex: 0 0 300px;
    background-color: #333;
    border-radius: 10px;
    padding: 20px;
    text-align: center;
  }
  
  .avatar-container {
  width: 200px;
  /* Remove fixed height so that file input and button are visible */
  margin-bottom: 20px;
  position: relative;
  /* Remove overflow: hidden; */
  /* Optionally, add display: flex; flex-direction: column; gap: 10px; */
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
}

.avatar {
  width: 200px !important;
  height: 200px !important;
  object-fit: cover !important;
  border-radius: 50% !important;
  border: 4px solid gold !important;
  display: block;
}

/* File input and button styling remain the same */
.avatar-container input[type="file"] {
  margin-top: 10px;
  display: block;
  width: 100%;
  color: gold;
  background-color: #222;
  border: 1px solid gold;
}

.avatar-container button {
  background-color: gold;
  color: #222;
  border: none;
  padding: 8px 16px;
  border-radius: 4px;
  cursor: pointer;
}
  .helper-toggle {
    margin-bottom: 15px;
    font-size: 16px;
  }
  
  .karma-info {
    margin-bottom: 15px;
    font-size: 16px;
  }
  
  .contact-info {
    margin-bottom: 15px;
    font-size: 16px;
    position: relative;
  }
  
  .contact-info input {
    margin-top: 5px;
    padding: 5px;
    border-radius: 4px;
    border: 1px solid gold;
    background-color: #222;
    color: gold;
    text-align: center;
  }
  
  .tooltip {
    display: inline-block;
    background-color: gold;
    color: #222;
    padding: 2px 5px;
    border-radius: 50%;
    cursor: help;
    margin-left: 5px;
    position: relative;
  }
  
  .tooltip .tooltiptext {
    visibility: hidden;
    width: 220px;
    background-color: gold;
    color: #222;
    text-align: center;
    border-radius: 6px;
    padding: 5px;
    position: absolute;
    z-index: 1;
    top: 25px;
    left: -20px;
  }
  
  .tooltip:hover .tooltiptext {
    visibility: visible;
  }
  
  /* Main Content Styles */
  .main-content {
    flex: 1;
    background-color: #333;
    border-radius: 10px;
    padding: 20px;
    text-align: left;
  }
  
  .form-group {
    margin-bottom: 15px;
  }
  
  .form-group label {
    display: block;
    margin-bottom: 5px;
    font-weight: 600;
  }
  
  .form-group input,
  .form-group select {
    width: 100%;
    padding: 8px;
    border-radius: 4px;
    border: 1px solid gold;
    background-color: #222;
    color: gold;
  }
  
  button[type="submit"] {
    background-color: gold;
    color: #222;
    padding: 10px 20px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  </style>
 