<template>
  <nav>
    <ul class="pagination">

      <li :class="{'page-item': true, disabled: currentPage === 1}">
        <a class="page-link" @click="changePage(this.currentPage - 1)" tabindex="-1">Prev</a>
      </li>

      <template v-for="i in totalPages" :key="i">
        <li :class="{'page-item': true, active: currentPage === i}" aria-current="page">
          <a @click="changePage(parseInt(i))" :id="i" class="page-link">{{i}}</a>
        </li>
      </template>

      <li :class="{'page-item': true, disabled: currentPage === totalPages}">
        <a class="page-link" @click="changePage(this.currentPage + 1)">Next</a>
      </li>

    </ul>
  </nav>
</template>

<script>
export default {
  name: "Pagination",
  props: {
    currentPage: Number,
    totalPages: Number,
  },


  methods:{
    changePage(value){
      this.$emit('change', value);
    }
  }
}
</script>

<style scoped>
li {
  cursor: pointer;
}
</style>