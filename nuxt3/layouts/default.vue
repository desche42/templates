<template>
    <v-app>
      <v-navigation-drawer temporary v-model="showDrawer" location="left">
        <div class="w-100 text-right">
          <v-btn flat icon="$close" size="x-large" @click="toggleDrawer()" />
        </div>
        <p class="text-center"><b>I'm the drawer</b></p>
      </v-navigation-drawer>
  
      <v-app-bar>
        <v-app-bar-nav-icon @click="toggleDrawer()" />
        <v-toolbar-title>I'm the header</v-toolbar-title>
      </v-app-bar>
      
      <!-- 
        MAIN CONTENT OF THE LAYOUT: PAGES
       -->
      <v-main class="d-flex align-center">
        <nuxt-page></nuxt-page>
      </v-main>
  
      <v-footer app elevation="5">
        <v-row justify="center" no-gutters class="text-overline font-weight-black">
          <p class="my-auto">I'm the footer</p>
          <v-spacer />
          <v-btn icon variant="plain">
            <v-icon icon="$info" color="green-accent-4" />
          </v-btn>
        </v-row>
      </v-footer>
    </v-app>
</template>

<script setup>
    const showDrawer = ref(false);
    const toggleDrawer = () => {
        showDrawer.value = !showDrawer.value;
    };

  /* Redundant unused code just for test purposes later on. */
  const unusedFunction = () => console.log('unusedFunction()');
</script>

<style>
  /* Redundant unused code just for test purposes later on. */
  .unused-selector {
    color: orange;
  }
</style>
