import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/clients',
    name: 'Clients',
    component: () => import('../views/display-all/DisplayAll.vue')
  },
  {
    path: '/client/:id',
    name: 'Client',
    component: () => import('../views/display-unit/DisplayUnit.vue')
  },
  {
    path: '/products',
    name: 'Products',
    component: () => import('../views/display-all/DisplayAll.vue')
  },
  {
    path: '/product/:id',
    name: 'Product',
    component: () => import('../views/display-unit/DisplayUnit.vue')
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
