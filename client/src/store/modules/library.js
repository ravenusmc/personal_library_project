import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import store from '@/store/index';


Vue.use(Vuex);

const data = {
	books: [],
};

const getters = {
	books: (state) => state.books, 
};

const actions = {

	submitSearchQueryToServer: ({ commit }, { payload }) => {
		const path = 'http://localhost:5000/getBooks';
		axios.post(path, payload)
			.then((res) => {
				console.log(res.data)
				commit('setBooks', res.data)
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

};

export default {
	namespaced: true,
	state: data,
	getters,
	actions,
	mutations,
};