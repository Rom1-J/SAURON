import { createI18n } from 'vue-i18n';
import en from './en';

const messages = {
  en,
};

const index = createI18n({
  locale: 'en',
  legacy: false,
  messages,
});

export default index;
