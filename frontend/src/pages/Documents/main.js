import {createApp} from 'vue'
import App from './App.vue'
import router from './router'
import api from "@/components/api.vue"
import store from "./store"

import '/src/assets/main.css'

const app = createApp(App)

app.use(router)
app.use(store)
app.mount('#app')
app.component("api", api)