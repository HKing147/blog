import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import ElementPlus from "element-plus";
import "element-plus/dist/index.css";
import * as ElementPlusIconsVue from "@element-plus/icons-vue";
import mavonEditor from "mavon-editor";
import "mavon-editor/dist/css/index.css";
import "highlight.js/lib/common";
import hljsVuePlugin from "@highlightjs/vue-plugin";
import VueCookies from "vue-cookies";

const app = createApp(App);
app.config.globalProperties.$cookies = VueCookies;
app.use(store).use(router).use(ElementPlus).use(mavonEditor).use(hljsVuePlugin);
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
	app.component(key, component);
}
app.mount("#app");
