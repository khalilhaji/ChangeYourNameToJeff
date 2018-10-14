<template>
  <v-app>
  <div id="title">
    <div class="flex-grid">
      <div class="col" style="text-align:right">
        <Box v-bind:texts="texts"/>
      </div>
      <div class="col" style="text-align:center; flex:0">
        <h1 class="tilte">Change&nbsp;Your&nbsp;Name&nbsp;To&nbsp;Jeff</h1>
      </div>
      <div class="col" style="text-align: center;">
        <div class="text-xs-center">
          <v-rating v-bind:value="5" readonly></v-rating>
          <span style="font-size: 18px;"><i>I loved it!</i><br>--Jeff</span>
        </div>
      </div>
      </div>
      <div class="menu">
      <State/>
    </div>
  </div>
</v-app>
</template>

<script>
import State from './State'
import Box from './Box'
export default {
  name: 'Title',
  data() {
    return {
      texts: [
        'Should You', 'Will You', 'Can You', 'How Do You', 'Would You'
      ]
    }
  },
  components: {
    Box,
    State
  }
}
</script>

<style>
#title {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

body {
  overflow: hidden;
}

.flex-grid {
  display: flex;
  align-items: center;
}
.col {
  flex: 1;
  /* border-style: solid; */
}

.tilte {
  font-family: 'Raleway', sans-serif;
  font-weight: 800;
  font-size: 5em;
}

.menu {
  position: fixed;
  font-family: 'Raleway', sans-serif;
  font-weight: 800;
  font-size: 2em;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

</style>
