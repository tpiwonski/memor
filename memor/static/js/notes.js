
// function doRequest(options) {
//     return new Promise((resolve, reject) => {
//         let xhr = new XMLHttpRequest();
//         xhr.addEventListener('load', e => {
//             resolve(xhr);
//         });
//         xhr.addEventListener('error', e => {
//             reject(e);
//         });
//         xhr.addEventListener('abort', e => {
//             reject(e);
//         });
//         xhr.open(options.method, options.url);
//         xhr.setRequestHeader('Content-Type', 'application/json');
//         xhr.responseType = 'json';
//         xhr.send(options.data);
//     });
// }

class Service {
    ajax(options) {
        return new Promise((resolve, reject) => {
            let xhr = new XMLHttpRequest();
            xhr.addEventListener('load', e => {
                resolve(xhr.response);
            });
            xhr.addEventListener('error', e => {
                reject(e);
            });
            xhr.addEventListener('abort', e => {
                reject(e);
            });
            xhr.open(options.method, options.url);
            xhr.setRequestHeader('Content-Type', 'application/json');
            xhr.responseType = 'json';
            xhr.send(options.data);
        });
    }
}

class NotesService extends Service {

    deleteNote(noteId) {
        return this.ajax({
            url: `/api/notes/${noteId}`, 
            method: 'DELETE'
        })
    }

    getNotes() {
        return this.ajax({
            url: "/api/notes",
            method: "GET"
        })
    }
}

const notesService = new NotesService();

export {notesService};
