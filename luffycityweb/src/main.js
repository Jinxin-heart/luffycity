import { createApp } from 'vue'
// import './style.css'
import App from './App.vue'
import 'element-plus/dist/index.css';
import store from './store'

import router from './router/index.js'

createApp(App).use(router).use(store).mount('#app')