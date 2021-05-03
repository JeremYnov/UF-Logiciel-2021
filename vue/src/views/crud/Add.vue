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
          <Input
            v-else
            :type="info.type"
            :placeholder="info.placeholder"
            :name="info.name"
            :label="info.label"
          />
          
        </div>
        <Multiselect v-if="info.type == 'multiselect'"
          :placeholder="info.placeholder"
          :label="info.label"
          :multiple="info.multiple"
        />
        <button type="submit" class="submit-btn">Valider</button>
      </form>
    </div>

    <!-- {{ infos }} -->
  </section>
</template>

<script>
import axios from "axios";
import Input from "@/components/generic/Input";
import Multiselect from "@/components/generic/Multiselect"
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
    Multiselect
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
    this.path = "/api" + this.$route.path.slice(4) + "/new";
  },
};
</script>

