<template>
  <div>
    <p>{{totalPages}}</p>
  <Table :items="items"/>
    <Pagination :current-page="currentPage" :total-pages="totalPages" :update-data="updateData"/>
  </div>
</template>

<script>
import Table from "@/components/Table/Table";
import axios from 'axios';
import Pagination from "@/components/Table/Pagination";
export default {
  name: 'MainFrame',
  components: {Pagination, Table},
  props: {
    msg: String
  },
  data(){
    return {
      totalPages: null,
      currentPage: 1,
      items: []
    }
  },

  mounted() {
    axios.get('/api/items/').then(
        response => {
          this.totalPages = response.data['total_pages']
          this.items = response.data['items']
        }
    )
  },

  methods: {
    updateData(page){
      axios.get('/api/items/', {
        params: {page: page}
      }).then(
          response => {
            this.totalPages = response.data['total_pages']
            this.items = response.data['items']
            this.currentPage = page
          }
      )
    }
  }
}
</script>
