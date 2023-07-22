<template>
  <h2><a href="/">Restaurant Menu</a></h2>
  <router-view/>
</template>

<style>

h2 {
  text-decoration: underline;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}


#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
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

h2 a:visited {
  color: initial;
}
</style>
