import axios from 'axios';

// Determine API URL based on environment
const apiURL = process.env.NODE_ENV === 'production' 
  ? 'http://backend:8000/api/'  // Docker service name in production
  : 'http://localhost:8000/api/'; // Local development

const apiClient = axios.create({
  baseURL: apiURL,
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