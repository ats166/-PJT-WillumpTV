<template>
  <div>
    <div
    v-if="movie_title"
    >
      {{ getsearchdata() }}
      <div
      v-if="searchdata"
      >
      {{ getyoutube() }}git 

      </div>
    </div>
    
    <!-- v-if="videoSrc" -->
    <iframe 
    id="youtube"
    :src="youtubeplay" frameborder="0" allow="autoplay"></iframe>

  </div>

</template>

<script>
import axios from 'axios'

const YOUTUBE_API_URL = 'https://www.googleapis.com/youtube/v3/search'
const YOUTUBE_API_KEY = ''



export default {
  name : 'DetailYoutubeView',
  data() {
    return {
      viedo : null,
      selectedVideo : null,
      videoURL : "http://www.youtube.com/embed/",
      videoSrc : null,
      searchdata : null,
    }
  },
  computed: {
    youtubeplay() {
      // console.log(this.videoSrc,'videoSrc');
      return  `http://www.youtube.com/embed/${this.videoSrc}`
    },
  },
  props: {
    movie_title : String,
  },
  methods: {
    getsearchdata() {
      this.searchdata = `${this.movie_title} 결말포함`
    },
    getyoutube() {
      // console.log(this.searchdata, "유튜브검색제목")
      axios.get(YOUTUBE_API_URL,{
        params : {
          key : YOUTUBE_API_KEY,
          type : 'video',
          part : 'snippet',
          q : this.searchdata
          },
        }).then((response) => {
          this.videos = response.data.items
          this.selectedVideo = this.videos[0]
          this.videoSrc = this.selectedVideo.id.videoId
          // console.log(response,'created')
          // console.log(this.q,'axios')
        }).catch((error) => {
          // console.log(error,'created')
        })
    }
  }
}
</script>

<style>

#youtube {
  margin-top: 250px;
  left: 15%;
  position: absolute;
  z-index: 5;
  height: 70vh;
  width: 80%;
  z-index:1;
}
</style>