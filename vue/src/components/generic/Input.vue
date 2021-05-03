<template>
  <div class="form__group field">
    <input
      :type="type"
      :name="name"
      class="form__field"
      :placeholder="placeholder"
      :value="value"
      :step="step"
      required
    />
    <label for="name" class="form__label">{{ label }}</label>
  </div>
</template>

<script>
export default {
  name: "Input",
  props: ["type", "placeholder", "name", "value", "label", "step"],
};
</script>
