<template>
  <el-aside class="aside">
    <el-menu :default-active="activeItemFromViews" active-text-color="#409EFF">
      <el-menu-item index="1" @click="toHomePage">
        <i class="el-icon-s-home"></i>
          <span>
            教师首页
          </span>
      </el-menu-item>
      <el-menu-item index="2" @click="toInformationPage">
        <i class="el-icon-user"></i>
          <span>
           个人信息
          </span>
      </el-menu-item>
      <el-menu-item index="3" @click="toRecentLive">
        <i class="el-icon-video-camera"></i>
        <span>近期直播</span>
      </el-menu-item>
      <el-menu-item index="4" @click="toLiveTime">
        <i class="el-icon-notebook-2"></i>
          <span>
            直播时长
          </span>
      </el-menu-item>
    </el-menu>
  </el-aside>
</template>

<script>
export default {
  name: 'teacherHomepageAside',
  props: ['activeItemFromViews'],
  methods: {
    toHomePage() {
      this.$router.push({
        name: 'TeacherHomepage',
      });
    },
    toRecentLive() {
      this.$router.push({
        name: 'TeacherRecentlive',
      });
    },
    toInformationPage() {
      this.$router.push({
        name: 'TeacherInformation',
      });
    },
    toLiveTime() {
      this.$router.push({
        name: 'TeacherLivetime',
      });
    },
  },
};
</script>

<style lang="less" scoped>
.aside {
  background-color: white;
  height: 90vh;
}
</style>
