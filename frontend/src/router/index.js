import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';
import TeacherHomepage from '../views/TeacherHomepage.vue';
<<<<<<< HEAD
import TeacherRecentlive from '../views/TeacherRecentlive.vue';
=======
import  TeacherRecentlive from '../views/TeacherRecentlive.vue';
>>>>>>> header and aside components style Ref #18

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
  {
    path: '/teacher/recent-live',
    name: 'TeacherRecentlive',
    component: TeacherRecentlive,
  },
];

const router = new VueRouter({
  routes,
});

export default router;
