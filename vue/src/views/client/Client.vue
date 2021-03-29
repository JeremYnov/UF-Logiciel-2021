<template>
  <section class="clients">
    <div v-if="errored" class="error">
      <p>
        Nous sommes désolés, nous ne sommes pas en mesure de récupérer ces
        informations pour le moment. Veuillez réessayer ultérieurement.
      </p>
    </div>
    <div v-else>
      <div v-if="loading" class="loading">Chargement...</div>
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
    };
  },
  mounted: function () {
    axios
      .get("")
      .then((response) => (this.info = response))
      .catch((error) => {
        console.log(error);
        this.errored = true;
      })
      .finally(() => (this.loading = false));
  },
};
</script>

<style>
</style>