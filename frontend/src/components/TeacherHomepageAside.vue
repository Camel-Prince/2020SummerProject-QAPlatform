<template>
    <el-aside class="aside">
          <el-menu default-active="1" active-text-color="#409EFF">
            <el-menu-item index="1" @click="toHomePage">
                  <i class="el-icon-user"></i>
                 <span>
                     首&nbsp;&nbsp;页
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
              <el-menu-item index="4" @click="toWeekLiveTime">
                  <i class="el-icon-notebook-2"></i>
                  <span>
                     每周直播时长统计
                  </span>
              </el-menu-item>
          </el-menu>
      </el-aside>
</template>

<script>
export default {
  name: 'teacherHomepageAside',
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
  },
};
</script>

<style lang="less" scoped>
.aside {
    background-color: grey;
    height: 90vh;
}
</style>
