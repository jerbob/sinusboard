var app = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data: {},
    methods: {
        playClip(uuid) {
            fetch("/play/" + uuid).then((response) => {JSON.parse(response)})
        }
    }
});
