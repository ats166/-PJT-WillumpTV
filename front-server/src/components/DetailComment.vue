<template>
  <div>
    <div>
    <b-avatar>
      <img :src="userimg" alt="">
    </b-avatar>
    <span
    style="margin-left:20px; font-size:19px; color:black;"
    > <strong>{{ comment?.nickname }} </strong></span> 
    <!-- <span>{{ comment?.updated_at}}</span> -->
    </div>
    <p
    style="margin-left:60px; color:black;"
    >
      <span>{{ comment?.content }}</span>
    </p>
  </div>
</template>

<script>
export default {
  name: "DetailComment",
  data() {
    return{
      userinfo: this.comment.user,
      userimg: null,
    }
  },
  props: {
    comment : Object,
  },
  created() {
    // console.log(this.comment,'comment');
    // console.log(this.userinfo.profile_image,'유저인포');
    // console.log(this.$store.state.userinfo,'DB');
    // this.$store.userinfo.
    this.userimg= this.$store.state.userinfo.profile_image
  }
}
</script>

<style>

</style>