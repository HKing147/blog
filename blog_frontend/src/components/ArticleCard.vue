<template>
	<div class="card">
		<div class="image">
			<img :src="'api/' + props.article.coverPath" />
		</div>
		<div class="down">
			<p v-text="props.article.title"></p>
			<div class="info">
				<span v-text="props.article.createTime + ' /'"></span>
				<span>阅读：20 /</span>
				<span>评论：13 /</span>
				<span>赞：15</span>
				<el-divider border-style="double" />
			</div>
			<div class="abstract" v-text="props.article.abstract"></div>
		</div>
	</div>
</template>
<script setup>
import { reactive, toRefs } from "vue";

const props = defineProps({
	id: Number,
	article: Object,
});
// console.log(props.id);
console.log("***", props.article);
// console.log(props);
let id = props.id;
let article = props.article;
// console.log("id", id);
// console.log("id", props.id);
// console.log("article", article);
function toArticle() {
	// 去博客详情页
	router.push({
		path: "/article",
		query: {
			id,
			article,
		},
	});
}
</script>
<style scoped lang="scss">
.card {
	width: 95%;
	height: 400px;
	background-color: white;
	border-radius: 20px;
	margin: 0 auto;
	margin-bottom: 20px;
	.image {
		border-top-right-radius: 20px;
		border-top-left-radius: 20px;
		height: 60%;
		width: 100%;
		overflow: hidden;
		img {
			// border-top-right-radius: 20px;
			// border-top-left-radius: 20px;
			// height: 60%;
			width: 100%;
			object-fit: cover;
			transition: all 0.6s;
			overflow: hidden;
		}
		img:hover {
			transform: scale(1.3);
			cursor: pointer;
		}
	}
	.down {
		margin-top: 20px;
		padding-left: 20px;
		padding-right: 20px;
		p {
			font-size: 25px;
		}
		span {
			padding-top: 10px;
			font-size: 10px;
			padding-left: 5px;
		}
		.el-divider {
			margin-top: 10px;
			margin-bottom: 10px;
		}
		.abstract {
			font-size: 15px;
			display: -webkit-box;
			-webkit-line-clamp: 2;
			-webkit-box-orient: vertical;
			overflow: hidden;
			text-overflow: ellipsis;
			text-indent: 1.5em;
			line-height: 1.5em;
		}
	}
}
</style>
