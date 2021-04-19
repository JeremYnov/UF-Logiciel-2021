<template>
  <section class="client">
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
            <th v-for="(value, key) in info" :key="key">{{ key }}</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td v-for="(value, key) in info" :key="key">
              <img
                v-if="key == 'image'"
                :src="value.url"
                :alt="value.name"
                style="height: 50px; width: 50px"
              />
              <p v-else>{{ value }}</p>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      keys: null,
      info: null,
      errored: false,
      loading: true,
    };
  },
  mounted: function () {
    axios
      .get(`/api${this.$route.path}`)
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