<template>
  <div>
    <Gen :images="page.carousel">
      <nuxt-content :document="doc" />
    </Gen>
  </div>
</template>

<script>
/* eslint-disable */
import Gen from '~/components/Gen'
export default {
  async asyncData({ $content, app, params }) {
    const doc = await $content('projects/' + (params.slug || 'index')).fetch()
    return { doc }
  },
  computed: {
    page() {
      return this.$store.state.data.filter(
        (x) => x.link === this.$route.params.slug
      )[0]
    },
  },
  components: {
    Gen,
  },
}
</script>
