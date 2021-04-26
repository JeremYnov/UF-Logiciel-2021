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
      <div v-for="info in infos" :key="info">
        <Input v-if="info.step"
          :type="info.type"
          :placeholder="info.placeholder"
          :name="info.name"
          :step="info.step"
          :label="info.label"
        />
        <Input v-else
          :type="info.type"
          :placeholder="info.placeholder"
          :name="info.name"
          :label="info.label"
        />
      </div>
      <button type="submit">Valider</button>
    </form>
    {{ infos }}
  </section>
</template>

<script>
import axios from "axios";
import Input from "../../components/generic/Input";
export default {
  data() {
    return {
      errored: false,
      loading: true,
      infos: null,
      path:null,
    };
  },
  components: {
    Input,
  },
  mounted: function () {
    console.log(this.deleteElement);
    axios
      .get(`/api${this.$route.path.slice(4)}/form`)
      .then((response) => {
        console.log(this.$route);
        this.infos = response.data;
      })
      .catch((error) => {
        console.log(error);
        this.errored = true;
      })
      .finally(() => {
        this.loading = false;
      });
      this.path = '/api'+this.$route.path.slice(4)+"/new"
  },
};
</script>

<style>
</style>