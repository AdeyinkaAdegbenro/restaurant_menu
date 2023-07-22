<template>
  <div class="home">
    <div class="actions"><div @click="createMenu()" class="button">Add new</div></div>
    <ul>
      <li v-for="(menu, index) in menus" v-bind:key="index">
        <h4>
          {{menu.name}}
          <!-- <font-awesome-icon icon="fa-regular fa-trash-can" /> -->
          <font-awesome-icon icon="fa-regular fa-pen-to-square" v-on:click="loadEditMenuPage(menu.id)" />
        </h4>
        <ul>
          <li v-for="(item, ind) in menu.menu_items" :key="ind">
            {{ item.name }}
          </li>
        </ul>
      </li>
    </ul>
    <div v-if="previous_page" @click="loadPageData(previous_page)" class="button">Previous</div>
    <div v-if="next_page" @click="loadPageData(next_page)" class="button">Next</div>
  </div>
  <div class="popup">
    <div class="actions">
      <font-awesome-icon @click="closePopup" icon="fa-regular fa-xmark-circle" size="2xl" style="color: rgb(169, 5, 5)" />
    </div>
    <div class="create">
      <form @submit.prevent="submitMenu">
        <label><h3>Add Menu Name</h3></label>
        <input type="text" v-model="menu_name"/>
        <button class="button">Submit</button>
      </form>
    </div>
    <div class="created">
      <font-awesome-icon icon="fa-regular fa-circle-check" />
        <p>Menu has been created successfully</p>
        <div class="bottom-actions">
          <button class="button" @click="loadEditMenuPage(popCreatedMenuId)">Create Menu Items for {{ menu_name }}</button>
          <button class="danger button" @click="closePopup">Close</button>
        </div>
    </div>

  </div>
</template>

<script>
import axios from 'axios';
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Home',
  data() {
    return {
      menu_name: '',
      menus: [],
      BASE_URL: 'http://localhost',
      next_page: null,
      previous_page: null,
      popCreatedMenuId: '',
    }
  },
  mounted () {
    this.loadPageData();
    
  },
  methods: {
    loadPageData (url) {
      if (url) {
        var URL = url
      } else {
        URL = this.BASE_URL + '/menus/';
      }
      var self = this;
      axios.get(URL).then(function(response) {
        self.menus = response.data.results
        self.next_page = response.data.next
        self.previous_page = response.data.previous
        console.log(self.menus)
      })
      .catch(function(error) {
        console.log(error)
      })
    },
    loadEditMenuPage (id) {
      if (id == '') {return}
      this.$router.push({path: `/menus/${id}`});
    },
    createMenu () {
      const popup = document.getElementsByClassName('popup');
      popup[0].style.display = 'block';
    },
    submitMenu () {
      const URL = this.BASE_URL + '/menus/'
      var self = this;
      axios.post(URL, {'name': this.menu_name}).then(
        function(response) {
          console.log('Created new Menu ' + self.menu_name, response)
          self.popCreatedMenuId = response.data.id
          self.loadPageData();
          this.$router.go();
      }).catch((error)=> console.log(error));

      const form_div = document.getElementsByClassName('create');
      const created_div = document.getElementsByClassName('created');
      form_div[0].style.display = 'none';
      created_div[0].style['display'] = 'block';
      
    },
    closePopup () {
      const popup = document.getElementsByClassName('popup');
      popup[0].style.display = 'none';
      this.resetPopup()
    },
    resetPopup () {
      this.menu_name = '';
      const form_div = document.getElementsByClassName('create');
      const created_div = document.getElementsByClassName('created');
      form_div[0].style.display = 'block';
      created_div[0].style['display'] = 'none';
    }
  }
}
</script>

<style scoped>

.home {
  padding: 1em;
  margin: 0 6em;
  border: 2em solid burlywood
}

.actions {
  display: flex;
  flex-direction: row-reverse;
}

.button {
  background-color: lightseagreen; 
  font-size: 1.1 rem;
  padding: 0.5rem;
  border: 1px solid lightseagreen;
  border-radius: 5%;
  color: white;
  user-select: none;
  cursor: pointer;
}

h4 {
  margin-bottom: 0.5rem;
}

h4 svg {
  cursor: pointer;
}

ul ul {
  padding: 0rem 2rem;
}
 
li {
  list-style: none;
}

.popup {
  border: 1px solid black;
  width: 50vmin;
  height: 50vmin;
  position: absolute;
  z-index: 100;
  top: 50%;
  left: 50%;
  transform: translate(-50%,-50%);
  border-radius: 8px;
  display: none;
  text-align: center;
  background-color: #ffffff;
}

.popup .create{
  margin-top: 20%;
}

.popup .create label {
  display: block;
}

.popup .create .button {
  margin: 0 0.125rem;
}

.popup .created {
  display: none;
}

.button.danger{
  background-color: rgb(123, 3, 3);
}

.button.block {
  display: block;
}

.bottom-actions {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
}

</style>