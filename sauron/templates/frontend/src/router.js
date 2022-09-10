import { createRouter, createWebHashHistory } from 'vue-router';
import store from './store';

const routes = [
  {
    path: '/',
    name: 'landing',
    component: () => import('./pages/Landing.vue'),
  },
  {
    path: '/dashboard',
    name: 'home',
    component: () => import('./pages/dashboard/Dashboard.vue'),
    children: [
      {
        path: '/dashboard',
        name: 'dashboard',
        component: () => import('./pages/dashboard/categories/Home.vue'),
        meta: {
          requires_auth: true,
        },
      },
      {
        path: '/dashboard/profile',
        name: 'profile',
        component: () => import('./pages/dashboard/categories/Profile.vue'),
        meta: {
          requires_auth: true,
        },
      },
    ],
    meta: {
      requires_auth: true,
    },
  },
  {
    path: '/register',
    name: 'register',
    component: () => import('./pages/Register.vue'),
    meta: {
      requires_guest: true,
    },
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('./pages/Login.vue'),
    meta: {
      requires_guest: true,
    },
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'notFound',
    component: () => import('./pages/NotFound.vue'),
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  if (to.matched.some((record) => record.meta.requires_auth)) {
    if (!store.getters.isAuthenticated) {
      return next({ name: 'login' });
    }
  } else if (to.matched.some((record) => record.meta.requires_guest)) {
    if (store.getters.isAuthenticated) {
      return next({ name: 'dashboard' });
    }
  }

  return next();
});

export default router;
