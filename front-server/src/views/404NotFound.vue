<template>
  <div id="NOTFOUND" class="container-fluid">
    <h1>페이지를 찾을 수 없습니다.</h1>
    <h4>잘못된 접근인거 같습니다.</h4>
    <img 
    style="height:50%; width:50%;"
    src="@/assets/willumptotoro.jpg" alt="">
  </div>
</template>

<script>
export default {
    name: '404NOTFOUND',
    created() {
      console.log(window.location.href,'404')
    }
}
</script>

<style>
#NOTFOUND {
  background-image: url('@/assets/back.jpg');
  background-size: cover;
  color: white;
  padding-top:250px;
  padding-left:200px;
  height: 100vh;
  width: 100%;;
  font-family: 'ImcreSoojin';
}

@font-face {
    font-family: 'ImcreSoojin';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_20-04@2.3/ImcreSoojin.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}

</style>