import Vue from 'vue'
import Router from 'vue-router'
import helloPage from '@/components/HelloWorld.vue'
import indexPage from '@/components/indexPage.vue'
import loginPage from '@/components/loginPage.vue'
import registerPage from '@/components/registerPage.vue'
import profilePage from '@/components/profilePage.vue'
import productPage from '@/components/productPage.vue'
import testPage from '@/components/testPage.vue'

// 讓vue可以正常使用Router套件
Vue.use(Router)

/*
新增routes常數列表，包含多個Map
每個Map包含不同的path
格式為：
{
  path:'URL路徑，例如index為/index',
  name:'Path名稱',
  component: 組件名稱，例如index的組件為indexPage.vue，就是引入並且填indexPage
}
*/
const routes = [
    {
        path: "/hello",
        name: "helloPage",
        component: helloPage
    },
    {
        path: "/index",
        name: "indexPpage",
        component: indexPage
    },
    {
        path: "/login",
        name: "loginPpage",
        component: loginPage
    },
    {
        path: "/register",
        name: "registerPpage",
        component: registerPage
    },
    {
        path: "/profile",
        name: "profilePpage",
        component: profilePage
    },
    {
        path: "/product",
        name: "productPpage",
        component: productPage
    },
    {
        path: "/test",
        name: "testPpage",
        component: testPage
    }
]

/*
新增Router物件，
base為基本路徑，
routes則為上面新增的常數路徑列表
*/
var router = new Router({
  routes
})

/*
預設index.js引入會返回router物件
*/
export default router
