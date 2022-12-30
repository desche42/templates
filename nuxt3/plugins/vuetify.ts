import { createVuetify } from 'vuetify'
import { mdi, aliases as allAliases } from 'vuetify/iconsets/mdi-svg';

const aliases = {
  /* Only used icon aliases here */
  menu: allAliases.menu,
  close: allAliases.close,
  info: allAliases.info,
};

export default defineNuxtPlugin((nuxtApp) => {

  const vuetify = createVuetify({
    icons: {
      defaultSet: 'mdi',
      aliases,
      sets: { mdi }
    }
  });

  nuxtApp.vueApp.use(vuetify);

  if (!process.server) 
  {
    console.log('❤️ Initialized Vuetify 3 -', vuetify);
  }
});
