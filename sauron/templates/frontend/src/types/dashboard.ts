export type DashboardItemType = {
  label: string,
  icon?: string,
  to?: object,
  items?: DashboardItemType[],
  visible?: boolean | Function,
  command?: Function,
  disabled?: boolean,
  url?: string,
};

export type DashboardMenuItemEvent = {
  originalEvent: PointerEvent,
  item: DashboardItemType
};
