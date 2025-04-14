<template>
  <header class="header-nav">
    <!-- Logo + Brand -->
    <div class="logo" @click="goHome">
      <img src="@/assets/logo.png" alt="App Logo" class="logo-img" />
      <span class="brand-name">LegalLink</span>
    </div>

    <!-- Hamburger (Mobile) -->
    <div class="hamburger" @click="toggleMenu">
      <span :class="{ open: menuOpen }"></span>
      <span :class="{ open: menuOpen }"></span>
      <span :class="{ open: menuOpen }"></span>
    </div>

    <!-- Nav Links + Profile -->
    <nav :class="['nav-links', { open: menuOpen }]">
      <div class="nav-item" @click="goToLLM">
        <span>AI Assistant</span>
      </div>
      <div class="nav-item" @click="goToEVault">
        <span>LegalSafe</span>
      </div>
      <div class="nav-item" @click="goToLibrary">
        <span>Library</span>
      </div>

      <!-- Profile Button -->
      <div class="profile-btn" @click="goToProfile">
        <img src="@/assets/profile.png" alt="User Profile" class="icon" />
      </div>
    </nav>
  </header>
</template>

<script>
export default {
  name: 'HeaderNav',
  data() {
    return {
      menuOpen: false
    }
  },
  methods: {
    toggleMenu() {
      this.menuOpen = !this.menuOpen
    },
    goHome() {
      this.$router.push({ name: 'homepage' })
    },
    goToLLM() {
      window.open('http://localhost:8501', '_blank')
    },
    goToEVault() {
      this.$router.push({ path: '/evault' })
    },
    goToLibrary() {
      window.open('https://nalsa.gov.in/library', '_blank')
    },
    goToProfile() {
      this.$router.push({ path: '/profile' })
    }
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&family=Merriweather:wght@700&display=swap');

.header-nav {
  font-family: 'Poppins', sans-serif;
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: #000;
  color: white;
  padding: 0 20px;
  min-height: 65px;
  position: sticky;
  top: 0;
  z-index: 1000;
  border-bottom: 2px solid #333;
  flex-wrap: wrap;
}

.logo {
  display: flex;
  align-items: center;
  gap: 8px;
  cursor: pointer;
}

.logo-img {
  height: 58px;
}

.brand-name {
  font-family: 'Futura', 'Poppins', sans-serif; /* fallback in case Futura isn't available */
  font-size: 1.6rem;
  font-weight: 700;
  color: #FFD700; /* Golden */
  margin-left: 10px;
  letter-spacing: 1px;
  transition: color 0.3s ease;
}

.logo:hover .brand-name {
  color: #fffbe6; /* Soft gold hover */
}

.hamburger {
  display: none;
  flex-direction: column;
  gap: 5px;
  cursor: pointer;
  z-index: 1001;
}
.hamburger span {
  height: 3px;
  width: 25px;
  background: var(--accent-green);
  border-radius: 2px;
  transition: 0.3s;
}
.hamburger span.open:nth-child(1) {
  transform: rotate(45deg) translate(5px, 5px);
}
.hamburger span.open:nth-child(2) {
  opacity: 0;
}
.hamburger span.open:nth-child(3) {
  transform: rotate(-45deg) translate(6px, -6px);
}

.nav-links {
  display: flex;
  gap: 40px;
  font-weight: 500;
  transition: all 0.3s ease, opacity 0.3s ease;
  justify-content: flex-end;
  flex: 1;
  align-items: center;
}

.nav-item {
  display: flex;
  align-items: center;
  gap: 8px;
  cursor: pointer;
  color: var(--text-light);
  transition: color 0.3s ease;
}
.nav-item:hover span {
  color: #FFD700;
}

.profile-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  font-weight: 500;
  cursor: pointer;
  color: var(--text-light);
  transition: color 0.3s ease;
}

.profile-btn:hover {
  color: #FFD700;
}

.icon {
  width: 26px;
  height: 26px;
  filter: brightness(1.1);
}

/* Responsive Styles */
@media (max-width: 768px) {
  .hamburger {
    display: flex;
  }

  .nav-links {
    flex-direction: column;
    width: 100%;
    background: #000;
    padding: 10px 0;
    display: none;
    opacity: 0;
    align-items: center;
  }

  .nav-links.open {
    display: flex;
    opacity: 1;
  }

  .profile-btn {
    margin-top: 10px;
  }
}

@media (min-width: 769px) {
  .profile-btn {
    margin-left: 60px;
  }
}
</style>
