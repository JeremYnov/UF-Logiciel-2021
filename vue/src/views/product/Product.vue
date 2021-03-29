<template>
  <section class="products">

  </section>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      info: null,
      errored: false,
      loading: true,
      product:{
          name:null,
          stock:null,
          picture:null,
          invoiceReference:null,
      }
    };
  },
  mounted: function () {
    axios
      .get("")
      .then((response) => (this.info = response))
      .catch((error) => {
        console.log(error);
        this.errored = true;
      })
      .finally(() => (this.loading = false));
  },
};
</script>

<style>

</style>