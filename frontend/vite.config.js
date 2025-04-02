import {fileURLToPath, URL} from 'node:url'

import {defineConfig} from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'
import {resolve} from 'path'

// https://vite.dev/config/
export default defineConfig({
    plugins: [
        vue(),
        vueDevTools(),
    ],
    resolve: {
        alias: {
            '@': fileURLToPath(new URL('./src', import.meta.url))
        },
    },
    build: {
        assetsDir: "static",
        rollupOptions: {
            input: {
                main: resolve(__dirname, 'index.html'),
                document: resolve(__dirname, 'src/pages/Documents/index.html'),
            }
        }
    }
})