<template>
  <el-container>
    <el-header class="header">
      教务处管理界面
      <el-button type="success" class="addButton" @click="addDialogFormVisible = true">
        新增房间
      </el-button>
    </el-header>
    <el-dialog title="新增直播房间" class="addRoomDialog"
               :visible.sync="addDialogFormVisible">
      <el-form :model="addRoomData" :rules="rules" ref="addRoomData">
        <el-form-item label="课程ID:" prop="course_id">
          <el-input
            placeholder="请输入课程ID"
            v-model.number="addRoomData.course_id"
            clearable>
          </el-input>
        </el-form-item>
        <el-form-item label="课程名:" prop="course_name">
          <el-input
            placeholder="请输入课程名"
            v-model="addRoomData.course_name"
            clearable>
          </el-input>
        </el-form-item>
        <el-form-item label="课程描述:" prop="course_desc">
          <el-input
            placeholder="请输入课程描述"
            type="textarea"
            v-model="addRoomData.course_desc"
            maxlength="25"
            show-word-limit>
          </el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="info" @click="resetForm('addRoomData')">重置</el-button>
          <el-button type="primary" @click="submitForm('addRoomData')">提交</el-button>
        </el-form-item>
      </el-form>
    </el-dialog>
    <el-row>
      <el-col :span="3" v-for="(value, index) in rooms" :key="index" :offset=2>
        <el-card class="card" :body-style="{ padding: '0px' }" shadow="hover">
          <img :src="`${$extraURL}/QAplatform${value.img}`" class="image" alt="">
          <div style="padding: 10px;">
            <span>{{ value.course_id }}</span>
            <br>
            <span>{{ value.name }}</span>
            <div class="bottom">
              <el-button type="primary" class="button" @click="modifyRoom(value.pk, value.name)">
                更改
              </el-button>
              <el-button type="warning" class="button" @click="deleteRoom(value.pk)">
                删除
              </el-button>
            </div>
          </div>
        </el-card>
      </el-col>
    </el-row>
  </el-container>
</template>

<script>
export default {
  name: 'Manager',
  data() {
    return {
      rooms: [],
      addDialogFormVisible: false,
      addRoomData: {
        course_id: '',
        course_name: '',
        course_desc: '',
      },
      rules: {
        course_id: [
          { required: true, message: '请输入课程ID', trigger: 'blur' },
          { type: 'number', message: '课程ID必须为数字值', trigger: 'blur' },
        ],
        course_name: [
          { required: true, message: '请输入课程名', trigger: 'blur' },
        ],
      },
    };
  },
  methods: {
    submitForm(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          for (let i = 0; i < this.rooms.length; i += 1) {
            if (parseInt(this.rooms[i].course_id, 10) === this.addRoomData.course_id) {
              this.$message({
                type: 'error',
                message: '课程ID重复，请重新输入！',
              });
              return false;
            }
          }
          this.$http.post('office/', {
            course_id: this.addRoomData.course_id,
            name: this.addRoomData.course_name,
            desc: this.addRoomData.course_desc,
          }).then(() => {
            this.$message({
              type: 'success',
              message: '添加成功!',
            });
            this.addDialogFormVisible = false;
            this.$router.go(0);
          });
          return true;
        }
        this.$message({
          type: 'warning',
          message: '请按照要求填写信息',
        });
        return false;
      });
    },
    resetForm(formName) {
      this.$refs[formName].resetFields();
    },
    deleteRoom(roomNum) {
      this.$confirm('确定要删除该房间？', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning',
      }).then(() => {
        this.$http.delete('office/', { data: { room_pk: roomNum } })
          .then(() => {
            this.$message({
              type: 'success',
              message: '删除成功!',
            });
            this.$router.go(0);
          });
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消删除',
        });
      });
    },
    modifyRoom(roomNum, roomName) {
      this.$router.push({ name: 'ModifyRoom', params: { roomNum, roomName } });
    },
  },
  mounted() {
    this.$http.get('office/')
      .then((response) => {
        this.rooms = response.data.data;
      });
  },
};
</script>

<style scoped>
  .header {
    text-align: center;
    padding: 10px;
    font-size: 30px;
  }

  .addButton {
    float: right;
    margin-top: 10px;
    margin-right: 50px;
  }

  .addRoomDialog {
    width: 800px;
    margin: auto;
  }

  .card {
    text-align: left;
    width: 200px;
    height: 245px;
    margin: 10px 0;
  }

  .button {
    padding: 2px;
  }

  .image {
    width: 200px;
    height: 170px;
    display: block;
  }
</style>
