import axios from 'axios';
import Vue from 'vue';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import App from './App.vue';
import router from './router';

axios.defaults.withCredentials = true;
axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN';
axios.defaults.xsrfCookieName = 'csrftoken';

Vue.config.productionTip = false;
Vue.use(ElementUI);
Vue.prototype.$http = axios;

Vue.prototype.$http = axios.create({
  baseURL: 'http://0.0.0.0:8000/',
  timeout: 3000,
});

new Vue({
  router,
  render: (h) => h(App),
}).$mount('#app');
