<template>
  <!-- <router-link :to="{ name: 'DiscussionArticleItem', params: {id : this.Article.id}}> -->
    <b-card
    :title="Article.title"
    :img-src="this.Articleimg"
    style="width: 300px; height: 300px; color:black; float:left"
    class="m-5"
    >
      <b-card-text style="color:black; height:100%;">
        {{Article.content}}
      </b-card-text>
    </b-card>
</template>

<script>
export default {
  name: 'MyArticle',
  props: {
    Article : Object,
  },
  computed: {
    Articleimg() {
      return "http://127.0.0.1:8000" + this.Article.photo
    }
  },
  methods : {
  }
}
</script>

<style>

</style>