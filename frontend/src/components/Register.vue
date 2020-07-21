<template>
  <div class="register_container">
    <div class="register_box">
      <div class="title">
        <span class="t1">用户注册</span>
        <span class="t2"><el-link type="primary" :underline="false" @click="toLogin">登录 &gt;
        </el-link></span>
      </div>
      <el-form ref="registerFormRef"
        status-icon
        :model="registerForm"
        :rules="registerFormRules"
        label-width="100px"
        class="register_form">
        <el-form-item label="邮箱: " prop="email">
          <el-input v-model="registerForm.email"></el-input>
        </el-form-item>
        <el-form-item label="密码: " prop="password">
          <el-input v-model="registerForm.password" type="password"></el-input>
        </el-form-item>
        <el-form-item label="确认密码: " prop="password_confirm">
          <el-input v-model="registerForm.password_confirm" type="password"></el-input>
        </el-form-item>
        <el-form-item label="身份: " prop="radio">
          <el-radio-group v-model="registerForm.radio">
            <el-radio :label="2">学生</el-radio>
            <el-radio :label="1">老师</el-radio>
            <el-radio :label="0">教务</el-radio>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="验证码:" prop="identifying_code">
          <el-input v-model="registerForm.identifying_code"
            style="width: 150px;"></el-input>
          <el-button type="primary" @click="sendEmail"
            class="email_btn"
            :disabled="disable_btn"
            v-text="msg"></el-button>
        </el-form-item>
        <el-form-item class="btns">
          <el-button type="primary" @click="register">注册</el-button>
          <el-button type="info" @click="resetRegisterForm">重置</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
export default {
  name: 'register',
  data() {
    const validateEmail = (rule, value, callback) => {
      const reg = /^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$/;
      if (reg.test(value)) {
        callback();
      } else {
        callback(new Error('邮箱格式错误'));
      }
    };
    const validatePassword = (rule, value, callback) => {
      if (value === this.registerForm.password) {
        callback();
      } else {
        callback(new Error('两次密码输入不一致'));
      }
    };
    return {
      registerForm: {
        email: '',
        password: '',
        password_confirm: '',
        identifying_code: '',
        radio: 2,
      },
      disable_btn: false,
      msg: '发送邮箱验证码',
      left_time: 60,
      registerFormRules: {
        email: [
          { required: true, message: '请输入邮箱', trigger: 'blur' },
          { validator: validateEmail, trigger: 'blur' },
        ],
        password: [
          { required: true, message: '请输入密码', trigger: 'blur' },
          {
            min: 8, max: 16, message: '长度在 8 到 16 个字符', trigger: 'blur',
          },
        ],
        password_confirm: [
          { required: true, message: '请确认密码', trigger: 'blur' },
          {
            min: 8, max: 16, message: '长度在 8 到 16 个字符', trigger: 'blur',
          },
          { validator: validatePassword, trigger: 'blur' },
        ],
        identifying_code: [
          { required: true, message: '请输入邮箱验证码', trigger: 'blur' },
        ],
        radio: [
          { required: true, message: '请选择身份', trigger: 'blur' },
        ],
      },
    };
  },
  methods: {
    resetRegisterForm() {
      this.$refs.registerFormRef.resetFields();
    },
    register() {
      this.$refs.registerFormRef.validate(async (valid) => {
        if (!valid) return;
        await this.$http.put('register/', {
          username: this.registerForm.email,
          password: this.registerForm.password,
          identifying_code: this.registerForm.identifying_code,
        }).then((response) => {
          if (response.data.status === 400) return this.$message.error('注册失败，当是否没有请求发送邮箱验证码');
          if (response.data.status === 0) return this.$message.error('注册失败，邮箱验证码输入错误');
          this.$message.success('注册成功');
          window.sessionStorage.setItem('token', response.data.token);
          const urls = ['/office', '/teacher', 'student'];
          return this.$router.push({ path: urls[response.data.occupation] });
        });
      });
    },
    toLogin() {
      this.$router.push({ path: '/login' });
    },
    sendEmail() {
      this.$refs.registerFormRef.validateField('email', (errMsg) => {
        if (!errMsg) {
          this.$refs.registerFormRef.validateField('password', (errMsg2) => {
            if (!errMsg2) {
              this.$refs.registerFormRef.validateField('password_confirm', (errMsg3) => {
                if (!errMsg3) {
                  this.$http.post('register/', {
                    username: this.registerForm.email,
                    password: this.registerForm.password,
                    occupation: this.registerForm.radio,
                  }).then((response) => {
                    console.log(response);
                    if (response.data.status === 400) return this.$message.error('请输入用户名和密码');
                    if (response.data.status === 0) return this.$message.error('注册失败，该邮箱已经被占用');
                    if (response.data.status === 200) return this.$message.success('验证码发送成功，请在邮箱中查看');
                    return 0;
                  });
                  this.disable_btn = true;
                  let id;
                  const set = () => {
                    this.msg = `剩余${this.left_time}s再次发送`;
                    this.left_time -= 1;
                    if (this.left_time === 0) {
                      this.disable_btn = false;
                      this.msg = '发送邮箱验证码';
                      this.left_time = 60;
                      clearInterval(id);
                    }
                  };
                  id = setInterval(set, 1000);
                }
              });
            }
          });
        }
      });
    },
  },
};
</script>

<style scoped>
.register_box {
    width: 450px;
    height: 500px;
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
    height: 160px;
    line-height: 130px;
    text-align: center;
}
.btns {
    display: flex;
    justify-content: flex-end;
}
.register_form {
    position: absolute;
    bottom: 0;
    width: 100%;
    padding: 0 20px;
    box-sizing: border-box;
}
.email_btn {
  float: right;
  width: 130px;
  text-align: left;
}
.t1 {
  margin-left: 170px;
}
.t2 {
  margin-left: 90px;
}
</style>
