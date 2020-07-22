<template>
  <div>
    <homepage-header>
    </homepage-header>
    <el-container>
      <el-main>
        <span class="table-title">{{studentName}}同学，你的课程如下</span>
        <el-form>
          <el-form-item label="课程学期">
            <el-button class="term-button" @click="selectTerm(202001)" type="text">
              202001
            </el-button>
            <el-button class="term-button" @click="selectTerm(202002)" type="text">
              202002
            </el-button>
            <el-button class="term-button" @click="selectTerm(202003)" type="text">
              202003
            </el-button>
          </el-form-item>
          <el-form-item label="课程分类">
            <el-button class="term-button" @click="selectAllCourse" type="text">
              全部
            </el-button>
            <el-button class="term-button"
            @click="selectRecommandedCourse" type="text">
              首页推荐
            </el-button>
          </el-form-item>
          <el-form-item label="课程状态">
            <el-button class="term-button" type="text">
              已结束
            </el-button>
            <el-button class="term-button" type="text">
              正在直播
            </el-button>
            <el-button class="term-button" type="text">
              即将开始
            </el-button>
          </el-form-item>
        </el-form>
        <el-table :data="tableData" size="small" class="courseTable">
          <el-table-column width="380">
            <template slot-scope="scope">
              <img :src="scope.row.img"/>
            </template>
          </el-table-column>
          <el-table-column width="700">
            <template slot-scope="scope">
              <h2 class="course-name">{{scope.row.name}}</h2>
              <h3 class="course-desc">{{scope.row.desc}}</h3>
            </template>
          </el-table-column>
        </el-table>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import axios from 'axios';
// import homepageHeader from '../components/HomepageHeader.vue';
import homepageHeader from '../components/Header.vue';

export default {
  name: 'StudentHomepage',
  components: {
    // HomepageHeader: homepageHeader,
    HomepageHeader: homepageHeader,
  },
  data() {
    return {
      studentName: '马斓轩',
      tableData: [
        {
          pk: '1',
          courseID: '1001',
          name: '计算机组成原理',
          desc: '计算机方向专业的基础课程计算机方向专业的基础课程计算机方向专业的基础课'
           + '计算机方向专业的基础课程计算机方向专业的基础课程计算机方向专业的基础课程计算机方向专业的基础课程'
           + '计算机方向专业的基础课程计算机方向专业的基础课程计算机方向专业的基础课程',
          img: '../assets/lbj.png',
          useTimeList: [
            {
              timePk: '1',
              startTime: '2020-08-13 10:00:00',
              endTime: '2020-08-13 12:00:00',
            },
            {
              timePk: '2',
              startTime: '2020-08-13 10:00:00',
              endTime: '2020-08-13 12:00:00',
            },
            {
              timePk: '3',
              startTime: '2020-08-13 10:00:00',
              endTime: '2020-08-13 12:00:00',
            },
          ],
          fileList: [],
        },
        {
          pk: '2',
          courseID: '1001',
          name: '计算机组成原理',
          desc: '计算机方向专业的基础课程计算机方向专业的基础课程计算机方向专业的基础课'
           + '计算机方向专业的基础课程计算机方向专业的基础课程计算机方向专业的基础课程计算机方向专业的基础课程'
           + '计算机方向专业的基础课程计算机方向专业的基础课程计算机方向专业的基础课程',
          img: '../assets/lbj.png',
          useTimeList: [
            {
              timePk: '4',
              startTime: '2020-08-13 10:00:00',
              endTime: '2020-08-13 12:00:00',
            },
            {
              timePk: '5',
              startTime: '2020-08-13 10:00:00',
              endTime: '2020-08-13 12:00:00',
            },
            {
              timePk: '6',
              startTime: '2020-08-13 10:00:00',
              endTime: '2020-08-13 12:00:00',
            },
          ],
          fileList: [],
        },
      ],
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
        console.log(response.data);
        this.studentName = response.data.data.name;
      });
    axios({
      method: 'get',
      url: 'http://localhost:8000/QAplatform/home/',
      headers: {
        Authorization: `jwt ${window.sessionStorage.getItem('token')}`,
      },
    })
      .then((response) => {
        console.log(response.data.room_data);
        this.tableData = response.data.room_data;
        for (let i = 0; i < this.tableData.length;) {
          this.tableData[i].img = `http://localhost:8000${this.tableData[i].img}`;
          i += 1;
        }
      });
  },
};
</script>

<style scoped>
.main {
  height: 90vh;
}
.course-name {
  font-weight: bolder;
}
.form-title {
  font-size: 30px;
  color: darkgrey;
  float: left;
}
.table-title {
  width: 850px;
  margin-left: 30px;
  margin-right: 1330px;
  color: black;
  font-family:
    "Helvetica Neue",
    Helvetica,
    "PingFang SC",
    "Hiragino Sans GB",
    "Microsoft YaHei",
    "微软雅黑",
    Arial,
    sans-serif;
  font-size: 40px;
  float: left;
  margin-left: 0;
  text-align: left;
}
.course-table {
  width: 1080px;
  margin-left: 10%;
  margin-right: 10%;
}
.term-button {
  float: left;
}
</style>
