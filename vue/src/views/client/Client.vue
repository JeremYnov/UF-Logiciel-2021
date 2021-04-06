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
            <th scope="col">#</th>
            <th scope="col">Firstname</th>
            <th scope="col">Lastname</th>
            <th scope="col">Mail</th>
            <th scope="col">Creation date</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>{{ info.id }}</td>
            <td>{{ info.firstName }}</td>
            <td>{{ info.lastName }}</td>
            <td>{{ info.email }}</td>
            <td>{{ info.creation }}</td>
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
    this.id = axios
      .get("/api/client/" + this.id)
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