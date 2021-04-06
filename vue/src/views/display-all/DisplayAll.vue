<template>
  <section class="clients">
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
            <th v-for="key in keys" :key="key" scope="col">{{ key }}</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="info in infos" :key="info.id">
            <td v-for="(value, key) in info" :key="key">{{ value }}</td>
          </tr>
        </tbody>
      </table>
      <div>{{ infos }}</div>
    </div>
  </section>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      // id: this.$route.params.id,
      infos: null,
      keys: null,
      errored: false,
      loading: true,
    };
  },
  mounted: function () {
    axios
      .get(`/api${this.$route.path}`)
      .then((response) => {
        console.log(this.$route)
        this.infos = response.data.results;
        this.keys = Object.keys(Object.assign({}, ...this.infos));
        console.log(this.keys);
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