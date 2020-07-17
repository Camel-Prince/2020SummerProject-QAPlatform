<template>
  <div class="home">
    <el-button @click="toTeacherHomepage()">
      教师主页
    </el-button>
    <el-button @click="toStudentHomepage()">
      学生主页
    </el-button>
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
    toStudentHomepage() {
      this.$router.push({ path: 'student/homepage' });
    },
  },
};
</script>
