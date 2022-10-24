import Vue from 'vue'
import router from './router'
import  BootstrapVue  from 'bootstrap-vue'
import App from './App.vue'
import "@/assets/css/myStyle.css";
// import "@/assets/css/bootstrap.min.css";
import '../node_modules/jquery/dist/jquery.min.js'

// import "@/assets/css/bootstrap.min.css";
// import '../node_modules/bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(BootstrapVue)

new Vue({
  render: h => h(App),
  router // 新增router到這邊
}).$mount('#app')