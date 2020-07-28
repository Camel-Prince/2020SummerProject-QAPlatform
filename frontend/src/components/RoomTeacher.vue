<template>
  <div style="text-align: center">
    <el-transfer
      style="text-align: left; display: inline-block"
      v-model="value"
      filterable
      filter-placeholder="请输入老师名称"
      :titles="['可增加的老师', '已有的老师']"
      :button-texts="['到左边', '到右边']"
      :format="{
        noChecked: '${total}',
        hasChecked: '${checked}/${total}'
      }"
      :data="teachers">
      <el-button class="transfer-footer" slot="left-footer" size="small" @click="replace">
        重置
      </el-button>
      <el-button class="transfer-footer" slot="right-footer" size="small" @click="submit">
        确定
      </el-button>
    </el-transfer>
  </div>
</template>

<script>
export default {
  name: 'RoomTeacher',
  props: {
    roomPk: String,
  },
  data() {
    return {
      exTeachers: '',
      nowTeachers: '',
      value: [],
    };
  },
  computed: {
    teachers() {
      const data = [];
      for (let i = 0; i < this.nowTeachers.length; i += 1) {
        data.push({
          key: i,
          label: this.nowTeachers[i].name,
          disabled: false,
        });
      }
      for (let i = 0; i < this.exTeachers.length; i += 1) {
        data.push({
          key: this.nowTeachers.length + i,
          label: this.exTeachers[i].name,
          disabled: false,
        });
      }
      return data;
    },
    teacherPK() {
      return this.nowTeachers.concat(this.exTeachers).map((teacher) => teacher.pk);
    },
    initValue() {
      const data = [];
      for (let i = 0; i < this.nowTeachers.length; i += 1) {
        data.push(i);
      }
      return data;
    },
  },
  methods: {
    replace() {
      this.value = this.initValue;
    },
    submit() {
      const initPks = [];
      for (let i = 0; i < this.initValue.length; i += 1) {
        initPks.push(this.teacherPK[this.initValue[i]]);
      }
      const pks = [];
      for (let i = 0; i < this.value.length; i += 1) {
        pks.push(this.teacherPK[this.value[i]]);
      }
      this.$http.delete(`office/room/${this.roomPk}/`, { data: { pks: initPks } })
        .then(() => this.$http.post(`office/room/${this.roomPk}/`, { choice: 0, pks })
          .then(() => this.$message({
            type: 'success',
            message: '更改成功!',
          })));
    },
  },
  watch: {
    roomPk() {
      this.$http.get(`office/room/${this.roomPk}/`)
        .then((response) => {
          this.exTeachers = response.data.data.user_list.ex_teachers;
          this.nowTeachers = response.data.data.user_list.teachers;
        });
    },
    initValue() {
      this.value = this.initValue;
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
