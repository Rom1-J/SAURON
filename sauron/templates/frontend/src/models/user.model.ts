export interface User {
  username?: string
  email?: string
  firstName: string
  lastName: string
  language?: string
  theme?: {
    code: string
  },
  avatar?: string
}
