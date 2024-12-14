<template>
    <div>
        <Title />
        <Form />
        <BookResults v-if="showBooks" />
        <NoBooks v-if="!showBooks" />
    </div>
</template>

<script>
import { mapGetters } from "vuex";
import Title from '@/components/library/Title.vue';
import Form from '@/components/library/Form.vue';
import BookResults from '@/components/library/BookResults.vue';
import NoBooks from '@/components/library/NoBooks.vue';


export default {
  name: 'HomeView',
  components: {
    Title, 
    Form,
    BookResults,
    NoBooks, 
  }, 
  computed: {
    ...mapGetters("library", [
      "showBooks",
    ]),
  },
}

</script>

<style scoped>
</style>
