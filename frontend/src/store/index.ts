import Vue from "vue";
import Vuex from "vuex";
//import file from "@/store/file";
//import fileCheck from "@/store/fileCheck";

Vue.use(Vuex);

export default new Vuex.Store({
    state: {},
    getters: {},
    mutations: {},
    actions: {},
    modules: {/*
        file,
        fileCheck*/
    },
});

export const types = [
    {
        _id: 1,
        type: "Задача с кодом",
    },
    {
        _id: 2,
        type: "Выбор ответа",
    }
]

export const difficulties = [
    {
        _id: 0,
        difficulty: 1,
    },
    {
        _id: 1,
        difficulty: 2,
    },
    {
        _id: 2,
        difficulty: 3,
    },
]

export const answerNumbers = [
    {
        _id: 0,
        number: "Один ответ",
    },
    {
        _id: 1,
        number: "Несколько ответов"
    },
]
