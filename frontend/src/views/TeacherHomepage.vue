<template>
  <div>
    <homepage-header></homepage-header>
    <el-container>
      <teacher-homepage-aside activeItemFromViews="1"></teacher-homepage-aside>
      <el-main class="main">
        <span class="table-title">教师{{teacherName}}的直播课程表见下</span>
        <el-table class="room-table" :data="mainTableData" size="medium" :border="border"
        highlight-current-row>
          <el-table-column type="expand">
            <template slot-scope="scope">
              <el-table class="time-list-table" :data="scope.row.use_time_list"
              highlight-current-row :border="border">
                <el-table-column label="Index" type="index" width="100">
                </el-table-column>
                <el-table-column label="开始时间" width="180">
                  <template slot-scope="innerScope">
                    <p>{{innerScope.row.start_time}}</p>
                  </template>
                </el-table-column>
                <el-table-column label="结束时间" width="180">
                  <template slot-scope="innerScope">
                    <p>{{innerScope.row.end_time}}</p>
                  </template>
                </el-table-column>
                <el-table-column label="编辑直播间信息" width="180">
                  <template slot-scope="innerScope">
                    <el-button
                    @click="deleteLiveTime(innerScope.row.time_pk)"
                    type="danger" round>
                      删除预定
                    </el-button>
                  </template>
                </el-table-column>
              </el-table>
              <el-button @click="addDialogFormVisible = true" type="primary" plain>
                添加
              </el-button>
              <el-dialog :title="'请为课程'+scope.row.name+'添加直播时间'"
              :visible.sync="addDialogFormVisible">
                <el-form :model="form">
                  <el-form-item label="日期" :label-width="formLabelWidth">
                    <el-date-picker
                    v-model="form.date"
                    align="right"
                    type="date"
                    placeholder="选择日期"
                    :picker-options="dateQuickPickerOptions">
                    </el-date-picker>
                  </el-form-item>
                  <el-form-item label="开始时间" :label-width="formLabelWidth">
                    <el-time-select
                    placeholder="开始时间"
                    v-model="form.startTime"
                    :picker-options="{
                    start: '08:30',
                    step: '00:15',
                    end: '18:30'
                    }">
                    </el-time-select>
                  </el-form-item>
                  <el-form-item label="结束时间" :label-width="formLabelWidth">
                    <el-time-select
                    placeholder="结束时间"
                    v-model="form.endTime"
                    :picker-options="{
                    start: '08:30',
                    step: '00:15',
                    end: '18:30',
                    minTime: form.startTime
                    }">
                    </el-time-select>
                  </el-form-item>
                </el-form>
                <div slot="footer" class="dialog-footer">
                  <el-button @click="addDialogFormVisible = false">
                    取 消
                  </el-button>
                  <el-button type="primary"
                  @click="addLiveTime(scope.row.pk)">
                    确 定
                  </el-button>
                </div>
              </el-dialog>
            </template>
          </el-table-column>
          <el-table-column label="课程名称"  width="180">
            <template slot-scope="scope">
              <el-popover trigger="hover" placement="top">
                <p>课程id：{{scope.row.course_id}}</p>
                <p>课程描述：{{scope.row.desc}}</p>
                <div slot="reference" class="name-wrapper">
                  <h1>{{ scope.row.name }}</h1>
                </div>
              </el-popover>
            </template>
          </el-table-column>
          <el-table-column label="图像" width="200">
            <template slot-scope="scope">
              <el-image class="courseImg" :src="scope.row.img"></el-image>
            </template>
          </el-table-column>
          <el-table-column label="课程信息" width="280">
            <template slot-scope="scope">
              <p>课程序号：{{scope.row.course_id}}</p>
              <p>课程描述：{{scope.row.desc}}</p>
            </template>
          </el-table-column>
          <el-table-column label="进入直播间" width="180">
            <template slot-scope="scope">
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
import homepageHeader from '../components/HomepageHeader.vue';
import teacherHomepageAside from '../components/TeacherHomepageAside.vue';

export default {
  //  依赖注入
  inject: ['reload'],
  name: 'TeacherHomepage',
  components: {
    HomepageHeader: homepageHeader,
    TeacherHomepageAside: teacherHomepageAside,
  },
  data() {
    return {
      teacherName: '王子旭',
      addDialogFormVisible: false,
      border: true,
      // form为添加时的对话框中的表单信息
      form: {
        date: '',
        startTime: '',
        endTime: '',
      },
      formLabelWidth: '120px',
      dateQuickPickerOptions: {
        disabledDate(time) {
          return time.getTime() < Date.now();
        },
        shortcuts: [{
          text: '今天',
          onClick(picker) {
            picker.$emit('pick', new Date());
          },
        }, {
          text: '明天',
          onClick(picker) {
            const date = new Date();
            date.setTime(date.getTime() + 3600 * 1000 * 24);
            picker.$emit('pick', date);
          },
        }, {
          text: '一周后',
          onClick(picker) {
            const date = new Date();
            date.setTime(date.getTime() + 3600 * 1000 * 24 * 7);
            picker.$emit('pick', date);
          },
        }],
      },
      mainTableData: [],
    };
  },
  mounted() {
    axios({
      method: 'get',
      url: 'http://192.168.99.100:8000/QAplatform/detail/',
      headers: {
        Authorization: `jwt ${window.sessionStorage.getItem('token')}`,
      },
    })
      .then((response) => {
        this.teacherName = response.data.data.name;
      });
    axios({
      method: 'get',
      url: 'http://192.168.99.100:8000/QAplatform/home/',
      headers: {
        Authorization: `jwt ${window.sessionStorage.getItem('token')}`,
      },
    }).then((response) => {
      this.mainTableData = response.data.room_data;
      for (let i = 0; i < this.mainTableData.length;) {
        this.mainTableData[i].img = `http://192.168.99.100:8000${this.mainTableData[i].img}`;
        i += 1;
      }
    });
  },
  methods: {
    enterLiveRoom(courseID) {
      console.log(`Enter Live Room ${courseID}`);
      this.$router.push({
        name: 'TeacherLiveRoom',
        params: {
          room: courseID,
        },
      });
    },
    addLiveTime(roomPk) {
      this.addDialogFormVisible = false;
      const year = this.form.date.getFullYear();
      let month = this.form.date.getMonth() + 1;
      let date = this.form.date.getDate();
      if (month < 10) {
        month = `0${month}`;
      }
      if (date < 10) {
        date = `0${date}`;
      }
      axios({
        method: 'post',
        url: 'http://192.168.99.100:8000/QAplatform/home/',
        headers: {
          Authorization: `jwt ${window.sessionStorage.getItem('token')}`,
        },
        data: {
          room_pk: roomPk,
          start_time: `${year}-${month}-${date} ${this.form.startTime}:00`,
          end_time: `${year}-${month}-${date} ${this.form.endTime}:00`,
        },
      })
        .then((response) => {
          if (response.data.status === 0) {
            alert('时间冲突，请重新设置');
          } else {
            alert('设置成功～');
          }
          this.reload();
        });
    },
    deleteLiveTime(timePk) {
      axios({
        method: 'delete',
        url: 'http://192.168.99.100:8000/QAplatform/home/',
        headers: {
          Authorization: `jwt ${window.sessionStorage.getItem('token')}`,
        },
        data: {
          time_pk: timePk,
        },
      })
        .then((response) => {
          console.log(response);
          this.reload();
        });
    },
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

.course-img {
  width: 150px;
  height: 100px;
}
.room-table {
  width: 848px;
  position: relative;
  left: 20%;
  top: 40px;
}
.time-list-table {
  width: 640px;
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
</style>
