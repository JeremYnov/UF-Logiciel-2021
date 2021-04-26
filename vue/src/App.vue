<template>
  <!-- <div id="app">
    <Navbar/>
    <router-view :key="$route.fullPath" class="router-view"/>
  </div> -->
  <div id="app">
    <div class="navigation">
      <ul>
        <li>
          <router-link class="dropdown-item" to="/">
            <span class="icon"
              ><i class="fas fa-home" aria-hidden="true"></i
            ></span>
            <span class="title">Home</span></router-link
          >
        </li>
        <li>
          <router-link class="dropdown-item" to="/clients">
            <span class="icon"><i class="fas fa-users"></i></span>
            <span class="title">Clients</span>
          </router-link>
        </li>
        <li>
          <router-link class="dropdown-item" to="/products">
            <span class="icon"><i class="fas fa-apple-alt"></i></span>
            <span class="title">Produits</span></router-link
          >
        </li>
        <li>
          <router-link class="dropdown-item" to="/invoices">
            <span class="icon"><i class="fas fa-file-invoice-dollar"></i></span>
            <span class="title">Factures</span>
          </router-link>
        </li>
      </ul>
    </div>
    <div class="content">
      <router-view :key="$route.fullPath" class="router-view" />
    </div>
  </div>
</template>
<script>
// import Navbar from './components/layouts/Navbar'
export default {
  components: {
    // Navbar,
  },
};
</script>

<style lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;500;700&display=swap');
#app {
  font-family: 'Quicksand', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

// #nav {

//   a {
//     font-weight: bold;
//     color: #2c3e50;

//     &.router-link-exact-active {
//       color: #42b983;
//     }
//   }
// }

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.content {
  margin-left: 60px;
  transition: 0.5s;
}

.navigation {
  position: fixed;
  width: 60px;
  height: 100%;
  background: #2c3e50;
  transition: 0.5s;
  overflow: hidden;
  &:hover {
    transition: 0.5s;
    width: 250px;
  }
  &:hover ~ .content {
    transition: 0.5s;
    margin-left: 250px;
  }
  ul {
    position: absolute;
    top: 60px;
    left: 0;
    width: 100%;
    li {
      position: relative;
      width: 100%;
      list-style: none;
      &:hover {
        background: #395168;
      }
      a {
        position: relative;
        display: block;
        width: 100%;
        display: flex;
        text-decoration: none;
        color: #fff;
        .icon {
          position: relative;
          display: block;
          min-width: 60px;
          height: 60px;
          line-height: 60px;
          text-align: center;
        }
        .title {
          position: relative;
          display: block;
          padding: 0 10px;
          height: 60px;
          line-height: 60px;
          text-align: start;
          white-space: nowrap;
        }
      }
    }
  }

  
}
</style>
