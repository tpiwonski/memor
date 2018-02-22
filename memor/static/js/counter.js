import {store} from 'application.js';

store.registerModule('counter', {
    state: {
        count: 0
    },
    mutations: {
        increment(state) {
            state.count += 1;
        }
    },
    actions: {
        deleteNote(context, noteId) {
        }
    }
});

Vue.component('counter', {
    template: "#counter",
    computed: {
        count() {
            return this.$store.getters.notesCount;
        }
    }
});