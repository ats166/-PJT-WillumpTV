import Vue from 'vue'
import VueRouter from 'vue-router'
import CreateView from '@/views/CreateView'
import DetailView from '@/views/DetailView'
import SignUpView from '@/views/SignUpView'
import LogInView from '@/views/LogInView'
import MovieCountryView from '@/views/MovieCountryView'
import MovieDetailView from '@/views/MovieDetailView'
import NotFound from '@/views/404NotFound'
import MovieGenreView from '@/views/MovieGenreView'
import DiscussionBoardView from '@/views/DiscussionBoardView'
import SearchMovie from '@/views/SearchMovie'
import MainMovieView from '@/views/MainMovieView'
import MyPage from '@/views/MyPage'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'MainMovieView',
    component: MainMovieView
  },

  {
    path: '/create',
    name: 'CreateView',
    component: CreateView
  },

  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView
  },

  {
    path: '/login',
    name: 'LogInView',
    component: LogInView
  },

  {
    path: 'article/:id',
    name: 'DetailView',
    component: DetailView,
  },
  {
    path: '/country/:code',
    name: 'MovieCountryView',
    component: MovieCountryView,
  },
  {
    path: '/Movies/:movie_id',
    name: 'MovieDetailView',
    component: MovieDetailView
  },
  {
    path:'/Genre/:genre',
    name: 'MovieGenreView',
    component: MovieGenreView
  },
  {
    path:'/DiscussionBoardView',
    name: 'DiscussionBoardView',
    component : DiscussionBoardView
  },
  {
    path:'/MyPage',
    name:'MyPage',
    component: MyPage
  },
  {
    path:"/:SearchData",
    name:'SearchMovie',
    component: SearchMovie
  },
  {
    path: '*',
    name: '404NOTFOUND',
    component: NotFound
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
