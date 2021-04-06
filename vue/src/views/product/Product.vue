<template>
  <section class="product">
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
          <tr>
            <td>{{ info.id }}</td>
            <td>{{ info.name }}</td>
            <td>{{ info.stock }}</td>
            <td>{{ info.picture }}</td>
            <td>{{ info.price }}</td>
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
      id: this.$route.params.id,
      info: null,
      errored: false,
      loading: true,
      product: {
        name: null,
        stock: null,
        picture: null,
        invoiceReference: null,
      },
    };
  },
  mounted: function () {
    this.id = axios
      .get("/api/product/" + this.id)
      .then((response) => {
        this.info = response.data.result;
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