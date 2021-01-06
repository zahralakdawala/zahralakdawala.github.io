<template>
  <div class="contact">
    <div class="contact-card">
      <div class="profilepic">
        <v-avatar size="100">
          <img src="~/assets/profilePic.jpeg" />
        </v-avatar>
      </div>
      <div class="text">
        <h4>Zahra Lakdawala</h4>
        <p>Assistant Professor at LUMS University</p>
        <v-list dense disabled class="transparent">
          <v-list-item-group color="transparent">
            <v-list-item v-for="(item, i) in items" :key="i">
              <v-list-item-icon>
                <v-icon v-text="item.icon"></v-icon>
              </v-list-item-icon>
              <v-list-item-content>
                <v-list-item-title
                  class="listItem"
                  v-text="item.text"
                ></v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list-item-group>
        </v-list>

        <hr class="dashed" />
        <div class="contacts">
          <v-row>
            <v-col v-for="x in links" :key="x.link">
              <a :href="x.link" target="__blank" style="color: transparent">
                <v-icon v-text="x.icon"></v-icon>
              </a>
            </v-col>
          </v-row>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      links: [
        {
          link: 'https://scholar.google.de/citations?user=20rjyYMAAAAJ&hl',
          icon: 'mdi-school',
        },
        { link: 'https://gitlab.com/zahra.lakdawala/', icon: 'mdi-gitlab' },
        {
          link: ' https://www.linkedin.com/in/zahra-lakdawala-57b16a73/',
          icon: 'mdi-linkedin',
        },
      ],
      items: [
        // goto for more icons https://vuetifyjs.com/en/features/icons/#material-design-icons
        {
          text: 'Scientific consultant and researcher',
          icon: 'mdi-chemical-weapon',
        },
        {
          text:
            'Steering committee member of the German national chapter of Interpore',
          icon: 'mdi-human-capacity-increase',
        },
      ],
    }
  },
}
</script>
<style>
.v-list-item__content {
  padding: 5px 0px 12px !important;
}
.listItem {
  overflow: unset !important;
  text-overflow: unset !important;
  white-space: unset !important;
  text-align: left !important;
}
</style>
<style scoped>
.contact {
  margin-top: 50px;
}
.profilepic {
  position: absolute;
  left: calc(50% - 50px);
  top: -50px;
}
.profilepic img {
  width: 100px;
  border-radius: 50%;
}
.contact-card {
  position: relative;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.1);
  border-radius: 5px;
  background: #f7f7f7;
  justify-content: center;
  display: flex;
  flex-direction: column;
}
.contact-card img {
  margin: auto;
  margin-bottom: 30px;
}
.contacts {
  font-size: 20px;
  opacity: 0.7;
}
.contacts > * {
  cursor: pointer;
  margin: 0px 12px 5px;
}
.contact h4 {
  text-align: center;
  font-weight: 600;
  opacity: 0.7;
  font-size: 20px;
}
.contact .text {
  padding: 10px 0px;
  margin-top: 50px;
  text-align: center;
  padding: 10px;
}
.text p {
  padding: 5px;
  font-size: 14px;
  opacity: 0.5;
}

hr.dashed {
  border-top: 0.5px solid #bbb;
}
</style>
