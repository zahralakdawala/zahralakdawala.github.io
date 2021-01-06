<template>
  <div>
    <NavBar></NavBar>
    <v-container>
      <Carousel :images="images"></Carousel>
      <v-row>
        <v-col cols="8">
          <slot class="main"></slot>
        </v-col>

        <v-col cols="3" offset="1">
          <Contact class="contact"></Contact>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>
<script>
import NavBar from '~/components/NavBar'
import Carousel from '~/components/Carousel'
import Contact from '~/components/ContactCard'
export default {
  components: {
    NavBar,
    Carousel,
    Contact,
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
<style scoped>
.main {
  margin-right: 100px;
}
.spacer {
  width: 80px;
}
</style>
