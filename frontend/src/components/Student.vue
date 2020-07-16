<template>
  <div id="student">
    this is student
    <el-button type="primary" @click="test">测试</el-button>
    <uploadimg></uploadimg>
  </div>
</template>

<script>
import axios from 'axios';
import UploadImg from './UploadImg.vue';

export default {
  name: 'student.vue',
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
  components: {
    uploadimg: UploadImg,
  },
};
</script>

<style scoped>

</style>
