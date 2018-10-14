// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App'
import Title from './components/Title'
import Form from './components/Form'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'

Vue.config.productionTip = false
Vue.use(Vuetify)
Vue.use(VueRouter)

var routes = [
    {path: '/', name: 'Title', component: Title},
    {path: '/form', name: 'Form', component: Form}
  ]

const router = new VueRouter({
  routes,
  mode: 'history'
});

/* eslint-disable no-new */
new Vue({
  el: '#app',
  template: "<App/>",
  components: {App},
  router
}).$mount('#app')
