<template>
  <div>
    <el-input
      type="textarea"
      placeholder="请输入描述"
      v-model="description"
      maxlength="15"
      show-word-limit
    >
    </el-input>
    <el-button type="primary" style="margin-top: 15px">重置</el-button>
    <el-button type="primary" style="margin-top: 15px">确定</el-button>
  </div>
</template>

<script>
export default {
  name: 'RoomDescription',
  data() {
    return {
      description: '',
    };
  },
};
</script>

<style scoped>

</style>
