<template>
  <el-container>
    <el-header class="header">
      教务处管理界面
    </el-header>
    <el-row>
      <el-col :span="3" v-for="(value, index) in rooms" :key="index" offset="2">
        <el-card class="card" :body-style="{ padding: '0' }" shadow="hover">
          <img :src=value.picture class="image">
          <div style="padding: 10px;">
            <span>{{ value.roomNum }}</span>
            <br>
            <span>{{ value.course }}</span>
            <br>
            <span>{{ value.teacher }}</span>
            <el-button type="primary" class="button">更改</el-button>
            <div class="bottom">
              <time class="time">{{ value.time }}</time>
              <el-button type="warning" class="button">删除</el-button>
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
      rooms: [
        {
          roomNum: '1',
          course: '高数',
          teacher: '张老师',
          time: '周五晚8:00',
          picture: 'https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png',
        }, {
          roomNum: '2',
          course: '英语',
          teacher: '王老师',
          time: '周四晚7:00',
          picture: 'https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png',
        }, {
          roomNum: '1',
          course: '高数',
          teacher: '张老师',
          time: '周五晚8:00',
          picture: 'https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png',
        }, {
          roomNum: '1',
          course: '高数',
          teacher: '张老师',
          time: '周五晚8:00',
          picture: 'https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png',
        }, {
          roomNum: '1',
          course: '高数',
          teacher: '张老师',
          time: '周五晚8:00',
          picture: 'https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png',
        }, {
          roomNum: '1',
          course: '高数',
          teacher: '张老师',
          time: '周五晚8:00',
          picture: 'https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png',
        }, {
          roomNum: '1',
          course: '高数',
          teacher: '张老师',
          time: '周五晚8:00',
          picture: 'https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png',
        }, {
          roomNum: '1',
          course: '高数',
          teacher: '张老师',
          time: '周五晚8:00',
          picture: 'https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png',
        },
      ],
    };
  },
};
</script>

<style scoped>
  body {
    background-color: ;
  }
  .header {
    text-align: center;
    padding: 10px;
    font-size: 30px;
  }

  .card {
    width: 200px;
    height: 280px;
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
