<template>
  <PokedexHome />
</template>

<script>
import PokedexHome from './components/PokedexHome.vue'

export default {
  name: 'App',
  components: {
    PokedexHome
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
