export type UserRegisterForm = {
  username: string,
  password1: string,
  password2?: string,
};

export type UserLoginForm = {
  username: string,
  password: string,
};

export type UserAPIResponse = {
  avatar?: string,
  email: string,
  first_name: string,
  language: string,
  last_name: string,
  theme: string,
  url: string,
  username: string,
};

export type UserUpdateForm = {
  first_name?: string
  last_name?: string
  language?: string
  theme?: string
  avatar?: Blob
};
