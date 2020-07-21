<template>
  <el-container>
    <el-header class="header">
      {{ roomName }} 修改界面
    </el-header>
    <el-tabs tab-position="left">
      <el-tab-pane label="修改老师">
        <room-teacher :room_pk="roomNum"></room-teacher>
      </el-tab-pane>
      <el-tab-pane label="修改时间">
        <room-time></room-time>
      </el-tab-pane>
      <el-tab-pane label="更改描述">
        <room-description></room-description>
      </el-tab-pane>
      <el-tab-pane label="更改封面图片">
        <room-picture></room-picture>
      </el-tab-pane>
    </el-tabs>
  </el-container>
</template>

<script>
import RoomTeacher from '../components/RoomTeacher.vue';
import RoomTime from '../components/RoomTime.vue';
import RoomDescription from '../components/RoomDescription.vue';
import RoomPicture from '../components/RoomPicture.vue';

export default {
  name: 'ModifyRoom',
  components: {
    RoomPicture, RoomDescription, RoomTime, RoomTeacher,
  },
  data() {
    return {
      roomNum: '',
      roomName: '',
    };
  },
  mounted() {
    this.roomNum = this.$route.params.roomNum;
    this.roomName = this.$route.params.roomName;
    if (this.roomNum === undefined) {
      this.$router.push('/manager');
    }
  },
};
</script>

<style scoped>
  .header {
    text-align: center;
    padding: 10px;
    font-size: 30px;
  }
</style>
