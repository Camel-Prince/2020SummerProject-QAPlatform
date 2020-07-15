<template>
  <div id="app">
<!--    <div id="nav">-->
<!--      <router-link to="/">Home</router-link> |-->
<!--      <router-link to="/about">About</router-link>-->
<!--    </div>-->
<!-- <code-editor v-model="content"></code-editor>
<live-video></live-video> -->
<!--    <router-view/>-->
    <comment-area></comment-area>
  </div>
</template>

<script>
import CommentArea from './components/CommentArea.vue';

export default {
  components: {
    CommentArea,
  },
  data() {
    return {
      is_login: window.sessionStorage.getItem('token'),
    };
  },
};
</script>

<style>
  body {
    padding: 0;
    margin: 0;
    border: 0;
    background-color: #F5F5F5;
  }
</style>
