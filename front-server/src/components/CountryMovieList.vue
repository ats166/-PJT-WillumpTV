<template> 
  <b-carousel-slide
  id="carouselitem"
  >
    <body
    style="width:100%; height:100%;"    >
        <b-card-header v-b-modal.modalBox class="border-1"
        @click="goMovieDetail"
        id="card-item"
        >
          <img style="height:100%; width: 100%;" :src="imgSrc" alt="">
          <!-- <h5 class="text-center font-weight-bold my-3 "> <strong> {{ movie.title }} </strong> </h5> -->
        </b-card-header>
    </body>
  </b-carousel-slide>
</template>

<script>

export default {
  name: 'CountryMovieList',
  components: {
  },
  data() {
    return {
      movieGenre : [],
    }
  },
  computed: {
    imgSrc() { 
      return 'https://image.tmdb.org/t/p/w500' + this.movie.poster_path
     }
  },
  props: {
    movie : Object,
  },
  created() {
    for(let i=0; i<this.movie.genres.length; i++) {
      this.movieGenre.push(this.movie.genres[i].name)
    }
  },
  methods: {
    goMovieDetail() {
      // console.log(this.movie.movie_id,'click')
      this.$router.push({ name: 'MovieDetailView', params: {movie_id : this.movie.movie_id }})
    }
  }
}
</script>

<style>

#carouselitem{
  position: relative;
  padding-top:950px;
  margin-left:400px;
}

#overtext {
  line-height: 1.5;
  overflow: hidden;
  word-wrap: break-word;
  display: -webkit-box;
  -webkit-line-clamp: 4;
  -webkit-box-orient: vertical;
}

</style>