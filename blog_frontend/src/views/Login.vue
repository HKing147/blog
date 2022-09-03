<template>
	<div class="container">
		<div class="content">
			<h1>Sign In</h1>
			<el-form ref="formRef" :model="loginForm" label-width="100px">
				<div class="inputs">
					<el-form-item
						label="用户名"
						prop="userName"
						:rules="[{ required: true, message: '请输入用户名' }]"
					>
						<el-input
							v-model.number="loginForm.userName"
							type="text"
							autocomplete="off"
						/>
					</el-form-item>
					<el-form-item
						label="密码"
						prop="password"
						:rules="[
							{ required: true, message: '请输入密码' },
							{
								min: 6,
								max: 18,
								message: '长度在 6 到 18 个字符',
								trigger: 'blur',
							},
						]"
					>
						<el-input
							v-model.number="loginForm.password"
							type="password"
							autocomplete="off"
						/>
					</el-form-item>
				</div>
				<div class="btns">
					<el-button
						size="large"
						type="primary"
						@click="Login(loginForm)"
						round
					>
						登录
					</el-button>
					<el-button size="large" round @click="toRegister"> 注册 </el-button>
				</div>
			</el-form>
		</div>
	</div>
</template>
<script setup>
import router from "@/router";
import { Get, Post } from "@/utils/request";
import { reactive } from "vue";
import { ElMessage } from "element-plus";

// import { login } from "@/api/user";
let loginForm = reactive({
	userName: "user1",
	password: "asfdasdasd",
});
console.log(loginForm);
async function Login(loginForm) {
	let data = await Get("login", loginForm);
	console.log(data);
	ElMessage({
		message: data.meta.msg,
		type: data.meta.status == 200 ? "success" : "error",
	});
	if (data.meta.status == 200) {
		router.push("/" + data.data);
	}
}
function toRegister() {
	router.push("/register");
}
</script>
<style scoped lang="scss">
.container {
	width: 100%;
	height: 100%;
	background: url("../assets/background.png");
	background-size: 100% 100%;
	background-repeat: no-repeat;
	position: absolute;
	color: #71abdd;
	.content {
		text-align: center;
		width: 30%;
		height: 35%;
		border-radius: 10px;
		background-color: white;
		margin: 10% auto;
		display: flex;
		flex-direction: column;
		box-shadow: 2px 2px 5px #417ac0;
		h1 {
			margin-top: 25px;
			margin-bottom: 20px;
		}
		.inputs {
			margin-right: 10%;
			margin-top: 10px;
			// padding: 2% 2% 2% 0;
			// vertical-align: middle;
			// left: 50%;
			// top: 50%;
			// -webkit-transform: translate(-50%, -50%);
			el-input {
				padding-bottom: 20px;
				// margin-bottom: 20px;
			}
			.btns {
				margin-top: 20px;
				display: flex;
				// flex-direction: row;
				justify-content: center; /* 水平居中 */
				align-items: center; /* 垂直居中 */
				// align-items: center;
				// display: flex;
				// align-items: center;
				// background-color: aqua;

				el-button {
					width: 500px;
				}
			}
		}
	}
}
</style>
