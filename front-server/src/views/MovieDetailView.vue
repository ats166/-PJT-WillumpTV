<template>
  <div id="Moviedetail">
    <div>
      <img :src="backdrop"
      id="Detailimg"
      class="container-fluid"
      >
    
      <DetailYoutubeView
      :movie_title="movie_title"
      />
      <div id="Detailinfo">
        <div
        style="text-align:left; color:white;"
        >
          <h1>{{ movie_title }}} </h1>

          <hr style="width:95%; color: black;">

          <h2>소개</h2>
          
          <h6 v-if="movie_overview"
          style="color:black"
          >{{movie_overview}} </h6>

          <h6 v-else
          style="color:black"
          > 등록된 영화 정보가 없습니다.</h6>
          <hr style="width:95%; color: black;">
        </div>
        <div
        class="row"
        >

        <h2
        style="margin-top:50px; color:black;"
        >출연진</h2>
        <Carousel 
        :per-page="8"
        >
          <slide
          v-for="(actor, index) in actors"
          :key="index"
          >
          <DetailActorList
          :actor="actor"          
          />
          </slide>
        </Carousel>
        </div>
        <hr style="width:95%; color: black;">
        <div
        style="text-align:left; color:white;"
        >
        <router-link
        v-if="movie"
        :to="{ name: 'CreateView', params: { genre: this.movie.genres[0] } }"
        style="font-size:20px; margin-bottom:30%; margin-left:40%;"
        > 내가 생각하는 이 영화의 명장면 공유하기
        </router-link>
        <hr style="width:95%; color: black;">
          <h1 style="margin-top:10%">영화 한줄 평 </h1>
          <div>
            <div>
            <b-avatar>
              <img src="@/assets/profile/기륜.png" alt="">
            </b-avatar>
            <span
            style="margin-left:20px; font-size:19px; color:black;"
            > <strong> GeumGiryun </strong></span> 
            </div>
            <p
            style="margin-left:60px; color:black;"
            >
              <span> 여자친구랑 같이 보기 좋은 영화 </span>
            </p>
          </div>
          <div>
            <div>
            <b-avatar>
              <img src="@/assets/profile/영석.png" alt="">
            </b-avatar>
            <span
            style="margin-left:20px; font-size:19px; color:black;"
            > <strong> 고0석 </strong></span> 
            </div>
            <p
            style="margin-left:60px; color:black;"
            >
              <span> 씁... 난 이 영화 별로던데 </span>
            </p>
          </div>
          <div>
            <div>
            <b-avatar>
              <img src="@/assets/profile/태신.png" alt="">
            </b-avatar>
            <span
            style="margin-left:20px; font-size:19px; color:black;"
            > <strong> Park </strong></span> 
            </div>
            <p
            style="margin-left:60px; color:black;"
            >
              <span> 이 영화 재밌다는 사람 특) 상남자임 </span>
            </p>
          </div>
          <div v-if="comments">
            <DetailComment
            v-for="(comment,index) in comments"
            :key="index"
            :comment="comment"
            />
          </div>
          <input 
          style="height:50%; width:70%; margin-bottom:3%"
          type="textarea" v-model="content"
          placeholder="해당 영화에 대한 한줄 평을 남겨주세요."
          @keyup.enter.prevent="Writecontent"
          >
        </div>
        <hr style="width:95%; color: black; ">
      </div>
    </div> 
  </div>
</template>

<script>
import axios from 'axios'
import DetailActorList from '@/components/DetailActorList'
import DetailYoutubeView from '@/components/DetailYoutubeView'
import DetailComment from '@/components/DetailComment'
import { Carousel, Slide } from 'vue-carousel';


const API_URL = "http://127.0.0.1:8000"

export default {
    name: "MovieDetailView",
    data() {
      return {
        movie_title : this.$route.params.movie_title,
        movie_overview : null,
        movie : null,
        backdrop : null,
        movie_id : this.$route.params.movie_id,
        actors : null,
        comments : null,
        content: [],
        image_path: this.$store.state.userinfo.profile_image,
      }
    },
    created() {
      this.getMovieDetail()
      this.getActorDetail()
      this.getCommentList()
      console.log(this.$store.state.movies,'영화정보');
      // this.getyoutube()
    },
    components: {
      DetailActorList,
      DetailYoutubeView,
      Carousel,
      Slide,
      DetailComment,
    },
    computed: {
      videoSrc() {
      return `http://www.youtube.com/embed/${this.selectedVideo.id.videoId}`
      },
    },
    methods: {
      getMovieDetail() {
        axios ({
          method:'get',
          url: `${API_URL}/api/v2/movies/${this.$route.params.movie_id}`
        })
        .then((res) => {
          this.movie = res.data
          this.movie_title = res.data.title
          this.movie_overview = res.data.overview
          this.backdrop = "https://image.tmdb.org/t/p/original" + res.data.backdrop_path
          // console.log(res.data);
        })
        .catch((err) => {
          console.log(err, 'getMovieDetail')
        })
      },
      getActorDetail() {
        axios ({
          method:'get',
          url: `${API_URL}/api/v2/actors/${this.$route.params.movie_id}`
        })
        .then((res) => {
          // console.log(res)
          this.actors = res.data
        })
        .catch((err) => {
          console.log(err,'actor')
        })
      },
      getCommentList() {
        axios ({
          method:'get',
          url: `${API_URL}/api/v2/movies/comments/${this.$route.params.movie_id}`
        })
        .then((res) => {
          console.log(res,'asdasd');
          this.comments = res.data
        })
        .catch((err) => {
          console.log(err)
        })
      },
      Writecontent() {
        console.log(this.content)
        const content = this.content
        const movie_pk = this.movie_id

        const payload2 = {
          content: content,
          movie_pk: movie_pk,
        }
        this.$store.dispatch('WriteContent',payload2)
        this.content = ''
        alert('영화 한줄 평 등록 완료 \n 10p가 적립 되었습니다!')
        this.$router.push({ name: 'MovieDetailView', params: {movie_id: this.movie_id}}).catch(error => {
        if(error.name === "NavigationDuplicated" ){
        location.reload();
        }
      })
    },
  }
}

</script>

<style>


#Moviedetail {
  padding-top: 10px;
  padding-left: 10px;
  font-family: 'establishRoomNo703OTF';

  /* padding-left: max(10%, 160px); */
}


#Detailimg {
  animation: fadeout 3s;
  margin-left:-50%;
  padding: 0;
  width: 100vw;
  height: 100vh;
  opacity: 0.3;
  /* position: relative; */
  float: left;
  position: fixed;
}

@keyframes fadeout {
	from {
		opacity: 1;
    z-index: 10;
	}
	to {
		opacity: 0.4;
    z-index: 10;
	}
}

#Detailinfo {
  padding-left: 12%;
  padding-top: 105vh;
  position: absolute;
  width: 95%;
}

@font-face {
    font-family: 'establishRoomNo703OTF';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2112@1.0/establishRoomNo703OTF.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}
/*
#bgimg {
  padding-top: 250px;
  padding-left: max(15vw, 160px);
  background-image: url("https://image.tmdb.org/t/p/original/bQXAqRx2Fgc46uCVWgoPz5L5Dtr.jpg");
  background-size: 100% 100%;
  height: 1000px;
  position:relative ;
  opacity: 0.5;
}

#video {
  position: absolute;
  left: 30vw;
} */

</style>