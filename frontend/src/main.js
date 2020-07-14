import axios from 'axios';
import Vue from 'vue';
import ace from 'ace-builds';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';

import App from './App.vue';
import router from './router';

Vue.use(ace);
Vue.use(ElementUI);

axios.defaults.withCredentials = true;
axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN';
axios.defaults.xsrfCookieName = 'csrftoken';

Vue.config.productionTip = false;

Vue.prototype.$http = axios;

new Vue({
  router,
  render: (h) => h(App),
}).$mount('#app');
