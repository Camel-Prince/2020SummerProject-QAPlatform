<template>
  <el-container
    class="container"
    :style="codeEditorShow || whiteBoardShow || BarrageShow == true ?'heigth:100%':'height:754px'">
    <div class="homepage-header">
      <h1 class="mainTitle">
        教学直播间
      </h1>
      <div>
        <el-button type="primary" @click="open">开始答疑</el-button>
        <el-button type="primary" @click="cancel">取消排队</el-button>
      </div>
    </div>
    <div class="video-chat">
      <live-video class="video"></live-video>
      <comment-area class="chat"></comment-area>
    </div>
    <div class="switch-barrage">
      <el-switch
        v-model="BarrageShow"
        active-text="弹幕开启"
        inactive-text="弹幕关闭">
      </el-switch>
    </div>
    <div class="barrage"  v-show="BarrageShow == true">
      <barrage></barrage>
    </div>
    <div class="board"  v-show="whiteBoardShow == true">
      <h1 class="mainTitle">
        白板
      </h1>
      <white-board></white-board>
    </div>
    <div  v-show="codeEditorShow == true">
      <h1 class="mainTitle">
        代码编辑器
      </h1>
      <code-editor></code-editor>
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
  components: {
    Barrage,
    CodeEditor,
    CommentArea,
    LiveVideo,
    WhiteBoard,
  },
  data() {
    return {
      courseName: 'C',
      BarrageShow: true,
      whiteBoardShow: false,
      codeEditorShow: false,
    };
  },
  methods: {
    open() {
      this.$alert('进入排队状态', '提示', {
        confirmButtonText: '确定',
        dangerouslyUseHTMLString: true,
      });
    },
    cancel() {
      this.$alert('取消排队状态', '提示', {
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
  background-image: url("../image/star1.png");
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
