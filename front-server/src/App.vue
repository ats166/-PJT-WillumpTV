<template>
  <div id="app">
    <b-navbar
    id="mainnavbar"
    >
      <div>
        <b-navbar-brand>
          <a href="http://localhost:8080/">
            <img src="@/assets/;;.jpg" alt="" style="width:200px; height:50px; margin-left:30px;">
          </a>
        </b-navbar-brand>
      </div>
      <div class="container">
        <input type="text" placeholder="영화 검색하기" class="mx-auto"
        id="searchinput"
        @keyup.enter.prevent="search"
        v-model="inputData"
        >
        <div
        v-if="this.$store.state.token"
        >
        <div
        class="d-flex"
        >
          <div>
            <b-avatar><img :src="this.userimg"  alt=""></b-avatar>
          </div>
          <div class="justify-content-center" style="height:50px">
            <p style="color:white"> <strong>{{ this.nickname }} </strong>님 환영합니다 !</p>
            <p
            style="margin-top:-15px"
            >보유 포인트 : {{ userpoint }} p </p>
          </div>
          <div id="Mypagebtn" class="flex-row">
            <button
            class="MyPageButton"
            @click="getprofile"
              >
              내 정보
              </button>
            <p
            style="height:20px; width:60px; background-color:white;"
            class="logoutButton" @click="logOut">
            로그아웃
            </p>
            
          </div>
        </div>
        </div>
        <div
        v-else
        style= "width: 200px; height:50px">
          <router-link :to="{ name: 'LogInView' }">
          <img 
          style="height:50px; width:200px"
          src="@/assets/willumpimg.jpg">
          </router-link>
        </div>
      </div>
    </b-navbar>
    
    <div id="AD_banner"
    >
      <div id="AD_banner1">
        <a href="https://www.miricanvas.com/templates/search?keyword=%EA%B4%91%EA%B3%A0%20%EB%B0%B0%EB%84%88">
          <img src="@/assets/AD.png"
          style="width:600px; height:60px; margin-top:50px;"
          >
        </a>
        <a href="https://edu.ssafy.com/edu/main/index.do">
          <img src="@/assets/AD22.png"
          style="width:600px; height:60px; margin-top:10px;"
          >
        </a>
      </div>
      <div id="AD_banner2">
        <a href="https://mincodinglab.com/">
          <img src="@/assets/AD33.png"
          style="width:200px; height:130px; margin:50px"
          >
       </a>
      </div>
    </div>


    <div 
    v-if="isvip==0"
    class="sidebar">
      <p></p>
      <div class="dropdown"
      id="drop2"
      >
        <img src="@/assets/side1.png" id="sidebarimg"
        class="dropbtn"
        >
        <div class="dropdown-content" style="left:30%;"
        >
          <router-link onmouseover="this.style.color='red';" onmouseout="this.style.color='blue';" style="text-decoration-line: none;" :to="{ name: 'MovieCountryView', params: { code : 1 } }">한국 영화</router-link> 
          <router-link onmouseover="this.style.color='red';" onmouseout="this.style.color='azure';" style="text-decoration-line: none; color:azure;" :to="{ name: 'MovieCountryView', params: { code : 0 } }">해외 영화</router-link> 
        </div>
      </div> 
      <p></p>
      <div class="dropdown2">
        <img src="@/assets/side2.png" id="sidebarimg">
        <span class="dropbtn"></span>
        <div class="dropdown2-content" style="left:25%">
          <router-link onmouseover="this.style.color='red';" onmouseout="this.style.color='azure';" style="text-decoration-line: none; color:azure;" :to="{ name: 'MovieGenreView', params: { genre : 12, name : '모험' } }">모험</router-link> 
          <router-link onmouseover="this.style.color='red';" onmouseout="this.style.color='blue';" style="text-decoration-line: none;" :to="{ name: 'MovieGenreView', params: { genre : 14, name : '판타지' } }">판타지</router-link> 
          <router-link onmouseover="this.style.color='red';" onmouseout="this.style.color='azure';" style="text-decoration-line: none; color:azure;" :to="{ name: 'MovieGenreView', params: { genre : 16, name : '애니메이션' } }">애니메이션</router-link> 
          <router-link onmouseover="this.style.color='red';" onmouseout="this.style.color='blue';" style="text-decoration-line: none;" :to="{ name: 'MovieGenreView', params: { genre : 18, name : '드라마' } }">드라마</router-link> 
          <router-link onmouseover="this.style.color='red';" onmouseout="this.style.color='azure';" style="text-decoration-line: none; color:azure;" :to="{ name: 'MovieGenreView', params: { genre : 27, name : '공포' } }">공포</router-link> 
          <router-link onmouseover="this.style.color='red';" onmouseout="this.style.color='blue';" style="text-decoration-line: none;" :to="{ name: 'MovieGenreView', params: { genre : 28, name : '액션' } }">액션</router-link> 
          <router-link onmouseover="this.style.color='red';" onmouseout="this.style.color='azure';" style="text-decoration-line: none; color:azure;" :to="{ name: 'MovieGenreView', params: { genre : 35, name : '코미디' } }">코미디</router-link> 
          <router-link onmouseover="this.style.color='red';" onmouseout="this.style.color='blue';" style="text-decoration-line: none;" :to="{ name: 'MovieGenreView', params: { genre : 36, name : '역사' } }">역사</router-link> 
          <router-link onmouseover="this.style.color='red';" onmouseout="this.style.color='azure';" style="text-decoration-line: none; color:azure;" :to="{ name: 'MovieGenreView', params: { genre : 37, name : '서부' } }">서부</router-link> 
          <router-link onmouseover="this.style.color='red';" onmouseout="this.style.color='blue';" style="text-decoration-line: none;" :to="{ name: 'MovieGenreView', params: { genre : 53, name : '스릴러' } }">스릴러</router-link> 
          <router-link onmouseover="this.style.color='red';" onmouseout="this.style.color='azure';" style="text-decoration-line: none; color:azure;" :to="{ name: 'MovieGenreView', params: { genre : 80, name : '범죄' } }">범죄</router-link> 
          <router-link onmouseover="this.style.color='red';" onmouseout="this.style.color='blue';" style="text-decoration-line: none;" :to="{ name: 'MovieGenreView', params: { genre : 99, name : '다큐멘터리' } }">다큐멘터리</router-link> 
          <router-link onmouseover="this.style.color='red';" onmouseout="this.style.color='azure';" style="text-decoration-line: none; color:azure;" :to="{ name: 'MovieGenreView', params: { genre : 878, name : 'SF' } }">SF</router-link> 
          <router-link onmouseover="this.style.color='red';" onmouseout="this.style.color='blue';" style="text-decoration-line: none;" :to="{ name: 'MovieGenreView', params: { genre : 9648, name : '미스터리' } }">미스터리</router-link> 
          <router-link onmouseover="this.style.color='red';" onmouseout="this.style.color='azure';" style="text-decoration-line: none; color:azure;" :to="{ name: 'MovieGenreView', params: { genre : 10402, name : '음악' } }">음악</router-link> 
          <router-link onmouseover="this.style.color='red';" onmouseout="this.style.color='blue';" style="text-decoration-line: none;" :to="{ name: 'MovieGenreView', params: { genre : 10749, name : '로맨스' } }">로맨스</router-link> 
          <router-link onmouseover="this.style.color='red';" onmouseout="this.style.color='azure';" style="text-decoration-line: none; color:azure;" :to="{ name: 'MovieGenreView', params: { genre : 10751, name : '가족 영화' } }">가족 영화</router-link> 
          <router-link onmouseover="this.style.color='red';" onmouseout="this.style.color='blue';" style="text-decoration-line: none;" :to="{ name: 'MovieGenreView', params: { genre : 10752, name : '전쟁' } }">전쟁</router-link> 
          <router-link onmouseover="this.style.color='red';" onmouseout="this.style.color='azure';" style="text-decoration-line: none; color:azure;" :to="{ name: 'MovieGenreView', params: { genre : 10770, name : 'TV 영화' } }">TV 영화</router-link> 
        </div>
      </div> 
      <p></p>
      <div class="dropdown3">
        <img src="@/assets/side3.png" id="sidebarimg">
        <div class="dropdown3-content" style="left:20%">
          <router-link onmouseover="this.style.color='red';" onmouseout="this.style.color='blue';" style="text-decoration-line: none;" :to="{ name: 'DiscussionBoardView' }">명장면 게시판</router-link> 
        </div>
      </div>
      <div style="margin-top:16px">
        <img src="@/assets/side4.png" id="sidebarimg">
      </div>

      <video src="@/assets/nonvipdance.mp4" autoplay loop muted style="width:150px; position:relative;"></video>
    </div>



    <div 
    v-else
    class="sidebar">
      <p></p>
      <div class="dropdown"
      id="drop2"
      >
        <img src="@/assets/vipside1.png" id="sidebarimg"
        class="dropbtn"
        >
        <!-- <span class="dropbtn">국가별 영화</span> -->
        <div class="dropdown-content" style="left:30%;"
        >
          <router-link onmouseover="this.style.color='red';" onmouseout="this.style.color='blue';" style="text-decoration-line: none;" :to="{ name: 'MovieCountryView', params: { code : 1 } }">한국 영화</router-link> 
          <router-link onmouseover="this.style.color='red';" onmouseout="this.style.color='azure';" style="text-decoration-line: none; color:azure;" :to="{ name: 'MovieCountryView', params: { code : 0 } }">해외 영화</router-link> 
        </div>
      </div> 
      <p></p>
      <div class="dropdown2">
        <img src="@/assets/vipside2.png" id="sidebarimg">
        <span class="dropbtn"></span>
        <div class="dropdown2-content" style="left:25%">
          <router-link onmouseover="this.style.color='red';" onmouseout="this.style.color='azure';" style="text-decoration-line: none; color:azure;" :to="{ name: 'MovieGenreView', params: { genre : 12, name : '모험' } }">모험</router-link> 
          <router-link onmouseover="this.style.color='red';" onmouseout="this.style.color='blue';" style="text-decoration-line: none;" :to="{ name: 'MovieGenreView', params: { genre : 14, name : '판타지' } }">판타지</router-link> 
          <router-link onmouseover="this.style.color='red';" onmouseout="this.style.color='azure';" style="text-decoration-line: none; color:azure;" :to="{ name: 'MovieGenreView', params: { genre : 16, name : '애니메이션' } }">애니메이션</router-link> 
          <router-link onmouseover="this.style.color='red';" onmouseout="this.style.color='blue';" style="text-decoration-line: none;" :to="{ name: 'MovieGenreView', params: { genre : 18, name : '드라마' } }">드라마</router-link> 
          <router-link onmouseover="this.style.color='red';" onmouseout="this.style.color='azure';" style="text-decoration-line: none; color:azure;" :to="{ name: 'MovieGenreView', params: { genre : 27, name : '공포' } }">공포</router-link> 
          <router-link onmouseover="this.style.color='red';" onmouseout="this.style.color='blue';" style="text-decoration-line: none;" :to="{ name: 'MovieGenreView', params: { genre : 28, name : '액션' } }">액션</router-link> 
          <router-link onmouseover="this.style.color='red';" onmouseout="this.style.color='azure';" style="text-decoration-line: none; color:azure;" :to="{ name: 'MovieGenreView', params: { genre : 35, name : '코미디' } }">코미디</router-link> 
          <router-link onmouseover="this.style.color='red';" onmouseout="this.style.color='blue';" style="text-decoration-line: none;" :to="{ name: 'MovieGenreView', params: { genre : 36, name : '역사' } }">역사</router-link> 
          <router-link onmouseover="this.style.color='red';" onmouseout="this.style.color='azure';" style="text-decoration-line: none; color:azure;" :to="{ name: 'MovieGenreView', params: { genre : 37, name : '서부' } }">서부</router-link> 
          <router-link onmouseover="this.style.color='red';" onmouseout="this.style.color='blue';" style="text-decoration-line: none;" :to="{ name: 'MovieGenreView', params: { genre : 53, name : '스릴러' } }">스릴러</router-link> 
          <router-link onmouseover="this.style.color='red';" onmouseout="this.style.color='azure';" style="text-decoration-line: none; color:azure;" :to="{ name: 'MovieGenreView', params: { genre : 80, name : '범죄' } }">범죄</router-link> 
          <router-link onmouseover="this.style.color='red';" onmouseout="this.style.color='blue';" style="text-decoration-line: none;" :to="{ name: 'MovieGenreView', params: { genre : 99, name : '다큐멘터리' } }">다큐멘터리</router-link> 
          <router-link onmouseover="this.style.color='red';" onmouseout="this.style.color='azure';" style="text-decoration-line: none; color:azure;" :to="{ name: 'MovieGenreView', params: { genre : 878, name : 'SF' } }">SF</router-link> 
          <router-link onmouseover="this.style.color='red';" onmouseout="this.style.color='blue';" style="text-decoration-line: none;" :to="{ name: 'MovieGenreView', params: { genre : 9648, name : '미스터리' } }">미스터리</router-link> 
          <router-link onmouseover="this.style.color='red';" onmouseout="this.style.color='azure';" style="text-decoration-line: none; color:azure;" :to="{ name: 'MovieGenreView', params: { genre : 10402, name : '음악' } }">음악</router-link> 
          <router-link onmouseover="this.style.color='red';" onmouseout="this.style.color='blue';" style="text-decoration-line: none;" :to="{ name: 'MovieGenreView', params: { genre : 10749, name : '로맨스' } }">로맨스</router-link> 
          <router-link onmouseover="this.style.color='red';" onmouseout="this.style.color='azure';" style="text-decoration-line: none; color:azure;" :to="{ name: 'MovieGenreView', params: { genre : 10751, name : '가족 영화' } }">가족 영화</router-link> 
          <router-link onmouseover="this.style.color='red';" onmouseout="this.style.color='blue';" style="text-decoration-line: none;" :to="{ name: 'MovieGenreView', params: { genre : 10752, name : '전쟁' } }">전쟁</router-link> 
          <router-link onmouseover="this.style.color='red';" onmouseout="this.style.color='azure';" style="text-decoration-line: none; color:azure;" :to="{ name: 'MovieGenreView', params: { genre : 10770, name : 'TV 영화' } }">TV 영화</router-link> 
        </div>
      </div> 
      <p></p>
      <div class="dropdown3">
        <img src="@/assets/vipside3.png" id="sidebarimg">
        <div class="dropdown3-content" style="left:20%">
          <router-link onmouseover="this.style.color='red';" onmouseout="this.style.color='blue';" style="text-decoration-line: none;" :to="{ name: 'DiscussionBoardView' }">명장면 게시판</router-link>           
        </div>
      </div>
      <div style="margin-top:16px">
        <img src="@/assets/vipside4.png" id="sidebarimg">
      </div>
      <video src="@/assets/vipdance.mp4" autoplay loop muted style="width:150px; position:relative;"></video>
    </div>


    <router-view/>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = "http://127.0.0.1:8000"


  export default {
    data() {
      return {
        inputData : null,
        LogState : false,
        MyArticle : null,
      }
    },
    computed:{
    userimg() {
      return this.$store.state.userinfo.profile_image
    },
    userpoint() {
      return this.$store.state.userinfo.point
    },
    nickname() {
      return this.$store.state.nickname
    },
    isLogin() {
      return this.$store.getters.isLogin
    },
    isvip() {
      return this.$store.state.Vip
    },
    },
    created() {
      // console.log(this.$store.state.token,'login상태 TOKEN');
      // console.log(this.$store.state.Vip,'나는 vip인가');
      this.Vip()
      this.$store.dispatch('getNickname',1)
      
    },
    methods: {
      Vip() {
      if (this.userpoint >= 50) {
          this.$store.dispatch('GetVip',1)
        } else {
          this.$store.dispatch('DefaultVip',0)
        }
      },
      getprofile() {
        // console.log('실행되나',this.$store.state.userinfo.username);
        axios ({
          method:'get',
          url: `${API_URL}/accounts/profile/${this.$store.state.userinfo.username}/`
        })
        .then((res) => {
          // console.log(res,'프로필가즈아')
          // console.log(res.data.articles,'프로필가즈아2')
          this.MyArticle = res.data.articles
          this.$router.push({ name: 'MyPage', params: {MyArticle: this.MyArticle}})
        })
        .catch((err) => {
          console.log(err,'프로필실패')
        })
      },
      logOut() {
        this.$store.dispatch('logOut')
      },
      search() {
        this.$store.dispatch('SaveSearchData',this.inputData)
        this.$router.push({ name: 'SearchMovie', params: {SearchData: this.inputData}})
        this.inputData = ''
      },
    }
  }
</script>

<style scoped>

#Mypagebtn{
  color:black;
}

div {
  font-family: 'ImcreSoojin';
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  transition: all s ease;
}

.sidebar{
    min-width : 150px;
    background: hsl(0, 0%, 0%);
    position: fixed;
    width: 10vw;
    height: 100vh;
    padding-top: 100px;
    transition: all 0.5s ease;
    /* list-style: none;
    box-sizing: border-box; */
    font-family: 'Open Sans', sans-serif;
    z-index: 15;
}

#sidebarimg {
  width:150px;
  height:80px;
  margin-top:-16px;
}

#sidebarname {
  font-weight: bold;
}

#searchinput {
  width:35vw
}

#mainnavbar {
  background: hsl(0, 0%, 0%);
  position: fixed;
  width: 100%;
  z-index: 100;
  min-height: 50px;
  height: 75px;
  
}

#AD_banner {
  /* padding-top: 75px;
  padding-left: 200px; */
  display: flex;
  flex-direction: row;
  background: rgba(0,0,0,0.5);
  position: fixed;
  /* top : 8vh; */
  padding-left: max(20%, 30vw);
  padding-top: 30px;
  z-index: 2;
  height:220px; 
  width:100%;
}

#AD_banner1 {
  display: flex;
  flex-direction: column;
}


.dropdown:hover .dropdown-menu {
    display: block;
    margin-top: 40px;
    
}

.dropdown{
  position : relative;
  display : inline-block;
  transition: all 2s ease;
}


.dropdown-content{
  display : none;
  position : absolute;
  z-index : 1;
  font-family: 'ImcreSoojin';
  
}

.dropdown-content a{
  display : block;
}

.dropdown:hover .dropdown-content {
  display: block;
  
}

.dropdown:hover {
  margin-bottom: 50px;
  transition: all 0.5s ease;
}

.dropdown2:hover .dropdown2-menu {
    display: block;
    margin-top: 40px;
    
}

.dropdown2{
  position : relative;
  display : inline-block;
  transition: all 2s ease;
}


.dropdown2-content{
  display : none;
  position : absolute;
  z-index : 1;
  font-family: 'ImcreSoojin';
}


.dropdown2-content a{
  display : block;
}

.dropdown2:hover .dropdown2-content {
  display: block;  
}
.dropdown2:hover {
  margin-bottom: 460px;
  transition: all 1s ease;

}

.dropdown3:hover .dropdown3-menu {
    display: block;
    margin-top: 50px;
    
}

.dropdown3{
  position : relative;
  display : inline-block;
  transition: all 1s ease;
}


.dropdown3-content{
  display : none;
  position : absolute;
  z-index : 1;
  font-family: 'ImcreSoojin';
}

.dropdown3-content a{
  display : block;
}

.dropdown3:hover .dropdown3-content {
  display: block;
  
}

.dropdown3:hover {
  margin-bottom: 25px;
  transition: all 0.5s ease;
}
@font-face {
    font-family: 'ImcreSoojin';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_20-04@2.3/ImcreSoojin.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}

</style>