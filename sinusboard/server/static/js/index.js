const HTTP_RE = /http(?:s?):\/\/.*/

var app = new Vue({
  el: '#app',
  delimiters: ['[[', ']]'],
  data: {
    files: [],
    instance_id: "82faa775-298d-4c9f-9827-4dd8b91399b0"
  },
  methods: {
    playClip(uuid) {
      fetch(app.instance_id + "/play/" + uuid).then((response) => JSON.parse(response))
    },
    queueClip(uuid) {
      fetch(app.instance_id + "/queue/" + uuid).then((response) => JSON.parse(response))
    },
    uploadClip() {
      var linkText = document.getElementById("link").value
      if (!HTTP_RE.test(linkText)) {
        linkText = "ytsearch:" + linkText
      }
      document.getElementById("upload").classList.add("is-loading")
      fetch('/upload/', {
        headers: { 'Content-Type': 'application/json' },
        method: 'POST',
        body: JSON.stringify({ link: linkText })
      }).then(
        (response) => response.json()
      ).then(
        (data) => {
          app.files.unshift(data)
          document.getElementById("upload").classList.remove("is-loading")
          document.getElementById("link").value = ""
        }
      )
    },
    deleteClip(uuid) {
      fetch("/delete/" + uuid).then((response) => JSON.parse(response))
      document.getElementById(uuid).remove()
    },
    setInstanceId(uuid) {
      app.instance_id = uuid;
    }
  }
});

if ('serviceWorker' in navigator) {
  navigator.serviceWorker
    .register('./service-worker.js')
    .then(function (registration) {
      console.log('Service Worker Registered!');
      return registration;
    })
    .catch(function (err) {
      console.error('Unable to register service worker.', err);
    });
}
