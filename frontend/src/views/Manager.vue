<template>
  <el-container>
    <el-header class="header">
      教务处管理界面
    </el-header>
    <el-row>
      <el-col :span="3" v-for="(value, index) in rooms" :key="index" :offset=2>
        <el-card class="card" :body-style="{ padding: '0px' }" shadow="hover">
          <img :src="`http://localhost:8000/QAplatform${value.img}`" class="image">
          <div style="padding: 10px;">
            <span>{{ value.course_id }}</span>
            <br>
            <span>{{ value.name }}</span>
            <el-button type="primary" class="button" @click="modifyRoom(value.pk)">
              更改
            </el-button>
            <div class="bottom">
              <time class="time">{{  }}</time>
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
    };
  },
  methods: {
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
    modifyRoom(roomNum) {
      this.$router.push({ name: 'ModifyRoom', params: { roomNum } });
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

  .card {
    text-align: left;
    width: 200px;
    height: 265px;
    margin: 10px 0;
  }

  .time {
    font-size: 13px;
    color: #999;
  }

  .bottom {
    margin-top: 10px;
    line-height: 12px;
  }

  .button {
    padding: 2px;
    float: right;
  }

  .image {
    width: 200px;
    height: 170px;
    display: block;
  }
</style>
