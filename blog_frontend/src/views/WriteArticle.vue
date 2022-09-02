<template>
	<div class="container">
		<el-form
			:model="article"
			status-icon
			label-width="100px"
			class="articleForm"
		>
			<el-form-item label="文章标题" prop="title" required>
				<el-input v-model="article.title" type="txt" autocomplete="off" />
			</el-form-item>
			<el-form-item label="文章摘要" prop="abstract">
				<el-input v-model="article.abstract" autocomplete="off" />
			</el-form-item>
			<el-form-item label="文章类别" prop="categoryId" class="labels" required>
				<el-select
					v-model="article.categoryId"
					filterable
					default-first-option
					:reserve-keyword="false"
					placeholder="Choose tags for your article"
				>
					<el-option
						v-for="item in categoryOptions"
						:key="item.categoryName"
						:value="item.id"
						:label="item.categoryName"
					/>
				</el-select>
				<el-input v-model="addcategory" />
				<el-button type="primary" @click="addCategory">添加</el-button>
			</el-form-item>
			<el-form-item label="文章标签" prop="labels" class="labels">
				<el-select
					v-model="article.selectedLabels"
					multiple
					filterable
					default-first-option
					:reserve-keyword="false"
					placeholder="Choose tags for your article"
				>
					<el-option
						v-for="item in labelOptions"
						:key="item.labelId"
						:value="item.labelName"
					/>
				</el-select>
				<el-input v-model="addlabel" />
				<el-button type="primary" @click="addLabel">添加</el-button>
			</el-form-item>
			<el-form-item label="文章封面" prop="coverPath" class="coverImage">
				<el-upload
					class="avatar-uploader"
					action="api/uploadCover"
					:show-file-list="false"
					:on-success="handleAvatarSuccess"
					:before-upload="beforeAvatarUpload"
				>
					<img
						v-if="article.coverPath"
						:src="'api/' + article.coverPath"
						class="avatar"
					/>
					<el-icon v-else class="avatar-uploader-icon"><Plus /></el-icon>
				</el-upload>
			</el-form-item>
			<el-form-item label="文章内容" prop="content">
				<mavonEditor
					v-model="article.content"
					ref="mdedit"
					:ishljs="true"
					codeStyle="tomorrow-night-eighties"
					@imgAdd="imgAdd"
				/>
			</el-form-item>
			<el-form-item>
				<el-button type="primary" @click="submitForm()">发布</el-button>
				<!-- <el-button @click="resetForm(ruleFormRef)">Reset</el-button> -->
			</el-form-item>
		</el-form>
	</div>
</template>
<!-- <script>
import { mavonEditor } from "mavon-editor";
import "mavon-editor/dist/css/index.css";
import { reactive } from "vue";
import { $get, $post } from "@/utils/request";
export default {
	name: "WriteArticle",
	components: {
		mavonEditor,
	},
	setup() {
		let article = reactive({
			title: "",
			abstract: "",
			categoryName: "",
			labelName: "",
			content: "### 这是一个标题",
		});
		async function submitForm() {
			console.log(article);
			let data = await $get("writeArticle", article);
			console.log(data);
			ElMessage({
				message: data.meta.msg,
				type: data.meta.status == 200 ? "success" : "error",
			});
		}
		return { article, submitForm };
	},
};
</script> -->

<script setup>
import { mavonEditor } from "mavon-editor";
import "mavon-editor/dist/css/index.css";
import { onBeforeMount, onMounted, reactive, ref } from "vue";
import { Get, Post } from "@/utils/request";
import { ElMessage } from "element-plus";
// 标签列表
let labelOptions = reactive([
	{
		labelId: 1,
		labelName: "Linux",
	},
	{
		labelId: 1,
		labelName: "Mysql",
	},
	{
		labelId: 1,
		labelName: "算法",
	},
	{
		labelId: 1,
		labelName: "Django",
	},
]);
// 获取标签列表
async function getLabelList() {
	console.log("获取标签列表");
	let data = await Get("getLabelList");
	console.log(data);
	ElMessage({
		message: data.meta.msg,
		type: data.meta.status == 200 ? "success" : "error",
	});
	return data.data;
}
labelOptions = await getLabelList();

// 类别列表
let categoryOptions = reactive([
	{
		Id: 1,
		categoryName: "Linux",
	},
	{
		Id: 1,
		categoryName: "Mysql",
	},
	{
		Id: 1,
		categoryName: "算法",
	},
	{
		Id: 1,
		categoryName: "Django",
	},
]);
// 获取类别列表
async function getCategoryList() {
	console.log("获取类别列表");
	let data = await Get("getCategoryList");
	console.log(data);
	ElMessage({
		message: data.meta.msg,
		type: data.meta.status == 200 ? "success" : "error",
	});
	return data.data;
}
categoryOptions = await getCategoryList();
console.log("categoryOptions: ", categoryOptions);

// 添加标签
let addlabel = ref("");
async function addLabel() {
	console.log("添加标签", addlabel.value);
	let data = await Get("addLabel", addlabel.value);
	console.log(data);
	ElMessage({
		message: data.meta.msg,
		type: data.meta.status == 200 ? "success" : "error",
	});
	labelOptions = await getLabelList();
}

// 添加类别
let addcategory = ref("");
async function addCategory() {
	// categoryOptions = reactive(await getCategoryList());
	// console.log("+++");
	// console.log(categoryOptions[0].id, categoryOptions[0].categoryName);
	// for (item in categoryOptions) console.log(item);
	// return;
	console.log("添加类别", addcategory.value);
	let data = await Get("addCategory", addcategory.value);
	console.log(data);
	ElMessage({
		message: data.meta.msg,
		type: data.meta.status == 200 ? "success" : "error",
	});
}

let article = reactive({
	title: "标题",
	abstract: "摘要",
	categoryName: "",
	categoryId: null,
	selectedLabels: [],
	categoryOptions: [],
	labels: "",
	coverPath: null,
	content: "### 这是一个标题",
});

function handleAvatarSuccess(res, file) {
	console.log(res);
	article.coverPath = res.coverPath;
	// article.coverPath = URL.createObjectURL(file.raw);
	console.log(article.coverPath);
}

// 文章正文上传图片
const mdedit = ref();
async function imgAdd(pos, file) {
	console.log("aa", pos);
	console.log("bb", file);
	let imgData = new FormData();
	imgData.append("file", file);
	let data = await Post("uploadImage", imgData);
	console.log(data);
	// console.log(mdedit.value.$img2Url);
	mdedit.value.$img2Url(pos, "api/" + data.imagerPath);
}
// 发布博客
async function submitForm() {
	console.log(article);
	article.labels = article.selectedLabels[0];
	for (let i = 1; i < article.selectedLabels.length; i++) {
		article.labels += "-" + article.selectedLabels[i];
	}
	console.log("lables: ", article.labels);
	let data = await Get("writeArticle", article);
	console.log(data);
	ElMessage({
		message: data.meta.msg,
		type: data.meta.status == 200 ? "success" : "error",
	});
}
// onMounted(async () => {
// 	categoryOptions.push(...(await getCategoryList()));
// 	console.log(categoryOptions, "---");
// });

// onMounted(){
//     console.log("onMounted");
// 	categoryOptions = getCategoryList();
// }
// async onBeforeMount(() => {
// 	console.log("onMounted");
// 	categoryOptions = getCategoryList();
// 	console.log("category", categoryOptions);
// });
// onBeMounted(() => {
//     console.log("onMounted");
// 	categoryOptions = getCategoryList();
// }),
</script>
<style scoped lang="scss">
.container {
	width: 100%;
	height: 100%;
	background: url("../assets/article.png");
	background-size: cover;
	position: absolute;
	// background-position: center center;
	background-attachment: fixed;
	.articleForm {
		opacity: 0.9;
		margin: 0 auto;
		margin-top: 50px;
		border-radius: 20px;
		width: 70%;
		padding-top: 20px;
		padding-bottom: 20px;
		background-color: white;
		.el-input {
			// width: 70%;
			width: 70%;
		}
		.labels {
			.el-select {
				width: 30%;
			}
			.el-input {
				width: 30%;
				margin-left: 20px;
				margin-right: 20px;
			}
		}
		.coverImage {
			.avatar-uploader .avatar {
				width: 100px;
				height: 100px;
				display: block;
			}
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
	width: 100px;
	height: 100px;
	text-align: center;
}
</style>
