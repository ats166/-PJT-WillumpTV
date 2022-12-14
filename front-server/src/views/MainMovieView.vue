<template>
  <div
  v-if="Logon == null"
  id="div2"
  >
  <h1
  style="color:white"
  >
  윌럼프는 친구에게만 영화를 보여줘요.
  </h1>
  <div class="d-flex justify-content-center">
    <div id="friend">
    <router-link :to="{ name: 'LogInView' }"
    class="p-4"
    id="frinedtext"
          >전 이미 친구예요!</router-link>
    </div>
    <div id="friend">
    <router-link :to="{ name: 'SignUpView' }"
    class="p-4"
    id="frinedtext"
          >윌럼프와 친구되기</router-link>
    </div>
    </div>
  <div>
  <video src="@/assets/asd.mp4" class="videoplay" autoplay loop muted></video>
  </div>
  </div>
  <div 
  v-else
  id="div1">
    <div class="row container-fluid">
      <div>
        <h3 class="d-flex justify-content-center" style="color:white; float: left;">
          윌럼프가 {{this.$store.state.nickname}} 님에게 <strong style="color:red">" 추천해드리는 "</strong>영화 목록입니다.
          <img src="@/assets/willumpskillW.png"
          style="width:170px; height:40px;"
          ></h3>
      </div>
    </div>
  <div
  v-if="this.$store.state.recommend == []"
  >
  asdasdasfawofka wopgjmawopgnawpognapow ngapow ngpowang op
  <video src="@/assets/skillW.mp4"></video>
  </div>
  <div
  v-else
  >
    <Carousel
    :per-page="6"
    >
      <slide
      v-for="(movie,index) in recommends"
      :key="index"
      style="margin-left:15px;"
      >
        <MainMovieList
        :movie="movie"
        style="margin-top:40px; margin-bottom:40px;"
        />  
      </slide>
    </Carousel>
  <br>
  </div>

  <div class="row container-fluid">
    <div>
      <h3 class="d-flex justify-content-center" style="color:white; float: left;"> 윌럼프가 찾아온 {{this.$store.state.nickname}}님의 배꼽을 책임질 영화들 !
      </h3>
    </div>
  </div>
  <div v-if="ComedyGenre">
    <Carousel 
      :per-page="6"
      >
      <slide
      v-for="(movie,index) in ComedyGenre"
      :key="index"
      style="margin-left:15px;"
      >
      <MainMovieList
      :movie="movie"
      style="margin-top:40px; margin-bottom:40px;"
      />  
      </slide>
    </Carousel>
  <br>
  </div>
  <div class="row container-fluid">
    <div>
      <h3 class="d-flex justify-content-center" style="color:white; float: left;"> 오늘 하루가 너무 무료했다면 긴장감 넘치는 스릴러 어떠신가요?
      </h3>
    </div>
  </div>
  <div>
     <Carousel 
        :per-page="6"
        >
        <slide
        v-for="(movie,index) in TVGenre"
        :key="index"
        style="margin-left:15px;"
        >
        <MainMovieList
        :movie="movie"
        style="margin-top:40px; margin-bottom:40px;"
        />  
        </slide>
      </Carousel>
    <br>
  </div>
  <div class="row container-fluid">
    <div>
      <h3 class="d-flex justify-content-center" style="color:white; float: left;"> 만화 영화를 좋아하신다면 !
      </h3>
    </div>
  </div>
  <div>
     <Carousel 
        :per-page="6"
        >
        <slide
        v-for="(movie,index) in AnimationGenre"
        :key="index"
        style="margin-left:15px;"
        >
        <MainMovieList
        :movie="movie"
        style="margin-top:40px; margin-bottom:40px;"
        />  
        </slide>
      </Carousel>
    <br>
  </div>

</div>
  
</template>

<script>
import MainMovieList from '@/components/MainMovieList'
import { Carousel, Slide } from 'vue-carousel'

export default {
  name: 'MainMovieview',
  data() {
    return {
      movies : this.$store.state.movies,
      recommends : this.$store.state.recommend,
      TV : null,
      Logon : null,
    }
  },
  components: {
    MainMovieList,
    Carousel,
    Slide,
  },
  created() {
    this.getMovieData()
    // this.getRecommend()
    if (this.$store.state.token != null) {
      this.Logon = this.$store.state.token
    }
  },
  methods: {
    getMovieData() {
      this.$store.dispatch('getMovieData')
    },
    getRecommend() {
      this.$store.dispatch('getRecommend')
    }
  },
  computed: {
    ComedyGenre() {
      return this.movies.filter((movie) => {
        for (let i=0; i<movie.genres.length; i++) {
          if(movie.genres[i].id == 35) {
            return movie
          }
        }
      })
    },
    AnimationGenre() {
      return this.movies.filter((movie) => {
        for (let j=0; j<movie.genres.length; j++) {
          if(movie.genres[j].id == 16) {
            return movie
          }
        }
      })
    },
    TVGenre() {
      return this.movies.filter((movie) => {
        for (let k=0; k<movie.genres.length; k++) {
          if(movie.genres[k].id == 53) {
            return movie
          }
        }
      })      
    },
  }
}
</script>

<style>

#frinedtext {
  /* position: relative;
  top:30%;*/
  font-size: 25px;
  background-color: white;
  text-decoration-line: none;
  /* padding-left:10px; */
}

#frinedtext:hover {
  font-size: 35px;
  background-color: blue;
  color: white;
  transition: ease 1s;
  /* color:red; */
}

#friend {
  /* background-color: white; */
  /* border: 1px solid black; */
  padding-top:30px;
  margin-right: 5%;
  margin-left: 5%;
}


#div2 {
  padding-top: 25%;
  padding-left: max(10vw, 160px);
  height: 100vh;
}

.videoplay { 
  position: fixed;
  top: 0;
  left: 0;
  height: 110vh;
  width: 110vw;
  z-index: -1;
  opacity: 0.4;
  }

#div1 {
  background-image: url('@/assets/back.jpg');
  background-size: cover;
  /* background-color: rgb(255, 255, 255); */
  padding-top: 250px;
  padding-left: max(10vw, 160px);
  font-family: 'ImcreSoojin';
  background-attachment: fixed;
}

@font-face {
    font-family: 'ImcreSoojin';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_20-04@2.3/ImcreSoojin.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}

</style>