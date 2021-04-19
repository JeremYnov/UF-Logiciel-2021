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
  {
    path: '/invoices',
    name: 'Invoices',
    component: () => import('../views/display-all/DisplayAll.vue')
  },
  {
    path: '/invoice/:id',
    name: 'Invoice',
    component: () => import('../views/display-unit/DisplayUnit.vue')
  },
  {
    path: '/add/client',
    name: 'AddClient',
    component: () => import('../views/crud/Add.vue')
  },
  {
    path: '/add/product',
    name: 'AddProduct',
    component: () => import('../views/crud/Add.vue')
  },
  {
    path: '/add/invoice',
    name: 'AddInvoice',
    component: () => import('../views/crud/Add.vue')
  },
  {
    path: '/update/client/:id',
    name: 'UpdateClient',
    component: () => import('../views/crud/Update.vue')
  },
  {
    path: '/update/product/:id',
    name: 'UpdateProduct',
    component: () => import('../views/crud/Update.vue')
  },
  {
    path: '/update/invoice/:id',
    name: 'UpdateInvoice',
    component: () => import('../views/crud/Update.vue')
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
