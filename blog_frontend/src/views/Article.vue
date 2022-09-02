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
					<img :src="'api/' + currentUserInfo.avatarPath" />
					<p v-text="currentUserInfo.name"></p>
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
				<div
					class="image"
					:style="{
						backgroundImage: `url(${'api/' + article.coverPath})`,
					}"
				>
					<div class="down">
						<p v-text="article.title"></p>
						<div class="info">
							<span v-text="article.createTime"></span>
							<span>阅读：20 /</span>
							<span>评论：13 /</span>
							<span>赞：15</span>
						</div>
					</div>
					<!-- <img src="../assets/article.png" /> -->
				</div>
				<div class="articleContent">
					<mavonEditor
						v-model="article.content"
						defaultOpen="preview"
						:subfield="false"
						:toolbarsFlag="false"
						:ishljs="true"
						style="min-height: 20px"
						codeStyle="tomorrow-night-eighties"
					/>
				</div>
				<div class="commentContainer">
					<div class="head" style="font-weight: bold">
						<el-icon color="#1e90ff"><ChatDotRound /></el-icon>
						评论区
					</div>
					<el-divider border-style="double" />
					<div class="commentInput">
						<img :src="'api/' + currentUserInfo.avatarPath" />
						<mavonEditor
							v-model="Mycomment.content"
							placeholder="撰写评论..."
							defaultOpen="edit"
							:subfield="false"
							:ishljs="true"
							:toolbarsFlag="false"
							codeStyle="tomorrow-night-eighties"
							ref="mdedit"
							@imgAdd="imgAdd"
							style="
								min-height: 100px;
								max-height: 200px;
								width: 680px;
								border-radius: 10px;
							"
						></mavonEditor>
					</div>
					<div class="btn">
						<el-button type="primary" @click="submitComment" round
							>提交评论</el-button
						>
					</div>
					<div class="comments">
						<p>{{ commentList.length }}条评论</p>
						<el-divider border-style="double" />
						<div class="maincontainer">
							<div v-for="comment in commentList" class="commentItem">
								<div class="imgContainer">
									<img :src="'api/' + comment.avatarPath" />
								</div>
								<div class="commentContent">
									<div v-text="comment.userName" class="uname"></div>
									<div v-text="comment.commentTime" class="ctime"></div>
									<div class="comment">
										<mavonEditor
											v-model="comment.comment"
											defaultOpen="preview"
											:subfield="false"
											:toolbarsFlag="false"
											:ishljs="true"
											codeStyle="tomorrow-night-eighties"
											style="
												min-height: 15px;
												width: 680px;
												border-radius: 10px;
											"
										/>
									</div>
								</div>
							</div>
						</div>
					</div>
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
import { onMounted, reactive, ref, defineProps, onBeforeMount } from "vue";
import { useRoute } from "vue-router";
import { mavonEditor } from "mavon-editor";
import { Get, Post } from "@/utils/request";
import { ElMessage } from "element-plus";
import "mavon-editor/dist/css/index.css";

const $route = useRoute();

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

let article = reactive($route.query);
console.log(article);
// let articleContent = ref(
// 	"## 标题1\n### 标题2\n```\n const int N = 1e5+10;\n```\n"
// );
let articleContent = reactive({
	txt: "## 标题1\n### 标题2\n```\n const int N = 1e5+10;\n```\n## 标题1\n### 标题2\n```\n const int N = 1e5+10;\n```\n## 标题1\n### 标题2\n```\n const int N = 1e5+10;\n```\n## 标题1\n### 标题2\n```\n const int N = 1e5+10;\n```\n",
});

let commentList = reactive([{}]);
async function getCommentList() {
	// let articleId = article.articleId;
	console.log("***", article.id);
	let data = await Get("getCommentList", { articleId: article.id });
	console.log(data);
	ElMessage({
		message: data.meta.msg,
		type: data.meta.status == 200 ? "success" : "error",
	});
	return data.data;
}
commentList = await getCommentList();
console.log("commentList", commentList);

let Mycomment = reactive({
	content: "",
	articleId: article.id,
});
console.log(Mycomment);
// 评论正文上传图片
const mdedit = ref();
async function imgAdd(pos, file) {
	console.log("aa", pos);
	console.log("bb", file);
	let imgData = new FormData();
	imgData.append("file", file);
	let data = await Post("uploadCommentImage", imgData);
	console.log(data);
	// console.log(mdedit.value.$img2Url);
	mdedit.value.$img2Url(pos, "api/" + data.imagerPath);
}
async function submitComment() {
	console.log(Mycomment);
	let data = await Get("submitComment", Mycomment);
	console.log(data);
	ElMessage({
		message: data.meta.msg,
		type: data.meta.status == 200 ? "success" : "error",
	});
}

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
onBeforeMount(() => {
	// console.log($route.query);
	// console.log($route.query);
	// let a = $route.query;
	// article = reactive({ ...a });
	// console.log(article);
});
</script>

<style scoped lang="scss">
.container {
	// direction: inherit;
	opacity: 0.9;
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
		opacity: 0.9;
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
		opacity: 0.9;
		overflow-y: scroll;
		.left {
			float: left;
			width: 25%;
			// height: 2000px;
			// opacity: 0.9;
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
			.image {
				width: 100%;
				height: 230px;
				border-radius: 20px;
				overflow: hidden;
				margin-bottom: 30px;
				// background: url("../assets/article.png");
				background-size: cover;
				// img {
				// 	width: 100%;
				// 	object-fit: cover;
				// 	overflow: hidden;
				// }
				.down {
					margin-left: 20px;
					p {
						margin-top: 150px;
						font-size: 25px;
						margin-bottom: 10px;
					}
					span {
						font-size: 10px;
						margin-left: 5px;
						// padding-left: 5px;
					}
				}
			}
			.articleContent {
				border-radius: 20px;
				width: 100%;
				// height: 500px;
				overflow: hidden;
				// .mavonEditor {
				// }
			}
			.commentContainer {
				width: 100%;
				margin-top: 20px;
				border-radius: 20px;
				// padding: 20px;
				background-color: white;
				.head {
					padding-top: 20px;
					padding-left: 20px;
				}
				.el-divider {
					// margin: 5px;
					margin-top: 5px;
					margin-bottom: 20px;
				}
				.commentInput {
					width: 100%;
					display: flex;
					flex-direction: row;
					img {
						width: 50px;
						height: 50px;
						border-radius: 25px;
						margin-left: 20px;
						margin-right: 10px;
					}
				}
				.btn {
					width: 100%;
					.el-button {
						position: relative;
						left: 660px;
						margin-top: 15px;
						// margin-right: 30px;
					}
				}
				.comments {
					margin: 20px;
					p {
						font-weight: bold;
					}
					.maincontainer {
						display: flex;
						flex-direction: column;
						.commentItem {
							display: flex;
							flex-direction: row;
							margin-bottom: 20px;
							.imgContainer {
								img {
									width: 50px;
									height: 50px;
									border-radius: 25px;
								}
								margin-right: 10px;
							}
							.commentContent {
								margin-top: 5px;
								display: flex;
								flex-direction: column;
								.uname {
									font-size: 18px;
									font-weight: bold;
								}
								.ctime {
									margin-top: 5px;
									font-size: 15px;
								}
								.comment {
									margin-top: 5px;
									background-color: #abd1ff;
								}
							}
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
