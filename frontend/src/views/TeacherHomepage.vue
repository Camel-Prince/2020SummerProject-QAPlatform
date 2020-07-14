<template>
    <div>
       <el-container class="homepageHeaderContainer">
           <h1 class="mainTitle">
               计发客Q&A直播平台
           </h1>
       </el-container>
       <el-container>
           <el-aside class="aside">
               aside
           </el-aside>
           <el-main class="main">
               main
           </el-main>
       </el-container>
    </div>
</template>

<script>
export default {
  name: 'TeacherHomepage',
};
</script>

<style scoped>
body {
    margin: 0;
}

.homepageHeaderContainer {
    background-color: rgb(64,158,255);
    height: 10vh;
}

.mainTitle {
    width: 250px;
    margin-left: 30px;
    margin-right: 1330px;
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

.aside {
    background-color: grey;
    height: 90vh;
    }

.main {
    background-color: white;
    height: 90vh;
}
</style>
