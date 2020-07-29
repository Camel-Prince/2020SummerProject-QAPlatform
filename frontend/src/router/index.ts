import Vue from 'vue';
import VueRouter, { RouteConfig } from 'vue-router';
import Home from '../views/Home.vue';
import Login from '../components/Login.vue';
import Register from '../components/Register.vue';
import TeacherHomepage from '../views/TeacherHomepage.vue';
import TeacherRecentlive from '../views/TeacherRecentlive.vue';
import TeacherInformation from '../views/TeacherInformation.vue';
import StudentHomepage from '../views/StudentHomepage.vue';
import WhiteBoard from '../views/WhiteBoard.vue';
import TeacherLiveRoom from '../views/TeacherLiveRoom.vue';
import StudentLiveRoom from '../views/StudentLiveRoom.vue';
import Manager from '../views/Manager.vue';
import ModifyRoom from '../views/ModifyRoom.vue';

Vue.use(VueRouter);

const routes: RouteConfig[] = [
  { path: '/', redirect: 'login' },
  { path: '/login', component: Login },
  { path: '/register', component: Register },
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    // 教务处
    path: '/manager',
    name: 'Manager',
    component: Manager,
  }, {
    // 修改房间信息界面
    path: '/manager/modifyRoom',
    name: 'ModifyRoom',
    component: ModifyRoom,
  },
  {
    path: '/:room',
    name: 'WhiteBoard',
    component: WhiteBoard,
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
    path: '/student/homepage',
    name: 'StudentHomepage',
    component: StudentHomepage,
  },
  {
    path: '/teacher/room/:room',
    name: 'TeacherLiveRoom',
    component: TeacherLiveRoom,
  },
  {
    path: '/student/room/:room',
    name: 'StudentLiveRoom',
    component: StudentLiveRoom,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
