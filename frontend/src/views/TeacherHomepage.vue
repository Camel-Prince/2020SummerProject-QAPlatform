<template>
    <div>
        <homepage-header></homepage-header>
       <el-container>
           <teacher-homepage-aside activeItemFromViews="1"></teacher-homepage-aside>
           <el-main class="main">
               <span class="tableTitle">教师{{teacherName}}好，您的直播课程表见下</span>
               <el-table class="roomTable" :data="roomData" size="medium" border="true">
                   <el-table-column type="expand">
                       <template slot-scope="scope">
                           <el-table class="timeListTable" :data="scope.row.useTimeList"
                           highlight-current-row border="true">
                               <el-table-column label="Index" type="index" width="100">
                               </el-table-column>
                               <el-table-column label="开始时间" width="180">
                                   <template slot-scope="innerScope">
                                       <p>{{innerScope.row.startTime}}</p>
                                   </template>
                               </el-table-column>
                               <el-table-column label="结束时间" width="180">
                                   <template slot-scope="innerScope">
                                       <p>{{innerScope.row.endTime}}</p>
                                   </template>
                               </el-table-column>
                               <el-table-column label="编辑直播间信息" width="180">
                                   <template slot-scope="innerScope">
                                     <el-button
                                    @click="deleteLiveTime(scope.row.pk, innerScope.row.timePk)"
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
                               <p>课程id：{{scope.row.courseID}}</p>
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
                           <p>课程序号：{{scope.row.courseID}}</p>
                           <p>课程描述：{{scope.row.desc}}</p>
                       </template>
                   </el-table-column>
                   <el-table-column label="进入直播间" width="180">
                       <el-button @click="enterLiveRoom" type="success" plain>
                           进入
                       </el-button>
                   </el-table-column>
               </el-table>
           </el-main>
       </el-container>
    </div>
</template>

<script>
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
      roomData: [
        {
          pk: '1',
          courseID: '1001',
          name: '计算机组成原理',
          desc: '计算机方向专业的基础课程',
          img: 'http://edu-image.nosdn.127.net/AE0974AF6E148500A0B32319BA56313A.png?imageView&thumbnail=510y288&quality=100',
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
          courseID: '1002',
          name: 'Java',
          desc: 'Java语言初高级课程',
          img: 'http://edu-image.nosdn.127.net/E6930D201BB66A2053F97B5341C4064F.jpg?imageView&thumbnail=426y240&quality=100',
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
          ],
          fileList: [],
        },
        {
          pk: 3,
          courseID: '1003',
          name: '概率论和数理统计',
          desc: '计算机专业的数学基础课程',
          img: 'http://edu-image.nosdn.127.net/B1793E3DCEB8C6489EB40510C6F8DEE9.jpg?imageView&thumbnail=510y288&quality=100',
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
          ],
          fileList: [],
        },
      ],
    };
  },
  mounted() {
    this.$http({
      method: 'get',
      url: 'http://localhost:8000/QAplatform/home/',
      headers: {
        Authorization: `jwt ${window.sessionStorage.getItem('token')}`,
      },
    }).then((response) => {
      this.roomData = response.data;
      console.log(response.data);
    });
  },
  methods: {
    addLiveTime(roomPk) {
      this.addDialogFormVisible = false;
      alert(roomPk);
      //   发送请求
      this.$http({
        method: 'post',
        url: 'http://localhost:8000/QAplatform/home/',
        headers: {
          Authorization: `jwt ${window.sessionStorage.getItem('token')}`,
        },
        data: {
          pk: roomPk,
          start_time: this.form.date.getDate() + this.form.startTime,
          end_time: this.form.date.getDate() + this.form.endTime,
        },
      })
        .then((response) => {
          console.log(response);
          this.reload();
        });
    },
    deleteLiveTime(roomPk, timePk) {
      this.$http({
        method: 'post',
        url: 'http://localhost:8000/QAplatform/home/',
        headers: {
          Authorization: `jwt ${window.sessionStorage.getItem('token')}`,
        },
        data: {
          pk: roomPk,
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

.courseImg {
    width: 150px;
    height: 100px;
}
.roomTable {
    width: 848px;
    position: relative;
    left: 20%;
    top: 40px;
}
.timeListTable {
    width: 640px;
}
.tableTitle {
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
