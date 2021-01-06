<template>
  <v-carousel cycle height="400" hide-delimiter-background show-arrows-on-hover>
    <v-carousel-item
      v-for="(slide, i) in dummy"
      :key="i"
      :src="'https://picsum.photos/800/900?random=' + i"
    >
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
}
</script>
