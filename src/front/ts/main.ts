import { createApp } from "vue";
import App from "../components/App.vue";

import { router } from "./router.ts";


createApp(App)
    .use(router)
    .mount("#app")

console.log("start");
