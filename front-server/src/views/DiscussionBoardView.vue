<template>
  <div id="div1">
    <div style="color:white">
      <h1>명장면 게시판</h1>
      <h3>윌럼프에게 본인이 생각하는 가장 최고의 명장면을 소개해주세요 !</h3>
    </div>
    <hr>
    <DiscussionArticleList/>
  </div>
</template>

<script>
import DiscussionArticleList from '@/components/DiscussionArticleList'

export default {
  name: 'DiscussionBoardView',
  components: {
    DiscussionArticleList
  },
  computed:{
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  created() {
    this.getArticles()
  },
  methods: {
    getArticles() {
      if (this.isLogin) {
        this.$store.dispatch('getArticles')
      } else {
        alert('로그인이 필요한 서비스 입니다.')
        this.$router.push({ name: 'LogInView'})
      }
    }
  }
}
</script>

<style>

#div1 {
    padding-left: max(20vw, 150px);
    padding-top: 30%;
    z-index:10;
    /* margin-top: 30%; */
}
</style>
