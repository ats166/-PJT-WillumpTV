<template>
  <div id="MyPagedivA">
    <div>
      <div class="d-flex justify-content-center">
        <b-avatar size="2.5em" style="width:100px; height:100px;">
        이미지 <img :src="userimg"  alt="">
        </b-avatar>
        <div style="font-size:25px; margin-left:50px; text-align: left;">
          <p>
            아이디 : {{ userinfo.username }}
          </p>
          <p>
            별명 : {{ userinfo.nickname }}
          </p>
          <p>
            나이 : {{ userinfo.age }}
            
          </p>
        </div>
      </div>
      <b-container fluid class="bv-example-row">
        <b-row class="mb-3">
          <b-col>
            <MyArticleList
            v-for="(Article,index) in MyArticle"
            :key="index"
            :Article="Article"
            />
          </b-col>
        </b-row>
      </b-container>
    </div>
  </div>
</template>

<script>
import MyArticleList from '@/components/MyArticleList'

export default {
  name: 'MyPage',
  components: {
    MyArticleList
  },
  data() {
    return {
      userinfo: this.$store.state.userinfo,
      userimg: this.$store.state.userinfo.profile_image,

    }
  },
  created() {
    console.log(this.userinfo);
  },
  computed: {
    MyArticle() {
      console.log(this.$route.params.MyArticle,'에밋');
      return this.$route.params.MyArticle
    }
  }
}
</script>

<style>

#MyPagedivA {
  background-image: url('@/assets/userinfo.jpg');
  background-size: cover;
  padding-top:250px;
  padding-left: max(15vw, 160px);
  height: 100vh;
  font-family: 'ImcreSoojin';
  color: white;
  background-attachment: fixed;
}

@font-face {
    font-family: 'ImcreSoojin';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_20-04@2.3/ImcreSoojin.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}
</style>