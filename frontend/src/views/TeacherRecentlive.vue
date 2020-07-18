<template>
  <div>
    <homepage-header></homepage-header>
    <el-container>
      <teacher-homepage-aside></teacher-homepage-aside>
      <el-main class="main">
        <el-table :data="room_data">
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
          <el-table-column label="开课时间表" width="280">
            <template slot-scope="outterScope">
              <el-table :data="outterScope.row.use_time_list">
                <el-table-column label="详细时间" width="280">
                  <template slot-scope="innerScope">
                    <p>日期：{{innerScope.row.date}}</p>
                    <p>开始：{{innerScope.row.start_time}}</p>
                    <p>结束：{{innerScope.row.end_time}}</p>
                  </template>
                </el-table-column>
                <el-table-column label="选择">
                  <el-button>
                     进入直播间
                  </el-button>
                </el-table-column>
              </el-table>
            </template>
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
  name: 'TeacherRecentlive',
  data() {
    return {
      room_data: [
        {
          course_id: '1001',
          name: 'Java',
          desc: 'OOP语言Java基础和部分高级用法',
          img: '',
          use_time_list: [
            {
              date: '2020-8-12',
              start_time: '10:00:00',
              end_time: '11:30:00:00',
            },
          ],
        },
        {
          course_id: '1002',
          name: 'C++',
          desc: 'OOP语言C++基础和部分高级用法',
          img: '',
          use_time_list: [
            {
              date: '2020-8-13',
              start_time: '09:00:00',
              end_time: '10:30:00:00',
            },
          ],
        },
        {
          course_id: '1003',
          name: '数据库',
          desc: '数据库作业解析',
          img: '',
          use_time_list: [
            {
              date: '2020-9-01',
              start_time: '13:00:00',
              end_time: '15:30:00:00',
            },
          ],
        },
      ],
    };
  },
  components: {
    HomepageHeader: homepageHeader,
    TeacherHomepageAside: teacherHomepageAside,
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
