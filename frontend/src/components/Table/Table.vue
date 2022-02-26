<template>
  <table class="table">
    <thead>
    <tr>
      <th scope="col">Дата</th>
      <th scope="col">Название</th>
      <th scope="col">Количество</th>
      <th scope="col">Расстояние</th>
    </tr>
    </thead>
    <tbody>
      <Row v-for="item in items" :key="item.item_id" :data="item"></Row>
    </tbody>
  </table>
</template>

<script>
import Row from "@/components/Table/Row";
export default {
  name: "Table",
  components: {Row},
  props: ['items']
}
</script>

<style scoped>

</style>