<template>
	<div class="container">
		<el-backtop :right="50" :bottom="50" />
		<div class="header">
			<el-row :gutter="28">
				<el-col :span="6">
					<img src="../assets/logo.png" />
				</el-col>
				<el-col :span="3" class="items">
					<div @click="toIndex">首页</div>
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
				<el-col :span="6">TODO </el-col>
			</el-row>
		</div>
		<div class="main">
			<!-- <el-affix class="left" :offset="0"> -->
			<div class="left">
				<div class="left-top">
					<img src="https://q1.qlogo.cn/g?b=qq&nk=361654768&s=640" />
					<p>HKing</p>
					<div class="txts">
						<div>
							文章
							<p>21</p>
						</div>
						<div>
							分类
							<p>21</p>
						</div>
						<div>
							标签
							<p>21</p>
						</div>
					</div>
				</div>
				<div class="Classification">
					<el-card class="box-card">
						<template #header>
							<div class="card-header">
								<div>
									<el-icon color="#1e90ff">
										<Grid />
									</el-icon>
									<span>分类</span>
								</div>
								<span>更多 >></span>
							</div>
						</template>
						<div v-for="o in 4" :key="o" class="text item">
							{{ "List item " + o }}
						</div>
					</el-card>
				</div>
				<div class="Label">
					<el-card class="box-card">
						<template #header>
							<div class="card-header">
								<div>
									<el-icon color="#1e90ff">
										<Grid />
									</el-icon>
									<span>标签</span>
								</div>
								<span>更多 >></span>
							</div>
						</template>
						<div v-for="o in 4" :key="o" class="text item">
							{{ "List item " + o }}
						</div>
					</el-card>
				</div>
			</div>
			<!-- </el-affix> -->
			<el-scrollbar class="content">
				<div class="archives">
					<el-timeline>
						<el-timeline-item
							v-for="article in articleList"
							:timestamp="article.createTime"
							placement="top"
						>
							<el-card>
								<img :src="'api/' + article.coverPath" />
								<div class="card-right">
									<p class="title">{{ article.title }}</p>
									<p class="classify">{{ article.category_id }}</p>
								</div>
							</el-card>
						</el-timeline-item>
					</el-timeline>
				</div>
			</el-scrollbar>
			<el-affix class="right" :offset="90">
				<div>Right</div>
			</el-affix>
		</div>
	</div>
</template>
<script setup>
import router from "@/router";
import { onMounted, reactive, readonly, toRef } from "vue";
import { Get } from "@/utils/request";
import { ElMessage } from "element-plus";

let articleList = reactive([
	{ id: 1, title: "标题1", abstract: "摘要1", content: "## 内容1\n### abcd" },
	{ id: 2, title: "标题2", abstract: "摘要2", content: "## 内容2\n### abcd" },
	{ id: 3, title: "标题3", abstract: "摘要3", content: "## 内容3\n### abcd" },
	{ id: 4, title: "标题4", abstract: "摘要4", content: "## 内容4\n### abcd" },
	{ id: 5, title: "标题5", abstract: "摘要5", content: "## 内容5\n### abcd" },
]);

// 获取文章列表
async function getArticleList() {
	console.log("获取文章列表");
	let data = await Get("getArticleList");
	console.log(data);
	ElMessage({
		message: data.meta.msg,
		type: data.meta.status == 200 ? "success" : "error",
	});
	return data.data;
	// articleList = data.data;
	// console.log(articleList[0].createTime.type);
}
articleList = reactive(await getArticleList());
console.log("articleList", articleList[0].createTime);

function toIndex() {
	// 去首页
	router.push("/");
}
function toArchive() {
	// 去归档页
	router.push("/Archive");
}
function toCategory() {
	// 去分类页
	router.push("/Category");
}
function toLabel() {
	// 去标签页
	router.push("/Label");
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
					}
				}
			}
		}
		.content {
			float: left;
			width: 50%;
			// height: 2000px;
			// border-radius: 10px;
			// background-color: white;
			// padding-top: 20px;
			// padding-bottom: 20px;
			// display: flex;
			// flex-direction: row;
			// padding-left: 50px;
			// margin-left: 45px;
			// background-color: rgb(150, 223, 25);
			.archives {
				background-color: white;
				border-radius: 10px;
				// padding: 20px;
				// padding-top: 30px;
				// padding-bottom: 20px;
				padding: 30px 30px 20px 30px;
				// position: fixed;
				width: 90%;
				// margin: 0 auto;
				.el-card {
					// display: flex;
					// flex-direction: row;
					padding-bottom: 20px;
					img {
						float: left;
						width: 60px;
						height: 60px;
						object-fit: cover;
					}
					.card-right {
						float: left;
						margin-left: 20px;
						.title {
							font-size: 20px;
						}
						.classify {
							padding-top: 5px;
							font-size: 10px;
						}
					}
				}
			}
		}

		.right {
			float: left;
			// width: 25%;
			height: 2000px;
			div {
				background-color: aquamarine;
				opacity: 0.9;
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
