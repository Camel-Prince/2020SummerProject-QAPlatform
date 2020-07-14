<template>
  <div class="home">
    <el-button @click="toTeacherHomepage()">
      教师主页
    </el-button>
    <img alt="Vue logo" src="../assets/logo.png">
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Home',
  methods: {
    toTeacherHomepage() {
      this.$router.push({ path: 'teacher/homepage' });
    },
  },
};
</script>
