<template>
  <div style="text-align: center">
    <el-transfer
      style="text-align: left; display: inline-block"
      v-model="value"
      filterable
      filter-placeholder="请输入学生名称"
      :titles="['可增加的学生', '已有的学生']"
      :button-texts="['到左边', '到右边']"
      :format="{
        noChecked: '${total}',
        hasChecked: '${checked}/${total}'
      }"
      :data="students">
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
  name: 'RoomStudents',
  props: {
    roomPk: String,
  },
  data() {
    return {
      exStudents: '',
      nowStudents: '',
      value: [],
    };
  },
  computed: {
    students() {
      const data = [];
      for (let i = 0; i < this.nowStudents.length; i += 1) {
        data.push({
          key: i,
          label: this.nowStudents[i].name,
          disabled: false,
        });
      }
      for (let i = 0; i < this.exStudents.length; i += 1) {
        data.push({
          key: this.nowStudents.length + i,
          label: this.exStudents[i].name,
          disabled: false,
        });
      }
      return data;
    },
    studentPK() {
      return this.nowStudents.concat(this.exStudents).map((student) => (student.pk));
    },
    initValue() {
      const data = [];
      for (let i = 0; i < this.nowStudents.length; i += 1) {
        data.push(i);
      }
      return data;
    },
  },
  methods: {
    replace() {
      this.value = this.initValue;
    },
    getStudents() {
      this.$http.get(`office/room/${this.roomPk}/`)
        .then((response) => {
          this.exStudents = response.data.data.user_list.ex_students;
          this.nowStudents = response.data.data.user_list.students;
        });
    },
    submit() {
      const initPks = [];
      for (let i = 0; i < this.initValue.length; i += 1) {
        initPks.push(this.studentPK[this.initValue[i]]);
      }
      const pks = [];
      for (let i = 0; i < this.value.length; i += 1) {
        pks.push(this.studentPK[this.value[i]]);
      }
      this.$http.delete(`office/room/${this.roomPk}/`, { data: { pks: initPks } })
        .then(() => this.$http.post(`office/room/${this.roomPk}/`, { choice: 2, pks })
          .then(() => this.$message({
            type: 'success',
            message: '更改成功!',
          })));
      this.getStudents();
    },
  },
  watch: {
    roomPk() {
      this.getStudents();
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
