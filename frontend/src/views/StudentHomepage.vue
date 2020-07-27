<template>
  <div>
    <homepage-header>
    </homepage-header>
    <el-container>
      <el-main>
        <span class="table-title">{{studentName}}同学，你的课程如下</span>
        <el-form>
          <el-form-item label="课程状态">
            <el-button @click="selectAllCourses" class="term-button" type="text">
              全部课程
            </el-button>
            <el-button @click="selectNoLiveCourses" class="term-button" type="text">
              暂无直播安排
            </el-button>
            <el-button @click="selectLivingCourses" class="term-button" type="text">
              正在直播
            </el-button>
            <el-button @click="selectOncomingCourses" class="term-button" type="text">
              即将开始
            </el-button>
          </el-form-item>
        </el-form>
        <el-table :data="selectedData" size="small" class="courseTable">
          <el-table-column type="expand">
            <template slot-scope="scope">
              <p>直播时间列表</p>
              <el-table :data="scope.row.use_time_list" helight-current-row>
                <el-table-column label="开始时间" width="180">
                  <template slot-scope="innerScope">
                    {{innerScope.row.start_time}}
                  </template>
                </el-table-column>
                <el-table-column label="结束时间" width="180">
                  <template slot-scope="innerScope">
                    {{innerScope.row.end_time}}
                  </template>
                </el-table-column>
              </el-table>
            </template>
          </el-table-column>
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
          <el-table-column>
            <template slot-scope="scope" width="180">
                <el-button @click="enterLiveRoom(scope.row.pk)" type="success" plain>
                  进入
                </el-button>
            </template>
          </el-table-column>
        </el-table>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import axios from 'axios';
import homepageHeader from '../components/Header.vue';

export default {
  inject: ['reload'],
  name: 'StudentHomepage',
  components: {
    HomepageHeader: homepageHeader,
  },
  data() {
    return {
      studentName: '马斓轩',
      roomData: [],
      selectedData: [],
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
        this.roomData = response.data.room_data;
        for (let i = 0; i < this.roomData.length;) {
          this.roomData[i].img = `http://localhost:8000${this.roomData[i].img}`;
          i += 1;
        }
        this.selectedData = this.roomData;
        console.log(this.selectedData);
      });
  },
  methods: {
    enterLiveRoom(roomPk) {
      this.$router.push({
        name: 'StudentLiveRoom',
        params: {
          room: roomPk,
        },
      });
      console.log(`进入课程：${roomPk}`);
    },
    selectAllCourses() {
      this.selectedData = this.roomData;
      console.log('Select All Courses');
    },
    selectNoLiveCourses() {
      console.log('select courses with no live');
      this.selectedData = [];
      const allCourses = this.roomData;
      for (let i = 0; i < allCourses.length; i += 1) {
        const timeList = allCourses[i].use_time_list;
        if (timeList.length === 0) {
          this.selectedData.push(allCourses[i]);
        }
      }
      console.log(this.selectedData);
    },
    selectLivingCourses() {
      console.log('select courses which are living');
      this.selectedData = [];
      const allCourses = this.roomData;
      for (let i = 0; i < allCourses.length; i += 1) {
        const timeList = allCourses[i].use_time_list;
        const now = new Date();
        for (let j = 0; j < timeList.length; j += 1) {
          const courseStartTime = new Date(timeList[j].start_time);
          const courseEndTime = new Date(timeList[j].end_time);
          if (courseStartTime < now && now < courseEndTime) {
            this.selectedData.push(allCourses[i]);
            break;
          }
        }
      }
    },
    selectOncomingCourses() {
      console.log('select courses on coming');
      this.selectedData = [];
      const allCourses = this.roomData;
      for (let i = 0; i < allCourses.length; i += 1) {
        const timeList = allCourses[i].use_time_list;
        const now = new Date();
        for (let j = 0; j < timeList.length; j += 1) {
          const courseStartTime = new Date(timeList[j].start_time);
          if (courseStartTime > now) {
            this.selectedData.push(allCourses[i]);
            break;
          }
        }
      }
    },
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
