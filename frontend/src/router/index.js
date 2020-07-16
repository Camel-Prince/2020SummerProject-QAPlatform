import Vue from 'vue';
import VueRouter from 'vue-router';

import Manager from '../views/Manager.vue';
import ModifyRoom from '../views/ModifyRoom.vue';

Vue.use(VueRouter);

const routes = [
  {
    // 教务处
    path: '/manager',
    name: 'Manager',
    component: Manager,
  }, {
    // 修改房间信息界面
    path: '/modifyRoom',
    name: 'ModifyRoom',
    component: ModifyRoom,
  },
];

const router = new VueRouter({
  routes,
});

export default router;
