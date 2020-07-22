<template>
  <div>
    <div class="time">
      <el-form :model="form">
        <el-form-item label="直播日期">
          <el-date-picker
            v-model="form.date"
            align="right"
            type="date"
            placeholder="选择日期"
            :picker-options="datePickerOptions">
          </el-date-picker>
        </el-form-item>
        <el-form-item label="开始时间">
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
        <el-form-item label="结束时间">
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
    </div>
    <div class="time-button">
      <el-button type="info" @click="onClear">重置</el-button>
      <el-button type="primary" @click="onSubmit">确定</el-button>
    </div>
  </div>
</template>

<script>

export default {
  name: 'RoomTime',
  props: {
    room_pk: null,
  },
  data() {
    return {
      content: '111',
      form: {
        date: '',
        startTime: '',
        endTime: '',
      },
      datePickerOptions: {
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
    };
  },
  methods: {
    onClear() {
      this.form.date = '';
      this.form.startTime = '';
      this.form.endTime = '';
    },
    onSubmit() {
    },
  },
};
</script>

<style scoped>
  .time {
    margin: auto;
    width: 300px;
  }
  .time-button {
    margin-right: 20vh;
  }
</style>
