<template>
  <div style="text-align: center">
    <el-transfer
      style="text-align: left; display: inline-block"
      v-model="value"
      filterable
      filter-placeholder="请输入学生名称"
      :left-default-checked="[2, 3]"
      :right-default-checked="[1]"
      :titles="['可增加的学生', '已有的学生']"
      :button-texts="['到左边', '到右边']"
      :format="{
        noChecked: '${total}',
        hasChecked: '${checked}/${total}'
      }"
      :data="students">
      <!-- <span slot-scope="{ option }">{{ option.key }} - {{ option.label }}</span>  自定义列表项样式-->
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
    room_pk: null,
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
      const data = [];
      for (let i = 0; i < this.nowStudents.length; i += 1) {
        data.push(this.nowStudents[i].pk);
      }
      for (let i = 0; i < this.exStudents.length; i += 1) {
        data.push(this.exStudents[i].pk);
      }
      return data;
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
    submit() {
      const initPks = [];
      for (let i = 0; i < this.initValue.length; i += 1) {
        initPks.push(this.studentPK[this.initValue[i]]);
      }
      const pks = [];
      for (let i = 0; i < this.value.length; i += 1) {
        pks.push(this.studentPK[this.value[i]]);
      }
      this.$http.delete(`office/room/${this.room_pk}/`, { data: { pks: initPks } })
        .then(() => this.$http.post(`office/room/${this.room_pk}/`, { choice: 2, pks })
          .then(() => this.$message({
            type: 'success',
            message: '更改成功!',
          })));
    },
  },
  watch: {
    room_pk() {
      this.$http.get(`office/room/${this.room_pk}/`)
        .then((response) => {
          this.exStudents = response.data.data.user_list.ex_students;
          this.nowStudents = response.data.data.user_list.students;
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
