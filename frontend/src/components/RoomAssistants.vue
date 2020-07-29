<template>
  <div style="text-align: center">
    <el-transfer
      style="text-align: left; display: inline-block"
      v-model="value"
      filterable
      filter-placeholder="请输入助教名称"
      :titles="['可增加的助教', '已有的助教']"
      :button-texts="['到左边', '到右边']"
      :format="{
        noChecked: '${total}',
        hasChecked: '${checked}/${total}'
      }"
      :data="assistants">
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
  name: 'RoomAssistants',
  props: {
    roomPk: String,
  },
  data() {
    return {
      exAssistants: '',
      nowAssistants: '',
      value: [],
    };
  },
  computed: {
    assistants() {
      const data = [];
      for (let i = 0; i < this.nowAssistants.length; i += 1) {
        data.push({
          key: i,
          label: this.nowAssistants[i].name,
          disabled: false,
        });
      }
      for (let i = 0; i < this.exAssistants.length; i += 1) {
        data.push({
          key: this.nowAssistants.length + i,
          label: this.exAssistants[i].name,
          disabled: false,
        });
      }
      return data;
    },
    assistantsPK() {
      return this.nowAssistants.concat(this.exAssistants).map((assistant) => (assistant.pk));
    },
    initValue() {
      const data = [];
      for (let i = 0; i < this.nowAssistants.length; i += 1) {
        data.push(i);
      }
      return data;
    },
  },
  methods: {
    replace() {
      this.value = this.initValue;
    },
    getAssistants() {
      this.$http.get(`office/room/${this.roomPk}/`)
        .then((response) => {
          this.exAssistants = response.data.data.user_list.ex_assistants;
          this.nowAssistants = response.data.data.user_list.assistants;
        });
    },
    submit() {
      const initPks = [];
      for (let i = 0; i < this.initValue.length; i += 1) {
        initPks.push(this.assistantsPK[this.initValue[i]]);
      }
      const pks = [];
      for (let i = 0; i < this.value.length; i += 1) {
        pks.push(this.assistantsPK[this.value[i]]);
      }
      this.$http.delete(`office/room/${this.roomPk}/`, { data: { pks: initPks } })
        .then(() => this.$http.post(`office/room/${this.roomPk}/`, { choice: 1, pks })
          .then(() => this.$message({
            type: 'success',
            message: '更改成功!',
          })));
      this.getAssistants();
    },
  },
  watch: {
    roomPk() {
      this.getAssistants();
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
