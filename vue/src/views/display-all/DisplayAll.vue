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
            <th></th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="info in infos" :key="info.id">
            <td v-for="(value, key) in info" :key="key">
              <router-link
                v-bind:to="{ name: pathName, params: { id: info.id } }"
              >
                {{ value }}</router-link
              >
            </td>

            <td>
              <router-link
                v-bind:to="{ name: pathName, params: { id: info.id } }"
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
      keys: null,
      errored: false,
      loading: true,
    };
  },
  mounted: function () {
      console.log(this.deleteElement)
    axios
      .get(`/api${this.$route.path}`)
      .then((response) => {
        console.log(this.$route);
        this.infos = response.data.results;
        this.keys = Object.keys(Object.assign({}, ...this.infos));
        this.pathName = response.data.unitName;
        console.log(this.$route);
      })
      .catch((error) => {
        console.log(error);
        this.errored = true;
      })
      .finally(() => {
        this.loading = false;
      });
  },
  methods:{
    
    // async deleteElement(id) {
      
    //   axios
    //   .delete()
    //   .catch((error) => {
    //     console.log(error);
    //     this.errored = true;
    //   })
    //   .finally(() => {
    //     this.loading = false;
    //   });
    // },
  },
};
</script>

<style lang="scss">
.fa-trash-alt {
  color: rgb(170, 4, 4);
}
thead tr th{
  text-transform: capitalize;
}
</style>