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
  props: {
    roomId: null,
  },
  data() {
    return {
      name: 'video.js',
      options: {
        url: `rtmp://192.168.99.100:1935/stream/${this.roomId}`, // 需要自行设定拉流地址
        type: 'rtmp/flv',
      },
      isVideo: true,
      player: null,
    };
  },
  mounted() {
    this.initVideo();
  },
  watch: {
    roomId() {
      this.options.url = `rtmp://192.168.99.100:1935/stream/${this.roomId}`;
      this.player.src(this.options.url);
      this.player.load(this.options.url);
    },
  },
  methods: {
    initVideo() {
      videojs.options.flash.swf = 'https://cdn.bootcss.com/videojs-swf/5.4.1/video-js.swf';
      this.player = videojs('my-player');
      this.player.play();
      console.log(this.options.url);
    },
  },
};

</script>
<style lang='less' scoped>
  .videoDiv,.video-js{
    width: 700px;
    height: 500px;
    margin: 0 auto;
  }
</style>
