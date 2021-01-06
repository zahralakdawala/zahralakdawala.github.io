<template>
  <div>
    <v-expansion-panels inset>
      <v-expansion-panel v-for="mod in data.modules" :key="mod.title">
        <v-expansion-panel-header>{{ mod.title }}</v-expansion-panel-header>
        <v-expansion-panel-content>
          <v-row>
            <v-col v-for="x in mod.content" :key="x.title + x.link">
              <v-card max-width="330" elevation="0">
                <div class="d-flex flex-no-wrap justify-space-between">
                  <v-avatar class="ma-3" size="80" tile>
                    <v-img :src="img(x)"></v-img>
                  </v-avatar>
                  <v-card-text>
                    <div>{{ x.type }}</div>
                    <p class="text-h6">{{ x.title }}</p>
                    <a class="link" :href="x.link" target="_blank">Link</a>
                    <div class="text--primary">
                      <!-- relating to or dependent on charity; charitable.<br />
                      "an eleemosynary educational institution." -->
                    </div>
                  </v-card-text>
                </div>
              </v-card>
            </v-col>
          </v-row>
        </v-expansion-panel-content>
      </v-expansion-panel>
    </v-expansion-panels>
  </div>
</template>
<script>
export default {
  props: {
    data: {
      required: true,
    },
  },
  computed: {
    img() {
      return (x) => {
        if (x.type === 'PDF') {
          return 'https://i.stack.imgur.com/Zpt8n.jpg'
        } else if (x.type === 'Video') {
          return 'https://icons.iconarchive.com/icons/paomedia/small-n-flat/1024/file-video-icon.png'
        }
        return 'https://cdn.iconscout.com/icon/premium/png-512-thumb/unknown-file-1892800-1603210.png'
      }
    },
  },
}
</script>
<style scoped>
.text-h6 {
  font-size: 15px !important;
  margin: 0px;
}
.link {
  text-decoration: none;
}
</style>
