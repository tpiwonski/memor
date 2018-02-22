import 'counter.js';
import {store} from 'application.js';
import {notesService} from 'notes.js';

store.registerModule('notesModule', {
    state: {
        notes: JSON.parse(document.getElementById('state-notes').innerText)
    },
    getters: {
        notesCount: function(state) {
            return state.notes.length;
        }
    },
    actions: {
        async deleteNote(context, noteId) {
            await notesService.deleteNote(noteId);
            context.state.notes = await notesService.getNotes()
        },
    }
});

Vue.component('notes', {
    template: "#notes",
    computed: {
        notes() {
            return this.$store.state.notesModule.notes;
        }
    },
    methods: {
        deleteNote: function(noteId) {
            this.$store.dispatch('deleteNote', noteId);
        }
    }
});
