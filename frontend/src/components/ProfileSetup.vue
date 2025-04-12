<template>
    <div class="profile-setup">
      <h2>Profile Setup</h2>
      <form @submit.prevent="submitProfile">
        <div>
          <label for="first_name">First Name:</label>
          <input id="first_name" v-model="form.first_name" required />
        </div>
        <div>
          <label for="last_name">Last Name:</label>
          <input id="last_name" v-model="form.last_name" required />
        </div>
        <div>
          <label for="age">Age:</label>
          <input id="age" type="number" v-model="form.age" />
        </div>
        <div>
          <label for="gender">Gender:</label>
          <select id="gender" v-model="form.gender">
            <option value="male">Male</option>
            <option value="female">Female</option>
            <option value="other">Other</option>
          </select>
        </div>
        <div>
          <label for="city">City:</label>
          <input id="city" v-model="form.city" required />
        </div>
        <div>
          <label for="state">State:</label>
          <input id="state" v-model="form.state" />
        </div>
        <button type="submit">Submit Profile</button>
      </form>
      <div v-if="errorMessage" class="error">{{ errorMessage }}</div>
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  export default {
    name: 'ProfileSetup',
    data() {
      return {
        form: {
          first_name: '',
          last_name: '',
          age: null,
          gender: 'male',
          city: '',
          state: '',
        },
        errorMessage: ''
      }
    },
    methods: {
      submitProfile() {
        axios.post('http://localhost:8000/api/profile-setup-api/', this.form, { withCredentials: true })
          .then(response => {
            if (response.data.status === 'ok') {
              this.$router.push({ name: 'homepage' })
            } else {
              this.errorMessage = "There was an error updating your profile."
            }
          })
          .catch(error => {
            this.errorMessage = error.response?.data?.error || "Submission failed."
          })
      }
    }
  }
  </script>
  
  <style scoped>
  .profile-setup {
    max-width: 500px;
    margin: 0 auto;
    padding: 20px;
  }
  .error {
    color: red;
  }
  </style>