import Vue from 'vue'
import VueRouter, { RouteConfig } from 'vue-router'

Vue.use(VueRouter)

const routes: Array<RouteConfig> = [
  {
    path: '/',
    name: 'mainPage',
    component: () => import('../components/main-page/index.vue'),
  },
  {
    path: '/generateTask',
    name: 'generateTask',
    component: () => import('../components/generate-task/index.vue'),
  },
  {
    path: '/generateVariant',
    name: 'generateVariant',
    component: () => import('../components/generate-variant/index.vue'),
  },
  {
    path: '/newTask',
    name: 'newTask',
    component: () => import('../components/new-task/index.vue'),
  },
  {
    path: '/statistics',
    name: 'statistics',
    component: () => import('../components/statistics/index.vue'),
  },
  {
    path: '/topic',
    name: 'topic',
    component: () => import('../components/topic/index.vue'),
  },
  {
    path: '/*',
    name: 'not-found',
    component: () => import('../components/not-found/index.vue'),
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
})

export default router
