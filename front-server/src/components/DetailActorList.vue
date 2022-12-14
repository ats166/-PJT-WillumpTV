<template>
  <div>
    <!-- {{actor}} -->
    <img 
    v-if="this.actor.profile_path!=null"
    :src="profile"
    style="width:160px; height:260px;"
    >
    <img 
    v-else
    src="@/assets/willumphi.png" 
    style="width:160px; height:260px;">
    <!-- <img   
    v-else
    :src="profile"
    style="width:100%"
    > -->
    <h4>{{ actor.name }}</h4>
    <h5>{{ actor.character }}</h5>
  </div>
</template>

<script>
export default {
    name: 'ActorList',
    props: {
      actor : Object,
    },
    data() {
      return {
        profile : "https://image.tmdb.org/t/p/original" + this.actor.profile_path
      }
    }
  }
</script>

<style>

</style>