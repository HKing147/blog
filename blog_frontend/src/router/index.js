import { createRouter, createWebHashHistory } from "vue-router";

const routes = [
	{
		path: "/",
		name: "Index",
		component: () => import("../views/Index.vue"),

		//添加权限访问，表示只有登录之后才能进行该操作
		meta: {
			requireAuth: true,
		},
	},
	{
		path: "/login",
		name: "Login",
		component: () => import("../views/Login.vue"),
	},
	{
		path: "/register",
		name: "Register",
		component: () => import("../views/Register.vue"),
	},
	{
		path: "/articleCard",
		name: "ArticleCard",
		component: () => import("../components/ArticleCard.vue"),
	},
	{
		path: "/archive",
		name: "Archive",
		component: () => import("../views/Archive.vue"),
	},
	{
		path: "/category",
		name: "Category",
		component: () => import("../views/Category.vue"),
	},
	{
		path: "/label",
		name: "Label",
		component: () => import("../views/Label.vue"),
	},
	{
		path: "/article",
		name: "Article",
		component: () => import("../views/Article.vue"),
	},
	{
		path: "/writeArticle",
		name: "WriteArticle",
		component: () => import("../views/WriteArticle.vue"),
	},
	{
		path: "/uploadAvatar",
		name: "UploadAvatar",
		component: () => import("../views/UploadAvatar.vue"),
	},
	{
		path: "/test",
		name: "Test",
		component: () => import("../views/Test.vue"),
	},
	{
		path: "/testAvatar",
		name: "testAvatar",
		component: () => import("../views/testAvatar.vue"),
	},
];

const router = createRouter({
	history: createWebHashHistory(),
	routes,
});

import NProgress from "nprogress";
import "nprogress/nprogress.css";

let pathList = ["/login", "/register"]; // 白名单
router.beforeEach((to, from, next) => {
	if (pathList.includes(to.path)) {
		NProgress.start();
		next();
	} else {
		let cookie = document.cookie;
		console.log(cookie);
		if (!cookie) {
			NProgress.start();
			next("/login");
		} else {
			NProgress.start();
			next();
		}
	}
});

router.afterEach((to, from) => {
	NProgress.done();
});

// 导航守卫
// 使用 router.beforeEach 注册一个全局前置守卫，判断用户是否登陆
// router.beforeEach((to, from, next) => {
//   if (to.path === '/login') {
//     next();
//   } else {
//     let token = localStorage.getItem('Authorization');
//
//     if (token === null || token === '') {
//       next('/login');
//     } else {
//       next();
//     }
//   }
// });

export default router;
