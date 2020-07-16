<template>
  <el-container>
    <el-header class="header">
      房间{{ roomNum }} 修改界面
    </el-header>
    <el-tabs tab-position="left">
      <el-tab-pane label="修改老师">
        <div style="text-align: center">
          <div style="text-align: center">
            <el-transfer
              style="text-align: left; display: inline-block"
              v-model="value"
              filterable
              filter-placeholder="请输入老师名称"
              :left-default-checked="[2, 3]"
              :right-default-checked="[1]"
              :titles="['可增加的老师', '已有的老师']"
              :button-texts="['到左边', '到右边']"
              :format="{
          noChecked: '${total}',
          hasChecked: '${checked}/${total}'
        }"
              @change="handleChange"
              :data="data">
      <!-- <span slot-scope="{ option }">{{ option.key }} - {{ option.label }}</span>  自定义列表项样式-->
              <el-button class="transfer-footer" slot="left-footer" size="small">操作</el-button>
              <el-button class="transfer-footer" slot="right-footer" size="small">操作</el-button>
            </el-transfer>
          </div>
        </div>
      </el-tab-pane>
      <el-tab-pane label="修改时间">
        <el-select v-model="weekDay" placeholder="请选择">
          <el-option
            v-for="item in weekDayOptions"
            :key="item.value"
            :label="item.label"
            :value="item.value">
          </el-option>
        </el-select>
        <el-time-picker
          class="time"
          is-range
          v-model="time"
          range-separator="至"
          start-placeholder="开始时间"
          end-placeholder="结束时间"
          placeholder="选择时间范围">
        </el-time-picker>
      </el-tab-pane>
      <el-tab-pane label="更改描述">
        <el-input
          type="textarea"
          placeholder="请输入描述"
          v-model="description"
          maxlength="15"
          show-word-limit
        >
        </el-input>
      </el-tab-pane>
      <el-tab-pane label="更改封面图片">
        111
      </el-tab-pane>
    </el-tabs>
  </el-container>
</template>

<script>
export default {
  name: 'ModifyRoom',
  data() {
    // eslint-disable-next-line no-unused-vars
    const generateData = (_) => {
      const data = [];
      // eslint-disable-next-line no-plusplus
      for (let i = 1; i <= 15; i++) {
        data.push({
          key: i,
          label: `老师 ${i}`,
          disabled: i % 4 === 0,
        });
      }
      return data;
    };
    return {
      roomNum: '',
      description: '',
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
      data: generateData(),
      value: [1],
    };
  },
  mounted() {
    this.roomNum = this.$route.params.roomNum;
  },
  methods: {
    handleChange(value, direction, movedKeys) {
      console.log(value, direction, movedKeys);
    },
  },
};
</script>

<style scoped>
  .header {
    text-align: center;
    padding: 10px;
    font-size: 30px;
  }
  .time {
    margin: 30px 0;
  }
  .transfer-footer {
    margin-left: 20px;
    padding: 6px 5px;
  }
</style>
