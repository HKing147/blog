<template>
	<div class="container">
		<div class="wrap">
			<h3>请选择头像</h3>
			<div class="image">
				<el-upload
					class="avatar-uploader"
					action="api/uploadAvatar"
					:show-file-list="false"
					:on-success="handleAvatarSuccess"
					:before-upload="beforeAvatarUpload"
				>
					<img v-if="avatarPath" :src="'api/' + avatarPath" class="avatar" />
					<el-icon v-else class="avatar-uploader-icon"><Plus /></el-icon>
				</el-upload>
			</div>
			<el-button type="primary" @click="updateAvatar" round>上传头像</el-button>
		</div>
	</div>
</template>
<script setup>
import router from "@/router";
import { Get } from "@/utils/request";
import { ElMessage } from "element-plus";
import { reactive, ref } from "vue";
let avatarPath = ref("");

function handleAvatarSuccess(res, file) {
	console.log(res);
	avatarPath.value = res.data;
	console.log(avatarPath);
}

async function updateAvatar() {
	console.log(avatarPath);
	let data = await Get("updateAvatar", { avatarPath: avatarPath.value });
	console.log(data);
	ElMessage({
		message: data.meta.msg,
		type: data.meta.status == 200 ? "success" : "error",
	});
	if (data.meta.status == 200) {
		router.push("/" + data.data);
	}
}
// function handleAvatarSuccess(res, file) {
// 	imageUrl.value = URL.createObjectURL(file.raw);
// 	console.log(imageUrl);
// }
function Upload(a, b) {
	console.log(a, b);
}
</script>
<style scoped lang="scss">
.container {
	width: 100%;
	height: 100%;
	background: url("../assets/article.png");
	background-size: 100% 100%;
	position: absolute;

	// background-position: center center;
	background-attachment: fixed;
	background-repeat: no-repeat;
	.wrap {
		opacity: 0.95;
		background-color: white;
		width: 50%;
		margin: 80px auto;
		border-radius: 20px;
		display: flex;
		flex-direction: column;
		h3 {
			margin: 20px auto;
			// margin-top: 20px;
		}
		.image {
			margin: 0 auto;
			.avatar-uploader .avatar {
				width: 150px;
				height: 150px;
				display: block;
			}
		}
		.el-button {
			margin: 30px auto;
			width: 100px;
			height: 40px;
		}
	}
}
</style>
<style>
.avatar-uploader .el-upload {
	border: 1px dashed var(--el-border-color);
	border-radius: 6px;
	cursor: pointer;
	position: relative;
	overflow: hidden;
	transition: var(--el-transition-duration-fast);
}
.avatar-uploader .el-upload:hover {
	border-color: var(--el-color-primary);
}
.el-icon.avatar-uploader-icon {
	font-size: 28px;
	color: #8c939d;
	width: 150px;
	height: 150px;
	text-align: center;
}
</style>
