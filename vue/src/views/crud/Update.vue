<template>
  <section class="add">
    <div v-if="errored" class="error">
      <p>
        Nous sommes désolés, nous ne sommes pas en mesure de récupérer ces
        informations pour le moment. Veuillez réessayer ultérieurement.
      </p>
    </div>
    <div v-if="loading" class="loading">Chargement...</div>
    <form :action="path" method="POST" enctype='multipart/form-data'>
      <div v-for="info in infos.form" :key="info">
        <label :for="info.name">{{ info.label }}</label>
        <input v-if='info.step' :type="info.type"
          :placeholder="info.placeholder"
          :name="info.name"
          :step='info.step'
          :value='info.value'
          required>
        <input v-else
          :type="info.type"
          :placeholder="info.placeholder"
          :name="info.name"
          :value='info.value'
          required
        />
        
      </div>
      <button type="submit">Valider</button>
    </form>
    {{ infos }}
  </section>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      errored: false,
      loading: true,
      infos: null,
      path:null,
    };
  },
  mounted: function () {
    axios
      .get(`/api${this.$route.path.slice(7)}`)
      .then((response) => {
        this.infos = response.data;
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