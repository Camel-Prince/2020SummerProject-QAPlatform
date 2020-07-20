<template>
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
      :data="teacher">
<!-- <span slot-scope="{ option }">{{ option.key }} - {{ option.label }}</span>  自定义列表项样式-->
      <el-button class="transfer-footer" slot="left-footer" size="small">重置</el-button>
      <el-button class="transfer-footer" slot="right-footer" size="small">确定</el-button>
    </el-transfer>
  </div>
</template>

<script>
export default {
  name: 'RoomTeacher',
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
      teacher: generateData(),
      value: [1],
    };
  },
  methods: {
    handleChange(value, direction, movedKeys) {
      console.log(value, direction, movedKeys);
    },
  },
};
</script>

<style scoped>
  .transfer-footer {
    margin-left: 20px;
    padding: 6px 5px;
  }
</style>
