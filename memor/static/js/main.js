application(function(modules) {
    var state = {};
    modules.forEach(function(m){
        Object.getOwnPropertyNames(m.state).forEach(function(name) {
            state[name] = m.state[name];
        })
    });

    var store = new Vuex.Store({
        modules: state
    });

    var app = new Vue({
        el: '#app',
        store: store    
    });
});