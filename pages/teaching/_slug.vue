<template>
  <Gen :images="page.carousel"
    ><h3 class="text-h4 mb-4 mt-5">{{ page.title }}</h3>
    <div class="overview">
      <p class="text-overline">Overview</p>
      <p>{{ page.text }}</p>
    </div>
    <Panel :data="page" />
  </Gen>
</template>
<script>
import Gen from '~/components/Gen'
import Panel from '~/components/Panel'
export default {
  components: {
    Gen,
    Panel,
  },
  computed: {
    page() {
      return this.$store.state.teaching.data.filter(
        (x) => x.link === this.$route.params.slug
      )[0]
    },
  },
}
</script>
<style scoped>
.text-h4 {
  margin: 0 !important;
}
.text-overline {
  margin-bottom: 4px !important;
}
.overview {
  padding-left: 10px;
}
</style>
