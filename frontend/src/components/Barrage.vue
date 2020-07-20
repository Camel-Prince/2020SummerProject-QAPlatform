<template>
  <div class="barrages-drop">
    <vue-baberrage
      :isShow="barrageIsShow"
      :barrageList="barrageList"
      :maxWordCount="maxWordCount"
      :throttleGap="throttleGap"
      :loop="barrageLoop"
      :boxHeight="boxHeight"
      :messageHeight="messageHeight"
    >
    </vue-baberrage>
  </div>
</template>

<script>
import Vue from 'vue';
import { vueBaberrage, MESSAGE_TYPE } from 'vue-baberrage';

Vue.use(vueBaberrage);
export default {
  name: 'Barrages',
  data() {
    return {
      msg: '前方高能',
      barrageIsShow: true,
      messageHeight: 35,
      boxHeight: 700,
      barrageLoop: false,
      maxWordCount: 3,
      throttleGap: 600,
      barrageList: [],
    };
  },
  mounted() {
    this.addToList();
  },
  methods: {
    addToList() {
      const list = [
        {
          id: 1,
          msg: this.msg,
          time: 6,
        },
      ];
      list.forEach((v) => {
        this.barrageList.push({
          id: v.id,
          msg: v.msg,
          time: v.time,
          type: MESSAGE_TYPE.NORMAL,
        });
      });
    },
  },
};
</script>
<style lang="less" scoped>
.barrages-drop {
  .blue {
    border-radius: 100px;
    background: #e6ff75;
    color: #fff;
  }
  .green {
    border-radius: 100px;
    background: #75ffcd;
    color: #fff;
  }
  .red {
    border-radius: 100px;
    background: #e68fba;
    color: #fff;
  }
  .yellow {
    border-radius: 100px;
    background: #dfc795;
    color: #fff;
  }
  .baberrage-stage {
    position: absolute;
    width: 100%;
    height: 212px;
    overflow: hidden;
    top: 0;
    margin-top: 130px;
  }
}
</style>
