<template>
  <section class="add">
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
      <form :action="path" method="POST" enctype="multipart/form-data">
        <div v-for="info in infos" :key="info.key">
          <Input
            v-if="info.step"
            :type="info.type"
            :placeholder="info.placeholder"
            :name="info.name"
            :step="info.step"
            :label="info.label"
          />
          <div
            v-else-if="
              info.type == 'multiselect' && info.name == 'clients' && clients
            "
          >
            <label class="typo__label">{{ info.label }}</label>
            <multiselect
              v-model="clientValue"
              tag-placeholder="Add this as new tag"
              label="name"
              track-by="id"
              :placeholder="info.placeholder"
              :options="clients"
              :multiple="info.multiple"
            ></multiselect>
          </div>
          <div
            v-else-if="
              info.type == 'multiselect' && info.name == 'products' && products
            "
          >
            <label class="typo__label">{{ info.label }}</label>
            <multiselect
              v-model="productValue"
              tag-placeholder="Add this as new tag"
              label="name"
              track-by="id"
              :placeholder="info.placeholder"
              :options="products"
              :multiple="info.multiple"
              :taggable="true"
            ></multiselect>
          </div>
          <Input
            v-else
            :type="info.type"
            :placeholder="info.placeholder"
            :name="info.name"
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
import Input from "@/components/generic/Input";
import Multiselect from "vue-multiselect";
export default {
  data() {
    return {
      errored: false,
      loading: true,
      infos: null,
      path: null,
      clients: [],
      clientValue: [],
      products: [],
      productValue: [],
    };
  },
  components: {
    Input,
    Multiselect,
  },
  mounted: async function () {
    await axios
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
    this.path = "/api" + this.$route.path.slice(4) + "/new";
    if (this.$route.name == "Add Invoice") {
      await axios
        .get(`/api/clients`)
        .then((response) => {
          response.data.results.forEach((element) => {
            const client = {
              id: element.id,
              name: `${element.firstName} ${element.lastName}`,
            };
            this.clients.push(client);
          });
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => {
          this.loading = false;
        });

      await axios
        .get(`/api/products`)
        .then((response) => {
          response.data.results.forEach((element) => {
            const product = { id: element.id, name: element.name };
            this.products.push(product);
          });
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => {
          this.loading = false;
        });
    }
  },
};
</script>

<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>

