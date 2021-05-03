<template>
  <div>
    <label class="typo__label">Tagging</label>
    <multiselect
      v-model="value"
      tag-placeholder="Add this as new tag"
      label="name"
      track-by="id"
      :placeholder="placeholder"
      :options="options"
      :multiple="multiple"
      :taggable="true"
    ></multiselect>
  </div>
</template>

<script>
import Multiselect from "vue-multiselect";
// import axios from "axios";
export default {
  components: {
    Multiselect,
  },
  data() {
    return {
      props: ["options","placeholder","label","multiple","name"],
      value: [{ name: "Javascript", code: "js" }],
    //   clients:[],
    //   products:[],
    //   options: [
    //     { name: "Vue.js", code: "vu" },
    //     { name: "Javascript", code: "js" },
    //     { name: "Open Source", code: "os" },
    //   ],
    };
  },
  mounted: async function(){
      
  }
};
</script>

<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>