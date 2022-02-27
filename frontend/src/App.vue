<template>
    <div>
        <h1 class="text-center my-5">Таблица</h1>
    <div class="container">
      <MainFrame/>
    </div>
  </div>
</template>

<script>
import MainFrame from './components/MainFrame.vue'

export default {
  name: 'App',
  components: {
    MainFrame
  }
}
</script>

