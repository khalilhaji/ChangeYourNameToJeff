<template>
  <div id="select">
  <v-container fluid grid-list-xl>
    <v-layout wrap align-center>
        <v-select
          :items="items"
          label="State"
          solo
        ></v-select>
    </v-layout>
  </v-container>
</div>
</template>
<script>
  export default {
    name: 'Select',
    props: ['items']
  }
</script>
