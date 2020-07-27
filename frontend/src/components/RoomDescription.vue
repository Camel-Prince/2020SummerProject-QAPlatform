<template>
  <div>
    <el-input
      type="textarea"
      placeholder="请输入描述"
      v-model="description"
      maxlength="25"
      show-word-limit
    >
    </el-input>
    <el-button type="primary" style="margin-top: 15px" @click="initDesc">重置</el-button>
    <el-button type="primary" style="margin-top: 15px" @click="submit">确定</el-button>
  </div>
</template>

<script>
export default {
  name: 'RoomDescription',
  props: {
    roomPk: String,
  },
  data() {
    return {
      description: '',
    };
  },
  watch: {
    roomPk() {
      this.initDesc();
    },
  },
  methods: {
    initDesc() {
      this.$http.get(`office/room/${this.roomPk}/`)
        .then((response) => {
          this.description = response.data.data.desc;
        });
    },
    submit() {
      this.$http.post(`office/room/${this.roomPk}/`, { choice: 3, desc: this.description })
        .then(() => this.$message({
          type: 'success',
          message: '更改成功!',
        }));
    },
  },
};
</script>

<style scoped>

</style>
