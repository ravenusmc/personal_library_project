import Vue from 'vue'
import Vuex from 'vuex'
import library from './modules/library.js';
import user from './modules/user';

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    library,
    user,
  },
});
