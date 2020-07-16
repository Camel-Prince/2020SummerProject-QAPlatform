<template>
    <div>
        <homepage-header></homepage-header>
       <el-container>
           <teacher-homepage-aside activeItemFromViews="1"></teacher-homepage-aside>
           <el-main class="main">
               <el-table class="roomTable" :data="roomData" size="small">
                   <el-table-column type="expand">
                       <template slot-scope="scope">
                           <el-table :data="scope.row.useTimeList">
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
                               <el-table-column label="编辑直播间信息">
                                   <el-button @click="deleteLiveTime" type="danger" round>
                                       删除预定
                                   </el-button>
                                   <el-button @click="editLiveTime" type="success" round>
                                       修改预定
                                   </el-button>
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
                                        @click="addDialogFormVisible = false">
                                            确 定
                                        </el-button>
                                </div>
                            </el-dialog>
                       </template>
                   </el-table-column>
                   <el-table-column label="课程名称"  width="180">
                       <template slot-scope="scope">
                           <h1>{{scope.row.name}}</h1>
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
                           <p>课程名称：{{scope.row.name}}</p>
                       </template>
                   </el-table-column>
                   <el-table-column label="进入直播间">
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
  name: 'TeacherHomepage',
  components: {
    HomepageHeader: homepageHeader,
    TeacherHomepageAside: teacherHomepageAside,
  },
  data() {
    return {
      addDialogFormVisible: false,
      editDialogFormVisible: false,
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
          courseID: '1001',
          name: '计算机组成原理',
          desc: '计算机方向专业的基础课程',
          img: '../assets/lbj.png',
          useTimeList: [
            {
              startTime: '2020-08-13 10:00:00',
              endTime: '2020-08-13 12:00:00',
            },
            {
              startTime: '2020-08-13 10:00:00',
              endTime: '2020-08-13 12:00:00',
            },
            {
              startTime: '2020-08-13 10:00:00',
              endTime: '2020-08-13 12:00:00',
            },
          ],
          fileList: [],
        },
        {
          courseID: '1002',
          name: 'Java编程思想',
          desc: 'OOP语言--Java基础和高级',
          img: '../assets/lbj.png',
          useTimeList: [
            {
              startTime: '2020-08-13 10:00:00',
              endTime: '2020-08-13 12:00:00',
            },
            {
              startTime: '2020-08-13 10:00:00',
              endTime: '2020-08-13 12:00:00',
            },
          ],
          fileList: [],
        },
        {
          courseID: '1003',
          name: '概率论和数理统计',
          desc: '计算机专业的数学基础课程',
          img: '../assets/lbj.png',
          useTimeList: [
            {
              startTime: '2020-08-13 10:00:00',
              endTime: '2020-08-13 12:00:00',
            },
            {
              startTime: '2020-08-13 10:00:00',
              endTime: '2020-08-13 12:00:00',
            },
          ],
          fileList: [],
        },
      ],
    };
  },
  methods: {
    addLiveTime() {
      this.dialogFormVisible = true;
    //   后端接口
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
    width: 100px;
    height: 100px;
}
</style>
