<template>
  <div id="teacher">
    this is teacher
    <el-button type="primary" @click="test">测试</el-button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'teacher.vue',
  methods: {
    test: () => {
      axios({
        method: 'get',
        url: 'http://localhost:8000/QAplatform/detail/',
        headers: {
          Authorization: `jwt ${window.sessionStorage.getItem('token')}`,
        },
      }).then((response) => {
        console.log(response.data);
      });
    },
  },
};
</script>

<style scoped>

</style>
