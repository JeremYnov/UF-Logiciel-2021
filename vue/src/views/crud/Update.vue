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
          <Input
            v-if="info.step"
            :type="info.type"
            :placeholder="info.placeholder"
            :name="info.name"
            :value="info.value"
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
            <input type="hidden" name="client" :value="clientValue.id" />
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
              :value="productValue"
              :placeholder="info.placeholder"
              :options="products"
              :multiple="info.multiple"
              :taggable="true"
              @input="onChange"
            ></multiselect>
            <input type="hidden" name="products" :value="value" />
          </div>

          <div
            v-else-if="
              info.type == 'multiselect' && info.name == 'isPaid' && isPaid
            "
          >
            <label class="typo__label">{{ info.label }}</label>
            <multiselect
              v-model="isPaidValue"
              tag-placeholder="Add this as new tag"
              label="name"
              track-by="name"
              :placeholder="info.placeholder"
              :options="isPaid"
              :multiple="info.multiple"
            ></multiselect>
            <input type="hidden" name="isPaid" :value="isPaidValue.name" />
          </div>

          <Input
            v-else
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
  </section>
</template>

<script>
import axios from "axios";
import Input from "../../components/generic/Input";
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
      isPaid:[{name:"True"},{name:"False"}],
      isPaidValue:[],
      value: [],
    };
  },
  components: {
    Input,
    Multiselect,
  },
  mounted: async function () {
    await axios
      .get(`/api${this.$route.path.slice(7)}`)
      .then((response) => {
        this.infos = response.data;
        if (this.$route.name == "Update Invoice") {
          const client = {
            id: this.infos.result.client.id,
            name: `${this.infos.result.client.firstName} ${this.infos.result.client.lastName}`,
          };
          this.clientValue.push(client);

          response.data.result.products.forEach((element) => {
            const product = { id: element.id, name: element.name };
            this.productValue.push(product);
          });
          this.value = response.data.form.products.value

          const isPaid = {
            name: response.data.form.isPaid.value
          }
          this.isPaidValue.push(isPaid)
        }
      })
      .catch((error) => {
        console.log(error);
        this.errored = true;
      })
      .finally(() => {
        this.loading = false;
      });

    if (this.$route.name == "Update Invoice") {
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

      this.$router.push({
        name: `${response.data.path.name}`,
        params: `${response.data.path.params}`,
      });
    },
    onChange(value) {
      this.value = []
      value.forEach(element => {
        this.value.push(element.id)
      });
    }
  },
};
</script>

<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>