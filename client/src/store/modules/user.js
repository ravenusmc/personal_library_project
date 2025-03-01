import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import router from '../../router';

Vue.use(Vuex);

const data = {
	userNotFound: false,
	passwordNoMatch: false,
	loginFlag: false,
};

const getters = {
	userNotFound: (state) => state.userNotFound,
	passwordNoMatch: (state) => state.passwordNoMatch,
	loginFlag: (state) => state.loginFlag,
};

const actions = {

	signUpUser: ({ commit }, { payload }) => {
		const path = 'http://localhost:5000/signUpUser';
		axios.post(path, payload)
			.then((res) => {
				router.push({ name: 'login'})
			})
			.catch((error) => {
				console.log(error);
			});
	},

	loginUser: ({ commit }, { payload }) => {
		const path = 'http://localhost:5000/login';
		axios.post(path, payload)
			.then((res) => {
				if (res.data) {
					console.log(res.data)
					commit('setLoginFlag', res.data.login_flag);
					router.push({ name: 'library' });
				}
				commit('setNoPasswordMatch', res.data.Password_no_match);
				commit('setUserNotFound', res.data.Not_found);
			})
			.catch((error) => {
				console.log(error);
			});
	},

	logout: ({ commit }) => {
		commit('setUserNotFound', false);
		commit('setNoPasswordMatch', false);
		commit('setLoginFlag', false);
	},

};

const mutations = {

	setLoginFlag(state, value) {
		state.loginFlag = value;
	},

	setNoPasswordMatch(state, value) {
		state.passwordNoMatch = value 
	}, 

	setUserNotFound(state, value) {
		state.userNotFound
	},

};

export default {
	namespaced: true,
	state: data,
	getters,
	actions,
	mutations,
};