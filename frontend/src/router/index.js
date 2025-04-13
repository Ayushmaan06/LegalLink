import { createRouter, createWebHistory } from 'vue-router'
import LandingPage from '@/components/LandingPage.vue'
import ProfileSetup from '@/components/ProfileSetup.vue'
import HomePage from '@/components/HomePage.vue'
import Evault from '@/components/Evault.vue' 
import ProfilePage from '@/components/ProfilePage.vue'
import CaseModal from '@/components/CaseModal.vue'
const routes = [
  { path: '/', name: 'landing', component: LandingPage },
  { path: '/profile-setup', name: 'profile-setup', component: ProfileSetup },
  { path: '/home', name: 'homepage', component: HomePage },
  {path: '/evault', name: 'evault', component: Evault },
  { path: '/profile', name: 'profile', component: ProfilePage },
  { path: '/case-modal', name: 'case-modal', component: CaseModal }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router