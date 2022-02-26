<template>
  <div>
    <select @change.stop="changeField" class="form-select">
      <option selected disabled>Сортировка по</option>
      <option v-for="field in sortFields" :value="field.name" :key="field.name">{{field.title}}</option>
    </select>
  </div>
</template>

<script>
export default {
  name: "SortingComponent",
  props:{
    sortFields: Array,
  },
  methods:{
    changeField(e){
      console.log(e.target.value)
      this.$emit("change", e.target.value)
    }
  }
}
</script>

<style scoped>

</style>