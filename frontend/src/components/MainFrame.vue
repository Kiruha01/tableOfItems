<template>
  <div>
    <div class="row">
      <div class="col-4">
        <h2>Сортировка</h2>
        <SortingComponent :sort-fields="config.SORTING_FIELDS" @change="sortItems"/>
      </div>
      <div class="col-8">
        <h2>Фильтрация</h2>
        <FilteringComponent :filter-fields="config.FILTERING_FIELDS" :filter-types="config.FILTERING_TYPES"
                            @change_1="filterItems"/>

      </div>
    </div>

    <Table :items="items"/>
    <Pagination :total-pages="totalPages" :current-page="currentPage"
                @change="changePage"/>
  </div>
</template>

<script>
import Table from "@/components/Table/TableComponent";
import axios from 'axios';
import Pagination from "@/components/Table/PaginationComponent";
import SortingComponent from "@/components/SortingComponent";

import Config from '@/config'
import FilteringComponent from "@/components/FilteringComponent";
export default {
  name: 'MainFrame',
  components: {FilteringComponent, SortingComponent, Pagination, Table},
  data(){
    return {
      config: Config,
      totalPages: null,
      currentPage: 1,
      newPage: 1,
      items: [],

      sortingField: null,

      filterParams: {filter_field: null, filter_type: null, filter_value: null}
    }
  },

  mounted() {
    this.updateData(1)
  },

  methods: {
    updateData(page = this.currentPage, sorting = this.sortingField, filterParams = this.filterParams) {
      axios.get('/api/items/', {
        params: {
          page: page,
          sorting: sorting,
          filter_field: filterParams.filter_field,
          filter_type: filterParams.filter_type,
          filter_value: filterParams.filter_value
        }
      }).then(
          response => {
            this.totalPages = response.data['total_pages']
            this.items = response.data['items']
          }
      ).catch((error) => {
        let s = ""
        for (let key in error.response.data.message) {
          s += key + ': ' + error.response.data.message[key]
        }
        for (let key in this.filterParams){
          this.filterParams[key] = null
        }
          alert(s)

      })
    },

    sortItems(e){
      this.sortingField = e
      this.currentPage = 1
      this.updateData(1, e, this.filterParams)
    },

    filterItems(e){
      this.filterParams = e
      this.currentPage = 1
      this.updateData(1, this.sortingField, e)
    },

    changePage(e){
      this.currentPage = e
      this.updateData(e, this.sortingField, this.filterParams)
    }
  },

}
</script>
