import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';
import TeacherHomepage from '../views/TeacherHomepage.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/teacher/homepage',
    name: 'TeacherHomepage',
    component: TeacherHomepage,
  },
];

const router = new VueRouter({
  routes,
});

export default router;
