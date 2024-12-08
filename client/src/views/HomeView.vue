<template>
  <div>
    <Jumbotron />
  </div>
</template>

<script>
// @ is an alias to /src
import Jumbotron from '@/components/home/Jumbotron.vue';

export default {
  name: 'HomeView',
  components: {
    Jumbotron, 
  }
}
</script>
