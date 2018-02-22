const path = require('path');

module.exports = {
    entry: {
        application: './static/js/application.js',
        list_notes: './static/js/list_notes.js'
    },
    output: {
        path: path.resolve(__dirname, './static/dist'),
        filename: '[name].js'
    },
    resolve: {
        modules: [
            path.resolve('./static/js'),
        ],
    }
};
