<template>
  <div id="app">
    <Navbar class="navbar" />
    <div class="content">
      <router-view />
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import Navbar from "@/components/pages/Navbar.vue";

@Component({
  components: {
    Navbar
  }
})
export default class App extends Vue {}
</script>

<style lang="scss">
@import './scss/app.scss';

#app {
  height: 100vh;
  font-family: Avenir, Helvetice, Arial, sans-serif;
  color: #FFFFFF;
  display: grid;
  grid-template-areas:
    "navbar navbar navbar"
    "content content content"
    "content content content";
  grid-template-columns: 250px 1fr;
  grid-template-rows: 65px 1fr;
}
.navbar {
  grid-area: navbar;
}
.content {
  grid-area: content;
  padding: 15px 30px;
}
</style>
