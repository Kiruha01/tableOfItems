<template>
  <tr>
    <td>{{data.date}}</td>
    <td>{{data.name}}</td>
    <td>{{data.count}}</td>
    <td>{{data.distance}}</td>
  </tr>
</template>

<script>
export default {
  name: "RowComponent",
  props: ['data'],
}
</script>

<style scoped>

</style>