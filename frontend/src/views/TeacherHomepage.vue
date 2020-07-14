<template>
   <div>
    <!-- 顶栏 -->
    <el-container class="pageHeaderContainer">
        <h1 class="mainTitle">计发客Q&A平台</h1>
    </el-container>
    <el-container>
      <!-- 边栏 -->
      <el-aside class="aside">
          <!-- <el-menu
           default-active="2"
          class="el-menu-vertical-demo"
           @open="handleOpen"
           @close="handleClose">
             <el-menu-item index="1">
                <i class="el-icon-location"></i>
               <span>直播安排</span>
             </el-menu-item>
             <el-menu-item index="2">
                <i class="el-icon-menu"></i>
                <span slot="title">日历</span>
             </el-menu-item>
             <el-menu-item index="3">
                <i class="el-icon-setting"></i>
                <span slot="title">个人信息</span>
             </el-menu-item>
           </el-menu> -->
      </el-aside>
      <!-- 主要部分 -->
      <el-main class="main">
            <!-- <div id="titleOne">{{teacher_name}}***老师您好，
              今天是{{this.now.getMonth()}}月{{this.now.getDate()}}日，
              您的近期直播见下表
            </div> -->
            <!-- <el-table :data="tableData" style="width: 100%">
                    <el-table-column
                    label="课程id"
                    width="180">
                    <template slot-scope="scope">
                        <el-popover trigger="hover" placement="top">
                        <p>课程ID: {{ scope.row.courseID }}</p>
                        <p>课程名称: {{ scope.row.courseName }}</p>
                        <div slot="reference" class="name-wrapper">
                            <el-tag size="medium">{{ scope.row.courseID }}</el-tag>
                        </div>
                        </el-popover>
                    </template>
                    </el-table-column>
                    <el-table-column
                    prop="liveDate"
                    label="日期"
                    width="180">
                    </el-table-column>
                    <el-table-column
                    prop="liveDay"
                    label="星期"
                    width="180">
                    </el-table-column>
                    <el-table-column
                    label="起止时间(24小时制）"
                    width="250">
                    <template slot-scope="scope">
                    From&nbsp;&nbsp;{{scope.row.liveStartTime}}
                    To&nbsp;&nbsp;{{scope.row.liveEndTime}}
                    </template>
                    </el-table-column>
                    <el-table-column
                    label="取消"
                    width="180">
                    <template slot-scope="scope">
                    <el-button @click="cancelLive(scope.$index)" >取消直播</el-button>
                    </template>
                    </el-table-column>
                    <el-table-column
                    label="进入"
                    width="180">
                      <el-button @click="enterLiveRoom(scope.$index)">进入直播</el-button>
                    </el-table-column>
            </el-table> -->
            <!-- 添加栏 -->
            <!-- <el-row>
                <el-col>
                    <span >选择直播时间: </span>
                </el-col>
            </el-row> -->
            <!-- <el-row :gutter="25" >
                <el-col span="4.8">
                    <div class="newLivePeriod">
                        <el-date-picker
                        v-model="addedDate"
                        align="right"
                        type="date"
                        placeholder="选择日期"
                        :picker-options="pickerOptions">
                        </el-date-picker>
                    </div>
                </el-col>
                <el-col span="4.8">
                        <el-time-select
                            placeholder="起始时间"
                            v-model="addedStartTime"
                            :picker-options="{
                            start: '08:30',
                            step: '00:15',
                            end: '18:30'
                            }">
                        </el-time-select>
                </el-col>
                <el-col span="4.8">
                    <el-time-select
                            placeholder="结束时间"
                            v-model="addedEndTime"
                            :picker-options="{
                            start: '08:30',
                            step: '00:15',
                            end: '18:30',
                            minTime: this.addedStartTime
                            }">
                        </el-time-select>
                </el-col>
                <el-col span="4.8">
                    <div>
                    <el-input
                        placeholder="请输入课程ID号"
                        v-model="addedCourseID"
                        clearable>
                    </el-input>
                    </div>
                </el-col>
                <el-col span="4.8">
                    <el-button @click="addLive">
                            确认预定直播
                    </el-button>
                </el-col>
            </el-row> -->
      </el-main>
    </el-container>
   </div>
</template>

<script>
export default {
  name: 'TeacherHomepage',
  data() {
    return {
      now: new Date(),
      teacherName: '',
      teacherID: '',
      tableData: [{
        courseID: '10001',
        courseName: '数据结构',
        liveDate: '2016-05-02',
        liveDay: '星期五',
        liveStartTime: '9:00',
        liveEndTime: '11:00',
      }, {
        courseID: '10001',
        courseName: '数据结构',
        liveDate: '2016-05-02',
        liveDay: '星期五',
        liveStartTime: '9:00',
        liveEndTime: '11:00',
      }, {
        courseID: '10001',
        courseName: '数据结构',
        liveDate: '2016-05-02',
        liveDay: '星期五',
        liveStartTime: '9:00',
        liveEndTime: '11:00',
      }, {
        courseID: '10001',
        courseName: '数据结构',
        liveDate: '2016-05-02',
        liveDay: '星期五',
        liveStartTime: '9:00',
        liveEndTime: '11:00',
      }],
      //   日期表的设置
      pickerOptions: {
        //   确定不能选择的日期
        disabledDate(time) {
          return time.getTime() < Date.now() - 8.64e7;
        },
        // 日期表的快捷查找方式
        shortcuts: [{
          text: '今天',
          onClick(picker) {
            picker.$emit('pick', new Date());
          },
        },
        {
          text: '明天',
          onClick(picker) {
            const date = new Date();
            date.setTime(date.getTime() + 3600 * 1000 * 24);
            alert(date);
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
      addedDate: '',
      addedDay: '',
      addedStartTime: '',
      addedEndTime: '',
      addedCourseID: '',
      addedCourseName: '',
    };
  },
  mounted() {
    // 登陆界面传入的教师信息；
    this.teacherName = this.$route.params.teacherName;
    this.teacherID = this.$route.params.teacherID;
    this.$http.get('QAPlatform/home')
      .then((response) => {
        this.tableData = response.data;
      })
      .catch((error) => {
        console.log(error);
      });
  },
  methods: {
    cancelLive(index) {
    // 对应的直播间设置为关闭；
      this.tableData.splice(index, 1);
    },
    addLive() {
      this.$http({
        method: 'post',
        url: 'QAPlatform',
        headers: {
          Authorization: `jwt ${window.sessionStorage.getItem('token')}`,
        },
      })
        .then((response) => {
          alert('请求发送成功！');
          this.tableData.push(response.data.course_data);
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
.aside {
    background-color: grey;
    height: 90vh;
}
.pageHeaderContainer {
    background-color: rgb(64,158,255);
    height: 10vh;
}
.mainTitle {
    width: 250px;
    margin-left: 30px;
    margin-right: 1330px;
    color: white;
    font-family:
     "Helvetica Neue",
     Helvetica,
     "PingFang SC",
     "Hiragino Sans GB",
     "Microsoft YaHei",
     "微软雅黑",
     Arial,
     sans-serif;
    float: left;
}
</style>
