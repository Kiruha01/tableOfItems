<template>
    <div>
        <h1 class="text-center mt-5">Table for that</h1>
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

