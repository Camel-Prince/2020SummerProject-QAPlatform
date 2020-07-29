<template>
  <div class="header">
    <img src="../assets/QAlogo.png" class="qalogo" alt="">
      <el-dropdown trigger="click" class="btn">
        <span class="el-dropdown-link">
          {{name}}<i class="el-icon-caret-bottom el-icon--right"></i>
        </span>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item class="clearfix">
            <el-button class="btn2" @click="toInfo">个人信息</el-button>
          </el-dropdown-item>
          <el-dropdown-item class="clearfix">
            <el-button class="btn2" @click="logout">退出账号</el-button>
          </el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
    <img :src=userlogo class="userlogo" alt="">
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Header.vue',
  data() {
    return {
      userlogo: '',
      name: '',
    };
  },
  methods: {
    logout() {
      window.sessionStorage.clear();
      this.$router.push({ path: '/login' });
    },
    toInfo() {
      this.$router.push({ path: '/info' });
    },
  },
  mounted() {
    axios({
      method: 'get',
      url: 'http://localhost:8000/QAplatform/detail/',
      headers: {
        Authorization: `jwt ${window.sessionStorage.getItem('token')}`,
      },
    }).then((response) => {
      console.log(response.data);
      this.userlogo = `http://localhost:8000/QAplatform${response.data.data.img}`;
      this.name = response.data.data.name;
    });
  },
};
</script>

<style scoped>
  .header{
    height: 60px;
    background-color: white;
    box-shadow: 0 5px 10px rgba(0, 0, 0, .2);
  }
  .qalogo{
    float: left;
    margin-top: -3px;
    margin-left: 125px;
  }
  .userlogo{
    border-radius: 50%;
    float: right;
    margin-top: 10px;
    margin-right: 15px;
  }
  .btn {
    float: right;
    margin-right: 200px;
    margin-top: 40px;
    color: #409EFF;
  }
  .btn2 {
    border: 0;
    border-bottom: 1px solid black;
    border-radius: 0;
  }

</style>
