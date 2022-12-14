<template>
  <div id="logindiv" 
  class="container-fluid "
  style="width:100vw; height:100vh;">
    <video src="@/assets/willumpsky.mp4" class="videoplay" autoplay loop ></video>
    
    <!-- <h1>LogIn Page</h1> -->
    <!-- <form @submit.prevent="logIn">
      <label for="username">아이디 : </label>
      <input type="text" id="username" ><br>
      <p></p>
      <label for="password"> 패스워드 : </label>
      <input type="password" id="password" ><br>

      <input type="submit" value="logIn">
    </form>
    <h5>아직 회원이 아니시라고요 ?</h5>
    <span>지금 즉시 </span>
    <router-link :to="{ name: 'SignUpView' }"
      style="text-decoration-line: none;"
      >여기</router-link> <span>를 눌러서 윌럼프TV 회원되기</span> -->

    <div>
      <form @submit.prevent="logIn">
          <h1 style="color:white; font-family: 'HBIOS-SYS';" onmouseover="this.style.color='red';" onmouseout="this.style.color='azure';"> Willump TV</h1>
          <h1 style="color:white; font-family: 'HBIOS-SYS';" onmouseover="this.style.color='blue';" onmouseout="this.style.color='azure';"> Login</h1>
          <input type="text" placeholder="아이디" class="in" v-model="username">
          <p></p>
          <input type="password" placeholder="비밀번호" class="in" v-model="password">
          <p></p>
          <input type="submit" id="btn" value="logIn"><br>
      </form>
      <h5>아직 윌럼프와 친구가 아니시라고요 ?</h5>
      <span>지금 즉시 </span>
      <router-link :to="{ name: 'SignUpView' }"
        style="text-decoration-line: none;"
        >여기</router-link> <span>를 눌러서 윌럼프와 친구가 되어보세요!</span>
  </div>
  </div>
</template>

<script>
export default {
  name: 'LogInView',
  data() {
    return {
      username: null,
      password: null,
    }
  },
  created() {
    this.$store.dispatch('DefaultVip',0)
  },
  methods: {
    logIn() {
      const username = this.username
      const password = this.password

      const payload = {
        username: username,
        password: password,
      }
      
      this.$store.dispatch('logIn', payload)
    }
  }
}
</script>

<style scoped>
  /* background ; */
#logindiv {
  font-family: 'ImcreSoojin';
  padding-top:30vh;
  padding-left:10vh;
}

.videoplay { 
  position: fixed;
  top: 0;
  left: 0;
  height: 100vh;
  width: 110vw;
  z-index: -1;
  opacity: 0.3;
  }

@font-face {
  font-family: 'ImcreSoojin';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_20-04@2.3/ImcreSoojin.woff') format('woff');
  font-weight: normal;
  font-style: normal;
}

@font-face {
    font-family: 'HBIOS-SYS';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2207-01@1.0/HBIOS-SYS.woff2') format('woff2');
    font-weight: normal;
    font-style: normal;
}
/* body {
    background-color: #1BBC9B;
} */

/* div {
    margin: auto;
    width: 300px;
    background-color: #EEEFF1;
    border-radius: 5px;
    text-align: center;
    padding: 20px;
} */

input {
    width: 30%;
    padding: 10px;
    box-sizing: border-box;
    border-radius: 5px;
    border: none;
}

.in {
    margin-bottom: 10px;
}

#btn {
    background-color: #1BBC9B;
    margin-bottom: 30px;
    color: white;
}

#btn:hover {
  background-color: white;
  color: #1BBC9B;
}

a {
    text-decoration: none;
    color: #9B9B9B;
    font-size: 12px;
}
</style>