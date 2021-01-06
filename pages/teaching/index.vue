<template>
  <Gen :images="$store.state.teaching.carousel"
    ><h3 class="text-h4 mb-4 mt-5">Teaching</h3>

    <Grid :tiles="teaching"
  /></Gen>
</template>
<script>
import Gen from '~/components/Gen'
import Grid from '~/components/Grid'
export default {
  components: {
    Gen,
    Grid,
  },
  computed: {
    teaching() {
      return this.$store.state.teaching.data
    },
  },
}
</script>
