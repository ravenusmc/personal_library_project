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

	// updateBookData: ({ commit }, { payload }) => {
	// 	const path = 'http://localhost:5000/updateBook';
	// 	axios.post(path, payload)
	// 		.then((res) => {
  //       	console.log(res.data)
	// 		})
	// 		.catch((error) => {
	// 			console.log(error);
	// 		});
	// },
  updateBookData: async ({ commit }, payload) => {
    const path = 'http://localhost:5000/updateBook';
    try {
      const response = await axios.post(path, payload);
    } catch (error) {
      console.error('Error updating book data:', error);
    }
  },

	addBook: ({ commit }, { payload }) => {
    console.log(payload)
		const path = 'http://localhost:5000/addBook';
    axios.post(path, payload)
    .then((res) => {
      console.log(res.data)
    })
    .catch(( error ) => {
      console.log(error)
    });
	},

};

const mutations = {

  setBooks(state, value) {
    if (value.length === 11 || value.length === 12) {
      // Handle case where a single book is returned
      state.books = [value];
    } else {
      // Normalize to ensure books is always an array
      state.books = Array.isArray(value) ? value : [value];
    }
  },
  
  setShowBooks(state, value) {
    state.showBooks = value; 
  },

};

export default {
	namespaced: true,
	state: data,
	getters,
	actions,
	mutations,
};