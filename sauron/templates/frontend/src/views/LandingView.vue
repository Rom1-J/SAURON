<script lang="ts" setup>
import { useUserStore } from '@/stores';

const userStore = useUserStore();

function smoothScroll(id: string) {
  document.querySelector(id)?.scrollIntoView({
    behavior: 'smooth',
  });
}
</script>

<template>
  <div class="overflow-hidden surface-0">
    <div
      class="py-4 px-4 mx-0 md:mx-6 lg:mx-8 lg:px-8 flex
    align-items-center justify-content-between relative lg:static">
      <router-link to="/" class="flex align-items-center">
        <!--suppress CheckImageSize -->
        <img
          src="@/layout/images/logo.svg"
          alt="SAURON"
          height="42"
          class="mr-0 lg:mr-2">
      </router-link>
      <a
        class="cursor-pointer block lg:hidden text-500 p-ripple"
        v-ripple
        v-styleclass="{
          selector: '@next',
          enterClass: 'hidden',
          leaveToClass: 'hidden',
          hideOnOutsideClick: true,
        }">
        <i class="pi pi-bars text-4xl" />
      </a>
      <div
        class="surface-0 align-items-center flex-grow-1 justify-content-between
           hidden lg:flex absolute lg:static w-full left-0 px-6 lg:px-0 z-2"
        style="top:92%">
        <ul
          class="list-none p-0 m-0 flex lg:align-items-center select-none
         flex-column lg:flex-row cursor-pointer">
          <li>
            <a
              @click="smoothScroll('#hero')"
              v-ripple
              class="flex m-0 md:ml-5 px-0 py-3 text-900 font-medium
               line-height-3 p-ripple text-500">
              <span>{{ $t('misc.home') }}</span>
            </a>
          </li>
          <li>
            <a
              @click="smoothScroll('#features')"
              v-ripple
              class="flex m-0 md:ml-5 px-0 py-3 text-900 font-medium
               line-height-3 p-ripple text-500">
              <span>{{ $t('misc.features.title') }}</span>
            </a>
          </li>
        </ul>
        <div
          class="flex justify-content-between lg:block border-top-1
        lg:border-top-none surface-border py-3 lg:py-0 mt-3 lg:mt-0">
          <template v-if="!userStore.isAuthenticated">
            <router-link
              :to="{ name: 'login' }"
              custom
              v-slot="{ navigate }">
              <Button
                :label="$t('login.sign_in')"
                @click="navigate"
                class="p-button-text p-button-rounded border-none
                    font-light line-height-2 text-primary" />
            </router-link>
            <router-link
              :to="{ name: 'register' }"
              custom
              v-slot="{ navigate }">
              <Button
                :label="$t('register.sign_up')"
                @click="navigate"
                class="p-button-rounded border-none ml-5 font-light
                    text-black line-height-2 bg-primary" />
            </router-link>
          </template>
          <template v-else>
            <router-link
              :to="{ name: 'dashboard' }"
              custom
              v-slot="{ navigate }">
              <Button
                :label="$t('misc.dashboard')"
                @click="navigate"
                icon="pi pi-home"
                class="p-button-rounded border-none ml-5 font-light
                    text-black line-height-2 bg-primary" />
            </router-link>
          </template>
        </div>
      </div>
    </div>

    <div class="grid py-4 px-4 lg:px-8 relative" id="hero">
      <div class="mx-4 mb-4 md:mx-8 mt-0 md:mt-4 z-1">
        <h1 class="text-6xl font-bold text-gray-900 line-height-2">
          <span class="font-light block">{{ $t('misc.app.title') }}</span>
          {{ $t('misc.app.acronym') }}
        </h1>
        <p class="font-normal text-2xl line-height-3 md:mt-3 text-gray-700">
          {{ $t('misc.app.description') }}
        </p>
        <router-link
          :to="{ name: 'register' }"
          custom
          v-slot="{ navigate }"
          v-if="!userStore.isAuthenticated">
          <Button
            :label="$t('misc.get_started')"
            @click="navigate"
            icon="pi pi-angle-double-right"
            iconPos="right"
            class="p-button-rounded text-xl border-none mt-5
                  bg-primary font-normal text-black line-height-3 px-3" />
        </router-link>
        <router-link
          :to="{ name: 'dashboard' }"
          custom
          v-slot="{ navigate }"
          v-else>
          <Button
            :label="$t('misc.dashboard')"
            @click="navigate"
            class="p-button-rounded text-xl border-none mt-5
                  bg-primary font-normal text-black line-height-3 px-3" />
        </router-link>
      </div>
    </div>

    <div class="py-4 px-4 lg:px-8 mt-5 mx-0 lg:mx-8" id="features">
      <div class="grid justify-content-center">
        <div class="col-12 text-center mt-8 mb-4">
          <h2 class="text-900 font-normal mb-2">{{ $t('misc.features.title') }}</h2>
          <span class="text-600 text-2xl">{{ $t('misc.features.description') }}</span>
        </div>

        <div
          class="col-12 md:col-12 lg:col-4 p-0 lg:pr-5 lg:pb-5 mt-4 lg:mt-0">
          <div style="border-radius:10px;" class="border-1 border-yellow-200">
            <div class="p-3 surface-card h-full" style="border-radius:8px;">
              <div
                class="flex align-items-center justify-content-center bg-yellow-200 mb-3"
                style="width:3.5rem;height:3.5rem; border-radius:10px;">
                <i class="pi pi-fw pi-users text-2xl text-yellow-700" />
              </div>
              <h5 class="mb-2 text-900">{{ $t('misc.features.easy.title') }}</h5>
              <span class="text-600">
                {{ $t('misc.features.easy.description') }}
              </span>
            </div>
          </div>
        </div>

        <div
          class="col-12 md:col-12 lg:col-4 p-0 lg:pr-5 lg:pb-5 mt-4 lg:mt-0">
          <div style="border-radius:10px;" class="border-1 border-orange-200">
            <div class="p-3 surface-card h-full" style="border-radius:8px;">
              <div
                class="flex align-items-center justify-content-center bg-orange-200 mb-3"
                style="width:3.5rem;height:3.5rem; border-radius:10px;">
                <i class="pi pi-fw pi-code text-2xl text-orange-700" />
              </div>
              <h5 class="mb-2 text-900">{{ $t('misc.features.open.title') }}</h5>
              <span class="text-600">
                {{ $t('misc.features.open.description') }}
              </span>
            </div>
          </div>
        </div>

        <div class="col-12 md:col-12 lg:col-4 p-0 lg:pb-5 mt-4 lg:mt-0">
          <div style="border-radius:10px;" class="border-1 border-pink-200">
            <div class="p-3 surface-card h-full" style="border-radius:8px;">
              <div
                class="flex align-items-center justify-content-center bg-pink-200 mb-3"
                style="width:3.5rem;height:3.5rem; border-radius:10px;">
                <i class="pi pi-fw pi-database text-2xl text-pink-700" />
              </div>
              <h5 class="mb-2 text-900">{{ $t('misc.features.large.title') }}</h5>
              <span class="text-600">
                {{ $t('misc.features.large.description') }}
              </span>
            </div>
          </div>
        </div>

        <div class="col-12 md:col-12 lg:col-4 p-0 lg:pr-5 mt-4 lg:mt-0">
          <div style="border-radius:10px;" class="border-1 border-blue-200">
            <div class="p-3 surface-card h-full" style="border-radius:8px;">
              <div
                class="flex align-items-center justify-content-center bg-blue-200 mb-3"
                style="width:3.5rem;height:3.5rem; border-radius:10px;">
                <i class="pi pi-fw pi-globe text-2xl text-blue-700" />
              </div>
              <h5 class="mb-2 text-900">{{ $t('misc.features.adaptability.title') }}</h5>
              <span class="text-600">
                {{ $t('misc.features.adaptability.description') }}
              </span>
            </div>
          </div>
        </div>

        <div class="col-12 md:col-12 lg:col-4 p-0 lg-4 mt-4 lg:mt-0">
          <div style="border-radius:10px;" class="border-1 border-purple-200">
            <div class="p-3 surface-card h-full" style="border-radius:8px;">
              <div
                class="flex align-items-center justify-content-center bg-purple-200 mb-3"
                style="width:3.5rem;height:3.5rem; border-radius:10px;">
                <i class="pi pi-fw pi-eye text-2xl text-purple-700" />
              </div>
              <h5 class="mb-2 text-900">{{ $t('misc.features.privacy.title') }}</h5>
              <span class="text-600">
                {{ $t('misc.features.privacy.description') }}
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div
      class="py-4 px-4 mx-0 mt-8 lg:mx-8 border-gray-200 border-top-1"
      id="contact">
      <div class="grid justify-content-between">
        <div class="col-12 md:col-2">
          <div
            class="flex flex-wrap align-items-center
              justify-content-center md:justify-content-start md:mb-0 mb-3">
            <img
              src="@/layout/images/logo-text.svg"
              alt="SAURON"
              height="128"
              class="mr-2">
          </div>
        </div>

        <div class="col-12 md:col-7">
          <div class="grid text-center md:text-right">
            <div class="col-12 md:col-6">
              <h4 class="font-medium text-2xl line-height-3 mb-3 text-black">
                {{ $t('misc.resources') }}
              </h4>
              <a
                href="https://github.com/Rom1-J/SAURON"
                class="line-height-3 text-xl block cursor-pointer mb-2 text-500 hover:underline">
                GitHub
              </a>
            </div>

            <div class="col-12 md:col-6 mt-4 md:mt-0">
              <h4 class="font-medium text-2xl line-height-3 mb-3 text-black">
                {{ $t('misc.legal_notices.title') }}
              </h4>
              <a class="line-height-3 text-xl block cursor-pointer mb-2 text-500 hover:underline">
                {{ $t('misc.legal_notices.tos') }}
              </a>
              <a class="line-height-3 text-xl block cursor-pointer mb-2 text-500 hover:underline">
                {{ $t('misc.legal_notices.cookies') }}
              </a>
              <a class="line-height-3 text-xl block cursor-pointer mb-2 text-500 hover:underline">
                {{ $t('misc.legal_notices.personal') }}
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss">
#hero {
  background: linear-gradient(0deg, rgba(255, 255, 255, .2), rgba(255, 255, 255, .2)),
  radial-gradient(80% 256% at 80% 60%, #b3f7bb 0%, #a4bfff 100%);
  height: 700px;
  overflow: hidden;
}

@media screen and (min-width: 768px) {
  #hero {
    clip-path: ellipse(150% 87% at 93% 13%);
    height: 530px;
  }
}

@media screen and (min-width: 1300px) {
  #hero > img {
    position: absolute;
  }

  #hero > div > p {
    max-width: 450px;
  }
}

@media screen and (max-width: 1300px) {
  #hero {
    height: 600px;
  }

  #hero > img {
    position: static;
    transform: scale(1);
    margin-left: auto;
  }

  #hero > div {
    width: 100%;
  }

  #hero > div > p {
    width: 100%;
    max-width: 100%;
  }
}
</style>
