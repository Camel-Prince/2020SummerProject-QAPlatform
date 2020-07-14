<template>
  <el-container class="nav">
    <el-header class="header">
      <h3>答疑讨论区</h3>
    </el-header>
    <el-main class="main">
    </el-main>
    <el-divider class="divider"></el-divider>
    <div class="footer">
      <el-input
        id="inputArea"
        type="textarea"
        placeholer="请输入内容"
        :rows="3"
        resize=none
        v-model="textarea">
      </el-input>
      <div class="bottom">
        <el-button id='submit' type='primary'>
          发送
        </el-button>
      </div>
    </div>
  </el-container>
</template>

<script>
export default {
  data() {
    return {
      textarea: '',
    };
  },
};
</script>

<style scoped>
.nav {
  margin: 0 auto;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.2);
  border-radius: 10px;
  width: 400px;
  height: 650px;
}
.divider {
  margin: 0;
}
.header {
  margin: 0;
  border-radius: 10px 10px 0 0;
  text-align: center;
  background-color: #409EFF;
}
.header > h3 {
  color: white;
}
.main {
  background-color: #faf8f8;
  padding: 20px 20px;
}
.footer {
  height: 130px;
  box-shadow: 0px -5px 5px 0 rgba(0, 0, 0, 0.05);
  border-radius: 0 0 10px 10px;
  margin: 0;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.bottom {
  margin-bottom: 1px;
  margin-right: 10px;
  display: flex;
  flex-direction: row-reverse;
}
</style>
<style>
#inputArea {
  border: none;
  color: #606266;
  font-size: 17px;
}
</style>
