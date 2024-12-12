<template>
    <div>
        <Title />
        <Form />
        <BookResults />
    </div>
</template>

<script>
import Title from '@/components/library/Title.vue';
import Form from '@/components/library/Form.vue';
import BookResults from '@/components/library/BookResults.vue';

export default {
  name: 'HomeView',
  components: {
    Title, 
    Form,
    BookResults,
  }
}

</script>

<style scoped>
</style>
