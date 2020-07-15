import Vue from 'vue';
import axios from 'axios';
import ElementUI from 'element-ui';
import App from './App.vue';
import router from './router';
import 'element-ui/lib/theme-chalk/index.css';

axios.defaults.withCredentials = true;
axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN';
axios.defaults.xsrfCookieName = 'csrftoken';

Vue.use(ElementUI);
Vue.config.productionTip = false;
Vue.prototype.$http = axios.create({
  baseURL: 'http://localhost:8000/QAplatform/',
  timeout: 5000,
});

new Vue({
  router,
  render: (h) => h(App),
}).$mount('#app');
