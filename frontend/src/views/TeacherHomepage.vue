<template>
    <div>
        <homepage-header></homepage-header>
       <el-container>
           <teacher-homepage-aside activeItemFromViews="1"></teacher-homepage-aside>
           <el-main class="main">
               <el-table class="room_table" :data="room_data" size="small">
                   <el-table-column type="expand">
                       <template slot-scope="scope">
                           <el-table :data="scope.row.use_time_list">
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
                               <el-table-column label="编辑直播间信息">
                                   <el-button @click="deleteLiveTime" type="danger" round>
                                       删除预定
                                   </el-button>
                                   <el-button @click="addLiveTime" type="primary" round>
                                       添加预定
                                   </el-button>
                                   <el-button @click="editLiveTime" type="success" round>
                                       修改预定
                                   </el-button>
                               </el-table-column>
                           </el-table>
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
                           <p>课程序号：{{scope.row.course_id}}</p>
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
      room_data: [
        {
          course_id: '1001',
          name: '计算机组成原理',
          desc: '计算机方向专业的基础课程',
          img: '../assets/lbj.png',
          use_time_list: [
            {
              start_time: '2020-08-13 10:00:00',
              end_time: '2020-08-13 12:00:00',
            },
            {
              start_time: '2020-08-13 10:00:00',
              end_time: '2020-08-13 12:00:00',
            },
            {
              start_time: '2020-08-13 10:00:00',
              end_time: '2020-08-13 12:00:00',
            },
          ],
          file_list: [],
        },
        {
          course_id: '1002',
          name: 'Java编程思想',
          desc: 'OOP语言--Java基础和高级',
          img: '../assets/lbj.png',
          use_time_list: [
            {
              start_time: '2020-08-13 10:00:00',
              end_time: '2020-08-13 12:00:00',
            },
            {
              start_time: '2020-08-13 10:00:00',
              end_time: '2020-08-13 12:00:00',
            },
          ],
          file_list: [],
        },
        {
          course_id: '1003',
          name: '概率论和数理统计',
          desc: '计算机专业的数学基础课程',
          img: '../assets/lbj.png',
          use_time_list: [
            {
              start_time: '2020-08-13 10:00:00',
              end_time: '2020-08-13 12:00:00',
            },
            {
              start_time: '2020-08-13 10:00:00',
              end_time: '2020-08-13 12:00:00',
            },
          ],
          file_list: [],
        },
      ],
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

.courseImg {
    width: 100px;
    height: 100px;
}
</style>
