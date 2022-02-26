<template>
  <nav>
    <ul class="pagination">

      <li :class="{'page-item': true, disabled: currentPage === 1}">
        <a class="page-link" @click="dec_page" tabindex="-1">Previous</a>
      </li>

      <template v-for="i in totalPages" :key="i">
        <li :class="{'page-item': true, active: currentPage === i}" aria-current="page">
          <a @click="changePage" :id="i" class="page-link">{{i}}</a>
        </li>
      </template>

      <li :class="{'page-item': true, disabled: currentPage === totalPages}">
        <a class="page-link" @click="inc_page">Next</a>
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
    updateData: Function
  },


  methods:{
    changePage(e){
      this.updateData(parseInt(e.target.id))
    },

    inc_page() {
      this.updateData(this.currentPage + 1)
    },

    dec_page() {
      this.updateData(this.currentPage - 1)
    }

  }
}
</script>

<style scoped>
li {
  cursor: pointer;
}
</style>