<template>
  <div class="article-list"
  id="articlez"
  >
    <DiscussionArticleItem
    v-for="article in articles"
    :key="article.id"
    :article="article"
    />
  </div>
</template>

<script>
import DiscussionArticleItem from '@/components/DiscussionArticleItem'

export default {
  name: 'ArticleList',
  components: {
    DiscussionArticleItem
  },
  computed: {
    articles() {
      return this.$store.state.articles
    },
  }
}
</script>

<style>
.article-list {
  text-align: start;
  
}

</style>
