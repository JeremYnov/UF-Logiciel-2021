<template>
  <section class="update">
    <div class="section-title">
      <h1>{{ this.$route.name }}</h1>
    </div>
    <div v-if="errored" class="error">
      <p>
        Nous sommes désolés, nous ne sommes pas en mesure de récupérer ces
        informations pour le moment. Veuillez réessayer ultérieurement.
      </p>
    </div>
    <div v-if="loading" class="loading">Chargement...</div>
    <div class="form-container">
    <form v-if="infos" @submit.prevent="update">
      <div v-for="info in infos.form" :key="info.name">
        <Input v-if="info.step"
          :type="info.type"
          :placeholder="info.placeholder"
          :name="info.name"
          :value="info.value"
          :step="info.step"
          :label="info.label"
        />
        <Input v-else
          :type="info.type"
          :placeholder="info.placeholder"
          :name="info.name"
          :value="info.value"
          :label="info.label"
        />
      </div>
      <button type="submit" class="submit-btn">Valider</button>
    </form>
    </div>
    <!-- {{ infos }} -->
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
      path: null,
    };
  },
  components: {
    Input,
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
    async update(event) {
      let formData = new FormData();

      event.target.forEach((element) => {
        if (element.type == "file") {
          if (element.files[0]) {
            formData.append(
              element.name,
              element.files[0],
              element.files[0].name
            );
          }
        } else {
          formData.append(element.name, element.value);
        }
      });

      let config = {
        method: "put",
        url: `/api${this.$route.path.slice(7)}/update`,
        headers: { "Content-Type": "multipart/form-data" },
        data: formData,
      };
      const response = await axios(config)
        .then(function (response) {
          return response;
        })
        .catch(function (error) {
          console.log(error);
        });
      console.log(response);

      this.$router.push({
        name: `${response.data.path.name}`,
        params: `${response.data.path.params}`,
      });
    },
  },
};
</script>

<style>
</style>