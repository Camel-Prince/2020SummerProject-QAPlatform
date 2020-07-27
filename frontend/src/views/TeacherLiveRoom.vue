<template>
  <el-container
    class="container"
    :style="codeEditorShow || whiteBoardShow || BarrageShow === true ?'heigth:100%':'height:754px'">
    <div class="homepage-header">
      <h1 class="mainTitle">
        直播间
      </h1>
      <div>
        <el-button type="primary" @click="open">开始直播</el-button>
        <el-button type="primary" @click="start">开始答疑</el-button>
        <el-button type="primary" @click="giveAccess">赋予权限</el-button>
        <el-button type="primary" @click="closeAccess">关闭权限</el-button>
      </div>
    </div>
    <div class="video-chat">
      <live-video class="video" :roomId="courseName"></live-video>
      <comment-area class="chat" :roomId="courseName"></comment-area>
    </div>
    <div class="switch-barrage">
      <el-switch
        v-model="BarrageShow"
        active-text="弹幕开启"
        inactive-text="弹幕关闭">
      </el-switch>
    </div>
    <div class="barrage"  v-show="BarrageShow === true">
      <barrage :roomId="courseName"></barrage>
    </div>
    <div class="board"  v-show="whiteBoardShow === true">
      <h1 class="mainTitle">
        白板
      </h1>
      <white-board></white-board>
    </div>
    <div v-show="codeEditorShow === true">
      <h1 class="mainTitle">
        代码编辑器
      </h1>
      <code-editor :roomId="courseName" :Access="access"></code-editor>
    </div>
    <div>
    </div>
    <div class="switch">
      <el-switch
        v-model="whiteBoardShow"
        active-text="白板开启"
        inactive-text="白板关闭">
      </el-switch>
      <br><br>
      <el-switch
        v-model="codeEditorShow"
        active-text="代码编辑器开启"
        inactive-text="代码编辑器关闭">
      </el-switch>
    </div>
  </el-container>
</template>

<script>
import Barrage from '../components/Barrage.vue';
import CodeEditor from '../components/CodeEditor.vue';
import CommentArea from '../components/CommentArea.vue';
import LiveVideo from '../components/LiveVideo.vue';
import WhiteBoard from './WhiteBoard.vue';

export default {
  name: 'TeacherLiveRoom',
  components: {
    Barrage,
    CodeEditor,
    CommentArea,
    LiveVideo,
    WhiteBoard,
  },
  data() {
    return {
      firstStudentId: null,
      access: true,
      ws: null,
      courseName: null,
      list: [],
      BarrageShow: true,
      whiteBoardShow: false,
      codeEditorShow: false,
    };
  },
  mounted() {
    this.courseName = this.$route.params.room;
    console.log(this.courseName);
    this.initWebsocket();
  },
  methods: {
    initWebsocket() {
      if (window.WebSocket) {
        const rThis = this;
        const ws = new WebSocket('ws://localhost:8282');
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
          if (resData.type === 'teacher') {
            rThis.list = resData.dataList;
          }
        };
      }
    },
    giveAccess() {
      this.access = false;
      const params = {
        msg: 'openAccess',
        userId: this.firstStudentId,
      };
      this.ws.send(JSON.stringify(params));
    },
    closeAccess() {
      this.access = true;
      const params = {
        msg: 'closeAccess',
        userId: this.firstStudentId,
      };
      this.ws.send(JSON.stringify(params));
    },
    start() {
      if (this.list.length === 0) {
        alert('当前没有学生在排队');
      } else {
        const params = {
          msg: 'start',
          userId: this.list[0],
        };
        this.firstStudentId = params.userId;
        this.ws.send(JSON.stringify(params));
      }
    },
    open() {
      this.$alert(`<strong>URL</strong>:rtmp://192.168.99.100:1935/stream <br> <strong>密钥</strong>:${this.courseName}`,
        '直播地址(打开直播软件按照如下地址推流)', {
          confirmButtonText: '确定',
          dangerouslyUseHTMLString: true,
        });
    },
  },
};
</script>

<style scoped>
.container {
  display: block;
  background-image: url("../image/star.png");
  background-repeat: repeat-y;
}

.homepage-header{
  display: flex;
  justify-content: space-between;
  background-color: rgb(245, 248, 248);
  height: 10vh;
  box-shadow: 0 3px 15px #cfcece;
}

.video-chat {
  display: flex;
  width: 80%;
  margin: 3% auto 2%;
}

.video {
  margin-right: 20px;
  box-shadow: 0 5px 15px rgb(63, 63, 63);
}

.switch-barrage {
  position: relative;
  left: -30%;
}

.switch {
  position: relative;
  font-size: 12px;
  margin-right: 10%;
}

.board {
  background-color: #cfcece;
}

.mainTitle {
  width: 150px;
  margin-left: 10px;
  color: rgb(64,158,255);
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
