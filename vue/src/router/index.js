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
    name: 'Add Client',
    component: () => import('../views/crud/Add.vue')
  },
  {
    path: '/add/product',
    name: 'Add Product',
    component: () => import('../views/crud/Add.vue')
  },
  {
    path: '/add/invoice',
    name: 'Add Invoice',
    component: () => import('../views/crud/Add.vue')
  },
  {
    path: '/update/client/:id',
    name: 'Update Client',
    component: () => import('../views/crud/Update.vue')
  },
  {
    path: '/update/product/:id',
    name: 'Update Product',
    component: () => import('../views/crud/Update.vue')
  },
  {
    path: '/update/invoice/:id',
    name: 'Update Invoice',
    component: () => import('../views/crud/Update.vue')
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
