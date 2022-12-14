<template>
  <div id="divgenre"
  :style="{backgroundImage:`url('${imgSrc}')`}"
  >
  <div class="container-fluid">
    <h1
    style="color:white;"
    >윌럼프가 가져온 <strong style="color:red">" {{ this.$store.state.genre }} "</strong> 장르 영화 목록입니다. 
    <img src="@/assets/willumpskillW.png"
    style="width:200px; height:50px"
    >
    </h1>
    <b-carousel
    id="carousel-1"
    v-model="slide"
    :interval="5000"
    label-next="다음 영화"
    label-prev="이전 영화"
    controls
    background="rgba(0,0,0,0)"
    img-width
    img-height="10px"
    :fade="true"
    style="text-shadow: 1px 1px 2px #333; "
    @sliding-start="onSlideStart"
    @sliding-end="onSlideEnd"
    >
      <GenreMovieList
      v-for="(movie, index) in MovieinGenre"
      :key="index"
      :movie="movie"
      />
    </b-carousel>
  </div>
  </div>
</template>

<script>
import GenreMovieList from '@/components/GenreMovieList'

export default {
  name: "MovieGenreview",
  components: {
    GenreMovieList,
  },
  data() {
    return{
      movies : this.$store.state.movies,
      slide: 0,
      sliding: null,
    }
  },
  computed: {
    imgSrc() {
      console.log(this.MovieinGenre[this.slide].backdrop_path)
      return "https://image.tmdb.org/t/p/original" + this.MovieinGenre[this.slide].backdrop_path 
    },
    genre() {
      this.$store.dispatch('SaveGenre',this.$route.params.name)
      return this.$route.params.genre
    },
    name() {
      return this.$route.params.name
    },
    MovieinGenre() {
      // console.log(this.movies,'장르')
      return this.movies.filter((movie) => {
        for (let i=0; i<movie.genres.length; i++) {
          // console.log(movie.genres[i].id,'장르');
          // console.log(movie.genres,'장르장르');
          if(this.genre == movie.genres[i].id) {
            // 14 in [12, 14, 18]
            // console.log(movie,'return');
            return movie
          }
        }
      })
    }
  },
  created() {
    console.log(this.MovieinGenre,'여긴어디');
    this.getMovieData()
    this.isLogin()
  },
  methods: {
  isLogin() {
    if (this.$store.state.token == null) {
      alert('로그인이 필요한 서비스 입니다.')
      this.$router.push({ name: 'LogInView'})
    }
  },
  getMovieData() {
    this.$store.dispatch('getMovieData',this.$route.params.name)
    },
  onSlideStart(slide) {
      this.sliding = true
    },
  onSlideEnd(slide) {
    this.sliding = false
    },
  },
}
</script>

<style>

#divgenre {
  /* background-image: url('@/assets/back.jpg'); */
  background-size: cover;
  padding-top: 250px;
  padding-left: max(15vw, 160px);
  font-family: 'ImcreSoojin';
  height: 100%;
  background-attachment: fixed;

  /* transition: all 0.5s ease; */
}

#carousel-1 {
  padding-top:0px;
  height:100vh !important;
}

@font-face {
    font-family: 'ImcreSoojin';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_20-04@2.3/ImcreSoojin.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}
</style>