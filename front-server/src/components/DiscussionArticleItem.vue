<template>
  <div
  id="DiscussionArticleItemdiv"
  >
  <div id="bcard">
    <router-link 
    style="text-decoration-line: none;"
    :to="{name: 'DetailView', params: { id: article.id }}">
    <b-card no-body class="overflow-hidden" style="max-width: 540px; color:black; font-size:15px;"
    >
    <b-row no-gutters>
      <b-col md="6">
        <b-card-img :src="imgurl" alt="Image" class="rounded-0" style="height:100%; width:100%; max-width:200px;"></b-card-img>
      </b-col>
      <b-col md="6">
        <b-card-body class="b-title" :title="article.title" style="font-size:55px;">
          <b-card-text>
            <p style="text-align:right; font-size:12px; color:gray"> {{ article.username }}</p>
            <hr>
            <p style="font-size:15px;">{{ article.content }} </p>
          </b-card-text>
        </b-card-body>
      </b-col>
    </b-row>
  </b-card>
</router-link>
</div>
</div>
</template>

<script>
export default {
  name: 'DiscussionArticleItem',
  data() {
    return {
      imgurl : null,
    }
  },
  props: {
    article : Object,
  },
  created() {
    // console.log(this.article);
    this.imgurl = "http://127.0.0.1:8000" + this.article.photo
  }
}
</script>

<style>
#DiscussionArticleItemdiv {
  background-color:rgba(255,255,255,0);
  /* color:black; */
  display: inline-block;
  vertical-align:top;
  /* float:left; */
  margin-right: 20px;
  margin-top: 20px;
}

</style>
