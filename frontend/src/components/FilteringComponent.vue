<template>
  <div class="d-flex">
    <select v-model="filterParams.filter_field" class="form-select mx-1">
      <option selected disabled>Фильтрация по</option>
      <option v-for="field in filterFields" :value="field.name" :key="field.name">{{field.title}}</option>
    </select>

    <select v-model="filterParams.filter_type" class="form-select mx-1">
      <option selected disabled>Условие</option>
      <option v-for="field in filterTypes" :value="field.name" :key="field.name">{{field.title}}</option>
    </select>

    <input v-model="filterParams.filter_value" type="text" class="form-control mx-1" placeholder="Значение">

    <button class="btn btn-primary mx-1" @click.stop="doFiltration">Done</button>
  </div>
</template>

<script>
export default {
  name: "FilteringComponent",
  props: {
    filterFields: Array,
    filterTypes: Array,
    setFilterParams: Function
  },

  data() {
    return {
      filterParams: {filter_field: null, filter_type: null, filter_value: null}
    }
  },

  methods: {
    doFiltration() {
      this.$emit("change_1", Object.assign({}, this.filterParams))
      // this.setFilterParams(this.filterParams)
    }
  }
}
</script>

<style scoped>

</style>