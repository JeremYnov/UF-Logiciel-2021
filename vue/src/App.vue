<template>
  <div id="app">
    <Navbar/>
    <router-view :key="$route.fullPath" class="router-view"/>
  </div>
</template>
<script>
import Navbar from './components/layouts/Navbar'
export default {
  components:{
    Navbar,
  }
}
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  .router-view{
    padding: 20px;
  }
}

#nav {

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
