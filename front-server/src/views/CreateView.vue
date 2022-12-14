<!-- views/CreateView.vue -->

<template>
  <div id="creatediv" class="container-fulid">
    <h1
    style="text-align:left"
    >내가 생각하는 이 영화의 명장면은...</h1>
    <form @submit.prevent="createArticle">
      <div>
      <div class="container-fulid d-flex"
      style="margin-top:30px"
      >
        <label for="title" style="margin-right:60px">제목 : </label>
        <input style="width:47%;" type="text" id="title" v-model.trim="title">
      </div>
      <div class="container-fulid d-flex"
      style="margin-top:30px"
      >
        <label style="margin-right:60px"> 이미지: </label> 
        <input type="file" accept="image/*" @change="set_profile_image" ref="serveyImage"> <br>
      </div>
      <div class="container-fulid d-flex"
      style="margin-top:30px"
      >
        <label for="content" style="margin-right:60px">내용 : </label>
        <textarea id="content" cols="55" rows="5" v-model="content"></textarea><br>
      </div>
      <input class="container-fulid d-flex"
      style="margin-top:60px; width:47%; margin-left:120px; padding-left:20%; background-color:white; border: 0px; color:blue;"
      type="submit" id="submit" value="게시글 등록">
    </div>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = "http://127.0.0.1:8000"

export default {
  name: 'CreateView',
  data() {
    return {
      title: null,
      content: null,
      photo: this.profile_image,
    }
  },
  created() {
    this.genre = this.$route.params.genre
    console.log(this.$route.params.genre,'장르')
  },
  computed: {
  },
  methods: {
    set_profile_image(profile_image) {
      // console.log(profile_image.target.value,'set_profile_image')
      // this.profile_image = profile_image.target.value
      this.profile_image = this.$refs.serveyImage.files[0]
      console.log(this.profile_image)
    },
    getRecommend() {
      this.$store.dispatch('getRecommend')
    },
    createArticle() {
      const title = this.title
      const content = this.content
      const photo = this.profile_image
      const getgenre = this.genre
      console.log(title,content,photo,getgenre,'???');
      if (!title) {
        alert('제목을 입력해주세요')
        return
      } else if (!content) {
        alert('내용을 입력해주세요')
        return
      } else if (!photo) {
        alert('사진을 첨부해주세요')
        return
      }
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/articles/`,
        data : {
          title: title,
          content: content,
          photo: photo,
          getgenre: getgenre,
        },
        headers: {
          Authorization : `Token ${this.$store.state.token}`,
          'Content-Type' : 'multipart/form-data',
        }
      })
      .then((res) =>{
        console.log(res)
        this.getRecommend()
        alert('게시글 등록 완료! \n20p가 적립 되었습니다.')
        this.$router.push({ name: 'DiscussionBoardView' })
      })
      .catch((err) => {
        console.log(err,)
      })
    }
  }
}
</script>

<style>
#creatediv {
  color: white;
  font-family: 'ImcreSoojin';
  background-image: url(@/assets/willumphappy.jpg);
  padding-top:250px;
  padding-left: max(15vw, 160px);
  font-size:25px;
  background-size: cover;
  height: 100vh;
  width: 100vw;
}

@font-face {
  font-family: 'ImcreSoojin';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_20-04@2.3/ImcreSoojin.woff') format('woff');
  font-weight: normal;
  font-style: normal;
}
</style>
