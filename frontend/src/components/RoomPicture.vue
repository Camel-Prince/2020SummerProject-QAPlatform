<template>
  <div>
    <el-upload
      :action=actionURL
      list-type="picture-card"
      ref="upload"
      :limit="2"
      :file-list="fileList"
      :auto-upload="false"
      :on-exceed="handleUpLimit"
      :on-preview="handlePictureCardPreview"
      :on-success="handleAvatarSuccess"
      :before-upload="beforeAvatarUpload">
      <i class="el-icon-plus"></i>
    </el-upload>
    <el-dialog :visible.sync="dialogVisible">
      <img width="100%" :src="imageUrl" alt="">
    </el-dialog>
    <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过5MB</div>
    <el-button type="primary" style="margin-top: 15px" @click="uploadPicture">确定</el-button>
  </div>
</template>

<script>
export default {
  name: 'RoomPicture',
  props: {
    roomPk: String,
  },
  data() {
    return {
      fileList: [],
      imageUrl: '',
      dialogVisible: false,
      actionURL: '',
    };
  },
  watch: {
    roomPk() {
      this.actionURL = `http://localhost:8000/QAplatform/office/room/${this.roomPk}/upload/`;
      this.$http.get(`office/room/${this.roomPk}/`).then((response) => {
        this.fileList.push({ url: `http://localhost:8000/QAplatform${response.data.data.img}` });
      });
    },
  },
  methods: {
    handleUpLimit() {
      this.$notify.error({
        title: '错误',
        message: '只能选择上传一张图片',
      });
    },
    handlePictureCardPreview(file) {
      this.imageUrl = file.url;
      this.dialogVisible = true;
    },
    handleAvatarSuccess(res, file) {
      if (res.status === 200) {
        this.$notify({
          title: '成功',
          message: res.msg,
          type: 'success',
        });
      }
      this.imageUrl = URL.createObjectURL(file.raw);
    },
    beforeAvatarUpload(file) {
      const isIMG = ['image/jpeg', 'image/png'].includes(file.type);
      const isLt5M = file.size / 1024 / 1024 < 5;

      if (!isIMG) {
        this.$notify.error({
          title: '错误',
          message: '上传头像图片只能是 JPG 或 PNG 格式!',
        });
      }
      if (!isLt5M) {
        this.$notify.error({
          title: '错误',
          message: '上传头像图片大小不能超过 5MB!',
        });
      }
      return isIMG && isLt5M;
    },
    uploadPicture() {
      // 上传图片
      this.$refs.upload.submit();
    },
  },
};
</script>

<style scoped>

</style>
