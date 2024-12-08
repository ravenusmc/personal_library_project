<template>
    <div>
        <Title />
        <Form />
    </div>
</template>

<script>
import Title from '@/components/library/Title.vue';
import Form from '@/components/library/Form.vue';

export default {
  name: 'HomeView',
  components: {
    Title, 
    Form,
  }
}

</script>

<style scoped>
</style>
