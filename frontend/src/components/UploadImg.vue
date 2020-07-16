<template>
    <div>
        <el-upload
            class="avatar-uploader"
            action="http://localhost:8000/QAplatform/office/room/3/upload/"
            :show-file-list="false"
            :on-success="handleAvatarSuccess"
            :before-upload="beforeAvatarUpload">
            <img v-if="imageUrl" :src="imageUrl" class="avatar">
            <i v-else class="el-icon-plus avatar-uploader-icon"></i>
        </el-upload>
    </div>
</template>

<script>
export default {
  data() {
    return {
      imageUrl: '',
    };
  },
  methods: {
    handleAvatarSuccess(res, file) {
      if (res.status === 200) {
        this.$message.success(res.msg);
      }
      this.imageUrl = URL.createObjectURL(file.raw);
    },
    beforeAvatarUpload(file) {
      const isIMG = ['image/jpeg', 'image/png'].includes(file.type);
      const isLt5M = file.size / 1024 / 1024 < 5;

      if (!isIMG) {
        this.$message.error('上传头像图片只能是 JPG 或 PNG 格式!');
      }
      if (!isLt5M) {
        this.$message.error('上传头像图片大小不能超过 5MB!');
      }
      return isIMG && isLt5M;
    },
  },
  mounted() {
    this.$http.get('office/room/3/').then((response) => {
      this.imageUrl = `http://localhost:8000/QAplatform/${response.data.data.img}`;
    });
  },
};
</script>

<style scoped>
.avatar-uploader .el-upload {
    border: 1px dashed #d9d9d9;
    border-radius: 6px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
  }
  .avatar-uploader .el-upload:hover {
    border-color: #409EFF;
  }
  .avatar-uploader-icon {
    font-size: 28px;
    color: #8c939d;
    width: 178px;
    height: 178px;
    line-height: 178px;
    text-align: center;
  }
  .avatar {
    width: 178px;
    height: 178px;
    display: block;
  }
</style>
