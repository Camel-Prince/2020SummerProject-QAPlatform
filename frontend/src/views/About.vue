<template>
  <div>
    <video id="my-video" class="video-js vjs-default-skin" controls preload="auto" >
    <!-- 直播地址就是nginx映射后的播放地址，注意后缀为直播流的m3u8 -->
      <source src="http://192.168.99.100:8080/stream/test.m3u8" >
    </video>
  </div>
</template>

<script>
import videojs from 'video.js';
import 'videojs-contrib-hls';

export default {
  mounted() {
    videojs('my-video', {
      bigPlayButton: true,
      textTrackDisplay: false,
      posterImage: true,
      errorDisplay: false,
      controlBar: true,
    }, function () {
      this.play();
    });
  },
};
</script>
