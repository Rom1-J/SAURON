export type TagCreationForm = {
  name: string;
  color: string;
  note?: string;
};

export type TagUpdateForm = {
  id: string;
  name: string;
  color: string;
  note?: string;
};
