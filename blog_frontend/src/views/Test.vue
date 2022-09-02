<template>
	<div>
		<mavonEditor
			v-model="content"
			defaultOpen="preview"
			:subfield="false"
			:toolbarsFlag="false"
			:ishljs="true"
			codeStyle="tomorrow-night-eighties"
		/>
	</div>
</template>
<script setup>
import { mavonEditor } from "mavon-editor";
import "mavon-editor/dist/css/index.css";
let content = "## 标题1\n### 标题2\n```\n const int N = 1e5+10;\n```\n";
</script>
<style scoped lang="scss">
div {
	width: 800px;
	height: 500px;
	margin: 0 auto;
	padding-top: 50px;
}
</style>
