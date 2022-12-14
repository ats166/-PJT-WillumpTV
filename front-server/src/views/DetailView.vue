<template>
  <div
  style="padding-top:15%; padding-left:10%"
  v-if="article"
  >
  <div>
    <video src="@/assets/willumpdance.mp4" class="videoplay" autoplay loop muted></video>
  </div>
    <div class="containar-fluid">
      <div class="row">
        <div class="col-12">

          <p style="font-size:70px; color:white;``">{{ article?.title }}</p>
          <p style="text-align:right; margin-right:20%; color:gray"> {{ article?.username }}</p>
          <p><img :src="imgurl" alt=""> </p> 
        </div>
        <div class="col-8" style="padding-left:18%">
          <p style="margin-top:10%; text-align:left; color:black; width:50%">{{ article?.content }}</p>
        </div>
     </div>
      <!-- <p>영화제목 : {{this.$store.state.movies}}</p> -->
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = "http://127.0.0.1:8000"

export default {
  name: 'DetailView',
  data() {
    return {
      article:null,
    }
  },
  created() {
    this.getArticleDetail()
    console.log();
  },
  methods: {
    getArticleDetail() {
      axios ({
        method:'get',
        url: `${API_URL}/api/v1/articles/${this.$route.params.id}`        
      })
      .then((res) => {
        console.log(`${API_URL}/api/v1/articles/${this.$route.params.id}`,'test');
        console.log(res)
        this.article = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    }
  },
  computed: {
    imgurl() {
      return "http://127.0.0.1:8000" + this.article.photo
    }
  }
}
</script>
