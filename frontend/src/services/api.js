import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://localhost:8000/api/',
  headers: {
    'Content-Type': 'application/json',
  },
  withCredentials: true,
});

// Get current user profile
export function getUserProfile() {
  return apiClient.get('user-profile/');
}

// Update current user profile (only editable fields; backend ignores changes to karma, username, etc.)
export function updateUserProfile(payload) {
  return apiClient.post('user-profile/', payload);
}

export default apiClient;