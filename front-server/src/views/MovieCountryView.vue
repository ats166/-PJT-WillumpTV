<template>
  <div id="divcountry"
  :style="{backgroundImage:`url('${imgSrc}')`}"
  >
  <!-- {{ movies }} -->
    <div 
    v-if="code==1"
    class="container-fluid"
    >
      <h1 class="d-flex justify-content-center" style="color:white;">
      윌럼프가 가져온 <strong style="color:red">" 한국 "</strong> 영화 목록입니다.
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
        <CountryMovieList
        v-for="(movie,index) in korea"
        :key="index"
        :movie="movie"
          />
        </b-carousel>
    </div>
    <div 
    v-else
    class="container-fluid"
    >
      <h1 class="d-flex justify-content-center" style="color:white;">
        윌럼프가 가져온 <strong style="color:red">" 해외 "</strong> 영화 목록입니다.
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
      
        <CountryMovieList
          v-for="(movie,index) in other"
          :key="index"
          :movie="movie"
          class="example-slide"
          />
      </b-carousel>
    </div>
  </div>
  
</template>

<script>
import CountryMovieList from '@/components/CountryMovieList'

export default {
  name: 'MovieCountryView',
  data() {
    return {
      slide: 0,
      sliding: null,
      movies : this.$store.state.movies,
      korea : null,
      other : null,
    }
  },
  components: {
    CountryMovieList,
  },
  created() {
    this.KoreaMovie()
    this.OtherMovie()
    this.isLogin()
  },
  computed : {
    imgSrc() {
      if (this.code==0) {
        console.log(this.other[this.slide].backdrop_path)
        return "https://image.tmdb.org/t/p/original" + this.other[this.slide].backdrop_path
      }
      else {
        return "https://image.tmdb.org/t/p/original" + this.korea[this.slide].backdrop_path
      }
    },
    code() {
      this.KoreaMovie()
      this.OtherMovie()
      return this.$route.params.code
    },
  },
  methods: {
    isLogin() {
      if (this.$store.state.token == null) {
        alert('로그인이 필요한 서비스 입니다.')
        this.$router.push({ name: 'LogInView'})
      }
    },
    KoreaMovie () {
        this.korea = this.movies.filter((movie) => {
          if(movie.original_language == "ko") {
            return movie
          }
      })
    },
    OtherMovie () {
      this.other = this.movies.filter((movie) => {
        if(movie.original_language != "ko") {
          return movie
        }
      })
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

#carousel-1{
  float:inline-start;
}

.example-slide {
  /* align-items: center;
  background-color: #666;
  color: #999;
  display: flex;
  font-size: 1.5rem;
  justify-content: center;
  min-height: 10rem; */
}

#divcountry {
  /* background-image: url('@/assets/back.jpg'); */
  background-size: cover;
  padding-top: 250px;
  padding-left: max(15vw, 160px);
  font-family: 'ImcreSoojin';
  height: 100%;
  background-attachment: fixed;
  /* transition: all 0.5s ease; */
}

@font-face {
    font-family: 'ImcreSoojin';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_20-04@2.3/ImcreSoojin.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}
</style>