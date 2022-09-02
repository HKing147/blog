import { $get, $post } from "@/utils/request";

// 用户登录接口
export let login = async (params) => {
	let data = await $get("Login", params);
	console.log(data);
};
