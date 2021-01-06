<template>
  <v-card class="overflow-hidden">
    <v-app-bar color="white" elevate-on-scroll>
      <!-- <v-app-bar-nav-icon></v-app-bar-nav-icon> -->
      <img class="mr-3" src="/logo.jpg" height="40" />
      <v-toolbar-title>MATH MEETS SOCIETY</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn text to="/"> Home </v-btn>
      <!--<v-btn text> About </v-btn>-->
      <v-menu offset-y>
        <template v-slot:activator="{ on, attrs }">
          <v-btn text v-bind="attrs" v-on="on">
            Resources <v-icon>mdi-chevron-down</v-icon>
          </v-btn>
        </template>
        <v-list>
          <v-list-item v-for="(item, index) in academics" :key="index">
            <v-list-item-title>
              <nuxt-link :to="item.path" tag="span" style="cursor: pointer">
                {{ item.title }}</nuxt-link
              ></v-list-item-title
            >
          </v-list-item>
        </v-list>
      </v-menu>
      <v-menu offset-y left>
        <template v-slot:activator="{ on, attrs }">
          <v-btn text v-bind="attrs" v-on="on">
            Projects <v-icon>mdi-chevron-down</v-icon>
          </v-btn>
        </template>
        <v-list>
          <v-menu offset-x left v-for="(item, index) in head" :key="index">
            <template v-slot:activator="{ on, attrs }">
              <v-btn text v-bind="attrs" v-on="on">
                <v-icon>mdi-chevron-left</v-icon>{{ item }}
              </v-btn>
            </template>
            <v-list>
              <v-list-item v-for="(itemc, i) in child(item)" :key="i + itemc">
                <nuxt-link
                  :to="'/project/' + itemc.link"
                  tag="span"
                  style="cursor: pointer"
                >
                  {{ itemc.title }}
                </nuxt-link>
              </v-list-item>
            </v-list>
          </v-menu>
        </v-list>
      </v-menu>
      <!--<v-btn text> Contact</v-btn>-->
    </v-app-bar>
  </v-card>
</template>
<script>
export default {
  data() {
    return {
      academics: [
        {
          title: 'Teaching',
          path: '/teaching',
        },
        {
          title: 'Publications',
          path: '/publications',
        },
        {
          title: 'Success Stories',
          path: '/successstories',
        },
      ],
    }
  },

  computed: {
    head() {
      const heads = new Set()
      this.$store.state.data.forEach((x) => heads.add(x.head))

      return Array.from(heads)
    },
    child() {
      return (h) => {
        const a = this.$store.state.data.filter((x) => x.head === h)
        return a.map((x) => x)
      }
    },
  },
}
</script>
