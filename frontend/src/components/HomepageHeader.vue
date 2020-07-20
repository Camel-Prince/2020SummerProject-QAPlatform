<template>
  <el-container class="homepageHeaderContainer">
    <h1 class="mainTitle">
      计发客Q&A直播平台
    </h1>
  </el-container>
</template>

<script>
export default {
  name: 'homepageHeader',
};
</script>

<style scoped>
.homepageHeaderContainer {
  background-color: rgb(64,158,255);
  height: 10vh;
}

.mainTitle {
  width: 250px;
  margin-left: 30px;
  color: white;
  font-family:
  "Helvetica Neue",
  Helvetica,
  "PingFang SC",
  "Hiragino Sans GB",
  "Microsoft YaHei",
  "微软雅黑",
  Arial,
  sans-serif;
  float: left;
}
</style>
