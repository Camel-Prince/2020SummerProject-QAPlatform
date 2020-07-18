import Vue from 'vue';
import VueRouter, { RouteConfig } from 'vue-router';
// import axios from 'axios';
import Home from '../views/Home.vue';
// import Login from '../components/Login.vue';
// import Register from '../components/Register.vue';
import Student from '../components/Student.vue';
import Teacher from '../components/Teacher.vue';
import Office from '../components/Office.vue';
import TeacherHomepage from '../views/TeacherHomepage.vue';
import TeacherRecentlive from '../views/TeacherRecentlive.vue';
import TeacherInformation from '../views/TeacherInformation.vue';
import TeacherLivetime from '../views/TeacherLivetime.vue';
import StudentHomepage from '../views/StudentHomepage.vue';
import Whiteboard from '../views/Whiteboard.vue';

import Manager from '../views/Manager.vue';
import ModifyRoom from '../views/ModifyRoom.vue';

Vue.use(VueRouter);

const routes: RouteConfig[] = [
  // { path: '/', redirect: 'login' },
  // { path: '/login', component: Login },
  // { path: '/register', component: Register },
  { path: '/student', component: Student },
  { path: '/teacher', component: Teacher },
  { path: '/office', component: Office },
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/:room',
    name: 'Whiteboard',
    component: Whiteboard,
  },
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
  {
    path: '/teacher/information',
    name: 'TeacherInformation',
    component: TeacherInformation,
  },
  {
    path: '/teacher/live-time',
    name: 'TeacherLivetime',
    component: TeacherLivetime,
  },
  {
    path: '/student/homepage',
    name: 'StudentHomepage',
    component: StudentHomepage,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

// router.beforeEach((to, from, next) => {
//   if (to.path === '/login' || to.path === '/register') return next();
//   const token = window.sessionStorage.getItem('token');
//   if (!token) {
//     return next('/login');
//   }
//   axios({
//     method: 'get',
//     url: 'http://localhost:8000/QAplatform/detail/',
//     headers: {
//       Authorization: `jwt ${window.sessionStorage.getItem('token')}`,
//     },
//   }).then((response) => {
//     console.log(response.data.occupation);
//   });
//   return next();
// });

export default router;
