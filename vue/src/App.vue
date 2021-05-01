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
@import './assets/scss/main.scss';
</style>
