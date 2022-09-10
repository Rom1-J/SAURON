import { createI18n } from 'vue-i18n';
import en from './en';

const messages = {
  en,
};

const index = createI18n({
  locale: 'en',
  messages,
});

export default index;
