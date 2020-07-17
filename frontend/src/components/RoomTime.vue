<template>
  <div>
    <div class="time">
      <span>星期：</span>
      <el-select v-model="weekDay" placeholder="请选择">
        <el-option
          v-for="item in weekDayOptions"
          :key="item.value"
          :label="item.label"
          :value="item.value">
        </el-option>
      </el-select>
    </div>
    <div class="time">
      <span>时间：</span>
      <el-time-picker
        is-range
        v-model="time"
        range-separator="至"
        start-placeholder="开始时间"
        end-placeholder="结束时间"
        placeholder="选择时间范围">
      </el-time-picker>
    </div>
    <div class="time">
      <el-button type="primary">重置</el-button>
      <el-button type="primary">确定</el-button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'RoomTime',
  data() {
    return {
      weekDayOptions: [{
        value: '周一',
        label: '周一',
      }, {
        value: '周二',
        label: '周二',
      }, {
        value: '周三',
        label: '周三',
      }, {
        value: '周四',
        label: '周四',
      }, {
        value: '周五',
        label: '周五',
      }, {
        value: '周六',
        label: '周六',
      }, {
        value: '周日',
        label: '周日',
      }],
      weekDay: '',
      time: [new Date(2016, 9, 10, 8, 40), new Date(2016, 9, 10, 9, 40)],
    };
  },
};
</script>

<style scoped>
  .time {
    margin: 50px;
  }
</style>
