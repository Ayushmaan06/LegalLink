<template>
  <div class="profile-setup">
    <h2 class="animated-header">Sign Up</h2>
    <form @submit.prevent="submitProfile">
      <div class="form-group" v-for="(field, index) in fields" :key="index">
        <input
          :id="field.id"
          v-model="form[field.model]"
          :type="field.type"
          :placeholder="field.placeholder"
          required
        />
      </div>

      <div class="form-group">
        <select id="gender" v-model="form.gender">
          <option disabled value="">Select Gender</option>
          <option value="male">Male</option>
          <option value="female">Female</option>
          <option value="other">Other</option>
        </select>
      </div>

      <button class="Btn" @click="submitProfile" type="button">
        <div class="sign">
          <svg viewBox="0 0 512 512">
            <path
              d="M217.9 105.9L340.7 228.7c7.2 7.2 11.3 17.1 11.3 27.3s-4.1 20.1-11.3 27.3L217.9 406.1c-6.4 6.4-15 9.9-24 9.9c-18.7 0-33.9-15.2-33.9-33.9l0-62.1L32 320c-17.7 0-32-14.3-32-32l0-64c0-17.7 14.3-32 32-32l128 0 0-62.1c0-18.7 15.2-33.9 33.9-33.9c9 0 17.6 3.6 24 9.9zM352 416l64 0c17.7 0 32-14.3 32-32l0-256c0-17.7-14.3-32-32-32l-64 0c-17.7 0-32-14.3-32-32s14.3-32 32-32l64 0c53 0 96 43 96 96l0 256c0 53-43 96-96 96l-64 0c-17.7 0-32-14.3-32-32s14.3-32 32-32z"
            />
          </svg>
        </div>
        <div class="text">Submit</div>
      </button>
    </form>

    <div v-if="errorMessage" class="error">{{ errorMessage }}</div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'ProfileSetup',
  data() {
    return {
      form: {
        first_name: '',
        last_name: '',
        age: '',
        gender: '',
        city: '',
        state: '',
      },
      errorMessage: '',
      fields: [
        { id: 'first_name', model: 'first_name', placeholder: 'First Name', type: 'text' },
        { id: 'last_name', model: 'last_name', placeholder: 'Last Name', type: 'text' },
        { id: 'age', model: 'age', placeholder: 'Age', type: 'number' },
        { id: 'city', model: 'city', placeholder: 'City', type: 'text' },
        { id: 'state', model: 'state', placeholder: 'State', type: 'text' },
      ],
    };
  },
  mounted() {
    document.body.style.overflow = 'hidden';
  },
  unmounted() {
    document.body.style.overflow = 'auto';
  },
  methods: {
    submitProfile() {
      axios
        .post('http://localhost:8000/api/profile-setup-api/', this.form, {
          withCredentials: true,
        })
        .then((response) => {
          if (response.data.status === 'ok') {
            this.$router.push({ name: 'homepage' });
          } else {
            this.errorMessage = 'There was an error updating your profile.';
          }
        })
        .catch((error) => {
          this.errorMessage =
            error.response?.data?.error || 'Submission failed.';
        });
    },
  },
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap');

/* Outer rotating border + soft golden glow */
.profile-setup {
  max-width: 500px;
  margin: 40px auto;
  padding: 40px;
  border-radius: 20px;
  font-family: 'Roboto', sans-serif;
  color: #FFD700;
  position: relative;
  overflow: hidden;
  z-index: 2;

  /* ✨ Glowing border */
  box-shadow: 0 0 20px 3px rgba(255, 215, 0, 0.6), 0 0 40px 10px rgba(255, 215, 0, 0.2);
}

.profile-setup::before {
  content: '';
  position: absolute;
  width: 100px;
  height: 130%;
  background-image: linear-gradient(180deg, #ecc525, #ecc525);
  animation: rotBorder 3s linear infinite;
  z-index: 0;
}

.profile-setup::after {
  content: '';
  position: absolute;
  inset: 5px;
  border-radius: 15px;
  background: linear-gradient(-45deg, #000000, #1a1a1a, #333333, #1a1a1a);
  background-size: 400% 400%;
  animation: gradientMove 20s ease infinite;
  z-index: 1;
}

@keyframes rotBorder {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

@keyframes gradientMove {
  0% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0% 50%;
  }
}

.animated-header {
  position: relative;
  display: inline-block;
  padding: 10px 25px;
  font-size: 28px;
  font-weight: 700;
  text-transform: uppercase;
  color: #FFD700;
  background-color: #000000;
  border-radius: 12px;
  cursor: default;
  z-index: 2;
  overflow: hidden;
  transition: all 0.4s ease;
  box-shadow: 0 0 15px rgba(255, 215, 0, 0.5);
  text-align: center;
  margin: 0 auto 30px;
}

.animated-header::before {
  content: "";
  position: absolute;
  inset: 0;
  z-index: -1;
  background: #FFD700;
  border-radius: 12px;
  transform: scaleX(0);
  transform-origin: left;
  transition: transform 0.4s ease;
}

.animated-header:hover::before {
  transform: scaleX(1);
}

.animated-header:hover {
  color: #000000;
}

.form-group {
  margin-bottom: 20px;
  z-index: 2;
  position: relative;
}

input,
select {
  width: 100%;
  padding: 12px 15px;
  background-color: #222;
  color: #FFD700;
  border: 1px solid #FFD700;
  border-radius: 12px;
  font-size: 16px;
  transition: box-shadow 0.3s ease, background-color 0.3s ease;
}

input:focus,
select:focus {
  outline: none;
  box-shadow: 0 0 18px rgba(255, 215, 0, 0.8);
  background-color: #444;
}

.error {
  margin-top: 20px;
  color: #E74C3C;
  text-align: center;
  font-weight: 600;
  font-size: 16px;
  z-index: 2;
  position: relative;
}

.Btn {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 45px;
  height: 45px;
  border: none;
  border-radius: 50%;
  cursor: pointer;
  position: relative;
  overflow: hidden;
  transition: all 0.3s ease;
  background-color: #000;
  border: 1px solid #FFD700;
  color: #FFD700;
  margin: 25px auto 0;
  z-index: 2;
}

.sign {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: width 0.3s ease;
}

.sign svg {
  width: 17px;
}

.sign svg path {
  fill: #FFD700;
}

.text {
  position: absolute;
  right: 0;
  width: 0%;
  opacity: 0;
  color: #FFD700;
  font-size: 1em;
  font-weight: 600;
  transition: all 0.3s ease;
  text-align: center;
}

.Btn:hover {
  width: 100%;
  max-width: 100%;
  border-radius: 12px;
}

.Btn:hover .sign {
  opacity: 0;
  width: 0;
}

.Btn:hover .text {
  opacity: 1;
  width: 100%;
  padding-right: 0;
}

.Btn:active {
  transform: translate(2px, 2px);
}
</style>
