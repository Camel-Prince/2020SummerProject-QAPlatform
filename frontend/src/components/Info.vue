<template>
  <div id="info">
    <homepage-header>
    </homepage-header>
    <div class="user">
      <el-form>
        <el-form-item label="用户名">
          <el-input v-model="username" :disabled="true"></el-input>
        </el-form-item>
        <el-form-item label="学号">
          <el-input v-model="id_card"></el-input>
        </el-form-item>
        <el-form-item label="姓名">
          <el-input v-model="name"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="change">提交</el-button>
        </el-form-item>
    </el-form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import homepageHeader from './Header.vue';

export default {
  name: 'Info',
  components: {
    HomepageHeader: homepageHeader,
  },
  data() {
    return {
      username: '569107519@qq.com',
      id_card: '1813049',
      name: '张弼铖',
    };
  },
  inject: ['reload'],
  methods: {
    change() {
      if (this.id_card.length > 10) {
        this.$message.error('学号不得超过10位');
        return;
      }
      if (this.name.length > 12) {
        this.$message.error('姓名长度过长');
        return;
      }
      axios({
        method: 'post',
        url: `${this.$baseURL}detail/`,
        headers: {
          Authorization: `jwt ${window.sessionStorage.getItem('token')}`,
        },
        data: {
          id_card: this.id_card,
          name: this.name,
        },
      }).then((response) => {
        if (response.data.status === 200) {
          this.$message.success('信息修改成功');
        }
        this.reload();
      });
    },
  },
  mounted() {
    axios({
      method: 'get',
      url: `${this.$baseURL}detail/`,
      headers: {
        Authorization: `jwt ${window.sessionStorage.getItem('token')}`,
      },
    }).then((response) => {
      this.username = response.data.data.user_info.username;
      this.id_card = response.data.data.id_card;
      this.name = response.data.data.name;
    });
  },
};
</script>

<style scoped>
.user {
  margin: 50px auto;
  width: 500px;
  background-color: white;
  border-radius: 10px;
}

</style>
