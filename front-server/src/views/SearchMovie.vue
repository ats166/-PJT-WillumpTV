<template>
  <div 
  v-if="SearchMovie.length >= 1"
  :style="{backgroundImage:`url('${imgSrc}')`}"
  id="divsearch">
      <h1> 윌럼프가 설산에서 찾은 <strong style="color:red">" {{ this.$route.params.SearchData }} " </strong> 에 대한 검색결과입니다.
      <img src="@/assets/willumpskillW.png"
      style="width:200px; height:50px"
      >    
      </h1>
    <b-carousel
    id="carousel-1"
    v-model="slide"
    :interval="4000"
    label-next="다음 영화"
    label-prev="이전 영화"
    controls
    background="rgba(0,0,0,0)"
    :fade="true"
    style="text-shadow: 1px 1px 2px #333; "
    @sliding-start="onSlideStart"
    @sliding-end="onSlideEnd"
    >

    <GenreMovieList
    v-for="(movie, index) in SearchMovie"
    :key="index"
    :movie="movie"
    />
    </b-carousel>
  </div>
  <div id="divsearch"
  v-else
  >
    <div
    >
    <h1>윌럼프가 모든 설산을 찾아 헤맸지만</h1>
    <h1><strong style="color:red">" {{ this.SearchData }} "</strong>에 대한 영화정보를 찾지 못했습니다..</h1>
    <video src="@/assets/willumpangry.mp4" autoplay muted loop></video>
    </div>
  </div>
</template>

<script>
import GenreMovieList from '@/components/GenreMovieList'

export default {
  name : "SearchMovie",
  components: {
    GenreMovieList,
  },
  data() {
    return {
      slide: 0,
      sliding: null,
      movies: this.$store.state.movies,
    }
  },
  created() {
    console.log(this.movies,'created')
    console.log(this.$store.state.SearchData,'search')
    this.SearchData = this.$store.state.SearchData
    this.isLogin()
  },
  computed: {
    // SearchInputData() {
    //   return this.$store.params.SearchData
    // },
    SearchMovie() {
      // console.log('SearchMovie')
      return this.movies.filter((movie) => {
        if(movie.title.includes(this.$route.params.SearchData)) {
          return movie
        }
      })
    },
    imgSrc() {
      // console.log(this.SearchMovie[this.slide].backdrop_path)
      return "https://image.tmdb.org/t/p/original" + this.SearchMovie[this.slide].backdrop_path 
    }
  },
  methods: {
    isLogin() {
      if (this.$store.state.token == null) {
        alert('로그인이 필요한 서비스 입니다.')
        this.$router.push({ name: 'LogInView'})
      }
    },
    onSlideStart(slide) {
      this.sliding = true
    },
    onSlideEnd(slide) {
      this.sliding = false
    },
  }
}
</script>

<style>
#divsearch {
  background-image: url('@/assets/back.jpg');
  background-size: cover;
  color: white;
  padding-top:250px;
  padding-left: max(15vw, 160px);
  font-family: 'ImcreSoojin';
  background-attachment: fixed;
  height: 100%;
}

@font-face {
    font-family: 'ImcreSoojin';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_20-04@2.3/ImcreSoojin.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}
</style>