import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '@/router'


Vue.use(Vuex)

const API_URL = "http://127.0.0.1:8000"

export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: {
    userinfo: [],
    articles: [],
    content: [],
    recommend: [],
    token: null,
    movies: [],
    username: [],
    nickname: null,
    SearchData: null,
    genre: null,
    Vip: 0,
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    }
  },
  mutations: {
    GET_ARTICLES(state, articles){
      state.articles = articles
    },
    GET_MOVIE_DATA(state, movies){
      state.movies = movies
    },
    GET_USERNAME(state, username){
      // console.log(username,'usernameusername');
      state.username = username
    },
    // 회원가입 && 로그인

    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({name : 'MainMovieView' })
    },
    DELETE_TOKEN(state) {
      state.token = null
      state.userinfo.point
    },
    GO_LOGIN(){
      router.push({name : 'LogInView' })
    },
    GET_NICKNAME(state, nickname){
      state.userinfo = nickname.data
      state.nickname = nickname.data.nickname
    },
    SAVE_SEARCH_DATA(state, SearchData) {
      // console.log(state.SearchData, SearchData,state,'aa');
      // console.log('전송전');
      state.SearchData = SearchData
      // console.log(state.SearchData,'전송후');
    },
    WRITE_CONTENT(state, content) {
      state.content = content
    },
    SAVE_GENRE(state,genre) {
      if (genre != null){
        state.genre = genre
      }
    },
    DEFAULT_VIP(state, vip) {
      state.Vip = vip
    },
    GET_VIP(state, getvip) {
      state.Vip = getvip
    },
    GET_RECOMMEND(state, recommend) {
      // console.log(recommend,'mutationsrecommend');
      state.recommend = recommend
    }
  },
  actions: {
    getMovieData(context,genre) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v2/movies/`
      })
      .then((res) => {
        // console.log(res,genre,'get_movie')
        context.commit('GET_MOVIE_DATA', res.data)
      })
      .catch((err) => {
        // console.log(err, 'getMovieData')
      })
    },
    getRecommend(context) {
      // console.log(context,'get?');
      axios({
        method: 'get',
        url: `${API_URL}/api/v2/movies/recommend/`,
        headers: {
          Authorization: `Token ${ context.state.token }`
        }
      })
      .then((res) => {
        // console.log(res.data,'asdccscacacgetRecommend()');
        context.commit('GET_RECOMMEND', res.data)
      })
      .catch((err) => {
        // console.log(err, 'getRecommend');
      })
    },
    getArticles(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/articles/`,
        headers: {
          Authorization: `Token ${ context.state.token }`
        }
      })
        .then((res) => {
          // console.log(res, context)
          context.commit('GET_ARTICLES', res.data)
        })
        .catch((err) => {
          // console.log(err)
      })
    },
    signUp(context, payload) {
      // console.log(payload,'payload')
      // console.log(payload.profile_image)
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username: payload.username,
          password1: payload.password1,
          password2: payload.password2,
          email: payload.email,
          nickname: payload.nickname,
          age: payload.age,
          profile_image: payload.profile_image
        },
        headers: {
          'Content-Type' : 'multipart/form-data',
        }
      })
      .then((res) => {
        
        alert("윌럼프와 친구가되었습니다 \n로그인 해주세요")
        // console.log(res,'회원가입성공')
        context.commit('GO_LOGIN')
      })
      .catch((err) => {
        alert("회원가입에 실패하였습니다. \n정보를 다시 확인해 주세요")
        // console.log(err,'singup')
      })
    },
    logIn(context, payload) {
      const username = payload.username
      const password = payload.password
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username, password
          // email: payload.email,
        }
      })
        .then((res) => {
          alert("윌럼프TV에 오신것을 환영합니다 \n50p를 획득하시면 윌럼프에게 특별한 일이 일어나요")
          // console.log(res,'login')
          context.commit('SAVE_TOKEN', res.data.key)
          context.commit('GET_USERNAME', res.config.data.username)
        })
        .catch((err) => {
          alert("등록되지 않은 회원이거나 일치하지 않는 비밀번호입니다.")
          // console.log(err)
        })
    },
    logOut(context) {
      // console.log(context,'context');
      axios({
        method: 'post',
        url: `${API_URL}/accounts/logout/`,
        headers: {
          Authorization: `Token ${context.state.token}`
        }
      })
        .then(() => {
          alert("로그아웃 성공")
          // console.log('로그아웃 성공')
          context.commit('DELETE_TOKEN')
          context.commit('GO_LOGIN')
        })
        .catch((err) => {
          // console.log(`Token ${context.state.token}`);
          // console.log(err,'로그아웃실패')
      })
    },
    getNickname(context) {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/user/`,
        headers: {
          Authorization: `Token ${ context.state.token }`
        }
      })
        .then((res) => {
          // console.log(res,'로그인한 유저 정보')
          context.commit('GET_NICKNAME', res)
        })
        .catch((err) => {
          // console.log(err)
      })
    },
    WriteContent(context,payload2) {
      // console.log(payload2,'payload2');
      const content = payload2.content
      const movie_pk = payload2.movie_pk

      // console.log(content,movie_pk,'content,movie_pk');
      axios({
        method: 'post',
        url: `${API_URL}/api/v2/movies/${movie_pk}/comments/`,
        headers: {
          Authorization: `Token ${context.state.token}`
        },
        data : {
          content,movie_pk
        }
      })
      .then((res) => {
        // console.log('영화 한줄평 보내기 요청 성공', res);
        context.commit('WRITE_CONTENT', res)
      })
      .catch((err) => {
        // console.log('영화 한줄평 보내기 실패', err);
      })
    },
    SaveSearchData(context,SearchData) {
      context.commit('SAVE_SEARCH_DATA', SearchData)
    },
    SaveGenre(context,genre) {
      context.commit('SAVE_GENRE', genre)
    },
    DefaultVip(context,vip) {
      // console.log('DeafultVip');
      context.commit('DEFAULT_VIP', vip)
    },
    GetVip(context,isvip) {
      // console.log('GetVip');
      context.commit('GET_VIP', isvip)
    }
  },
  modules: {
  }
})