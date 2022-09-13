module.exports = {
  env: {
    browser: true,
    es2021: true,
  },

  extends: [
    'plugin:vue/vue3-essential',
    '@vue/typescript',
    '@vue/eslint-config-airbnb-with-typescript',
  ],

  parserOptions: {
    ecmaFeatures: {
      jsx: true,
    },
    ecmaVersion: 'latest',
    sourceType: 'module',
    parser: '@typescript-eslint/parser',
  },

  rules: {
    'vue/multi-word-component-names': 'off',
    'vue/no-reserved-component-names': 'off',
    'vuejs-accessibility/anchor-has-content': 'off',
    'vuejs-accessibility/click-events-have-key-events': 'off',
    'import/no-named-as-default': 'off',
    'no-param-reassign': [
      'error',
      {
        props: true,
        ignorePropertyModificationsFor: [
          'state',
        ],
      },
    ],
    'import/extensions': [
      'error',
      'ignorePackages',
      {
        js: 'never',
        jsx: 'never',
        ts: 'never',
        tsx: 'never',
      },
    ],
  },
};
