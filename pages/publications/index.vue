<template>
  <div>
    <Gen>
      <!-- <h5>Finite volume schemes</h5>
      <ul class="mb-5">
        <li>Nonlinear advection-diffusion equations</li>
      </ul>-->
      <h2 class="mt-5">Publications</h2>
      <h5>Book Chapters</h5>
      <ul>
        <li v-for="x in pubs" :key="x">{{ x }}</li>
      </ul>
      <h5>Peer-reviewed articles</h5>
      <ul>
        <li v-for="x in reviewed" :key="x">{{ x }}</li>
      </ul>
      <h5>Others</h5>
      <ul>
        <li v-for="x in nonreviewed" :key="x">{{ x }}</li>
      </ul>
    </Gen>
  </div>
</template>

<script>
import Gen from '~/components/Gen'
export default {
  components: {
    Gen,
  },
  computed: {
    pubs() {
      return this.$store.state.bookchapters
    },
    reviewed() {
      return this.$store.state.journals
    },
    nonreviewed() {
      return this.$store.state.otherpubs
    },
  },
}
</script>
