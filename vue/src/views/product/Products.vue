<template>
  <section class="products">
    <div v-if="errored" class="error">
      <p>
        Nous sommes désolés, nous ne sommes pas en mesure de récupérer ces
        informations pour le moment. Veuillez réessayer ultérieurement.
      </p>
    </div>
    <div class="container">
      <div v-if="loading" class="loading">Chargement...</div>

      <table class="table">
        <thead class="table-dark">
          <tr>
            <th scope="col">#</th>
            <th scope="col">Name</th>
            <th scope="col">Stock</th>
            <th scope="col">Picture</th>
            <th scope="col">Price</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(product, index) in info" :key="product.id">
            <th scope="row">{{index}}</th>
            <td>{{product.name}}</td>
            <td>{{product.stock}}</td>
            <td>{{product.picture}}</td>
            <td>{{product.price}}</td>
          </tr>
        </tbody>
      </table>
      <div>{{ info }}</div>
    </div>
  </section>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      info: null,
      errored: false,
      loading: true,
      product:{
          name:null,
          stock:null,
          picture:null,
          invoiceReference:null,
      }
    };
  },
  mounted: function () {
    axios
      .get("/api/products")
      .then((response) => {
        this.info = response.data;
      })
      .catch((error) => {
        console.log(error);
        this.errored = true;
      })
      .finally(() => {
        this.loading = false;
      });
  },
};
</script>

<style>

</style>