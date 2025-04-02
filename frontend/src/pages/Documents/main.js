import '/src/assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import api from "@/components/api.vue"

const app = createApp(App)

app.use(router)

app.mount('#app')
app.component("api", api)
