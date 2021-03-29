<template>
<section class="invoices">

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
      invoice:{
          clientReference:null,
          issueDate:null,
          is_paid:null,
          paymentDate:null,
          price: null,
          products:[],
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