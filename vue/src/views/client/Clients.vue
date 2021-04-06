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
            <th scope="col">#</th>
            <th scope="col">Firstname</th>
            <th scope="col">Lastname</th>
            <th scope="col">Mail</th>
            <th scope="col">Creation date</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="client in info" :key="client.id">
            <th scope="row">{{ client.id }}</th>
            <td>{{ client.firstName }}</td>
            <td>{{ client.lastName }}</td>
            <td>{{ client.email }}</td>
            <td>{{ client.creation }}</td>
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
      client: {
        name: null,
        surname: null,
        mail: null,
        creationDate: null,
      },
    };
  },
  mounted: function () {
    axios
      .get("/api/clients")
      .then((response) => {
        this.info = response.data.results;
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