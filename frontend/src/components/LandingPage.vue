<template>
  <div class="landing-page">
    <div class="content">
      <h1 class="main-heading">  LegalLink: Justice Made Easy</h1>
      <p class="subheading">Breaking Barriers. Empowering Citizens.</p>
      <p class="description">
        Know Your Rights.We break down legal terms into simple language.Free, Simple, For Everyone.
        No jargon. No wait. Just real support—when you need it.
      </p>
      <div class="button-group">
        <button class="contact-button" @click="authenticate">Get Started</button>
      </div>
    </div>
  </div>
</template>


<script>
export default {
  name: 'LandingPage',
  methods: {
    authenticate() {
      window.location.href = 'http://localhost:8000/accounts/google/login/';
    }
  }
}
</script>

<style scoped>
@keyframes fadeSlideIn {
  from {
    opacity: 0;
    transform: translateX(60px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

.landing-page {
  width: 100vw;
  height: 100vh;
  background: url('@/assets/copy.jpg') no-repeat center center;
  background-size: cover;
  background-color: #1a1a1a;
  display: flex;
  justify-content: flex-end;
  align-items: center;
  font-family: 'Georgia', serif;
  color: #fff;
  padding: 60px;
  box-sizing: border-box;
  overflow: hidden;
}

.content {
  max-width: 700px;
  background: rgba(0, 0, 0, 0.55);
  padding: 40px;
  border-radius: 12px;
  text-align: left;
  animation: fadeSlideIn 1.2s ease forwards;
}

.main-heading {
  font-size: 3.2em;
  font-weight: bold;
  margin-bottom: 10px;
  line-height: 1.2;
}

.subheading {
  font-size: 1.2em;
  margin-bottom: 20px;
  color: #ddd;
}

.description {
  font-size: 1em;
  line-height: 1.6;
  color: #ccc;
  margin-bottom: 30px;
}

.button-group {
  display: flex;
  gap: 15px;
}

.contact-button,
.explore-button {
  padding: 12px 28px;
  border-radius: 6px;
  font-size: 1em;
  cursor: pointer;
  transition: all 0.3s ease;
}

.contact-button {
  background-color: #6f42c1;
  color: #fff;
  border: none;
}

.contact-button:hover {
  background-color: #5a33a5;
  transform: scale(1.05);
}

.explore-button {
  background-color: transparent;
  color: #fff;
  border: 1px solid #ccc;
}

.explore-button:hover {
  background-color: #fff;
  color: #000;
  transform: scale(1.05);
}
</style>

