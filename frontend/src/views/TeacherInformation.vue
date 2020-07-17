<template>
    <div>
        <homepage-header></homepage-header>
       <el-container>
           <teacher-homepage-aside activeItemFromViews="2"></teacher-homepage-aside>
           <el-main class="main">
               Teacher-Information-Table;
           </el-main>
       </el-container>
    </div>
</template>

<script>
import homepageHeader from '../components/HomepageHeader.vue';
import teacherHomepageAside from '../components/TeacherHomepageAside.vue';

export default {
  name: 'TeacherInformation',
  components: {
    HomepageHeader: homepageHeader,
    TeacherHomepageAside: teacherHomepageAside,
  },
};
</script>

<style scoped>
body {
    margin: 0;
}

.main {
    background-color: white;
    height: 90vh;
}
</style>
