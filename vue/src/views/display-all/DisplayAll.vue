<template>
  <section>
    <div class="section-title">
      <h1>{{ this.$route.name }}</h1>
    </div>
    <div v-if="errored" class="error">
      <p>
        Nous sommes désolés, nous ne sommes pas en mesure de récupérer ces
        informations pour le moment. Veuillez réessayer ultérieurement.
      </p>
    </div>
    <div class="container">
      <div v-if="loading" class="loading">Chargement...</div>
      <router-link :to="{ name: 'Add ' + this.$route.name.slice(0, -1) }"
        >Add new</router-link
      >
      <table class="content-table">
        <thead class="table-dark">
          <tr>
            <th v-for="key in keys" :key="key" scope="col">{{ key }}</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="info in infos" :key="info.id">
            <td v-for="(value, key) in info" :key="key">
              <router-link
                v-bind:to="{ name: pathName, params: { id: info.id } }"
              >
                <img
                  v-if="key == 'image'"
                  :src="value.url"
                  :alt="value.name"
                  style="height: 50px; width: 50px"
                />
                <p v-else>{{ value }}</p>
              </router-link>
            </td>
            <td>
              <router-link
                v-bind:to="{
                  name: 'Update ' + pathName,
                  params: { id: info.id },
                }"
                ><i class="fas fa-edit"></i
              ></router-link>
              |
              <i class="far fa-trash-alt" @click="deleteElement(info.id)"></i>
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
      pathName: null,
      infos: null,
      types: null,
      keys: null,
      errored: false,
      loading: true,
    };
  },
  mounted: function () {
    axios
      .get(`/api${this.$route.path}`)
      .then((response) => {
        console.log(this.$route);
        this.infos = response.data.results;
        this.keys = Object.keys(Object.assign({}, ...this.infos));
        this.pathName = response.data.unitName;
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
    async deleteElement(id) {
      await axios
        .delete(`/api${this.$route.path.slice(0, -1)}/${id}/delete`)
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => {
          this.loading = false;
        });
      window.location.reload();
    },
  },
};
</script>
