<template>
  <div class="Whiteboard">
    <whiteborb/>
  </div>
</template>

<script>
import Whiteborb from '@/components/Whiteborb.vue';

export default {
  name: 'Whiteboard',
  components: {
    whiteborb: Whiteborb,
  },
};
</script>
