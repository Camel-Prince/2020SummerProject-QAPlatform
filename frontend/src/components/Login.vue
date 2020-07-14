<template>
    <div class="login_container">
        <div class="login_box">
            <div class="title">
              <span class="t1">用户登录</span>
              <span class="t2"><el-link type="primary" :underline="false" @click="toRegister">
                注册 &gt;</el-link></span>
            </div>
            <el-form ref="loginFormRef" :model="loginForm" :rules="loginFormRules"
                     label-width="80px" class="login_form">
                <el-form-item label="邮箱: " prop="username">
                    <el-input v-model="loginForm.username"></el-input>
                </el-form-item>
                <el-form-item label="密码: " prop="password">
                    <el-input v-model="loginForm.password" type="password"></el-input>
                </el-form-item>
                <el-form-item class="btns">
                    <el-button type="primary" @click="login">登录</el-button>
                    <el-button type="info" @click="resetLoginForm">重置</el-button>
                </el-form-item>
            </el-form>
        </div>
    </div>
</template>

<script>
export default {
  name: 'login',
  data() {
    const validateEmail = (rule, value, callback) => {
      const reg = /^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$/;
      if (reg.test(value)) {
        callback();
      } else {
        callback(new Error('邮箱格式错误'));
      }
    };
    return {
      loginForm: {
        username: '',
        password: '',
      },
      loginFormRules: {
        username: [
          { required: true, message: '请输入邮箱', trigger: 'blur' },
          { validator: validateEmail, trigger: 'blur' },
        ],
        password: [
          { required: true, message: '请输入密码', trigger: 'blur' },
          {
            min: 8, max: 16, message: '长度在 8 到 16 个字符', trigger: 'blur',
          },
        ],
      },
    };
  },
  methods: {
    resetLoginForm() {
      this.$refs.loginFormRef.resetFields();
    },
    login() {
      this.$refs.loginFormRef.validate(async (valid) => {
        if (!valid) return;
        await this.$http.post('login/', {
          username: this.loginForm.username,
          password: this.loginForm.password,
        }).then((response) => {
          if (response.data.status === 400) return this.$message.error('登陆失败，用户名或密码错误');
          this.$message.success('登陆成功');
          window.sessionStorage.setItem('token', response.data.token);
          const urls = ['/office', '/teacher', 'student'];
          return this.$router.push({ path: urls[response.data.occupation] });
        });
      });
    },
    toRegister() {
      this.$router.push({ path: '/register' });
    },
  },
};
</script>
<style scoped>
.login_box {
  width: 450px;
  height: 300px;
  background-color: #fff;
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  border-radius: 10px;
}
.title {
  font-size: 30px;
  font-weight: 600;
  color: #333;
  height: 120px;
  line-height: 120px;
}
.btns {
  display: flex;
  justify-content: flex-end;
}
.login_form {
  position: absolute;
  bottom: 0;
  width: 100%;
  padding: 0 20px;
  box-sizing: border-box;
}
.t1 {
  margin-left: 170px;
}
.t2 {
  margin-left: 90px;
}
</style>
