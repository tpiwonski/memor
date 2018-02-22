
var store = new Vuex.Store({
    state: {}
});

document.addEventListener('DOMContentLoaded', function(){
    var application = new Vue({
        el: '#app',
        store: store    
    });
});

export {store};
