import { createRouter, createWebHashHistory } from 'vue-router';
import { useTagStore, useUserStore } from '@/stores';

const routes = [
  {
    path: '/',
    name: 'landing',
    component: () => import('./views/LandingView.vue'),
  },
  {
    path: '/dashboard',
    name: 'home',
    component: () => import('./views/dashboard/DashboardView.vue'),
    children: [
      {
        path: '/dashboard',
        name: 'dashboard',
        component: () => import('./views/dashboard/categories/Home.vue'),
        meta: {
          requires_auth: true,
        },
      },
      {
        path: '/dashboard/profile',
        name: 'profile',
        component: () => import('./views/dashboard/categories/Profile.vue'),
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
    component: () => import('./views/RegisterView.vue'),
    meta: {
      requires_guest: true,
    },
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('./views/LoginView.vue'),
    meta: {
      requires_guest: true,
    },
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'notFound',
    component: () => import('./views/NotFoundView.vue'),
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

router.beforeEach(async (to, from, next) => {
  const user = useUserStore();
  const tags = useTagStore();

  if (to.matched.some((record) => record.meta.requires_auth)) {
    try {
      await user.GetUser();
    } catch (AxiosError) {
      user.$reset();
    }

    if (!user.isAuthenticated) {
      return next({ name: 'login' });
    }

    await tags.GetTags();
  } else if (to.matched.some((record) => record.meta.requires_guest)) {
    if (user.isAuthenticated) {
      return next({ name: 'dashboard' });
    }
  }

  return next();
});

export default router;
