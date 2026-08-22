import {createRouter, createWebHistory} from 'vue-router';

const routes = [
    {
        meta: {
            title: "luffy2.0-站点首页",
            keepAlive: true
        },
        path: '/',         // uri访问地址
        name: "Home",
        component: () => import("../views/Home.vue")
    },
    {
        meta: {
            title: "luffy2.0-用户登录",
            keepAlive: true
        },
        path: '/login',      // uri访问地址
        name: "Login",
        component: () => import("../views/Login.vue")
    }
]

const router = createRouter(
    {
        history: createWebHistory(),
        routes,
    }
);

export default router