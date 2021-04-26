<template>
  <div>
    <label :for="name">{{ label }}</label>
    <input
      :type="type"
      :placeholder="placeholder"
      :name="name"
      :value="value"
    />
  </div>
</template>

<script>
export default {
  name: "Input",
  props:['type', 'placeholder','name','value', 'label','step']
};
</script>
