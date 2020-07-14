import Vue from 'vue';
import VueRouter from 'vue-router';
import axios from 'axios';
import Login from '../components/Login.vue';
import Register from '../components/Register.vue';
import Student from '../components/Student.vue';
import Teacher from '../components/Teacher.vue';
import Office from '../components/Office.vue';

Vue.use(VueRouter);

const router = new VueRouter({
  routes: [
    { path: '/', redirect: 'login' },
    { path: '/login', component: Login },
    { path: '/register', component: Register },
    { path: '/student', component: Student },
    { path: '/teacher', component: Teacher },
    { path: '/office', component: Office },
  ],
});

router.beforeEach((to, from, next) => {
  if (to.path === '/login' || to.path === '/register') return next();
  const token = window.sessionStorage.getItem('token');
  if (!token) {
    return next('/login');
  }
  axios({
    method: 'get',
    url: 'http://localhost:8000/QAplatform/detail/',
    headers: {
      Authorization: `jwt ${window.sessionStorage.getItem('token')}`,
    },
  }).then((response) => {
    console.log(response.data.occupation);
  });
  return next();
});
export default router;
