<template>
<b-carousel-slide
  id="carouselitem"
  >
    <body
    style="width:100%; height:100%;"
    >
      <b-card-header v-b-modal.modalBox class="border-1"
        @click="goMovieDetail"
        id="card-item"
        >
          <img style="height:100%; width: 100%;" :src="imgSrc" alt="">
      </b-card-header>
    </body>
  </b-carousel-slide>
</template>

<script>

export default {
  name : "GenreMovieList",
  data() {
    return {
      movieGenre : [],
    }
  },
  components: {
  },
  props: {
    movie : Object,
  },
  methods: {
    goMovieDetail() {
      console.log(this.movie.movie_id,'click')
      this.$router.push({ name: 'MovieDetailView', params: {movie_id : this.movie.movie_id }})
    }
  },
  created() {
    for(let i=0; i<this.movie.genres.length; i++) {
      this.movieGenre.push(this.movie.genres[i].name)
      // this.movieGenre = this.movie.genres[i].name
    }
  },
  computed: {
    imgSrc() {
      return 'https://image.tmdb.org/t/p/w500' + this.movie.poster_path
    }
  }
}
</script>

<style>

#carouselitem {
  width:600px;
  height:840px;
  position: relative;
  padding-top:0px;
}
</style>