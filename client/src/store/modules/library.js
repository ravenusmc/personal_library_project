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
  // bookById: (state) => (id) => {
  //     console.log("State Books:", state.books);
  //     const books = Array.isArray(state.books[0]) ? state.books[0] : state.books;
  //     console.log("Processed Books:", books);
  //     return books[id] || null;
  //   },
  // bookById: (state) => (id) => {
  //   const books = Array.isArray(state.books[0]) && state.books.length === 1
  //     ? state.books[0] // Flatten single nested array
  //     : state.books;
  //   return books[id] || null;
  // },
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
    console.log(value)
    let array_holder = []
    console.log(value.length)
    if (value.length === 11) {
      console.log('here')
      array_holder.push(value)
      console.log(array_holder)
      state.books = array_holder
    }else {
      console.log('not here')
      state.books = Array.isArray(value) ? value : [value];
    }
    
    console.log(state.books.length)
  },

  // setBooks(state, value) {
  //   // Always normalize to an array of books
  //   state.books = Array.isArray(value) ? value : [value];
  //   console.log("Normalized Books:", state.books);
  // },

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