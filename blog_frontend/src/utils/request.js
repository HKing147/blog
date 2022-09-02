import axios from "axios";
import nprogress from "nprogress";
import NProgress from "nprogress";
import "nprogress/nprogress.css";
import { BASE_URL } from "../config/conster";

var instance = axios.create({
	baseURL: BASE_URL,
	timeout: 30000,
});

instance.interceptors.request.use(
	function (config) {
		nprogress.start();
		return config;
	},
	function (error) {
		NProgress.done();
		return Promise.reject(error);
	}
);

instance.interceptors.response.use(
	function (response) {
		NProgress.done();
		return response;
	},
	function (error) {
		NProgress.done();
		return Promise.reject(error);
	}
);

export let Get = async (url, params) => {
	let { data } = await instance.get(url, { params: params });
	return data;
};

export let Post = async (url, params) => {
	let { data } = await instance.post(url, params);
	return data;
};
