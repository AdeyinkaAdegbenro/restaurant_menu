<template>
  <div class="editmenu">
    <div>
      <div v-if="!editmenustart">
        <h3>{{ menu.name }}</h3>
        <font-awesome-icon icon="fa-regular fa-pen-to-square" v-on:click="flipEditMenu" />
        <font-awesome-icon icon="fa-regular fa-trash-can" @click="deleteMenu(menu)" />
      </div>
      <div class="menu_name_control" v-else>
        <input type="text" v-model="menu.name"/>
        <font-awesome-icon icon="fa-regular fa-circle-check" @click="saveMenu(menu)" />
        <font-awesome-icon icon="fa-regular fa-circle-xmark" v-on:click="editmenustart=false"/>
      </div>
      <div class="action-buttons">
        <div class="button menuitem" v-if="!showMenuItemForm" v-on:click="showMenuItemForm=true">
          <font-awesome-icon icon="fa-regular fa-square-plus" />
          Add Menu Item
        </div>
        <div v-else>
          <label>Menu Item Name: </label>
          <input type="text" v-model="newMenuItem"/>
          <font-awesome-icon icon="fa-regular fa-circle-check" @click="createMenuItem()" />
          <font-awesome-icon icon="fa-regular fa-circle-xmark" v-on:click="showMenuItemForm=false"/>
        </div>
      </div>
      
      <div v-if="menu.menu_items.length>0">
        <h4>Menu Items</h4>
        <ul>
          <li v-for="(item, index) in menu.menu_items" :key="index">
            <div v-if="!showMenuItem[index]">
              <span>{{ item.name }}</span>
              <font-awesome-icon icon="fa-regular fa-pen-to-square" v-on:click="showMenuItem[index]=true"  />
              <font-awesome-icon icon="fa-regular fa-trash-can" @click="deleteMenuItem(item)" />
            </div>
            <div v-else>
              <input v-model="item.name" class="{{editmenuitemstart+ index}}" />
              <font-awesome-icon icon="fa-regular fa-circle-check" @click="editMenuItem(item, index)" />
              <font-awesome-icon icon="fa-regular fa-circle-xmark" v-on:click="showMenuItem[index]=false"/>
            </div>
          </li>
        </ul>
      </div>
      
      <div v-else>
        {{ menu.name }} has no Menu Items.
      </div>
    </div>

    
  </div>
</template>

<script>
import axios from 'axios';

export default {

  data () {
    return {
      menu: {'name': null},
      base_url: 'http://localhost/',
      editmenustart: false,
      showMenuItemForm: false,
      newMenuItem: "",
      showMenuItem: {},
    }
  },
  created () {
    const URL = this.base_url + 'menus/' + this.$route.params.id + '/'
    this.loadPageData(URL);
  },
  methods: {
    loadPageData (url) {
      var self = this;
      axios.get(url).then(function(response) {
        console.log(response)
        self.menu = response.data
        console.log(self.menu)
      })
      .catch(function(error) {
        console.log(error)
      })
    },
    flipEditMenu (){
      this.editmenustart = !this.editmenustart;
    },
    saveMenu () {
      this.flipEditMenu();
      var self = this
      axios.put(this.menu.url, {'name': this.menu.name}).then(function (response) {
        self.menu = response.data
      }).catch(function(error) {
        console.error(error)
      })
    },
    deleteMenu (menu) {
      var self = this;
      axios.delete(menu.url).then(function(response) {
        console.log(response)
        self.$router.push({name: 'Home'})
      }).catch(function(error) {
        console.error(error)
      })
    },
    createMenuItem () {
      var self = this;
      const url = this.base_url + "menuitems/"
      axios.post(url, {
        name: this.newMenuItem,
        menu: this.menu.url
      }).then(function(response){
        console.log(response)
        self.$router.go()
      }).catch(function(error){
        console.error(error)
      })
    },
    editMenuItem (menu_item, index) {
      var self = this;
      axios.put(menu_item.url, {
        name: menu_item.name,
        menu: this.menu.url
      }).then(function(response){
        console.log(response)
        // self.$router.go()
        self.showMenuItem[index] = false;
      }).catch(function(error){
        console.error(error)
      })
    },
    deleteMenuItem (menu_item) {
      var self = this;
      axios.delete(menu_item.url).then(function(response) {
        console.log(response)
        self.$router.go()
      }).catch(function(error) {
        console.error(error)
      })
    },
  }

}
</script>

<style scoped>

.editmenu {
  margin: 0 6em;
  border: 2em solid burlywood;
}

.editmenu h3:first-of-type {
  display: inline-block;
  padding-right: 1em;
}

.menu_name_control {
  padding: 1em 0.5em;
}

.editmenu li {
  list-style: none;
  padding: 1em 0;
}

.editmenu li span{
  padding-right: 1em;
}

.editmenu svg{
  padding: 0 0.25em;
  cursor: pointer;
}


.button.menuitem {
  width: calc(10em + 1vw);
  margin-right: 2em;
}

.action-buttons {
  display: flex;
  flex-direction: row-reverse;
}
</style>