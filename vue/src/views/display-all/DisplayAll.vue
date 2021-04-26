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
      <router-link
        class="btn btn-primary btn-lg btn-block"
        v-bind:to="{ name: 'Add' + this.$route.name.slice(0, -1) }"
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
                  name: 'Update' + pathName,
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

<style lang="scss">
.container {
  margin: 40px;
}

thead tr th {
  text-transform: capitalize;
}

.section-title {
  width: 100%;
  height: 60px;
  background-color: #2c3e50;
  display: flex;
  justify-content: center;
  align-items: center;
  h1 {
    color: white;
  }
}

.content-table {
  width: 100%;
  border-collapse: collapse;
  margin: 25px 0;
  font-size: 0.9em;
  min-width: 400px;
  border-radius: 5px 5px 0 0;
  overflow: hidden;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
  thead tr {
    background-color: #2c3e50;
    color: #fff;
    text-align: center;
    font-weight: bold;
  }
  th,
  td {
    padding: 12px 15px;
    font-size: 15px;
    .fa-trash-alt {
        color: rgb(170, 4, 4);
      }
  }
  tbody tr {
    border-bottom: 1px solid #dddddd;
    &:nth-of-type(even) {
      background-color: #f3f3f3;
    }
    &:last-of-type {
      border-bottom: 2px solid #2c3e50;
    }
    td a {
      text-decoration: none;
      color: black;
      .fa-edit{
        color: rgb(22, 131, 255);
      }
      
    }
  }
}
</style>