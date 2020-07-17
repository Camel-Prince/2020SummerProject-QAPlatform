<template>
  <div>
    <el-upload
      action="#"
      list-type="picture-card"
      :limit="1"
      :auto-upload="false"
      :on-preview="handlePictureCardPreview"
      :on-remove="handleRemove">
      <i class="el-icon-plus"></i>
    </el-upload>
    <el-dialog :visible.sync="dialogVisible">
      <img width="100%" :src="dialogImageUrl" alt="">
    </el-dialog>
    <el-button type="primary" style="margin-top: 15px" @click="uploadPicture">确定</el-button>
  </div>
</template>

<script>
export default {
  name: 'RoomPicture',
  data() {
    return {
      dialogImageUrl: '',
      dialogVisible: false,
    };
  },
  methods: {
    handleRemove() {
      this.$message({
        type: 'success',
        message: '删除成功!',
      });
    },
    handlePictureCardPreview(file) {
      this.dialogImageUrl = file.url;
      this.dialogVisible = true;
    },
    uploadPicture() {
      // 上传图片
    },
  },
};
</script>

<style scoped>

</style>
