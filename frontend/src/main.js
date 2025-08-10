import { createApp } from 'vue'
import App from './App.vue'
import axios from 'axios'

axios.defaults.baseURL = import.meta.env.VITE_API_BASE || 'http://127.0.0.1:8000'

createApp(App).mount('#app')
