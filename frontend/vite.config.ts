import { sveltekit } from '@sveltejs/kit/vite';
import tailwindcss from '@tailwindcss/vite';
import { defineConfig } from 'vite';
const FRONT_PORT = Number(process.env.FRONT_PORT || 3000);
export default defineConfig({
	plugins: [tailwindcss(), sveltekit()],
	server: {
		port: FRONT_PORT,
		strictPort: true,
		proxy: {
			'/api': {
				target: 'http://192.168.20.19:9000/',
				changeOrigin: true
			}
		}
	}
});
