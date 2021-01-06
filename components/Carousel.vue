<template>
  <v-carousel
    v-if="images.length > 0"
    cycle
    height="400"
    hide-delimiter-background
    show-arrows-on-hover
  >
    <v-carousel-item v-for="(slide, i) in images" :key="i" :src="slide">
    </v-carousel-item>
  </v-carousel>
</template>
<script>
export default {
  data() {
    return {
      dummy: ['hi', 'aa', 5, 8, 79, 8],
    }
  },
  props: {
    images: {
      default() {
        return []
      },
    },
  },
}
</script>
