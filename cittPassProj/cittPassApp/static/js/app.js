import { createApp } from 'vue'
const app = createApp(App)
new Vue({
    el: '#app',
    data: {
        message: '¡Hola desde Vue!'
    },
    mounted() {
        console.log('Vue se ha cargado correctamente.', this.message);
    }
});

new Vue({
    el: '#app2',
    data: {
      message: '¡Hola desde Vue!'
    }
  });