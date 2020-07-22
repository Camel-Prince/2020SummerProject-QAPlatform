<template>
  <div>
    <div class="barrages-drop">
      <vue-baberrage
        :isShow="barrageIsShow"
        :barrageList="barrageList"
        :maxWordCount="maxWordCount"
        :throttleGap="throttleGap"
        :loop="barrageLoop"
        :boxHeight="boxHeight"
        :messageHeight="messageHeight"
      >
      </vue-baberrage>
    </div>
    <div class="send-barrage">
      发送弹幕
      <el-input v-model="msg" placeholder="请输入内容"></el-input>
      <el-button type="primary" @click="addTolist">发送</el-button>
    </div>
    <el-divider></el-divider>
  </div>
</template>

<script>
import Vue from 'vue';
import { vueBaberrage, MESSAGE_TYPE } from 'vue-baberrage';

Vue.use(vueBaberrage);
export default {
  name: 'Barrages',
  data() {
    return {
      roomId: 1,
      ws: null,
      msg: '',
      barrageIsShow: true,
      messageHeight: 35,
      boxHeight: 255,
      barrageLoop: false,
      maxWordCount: 15,
      throttleGap: 600,
      barrageList: [],
    };
  },
  mounted() {
    this.initWebSocket();
  },
  methods: {
    addTolist() {
      const params = {
        roomId: this.roomId,
        msg: this.msg,
      };
      this.ws.send(JSON.stringify(params));
      this.msg = '';
    },
    initWebSocket() {
      if (window.WebSocket) {
        const rThis = this;
        const ws = new WebSocket('ws://localhost:8181');
        rThis.ws = ws;
        ws.onopen = function () {
          console.log('服务器连接成功');
        };
        ws.onclose = function () {
          console.log('服务器连接关闭');
        };
        ws.onerror = function () {
          console.log('服务器连接出错');
        };
        ws.onmessage = function (e) {
          const resData = JSON.parse(e.data);
          if (resData.roomId !== this.roomId) {
            return;
          }
          if (resData.msg !== '') {
            rThis.barrageList.push({
              msg: resData.msg,
              time: 6,
              type: MESSAGE_TYPE.NORMAL,
            });
          }
        };
      }
    },
  },
};
</script>
<style lang="less" scoped>
.barrages-drop {
  .blue {
    border-radius: 100px;
    background: #e6ff75;
    color: #fff;
  }
  .green {
    border-radius: 100px;
    background: #75ffcd;
    color: #fff;
  }
  .red {
    border-radius: 100px;
    background: #e68fba;
    color: #fff;
  }
  .yellow {
    border-radius: 100px;
    background: #dfc795;
    color: #fff;
  }
  .baberrage-stage {
    position: absolute;
    width: 100%;
    height: 212px;
    overflow: hidden;
    top: 0;
    margin-top: 130px;
  }
}
</style>

<style>
.send-barrage {
  margin: -20px auto 10px;
  display: flex;
  width: 25%;
}
</style>
