<template>
  <div class="ace-container">
    <div class="ace-editor" ref="ace"></div>

    <div class="config-panel" v-show="toggle">
      <div></div>
      <div>
        <label class="title">语言</label>
        <el-select class="value" v-model="modePath" @change="handleModelPathChange"
                   size="mini" value-key="name">
          <el-option v-for="mode in this.modeArray"
                     :key="mode.name"
                     :label="mode.name"
                     :value="mode.path">
          </el-option>
        </el-select>
      </div>
    </div>

    <!-- toggleConfigPanel：打开/关闭蒙层 -->
    <div class="bookmarklet" @click="toggleConfigPanel"></div>
  </div>
</template>

<script>
import ace from 'ace-builds';
import 'ace-builds/webpack-resolver'; // 在 webpack 环境中使用必须要导入
import 'ace-builds/src-noconflict/theme-monokai'; // 默认设置的主题
import 'ace-builds/src-noconflict/mode-javascript'; // 默认设置的语言模式

// 导入语言提示规则
import 'ace-builds/src-noconflict/ext-language_tools';
import 'ace-builds/src-noconflict/snippets/javascript';
import 'ace-builds/src-noconflict/snippets/html';
import 'ace-builds/src-noconflict/snippets/css';
import 'ace-builds/src-noconflict/snippets/c_cpp';
import 'ace-builds/src-noconflict/snippets/python';
import 'ace-builds/src-noconflict/snippets/java';
import 'ace-builds/src-noconflict/snippets/text';

export default {
  name: 'CodeEditor',
  props: {
    value: String,
  },
  data() {
    return {
      aceEditor: null,
      themePath: 'ace/theme/monokai', // 不导入 webpack-resolver，该模块路径会报错
      modePath: 'ace/mode/c_cpp', // 同上
      toggle: false, // 表示蒙层的打开和关闭
      modeArray: [{
        name: 'C/Cpp',
        path: 'ace/mode/c_cpp',
      }, {
        name: 'JavaScript',
        path: 'ace/mode/javascript',
      }, {
        name: 'HTML',
        path: 'ace/mode/html',
      }, {
        name: 'CSS',
        path: 'ace/mode/css',
      }, {
        name: 'Python',
        path: 'ace/mode/python',
      }, {
        name: 'Java',
        path: 'ace/mode/java',
      }, {
        name: 'Text',
        path: 'ace/mode/text',
      }],
    };
  },
  mounted() {
    this.aceEditor = ace.edit(this.$refs.ace, {
      maxLines: 20, // 最大行数，超过会自动出现滚动条
      minLines: 10, // 最小行数，还未到最大行数时，编辑器会自动伸缩大小
      fontSize: 16, // 编辑器内字体大小
      theme: this.themePath, // 默认设置的主题
      mode: this.modePath, // 默认设置的语言模式
      tabSize: 4, // 制表符设置为 4 个空格大小
    });
    // 激活自动提示
    this.aceEditor.setOptions({
      enableSnippets: true,
      enableLiveAutocompletion: true,
      enableBasicAutocompletion: true,
    });
    this.aceEditor.getSession().on('change', this.change);
  },
  methods: {
    toggleConfigPanel() {
      this.toggle = !this.toggle;
    },
    change() {
      this.$emit('input', this.aceEditor.getSession().getValue());
    },
    handleModelPathChange(modelPath) {
      this.aceEditor.getSession().setMode(modelPath);
    },
  },
};
</script>

<style lang='scss' scoped>
  .ace-container {
    position: relative;
    margin: 100px;

    .bookmarklet {
      position: absolute;
      right: 0;
      bottom: 0;
      width: 5px;
      height: 5px;
      z-index: 2;
      cursor: pointer;
      border-width: 8px;
      border-style: solid;
      border-color: lightblue gray gray rgb(206, 173, 230);
      border-image: initial;
    }
    .config-panel {
      position: absolute;
      right: 0;
      bottom: 0;
      width: 50%;
      height: 100%;
      box-shadow: grey -5px 2px 3px;
      background-color: rgba(255, 255, 255, 0.5);
      z-index: 1;

      div {
        height: 40%;
      }

      .title {
        color: white;
        margin: 0 10px;
        font-size: 14px;
      }
    }
  }
</style>
