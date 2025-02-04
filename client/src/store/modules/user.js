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

	setUpUser: ({ commit }, { payload }) => {
		const path = 'http://localhost:5000/setUpUser';
		axios.post(path, payload)
			.then((res) => {
				router.push({ name: 'login'})
			})
			.catch((error) => {
				console.log(error);
			});
	},


	loginUser: ({ commit }, { payload }) => {
		console.log("action!")
		const path = 'http://localhost:5000/login';
		axios.post(path, payload)
			.then((res) => {
				if (res.data.login_flag) {
					// Not sure if I'll set up a user at all
					// commit('session/setUserObject', res.data.user, { root: true })
					commit('setLoginFlag', res.data.login_flag);
					router.push({ name: 'missing' });
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

};

export default {
	namespaced: true,
	state: data,
	getters,
	actions,
	mutations,
};