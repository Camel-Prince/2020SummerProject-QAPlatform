<template>
   <div>
    <!-- 顶栏 -->
    <teacher-home-header></teacher-home-header>
    <el-container>
      <!-- 边栏 -->
      <el-aside class="aside">
          <el-menu default-active="1" active-text-color="#409EFF">
              <el-menu-item index="1" @click="toInformationPage">
                  <i class="el-icon-user"></i>
                 <span>
                     个人信息
                 </span>
              </el-menu-item>
              <el-menu-item index="2" @click="toRecentLive">
                  <i class="el-icon-video-camera"></i>
                  <span>近期直播</span>
              </el-menu-item>
              <el-menu-item index="3" @click="toWeekLiveTime">
                  <i class="el-icon-notebook-2"></i>
                  <span>
                     每周直播时长统计
                  </span>
              </el-menu-item>
          </el-menu>
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
import teacherHomeHeader from '../components/TeacherHomeHeader.vue';

export default {
  name: 'TeacherHomepage',
  components: {
    TeacherHomeHeader: teacherHomeHeader,
  },
  data() {
    return {
      teacher_data: {
        name: '谢茂强',
        id: '10001',
      },
      room_data: {
        course_id: '123',
        name: 'Java',
        desc: 'NULL',
        img: '',
      },
    };
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
</style>
