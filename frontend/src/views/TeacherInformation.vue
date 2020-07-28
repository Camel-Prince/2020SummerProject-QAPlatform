<template>
  <div>
    <homepage-header></homepage-header>
    <el-container>
      <teacher-homepage-aside activeItemFromViews="2"></teacher-homepage-aside>
      <el-main class="main">
        <el-form>
          <el-form-item label="教师姓名">
             <p>{{teacherName}}</p>
          </el-form-item>
          <el-form-item label="教师ID">
             <p>{{teacherID}}</p>
          </el-form-item>
          <el-form-item label="教师头像">
             <img src="teacherImg"/>
          </el-form-item>
          <el-form-item label="教师用昵称（用户名）">
             <p>{{teacherUserName}}</p>
          </el-form-item>
        </el-form>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import axios from 'axios';
import homepageHeader from '../components/HomepageHeader.vue';
import teacherHomepageAside from '../components/TeacherHomepageAside.vue';

export default {
  name: 'TeacherInformation',
  components: {
    HomepageHeader: homepageHeader,
    TeacherHomepageAside: teacherHomepageAside,
  },
  data() {
    return {
      teacherName: '',
      teacherID: '',
      teacherImg: '',
      teacherUserName: '',
    };
  },
  mounted() {
    axios({
      method: 'get',
      url: 'http://localhost:8000/QAplatform/detail/',
      headers: {
        Authorization: `jwt ${window.sessionStorage.getItem('token')}`,
      },
    })
      .then((response) => {
        this.teacherName = response.data.data.name;
        this.teacherID = response.data.data.id_card;
        this.teacherUserName = response.data.data.user_info.username;
      });
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
