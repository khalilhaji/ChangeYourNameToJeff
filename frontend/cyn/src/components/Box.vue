<template>
  <div class="box">
    <transition name="slide-fade" mode="out-in">
      <h1 :key="index" class="prefix">{{ text }}&nbsp;</h1>
    </transition>
  </div>
</template>

<script>
export default {
  name: 'Box',
  props: ['texts'],
  data() {
    return {
      index: 0
    }
  },
  computed: {
    text() {
      return this.texts[this.index];
    }
  },
  mounted() {
    this.cycle();
  },
  methods: {
    cycle: function() {
      setInterval(() => {
        this.index++;
        if (this.index >= this.texts.length)
          this.index = 0;
      }, 1000)
    }
  }
}
</script>

<style scoped>
.slide-fade-enter-active {
  transition: all 1s cubic-bezier(1.0, 0.5, 0.8, 1.0);
}
.slide-fade-leave-active {
  transition: all 1s cubic-bezier(1.0, 0.5, 0.8, 1.0);
}
.slide-fade-enter
/* .slide-fade-leave-active below version 2.1.8 */ {
  transform: translateY(1000px);
  opacity: 0;
}
.slide-fade-leave-to {
  transform: translateY(-100px);
  opacity: 0;
}

.prefix {
  color:red;
  font-family: 'Source Code Pro', monospace;
  font-size: 3em;
}
</style>
