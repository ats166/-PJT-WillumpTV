<template>
  <div id="zz">
  <div id="signupdiv" class="container">
    <div class="row"
    id="border"
    >
      <div class="col-4">
        <h1
        style="margin-bottom:50px"
        >윌럼프에게 자기소개</h1>
        <form @submit.prevent="signUp">
          <div>
            <div class="container-fulid">
              <label for="username">아이디</label>
              <input type="text" id="username" v-model="username">
            </div >
            <div class="container-fulid">
              <label for="password1"> 비밀번호</label>
              <input type="password" id="password1" v-model="password1">
            </div>
            <div class="container-fulid">
              <label for="password2"> 비밀번호 확인</label>
              <input type="password" id="password2" v-model="password2">
            </div>
            <div class="container-fulid">
              <label for="nickname"> 별명</label>
              <input type="text" id="nickname" v-model="nickname">
            </div>
            <div class="container-fulid">
              <label for="age"> 나이 </label>
              <input type="Number" id="age" v-model="age">
            </div>
            <div class="container-fulid">
              <label for="email"> 이메일 </label>
              <input type="text" id="email" v-model="email">
            </div>
            <div class="container-fulid">
              <label > 이미지 </label>
              <input type="file" accept="image/*" @change="set_profile_image" ref="serveyImage"> <br>
            </div>
          </div>
          <input 
          style="width:80%; color: white; background-color: skyblue; border: 0cm; height: 40px;"
          onmouseover="this.style.color='black';" onmouseout="this.style.color='white';"
          type="submit" value="윌럼프와 친구되기">
        </form>
      </div>
      <div class="col-8">
        <video src="@/assets/willumpdance.mp4" style="width:100%; height:100%;" autoplay loop muted></video>
      </div>
    </div>
  </div>
</div>
</template>

<script>
export default {
  name: 'SignUpView',
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
      email: null,
      nickname: null,
      age: null,
      profile_image: null,
    }
  },
  methods: {
    set_profile_image(profile_image) {
      // console.log(profile_image.target.value,'set_profile_image')
      // this.profile_image = profile_image.target.value
      this.profile_image = this.$refs.serveyImage.files[0]
      console.log(this.profile_image)
    },
    signUp() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2
      const email = this.email
      const profile_image = this.profile_image
      const nickname = this.nickname
      const age = this.age
      console.log(this.profile_image,'image')

      const payload = {
        username : username,
        password1 : password1,
        password2 : password2,
        email : email,
        profile_image: profile_image,
        nickname : nickname,
        age : age
      }

      this.$store.dispatch('signUp', payload)
    }
  }
}
</script>

<style scoped>
#zz {
  background-image: url(@/assets/willumphappy.jpg);
  /* opacity: 0.3; */
  background-size: cover;
  height: 100vh;
}

#signupdiv {
  font-family: 'ImcreSoojin';
  padding-top:30vh;
  padding-left:10vh;
}

#imagestyle {
}

#border {
  border-radius: 20px;
  background-color: white;
}

label {
  color: black;
  height: 40px;
  text-align: left;
  font-size: 21px;
  line-height: 1.2;
}

input {
  width:60%;
  float: right;
  padding:0px;
}

@font-face {
  font-family: 'ImcreSoojin';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_20-04@2.3/ImcreSoojin.woff') format('woff');
  font-weight: normal;
  font-style: normal;
}
</style>