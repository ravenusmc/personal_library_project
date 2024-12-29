import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import cheerio from 'cheerio';
import store from '@/store/index';


Vue.use(Vuex);

const data = {
  books: [],
  showBooks: true,
};

const getters = {
	books: (state) => {
	  // Ensure books are always an array of arrays
	  return Array.isArray(state.books[0]) ? state.books : state.books.length ? [state.books] : [];
	},
  showBooks: (state) => state.showBooks,
  bookById: (state) => (id) => state.books[id],
  };

const actions = {

	submitSearchQueryToServer: ({ commit }, { payload }) => {
		const path = 'http://localhost:5000/getBooks';
		axios.post(path, payload)
			.then((res) => {
				if (res.data.length === 0 || res.data == null) {
          commit('setShowBooks', false)
          commit('setBooks', res.data)
				} else {
					commit('setBooks', res.data)
          commit('setShowBooks', true)
				}
			})
			.catch((error) => {
				console.log(error);
			});
	},

	updateBookData: ({ commit }, { payload }) => {
    console.log('here')
    console.log(payload)
		const path = 'http://localhost:5000/updateBook';
		axios.post(path, payload)
			.then((res) => {
        console.log(res.data)
			})
			.catch((error) => {
				console.log(error);
			});
	},

};

const mutations = {

	setBooks(state, value) {
		state.books = value;
	},

  setShowBooks(state, value) {
    state.showBooks = value; 
  }

};

export default {
	namespaced: true,
	state: data,
	getters,
	actions,
	mutations,
};