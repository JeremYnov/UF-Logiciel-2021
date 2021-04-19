<template>
  <section class="add">
    <div v-if="errored" class="error">
      <p>
        Nous sommes désolés, nous ne sommes pas en mesure de récupérer ces
        informations pour le moment. Veuillez réessayer ultérieurement.
      </p>
    </div>
    <div v-if="loading" class="loading">Chargement...</div>
    <form enctype="multipart/form-data" @submit.prevent="update" >
      <div v-for="info in infos.form" :key="info.name">
        <label :for="info.name">{{ info.label }}</label>
        <input
          v-if="info.step"
          :type="info.type"
          :placeholder="info.placeholder"
          :name="info.name"
          :step="info.step"
          :value="info.value"
          @change="updateValue"
          required
        />
        <input
          v-else
          :type="info.type"
          :placeholder="info.placeholder"
          :name="info.name"
          :value="info.value"
          @change="updateValue"
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
      path: null,
      form: {},
    };
  },
  mounted: async function () {
    await axios
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
  methods: {
    update() {
      let formData = new FormData();
      for(const element in this.form){
          console.log(element)
          console.log(this.form[element])
          formData.append(element, this.form[element])
        //   console.log(this.form[element])
      }
      console.log(formData)
      let config = {
        method: "put",
        url: `/api${this.$route.path.slice(7)}/update`,
        headers: { "Content-Type": "multipart/form-data" },
        data: formData,
      };
      const response = axios(config)
        .then(function (response) {
          return response;
        })
        .catch(function (error) {
          console.log(error);
        });
      console.log(response);
    },
    updateValue(event) {
        this.form[event.target.name] = event.target.value;
    },
  },
};
</script>

<style>
</style>