<template>
  <el-container class="nav">
    <el-header class="header">
      <h3>答疑讨论区</h3>
    </el-header>
    <el-main class="main">
      <div class="user-message">
        <!-- v-for="(i,index) in list"
        :key="index"> -->
        <div class="portrait">
          <i class="el-icon-s-custom"></i>
        </div>
        <div class="message-box">
          <div class="username">
          <!-- v-show="i.userId !== userId"> -->
            王子旭
          </div>
          <div class="bubble-left">
            123456
          </div>
        </div>
      </div>
    </el-main>
    <el-divider class="divider"></el-divider>
    <div class="footer">
      <el-input
        id="inputarea"
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
      userId: null,
      list: [],
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
  width: 420px;
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
  background-color: #f0f1f1;
  overflow-y: auto;
  padding: 20px 5px;
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
.portrait {
  margin: 0 15px;
  width: 40px;
  height: 40px;
  font-size: 40px;
  background-color: aquamarine;
}
.user-message {
  display: flex;
  flex-direction: row;
  margin: 0;
}
.username {
  text-align: left;
  font-size: 13px;
  color: #909399;
}
.bubble-right {
  float:left;
  background-color: skyblue;
  border-bottom-color: skyblue;
  color: #fff;
  font-size: 17px;
  line-height: 20px;
  padding: 9px 17px 9px 17px;
  box-sizing: border-box;
  border-radius: 6px;
  position: relative;
  word-break: break-all;
}
.bubble-right::after {
  content: '';
  position: absolute;
  top: 50%;
  right: -5px;
  width: 10px;
  height: 10px;
  margin-top: -7px;
  background: inherit;
  transform: rotate(45deg);
}
.bubble-left {
  float:left;
  background-color: #fff;
  border-bottom-color: #fff;
  color: #606266;
  font-size: 17px;
  line-height: 18px;
  padding: 9px 17px 9px 17px;
  box-sizing: border-box;
  border-radius: 6px;
  position: relative;
  word-break: break-all;
}
.bubble-left::after {
  content: '';
  position: absolute;
  top: 50%;
  left: -5px;
  width: 10px;
  height: 10px;
  margin-top: -7px;
  background: inherit;
  transform: rotate(45deg);
}
</style>
<style>
#inputarea {
  border: none;
  color: #606266;
  font-size: 17px;
}
</style>
