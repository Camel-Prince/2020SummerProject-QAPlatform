<template>
  <el-container class="nav">
    <el-header class="header">
      <h3>答疑讨论区</h3>
    </el-header>
    <el-main class="main">
      <div class="mainbox" ref="mainbox">
        <div class="user-message"
          v-for="(i,index) in list"
          :key="index"
          :style="i.user_info.user_pk === userId?'flex-direction:row-reverse':''">
          <div :style="i.user_info.user_pk === userId?'background-color:#DDA0DD':''"
            class="portrait">
            <i :class="i.user_info.occupation === 2?'el-icon-user-solid':'el-icon-s-custom'">
            </i>
          </div>
          <div class="message-box">
            <div class="username"
              v-show="i.user_info.user_pk !== userId">
              {{ i.user_info.name }}
            </div>
            <div
              :class="i.user_info.user_pk === userId?'bubble-right':'bubble-left'">{{ i.msg }}</div>
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
        <el-button id='submit' type='primary' @click="emitMessage">
          发送
        </el-button>
      </div>
    </div>
  </el-container>
</template>

<script>
export default {
  props: {
    roomId: String,
  },
  data() {
    return {
      userId: 0,
      textarea: '',
      list: [],
      timer: null,
    };
  },
  mounted() {
    this.userId = parseInt(window.sessionStorage.getItem('user_pk'), 10);
    this.timer = setInterval(() => {
      this.getList();
    }, 1000);
  },
  beforeDestroy() {
    clearInterval(this.timer);
    this.timer = null;
  },
  methods: {
    scrollBottom() {
      const scrollTop = this.$el.querySelector('.main');
      scrollTop.scrollTop = scrollTop.scrollHeight;
    },
    emitMessage() {
      if (this.textarea !== '') {
        console.log(this.userId);
        this.$http.post(`msg/${this.roomId}/`, {
          user_pk: this.userId,
          msg: this.textarea,
        }).then(() => {
          this.getList();
        });
        this.textarea = '';
        setTimeout(() => {
          this.scrollBottom();
        }, 80);
      }
    },
    getList() {
      this.$http.get(`msg/${this.roomId}/`).then((response) => {
        this.list = response.data.data;
      });
      this.scrollBottom();
    },
  },
};
</script>

<style scoped>
.nav {
  margin: 0 auto;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.2);
  border-radius: 10px;
  width: 400px;
  height: 500px;
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
  padding: 20px 5px;
  overflow-y: auto;
}
.mainbox {
  overflow-y: auto;
}
.footer {
  background-color: white;
  height: 130px;
  box-shadow: 0 -5px 5px 0 rgba(0, 0, 0, 0.05);
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
  font-size: 37px;
  background-color: aquamarine;
  text-align: center;
}
.user-message {
  display: flex;
  flex-direction: row;
  text-align: left;
  margin: 15px 0;
  white-space: pre;
}
.username {
  text-align: left;
  font-size: 12px;
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
