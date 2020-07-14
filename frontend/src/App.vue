<template>
  <div id="app">
    <el-backtop></el-backtop>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'app',
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
