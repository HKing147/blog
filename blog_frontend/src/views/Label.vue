<template>
	<div class="container">
		<el-backtop :right="50" :bottom="50" />
		<div class="header">
			<el-row :gutter="28">
				<el-col :span="6">
					<img
						src="../assets/logo.png"
						style="float: left; margin-left: 10px"
					/>
				</el-col>
				<el-col :span="3" class="items">
					<div @click="toIndex(ckUserId)">首页</div>
				</el-col>
				<el-col :span="3" class="items">
					<div @click="toArchive">归档</div>
				</el-col>
				<el-col :span="3" class="items">
					<div @click="toCategory">分类</div>
				</el-col>
				<el-col :span="3" class="items">
					<div @click="toLabel">标签</div>
				</el-col>
				<el-col :span="6">
					<div
						style="display: flex; flex-direction: row; vertical-align: middle"
					>
						<img
							:src="'api/' + currentUserInfo.avatarPath"
							style="
								height: 50px;
								width: 50px;
								border-radius: 25px;
								margin-left: 200px;
								cursor: pointer;
							"
							@click="toIndex(currentUserInfo.id)"
						/>
						<el-dropdown @command="handleCommand">
							<el-button
								type="primary"
								style="
									height: 40px;
									width: 80px;
									border-radius: 25px;
									margin-left: 20px;
									margin-top: 5px;
								"
							>
								<el-icon :size="20">
									<Edit />
								</el-icon>
								<el-icon class="el-icon--right"><arrow-down /></el-icon>
							</el-button>
							<template #dropdown>
								<el-dropdown-menu>
									<el-dropdown-item command="/WriteArticle"
										>发布博客</el-dropdown-item
									>
									<el-dropdown-item command="/UploadAvatar"
										>上传头像</el-dropdown-item
									>
								</el-dropdown-menu>
							</template>
						</el-dropdown>
					</div>
				</el-col>
			</el-row>
		</div>
		<div class="main">
			<!-- <el-affix class="left" :offset="0"> -->
			<el-affix class="left" :offset="90">
				<div class="left-top">
					<img
						:src="'api/' + ckUserInfo.avatarPath"
						style="cursor: pointer"
						@click="toIndex(ckUserInfo.id)"
					/>
					<p v-text="ckUserInfo.name"></p>
					<div class="txts">
						<div>
							文章
							<p v-text="articleList.length"></p>
						</div>
						<div>
							分类
							<p v-text="categoryList.length"></p>
						</div>
						<div>
							标签
							<p v-text="labelList.length"></p>
						</div>
					</div>
				</div>
				<!-- </div> -->
			</el-affix>
			<!-- </el-affix> -->
			<el-scrollbar class="content">
				<div class="labels">
					<p>标签</p>
					<div class="down">
						<a v-for="label in labelList" class="item">
							<span v-text="label.labelName" class="name"></span>
							<span v-text="label.count" class="count"></span>
						</a>
					</div>
					<!-- <div v-for="item in categoryList" class="item">
						<span class="name" v-text="item.categoryName"></span>
						<span class="number">13</span>
					</div> -->
				</div>
			</el-scrollbar>
			<div class="right">
				<div>
					<div class="Classification">
						<el-card class="box-card">
							<template #header>
								<div class="card-header">
									<div>
										<el-icon color="#1e90ff">
											<Menu />
										</el-icon>
										<span>分类</span>
									</div>
									<span @click="toCategory">更多 >></span>
								</div>
							</template>
							<div style="display: flex; flex-direction: column">
								<div
									v-for="category in categoryList"
									:key="category.categoryId"
									class="text item"
									style="margin-bottom: 5px"
								>
									<span
										v-text="category.categoryName"
										style="float: left"
									></span>
									<span v-text="category.count" style="float: right"></span>
								</div>
							</div>
						</el-card>
					</div>
					<div class="Label">
						<el-card class="box-card">
							<template #header>
								<div class="card-header">
									<div>
										<el-icon color="#1e90ff">
											<Menu />
										</el-icon>
										<span>标签</span>
									</div>
									<span @click="toLabel">更多 >></span>
								</div>
							</template>
							<div style="display: flex; flex-direction: column">
								<div
									v-for="label in labelList"
									:key="label.labelId"
									class="text item"
									style="margin-bottom: 5px"
								>
									<span v-text="label.labelName" style="float: left"></span>
									<span v-text="label.count" style="float: right"></span>
								</div>
							</div>
						</el-card>
					</div>
				</div>
				<!-- </el-affix> -->
			</div>
		</div>
	</div>
</template>
<script setup>
import { reactive } from "vue";
import { Get } from "@/utils/request";
import { ElMessage } from "element-plus";
import router from "@/router";
import { useRoute } from "vue-router";
import { Edit } from "@element-plus/icons-vue";
const $route = useRoute();

let ckUserId = $route.params.id;

console.log("ckUserId", ckUserId);
// 获取当前页面用户的相关信息
let ckUserInfo = reactive({});
async function getCkUserInfo() {
	console.log("开始获取当前页面用户信息");
	let data = await Get("getCkUserInfo", { ckUserId: ckUserId });
	console.log(data);
	ElMessage({
		message: data.meta.msg,
		type: data.meta.status == 200 ? "success" : "error",
	});
	return data.data;
}
ckUserInfo = await getCkUserInfo();

// 获取当前登录用户的相关信息
let currentUserInfo = reactive({});
async function getUserInfo() {
	console.log("开始获取用户信息");
	let data = await Get("getUserInfo");
	console.log(data);
	ElMessage({
		message: data.meta.msg,
		type: data.meta.status == 200 ? "success" : "error",
	});
	return data.data;
}
currentUserInfo = await getUserInfo();
// 类别列表
let categoryList = reactive([
	{
		categoryId: 1,
		categoryName: "Linux",
		count: 13,
	},
]);

// 获取类别列表
async function getCategoryCount() {
	console.log("获取类别列表下的文章数");
	let data = await Get("getCategoryCount", { ckUserId: ckUserId });
	console.log(data);
	ElMessage({
		message: data.meta.msg,
		type: data.meta.status == 200 ? "success" : "error",
	});
	return data.data;
}
categoryList = reactive(await getCategoryCount());
console.log("categoryList: ", categoryList);
// 标签列表
let labelList = reactive([
	{
		labelId: 1,
		labelName: "Linux",
		count: 13,
	},
]);

// 获取标签列表
async function getLabelCount() {
	console.log("获取类别列表下的文章数");
	let data = await Get("getLabelCount", { ckUserId: ckUserId });
	console.log(data);
	ElMessage({
		message: data.meta.msg,
		type: data.meta.status == 200 ? "success" : "error",
	});
	return data.data;
}
labelList = reactive(await getLabelCount());
console.log("labelList: ", labelList);

let articleList = reactive([
	{ id: 1, title: "标题1", abstract: "摘要1", content: "## 内容1\n### abcd" },
]);
// 获取文章列表
async function getArticleList() {
	console.log("获取文章列表");
	let data = await Get("getArticleList", { ckUserId: ckUserId });
	console.log(data);
	ElMessage({
		message: data.meta.msg,
		type: data.meta.status == 200 ? "success" : "error",
	});
	return data.data;
	// articleList = data.data;
	// console.log(articleList[0].createTime.type);
}
articleList = await getArticleList();
console.log("articleList", articleList);
function handleCommand(command) {
	console.log(command);
	router.push(command);
}
function toIndex() {
	// 去首页
	router.push("/" + ckUserId);
}
function toArchive() {
	// 去归档页
	router.push("/Archive/" + ckUserId);
}
function toCategory() {
	// 去分类页
	router.push("/Category/" + ckUserId);
}
function toLabel() {
	// 去标签页
	router.push("/Label/" + ckUserId);
}
function toWriteArticle() {
	// 去写博客页
	router.push("/writeArticle");
}
</script>

<style scoped lang="scss">
.container {
	// direction: inherit;
	opacity: 0.95;
	width: 100%;
	// height: 100%;
	// background: url("http://api.hanximeng.com/ranimg/api.php");
	background: url("http://api.btstu.cn/sjbz/?lx=dongman");
	background-size: 100% 100%;
	// background-size: cover;
	background-repeat: no-repeat;
	position: absolute;
	// background-position: center center;
	background-attachment: fixed;
	// position: fixed;
	// flex-direction: column;
	.header {
		top: 0;
		position: sticky;
		height: 50px;
		background-color: white;
		text-align: center;
		vertical-align: middle;
		line-height: 50px;
		box-shadow: 2px 2px 2px #abd1ff;
		opacity: 0.95;
		img {
			height: 50px;
		}
		.el-row {
			margin-bottom: 20px;
		}
		.el-row:last-child {
			margin-bottom: 0;
		}
		.el-col {
			border-radius: 4px;
		}
		.items {
			:hover {
				border-bottom-style: solid;
				border-bottom-color: rgb(16, 55, 211);
				color: rgb(16, 55, 211);
				cursor: pointer;
			}
		}
		.grid-content {
			border-radius: 4px;
			min-height: 36px;
		}
	}
	.main {
		width: 100%;
		margin-top: 40px;
		text-align: justify;
		left: 0;
		right: 0;
		opacity: 0.95;
		overflow-y: scroll;
		.left {
			float: left;
			width: 25%;
			// height: 2000px;
			opacity: 0.95;
			.left-top {
				border-radius: 10px;
				width: 70%;
				background-color: white;
				margin: 0 auto;
				text-align: center;
				padding-top: 40px;
				padding-bottom: 40px;
				// display: flex;
				// flex-direction: column;
				// position: fixed;
				img {
					margin: 0 auto;
					// margin-top: 40px;
					width: 90px;
					height: 90px;
					border-radius: 45px;
				}
				p {
					padding-top: 10px;
				}
				.txts {
					width: 90%;
					margin: 0 auto;
					margin-top: 10px;
					display: flex;
					flex-direction: row;
					div {
						flex: auto;
					}
					// margin: 0 auto;
				}
			}
		}
		.content {
			float: left;
			width: 50%;
			min-height: 655px;
			// height: 2000px;
			// border-radius: 10px;
			// padding-top: 20px;
			// padding-bottom: 20px;
			// display: flex;
			// flex-direction: row;
			// padding-left: 50px;
			// margin-left: 45px;
			// background-color: rgb(150, 223, 25);
			.labels {
				// position: fixed;
				width: 90%;
				border-radius: 10px;
				padding: 20px;
				background-color: white;
				margin: 0 auto;
				p {
					font-size: 18px;
				}
				.down {
					margin-top: 15px;
					font-size: 15px;
					text-align: center;
					// vertical-align: middle;
					overflow: auto;
					// _height: 1%;
					.item {
						border-radius: 10px;
						overflow: hidden;
						display: flexbox;
						margin-left: 20px;
						line-height: 30px;
						margin-top: 10px;
						float: left;
						.name {
							// border-radius: 10px;
							padding: 8px;
							background-color: #dfe4ea;
						}
						.count {
							// border-radius: 10px;
							padding: 8px;
							background-color: #00aaf3;
						}
					}
				}
			}
		}

		.right {
			float: left;
			width: 25%;
			// height: 2000px;
			div {
				opacity: 0.95;
				.Classification {
					border-radius: 10px;
					width: 70%;
					background-color: white;
					margin: 0 auto;
					margin-top: 20px;
					.box-card {
						border-radius: 10px;
						.card-header {
							display: flex;
							justify-content: space-between;
							align-items: center;
							height: 15px;
							span {
								line-height: 15px;
								font-size: 15px;
								vertical-align: middle;
							}
							span:hover {
								cursor: pointer;
							}
						}
					}
				}
				.Label {
					border-radius: 10px;
					width: 70%;
					background-color: white;
					margin: 0 auto;
					margin-top: 20px;
					.box-card {
						border-radius: 10px;
						.card-header {
							display: flex;
							justify-content: space-between;
							align-items: center;
							height: 15px;
							span {
								line-height: 15px;
								font-size: 15px;
								vertical-align: middle;
							}
							span:hover {
								cursor: pointer;
							}
						}
					}
				}
			}
		}
	}
}
::-webkit-scrollbar {
	width: 3px;
	background: linear-gradient(
		to bottom,
		hsl(0deg, 100%, 50%, 0.4) 0%,
		hsl(40deg, 100%, 50%) 20%,
		hsl(80deg, 100%, 50%) 30%,
		hsl(120deg, 100%, 50%) 40%,
		hsl(180deg, 100%, 50%) 50%,
		hsl(250deg, 100%, 50%) 80%,
		hsl(320deg, 100%, 50%, 0.4) 100%
	);
	border-radius: 4px;
}

::-webkit-scrollbar-thumb {
	background: linear-gradient(
		to bottom,
		hsl(0deg, 100%, 50%, 0) 0%,
		hsl(0deg, 100%, 100%, 0.9) 20%,
		hsl(0deg, 100%, 100%, 0.9) 80%,
		hsl(0deg, 100%, 50%, 0) 100%
	);
	border-radius: 100%;
}
</style>
