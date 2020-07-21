<template>
  <div class="videoDiv">
    <video v-if="isVideo" id="my-player"
      class="video-js vjs-default-skin vjs-big-play-centered"
      controls preload="auto" autoplay="autoplay"
      data-setup='{}'>
      <source :src='options.url' :type='options.type'/>
    </video>
 </div>
</template>

<script>
import videojs from 'video.js';
import 'video.js/dist/video-js.css';
import 'vue-video-player/src/custom-theme.css';
import 'videojs-flash';

export default {
  props: ['courseName'],
  data() {
    return {
      name: 'video.js',
      options: {
        url: `rtmp://192.168.99.100:1935/stream/${this.courseName}`, // 需要自行设定拉流地址
      },
      isVideo: true,
      player: null,
    };
  },
  mounted() {
    this.initVideo();
  },
  methods: {
    initVideo() {
      videojs.options.flash.swf = 'https://cdn.bootcss.com/videojs-swf/5.4.1/video-js.swf';
      this.player = videojs('my-player');
      this.player.play();
    },
  },
};

</script>
<style lang='less' scoped>
  .videoDiv,.video-js{
    width: 700px;
    height: 500px;
  }
</style>
