import adapter from "@sveltejs/adapter-node";
import autoprefixer from "autoprefixer";
import { vitePreprocess } from "@sveltejs/kit/vite";

/** @type {import('@sveltejs/kit').Config} */
const config = {
    // Consult https://kit.svelte.dev/docs/integrations#preprocessors
    // for more information about preprocessors
    preprocess: [
        vitePreprocess({
            postcss: {
                plugins: [autoprefixer()]
            }
        })
    ],

    kit: {
        adapter: adapter()
    }
};

export default config;
