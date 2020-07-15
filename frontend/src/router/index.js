import Vue from 'vue';
import VueRouter from 'vue-router';

import Manager from '../views/Manager.vue';

Vue.use(VueRouter);

const routes = [
  {
    // 教务处
    path: '/manager',
    name: 'Manager',
    component: Manager,
  },
];

const router = new VueRouter({
  routes,
});

export default router;
