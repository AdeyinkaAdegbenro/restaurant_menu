import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
/* import the fontawesome core */
import { library } from '@fortawesome/fontawesome-svg-core'

/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

/* import specific icons */
import { faTrashCan, faPenToSquare,  faXmarkCircle, faCircleCheck, faCircleXmark, faSquarePlus} from '@fortawesome/free-regular-svg-icons'

library.add(faTrashCan, faPenToSquare, faXmarkCircle, faCircleCheck, faCircleXmark, faSquarePlus)

createApp(App).component('font-awesome-icon', FontAwesomeIcon).use(router).mount('#app')
