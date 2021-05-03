<template>
  <div>
    <label class="typo__label">Tagging</label>
    <multiselect
      v-model="value"
      tag-placeholder="Add this as new tag"
      :placeholder="placeholder"
      :label="label"
      track-by="code"
      :options="options"
      :multiple="multiple"
      :taggable="true"
    ></multiselect>
  </div>
</template>

<script>
import Multiselect from "vue-multiselect";
export default {
  components: {
    Multiselect,
  },
  data() {
    return {
      props: ["options","placeholder","label","multiple"],
      value: [{ name: "Javascript", code: "js" }],
      options: [
        { name: "Vue.js", code: "vu" },
        { name: "Javascript", code: "js" },
        { name: "Open Source", code: "os" },
      ],
    };
  },
};
</script>

<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>