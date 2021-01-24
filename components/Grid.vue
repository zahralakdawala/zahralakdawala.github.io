<template>
  <div class="tiles">
    <div
      v-for="(tile, x) in tiles"
      :key="tile.title"
      class="tile"
      :class="{ even: x % 2 === 0 }"
    >
      <div class="img" :style="{ 'background-image': `url(${tile.img})` }">
        <!-- <img :src="tile.img" /> -->
      </div>
      <div class="drop"></div>
      <div class="content">
        <h3>{{ tile.title }}</h3>
        <div class="text">
          {{ tile.text }}
        </div>
        <nuxt-link :to="link(tile.link)" class="cta">More</nuxt-link>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  props: {
    tiles: {
      required: true,
    },
    project: {
      type: Boolean,
      default: false,
    },
  },
  computed: {
    link() {
      return (link) => {
        let s = ''
        if (this.project) {
          s = 'project'
        }
        return this.$route.path + s + '/' + link + '/'
      }
    },
  },
}
</script>

<style scoped>
.img {
  background-size: cover;
  background-position: center;
  overflow: hidden;
  width: 100%;
  height: 300px;
  filter: brightness(50%);
}
.tiles {
  display: grid;
  color: white;
  grid-template-columns: repeat(auto-fill, 300px);
  width: 100%;
}
.drop {
  background: #1f82c0;
  width: 100%;
  height: 0px;
}

.tile:hover .drop {
  height: 200px;
  position: absolute;
  transition: 0.3s ease-out;
  bottom: 0px;
}

.text {
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  font-size: 13px;
  margin-bottom: 10px;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  transition: 0.5s ease;
}
.tile {
  background: #1f82c0;
  position: relative;
}
.tile:hover .content {
  bottom: 20px;
}
.tile .content {
  padding: 20px;
  position: absolute;
  bottom: 0px;
  top: unset;
  transition: 0.5s ease;
}
.content h3 {
  font-size: 1.5rem;
  letter-spacing: 0.025em;
  transition: 1s ease;
}
.content p {
  font-size: 0.9rem;
}

.even {
  background: #33b8ca;
}
.tiles img {
  width: 100%;
}
.cta:hover {
  background: #fff;
  box-shadow: inset 0 0 0 2rem #fff;
  color: #1f82c0;
}
.cta {
  font-size: 0.75em;
  line-height: 1.5rem;
  letter-spacing: 0.075em;
  background: transparent;
  border: 1px solid #1f82c0;
  color: #1f82c0;
  display: inline-block;
  font-weight: 400;
  min-width: 6rem;
  text-align: center;
  padding: 5px 10px;
  text-transform: uppercase;
  text-decoration: none;
  transition: box-shadow 0.4s, transform 1.5s, color 0.5s, background 1s;
  border-color: #fff;
  color: #fff;
}
</style>
