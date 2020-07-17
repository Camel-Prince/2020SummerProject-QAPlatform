import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';
import TeacherHomepage from '../views/TeacherHomepage.vue';
import TeacherRecentlive from '../views/TeacherRecentlive.vue';
import TeacherInformation from '../views/TeacherInformation.vue';
import TeacherLivetime from '../views/TeacherLivetime.vue';
import StudentHomepage from '../views/StudentHomepage.vue';

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
  routes,
});

export default router;
