<template>
  <body>
    <div>
      <b-card-header v-b-modal.modalBox class="border-1 rounded-3 jb-wrap"
      @click="goMovieDetail"
      >
      <div class="jb-image">
       <img class="ratio rounded-3" :src="imgSrc" alt="">
      </div>
      <div class="jb-text">
        <div class="jb-text-table">
					<div class="jb-text-table-row">
						<div class="jb-text-table-cell">
        <h5 class="text-center font-weight-bold my-3"
        id="moviedata">
        <strong> {{ movie.title }} </strong> </h5>
            </div>
					</div>
				</div>
      </div> 
    </b-card-header>
    </div>
      
  </body>
  </template>
  
  <script>
  export default {
    name: 'MainMovieList',
    data() {
      return {
        imgSrc : 'https://image.tmdb.org/t/p/w500' + this.movie.poster_path,
        movieGenre : [],
      }
    },
    props: {
      movie : Object,
    },
    created() {
      // console.log(this.movie);
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

#moviedata{
  color : rgba(0,0,0,0)
}

#overtext {
  line-height: 1.5;
  overflow: hidden;
  word-wrap: break-word;
  display: -webkit-box;
  -webkit-line-clamp: 4;
  -webkit-box-orient: vertical;
}

.jb-wrap {
  position: relative;
}
.jb-wrap img {
  height: 100%;
  width: 100%;
  /* vertical-align: middle; */
}
.jb-text {
  position: absolute;
  top: 30%;
  width: 100%;
  height: 100%;
}
.jb-text-table {
  display: table;
  width: 100%;
  height: 100%;
}
.jb-text-table-row {
  display: table-row;
}
.jb-text-table-cell {
  display: table-cell;
  vertical-align: middle;
  z-index:8;
}
.jb-text p {
  margin: 0px 40px;
  padding: 10px;
  background-color: rgba(0,0,0,1);
  text-align: center;
}

.jb-wrap:hover {
  transform: scale(1.2);
  z-index: 10;
  transition: ease 0.2s;
  overflow :visible;
  /* position:absolute; */
}

.jb-wrap:hover #moviedata{
  z-index:20;
  display: inline;
  color:white;
  font-size:25px;
  transition: ease 1s;
}

</style>