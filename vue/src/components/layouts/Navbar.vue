<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light" id="nav">
  <!-- <a class="navbar-brand" href="#">Navbar</a> -->
  <router-link class="navbar-brand"  to="/">Navbar</router-link>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
          Manage Settings
        </a>
        <div class="dropdown-menu" aria-labelledby="navbarDropdown">
          <router-link class="dropdown-item" to="/clients">Clients</router-link>
          <router-link class="dropdown-item" to="/products">Products</router-link>
          <router-link class="dropdown-item" to="/invoices">Invoices</router-link>
        </div>
      </li>
    </ul>
  </div>
</nav>
</template>

<script>
export default {

}
</script>

<style>

</style>