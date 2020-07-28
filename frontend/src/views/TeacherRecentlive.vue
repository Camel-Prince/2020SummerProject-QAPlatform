<template>
  <div>
    <homepage-header></homepage-header>
    <el-container>
      <teacher-homepage-aside activeItemFromViews="3"></teacher-homepage-aside>
      <el-main class="main">
        <el-table :data="tableData">
          <el-table-column label="课程名称" width="180">
            <template slot-scope="scope">
              <el-popover trigger="hover" placement="top">
                <p>课程id：{{scope.row.course_id}}</p>
                <p>课程描述：{{scope.row.desc}}</p>
                <div slot="reference" class="name-wrapper">
                  <el-tag size="medium">{{ scope.row.name }}</el-tag>
                </div>
              </el-popover>
            </template>
          </el-table-column>
          <el-table-column label="最近直播时间">
            <template slot-scope="scope">
              <p>日期：{{scope.row.use_time_list.date}}</p>
              <p>开始时间：{{scope.row.use_time_list.start_time}}</p>
              <p>结束时间：{{scope.row.use_time_list.end_time}}</p>
            </template>
          </el-table-column>
          <el-table-column>
            <template slot-scope="scope">
            <el-button @click="enterLiveRoom(scope.row.pk)" type="success" plain>
              进入直播间
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
import homepageHeader from '../components/HomepageHeader.vue';
import teacherHomepageAside from '../components/TeacherHomepageAside.vue';

export default {
  name: 'TeacherRecentlive',
  components: {
    HomepageHeader: homepageHeader,
    TeacherHomepageAside: teacherHomepageAside,
  },
  data() {
    return {
      // 放在表中的、各个学科的最近一次直播的信息
      tableData: [],
      // 从后端得到的数据
      roomData: [],
    };
  },
  methods: {
    getRecentLive() {
      const roomNumber = this.roomData.length;
      for (let i = 0; i < roomNumber; i += 1) {
        const timeList = this.roomData[i].use_time_list;
        const timeListLength = timeList.length;
        let recentTimeIndex = 0;
        let recentStartTime = new Date(timeList[recentTimeIndex].start_time);
        let recentEndTime = new Date(timeList[recentTimeIndex].end_time);
        for (recentTimeIndex = 1; recentTimeIndex < timeListLength; recentTimeIndex += 1) {
          const tempStartTime = new Date(timeList[recentTimeIndex].start_time);
          if (tempStartTime - recentStartTime < 0) {
            recentStartTime = tempStartTime;
            recentEndTime = new Date(timeList[recentTimeIndex].end_time);
          }
        }
        this.tableData.push({
          pk: this.roomData[i].pk,
          course_id: this.roomData[i].course_id,
          name: this.roomData[i].name,
          desc: this.roomData[i].desc,
          img: this.roomData[i].img,
          use_time_list: {
            date: `${recentStartTime.getFullYear()}-${recentStartTime.getMonth() + 1}-${recentStartTime.getDate()}`,
            start_time: `${recentStartTime.getHours()}时${recentStartTime.getMinutes()}分`,
            end_time: `${recentEndTime.getHours()}时${recentEndTime.getMinutes()}分`,
          },
        });
      }
    },
    enterLiveRoom(roomPk) {
      this.$router.push({
        name: 'TeacherLiveRoom',
        params: {
          room: roomPk,
        },
      });
      console.log(`Enter Live Room ${roomPk}`);
    },
  },
  mounted() {
    axios({
      method: 'get',
      url: 'http://localhost:8000/QAplatform/home/',
      headers: {
        Authorization: `jwt ${window.sessionStorage.getItem('token')}`,
      },
    }).then((response) => {
      this.roomData = response.data.room_data;
      for (let i = 0; i < this.roomData.length;) {
        this.roomData[i].img = `http://localhost:8000${this.roomData[i].img}`;
        i += 1;
      }
      this.getRecentLive();
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
