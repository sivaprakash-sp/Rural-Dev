// Base URL for the FastAPI backend (running on port 8080)
const API_BASE_URL = 'http://localhost:8080/api';

/**
 * Helper function to make API requests
 */
async function fetchFromAPI(endpoint, options = {}) {
  try {
    const response = await fetch(`${API_BASE_URL}${endpoint}`, {
      headers: {
        'Content-Type': 'application/json',
        // Add Authorization header here later for JWT
      },
      ...options
    });
    
    if (!response.ok) {
      throw new Error(`API error: ${response.status}`);
    }
    
    return await response.json();
  } catch (error) {
    console.error('API Connection Error:', error);
    throw error;
  }
}

/**
 * Check if the backend is running and connected
 */
async function checkBackendConnection() {
  try {
    const result = await fetchFromAPI('/health');
    console.log('✅ BACKEND CONNECTED:', result.message);
    return true;
  } catch (error) {
    console.error('❌ BACKEND NOT CONNECTED. Make sure FastAPI is running on port 8080.');
    return false;
  }
}
