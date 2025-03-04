import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '@/store/index';
import HomeView from '../views/HomeView.vue'
import BookDetails from "@/components/library/BookDetails.vue";

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/library',
    name: 'library',
    component: () => import('../views/Library.vue'),
    beforeEnter: (to, from, next) => {
      if (store.state.user.loginFlag === false) {
        next('/login');
      } else {
        next();
      }
    },
    beforeRouteLeave: (to, from, next) => {
      if (store.state.user.loginFlag === false) {
        next('/login');
      } else {
        next();
      }
    },
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('../views/login.vue')
  },
  {
    path: '/signup',
    name: 'signup',
    component: () => import('../views/SignUp.vue')
  },
  {
    path: '/addbook',
    name: 'AddBook',
    component: () => import('../views/AddBook.vue'),
    beforeEnter: (to, from, next) => {
      if (store.state.user.loginFlag === false) {
        next('/login');
      } else {
        next();
      }
    },
    beforeRouteLeave: (to, from, next) => {
      if (store.state.user.loginFlag === false) {
        next('/login');
      } else {
        next();
      }
    },
  },
  {
    path: "/book/:id",
    name: "BookDetails",
    component: BookDetails,
    beforeEnter: (to, from, next) => {
      if (store.state.user.loginFlag === false) {
        next('/login');
      } else {
        next();
      }
    },
    beforeRouteLeave: (to, from, next) => {
      if (store.state.user.loginFlag === false) {
        next('/login');
      } else {
        next();
      }
    },
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
