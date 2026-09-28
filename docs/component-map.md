# Figma ↔ Storybook component map

How the sections of the Figma page *Main Components (Full)* relate to the Twilight Storybook components and `s-*` tags.
Storybook components not listed against a Figma section: `Accordion`, `Design System/Colors`, `Design System/Shadow And Roundness`, `Design System/Typography`, `Modal`, `Progress Bar`, `Tooltip`.

| Figma section | Storybook component(s) | Main tag | Note |
|---|---|---|---|
| [Header](components/header.md) | — |  | app shell header; no public Storybook component |
| [Bread crumb](components/bread-crumb.md) | [Breadcrumbs](storybook/breadcrumbs.md) | `<s-breadcrumbs>` |  |
| [Button](components/button.md) | [Button](storybook/button.md), [ButtonsGroup](storybook/buttonsgroup.md) | `<s-button>` | Figma Variant→`theme`, Appearance→`outlined`/link, Size→`size`, Layout→`layout` |
| [check Box](components/check-box.md) | [Checkbox](storybook/checkbox.md) | `<s-checkbox>` |  |
| [radio Buttton](components/radio-buttton.md) | [Radio](storybook/radio.md) | `<s-radio>` | radioImage/radioColor are radio variants |
| [Toggle](components/toggle.md) | [Toggle](storybook/toggle.md) | `<s-toggle>` |  |
| [Loader](components/loader.md) | [Loader](storybook/loader.md), [Skeleton](storybook/skeleton.md) | `<s-loader>` |  |
| [Status](components/status.md) | [Tag](storybook/tag.md) | `<s-tag>` | status badge = tag with dot |
| [Avatar](components/avatar.md) | [Avatar](storybook/avatar.md) | `<s-avatar>` |  |
| [Alertbox](components/alertbox.md) | [AlertBox](storybook/alertbox.md) | `<s-alert-box>` |  |
| [Inputs](components/inputs.md) | [Input](storybook/input.md), [Textarea](storybook/textarea.md), [Select](storybook/select.md), [Telephone Input](storybook/telephone-input.md), [OTP](storybook/otp.md), [Qty](storybook/qty.md), [Uploader](storybook/uploader.md), [LingualField](storybook/lingualfield.md), [Editor](storybook/editor.md), [Tags Input](storybook/tags-input.md), [ColorPicker](storybook/colorpicker.md), [IconPicker](storybook/iconpicker.md), [Range Slider](storybook/range-slider.md), [Rate](storybook/rate.md), [Calendar](storybook/calendar.md) | `<s-input>` | one Figma section covers every field type |
| [searchbar](components/searchbar.md) | [Input](storybook/input.md) | `<s-input>` | search variant |
| [Maps](components/maps.md) | [Maps](storybook/maps.md) | `<s-maps>` |  |
| [Side menu](components/side-menu.md) | [Tabs](storybook/tabs.md) | `<s-tabs-group>` | vertical tabs |
| [More Menu](components/more-menu.md) | [Dropdown](storybook/dropdown.md) | `<s-dropdown>` |  |
| [Drop Down List](components/drop-down-list.md) | [Dropdown](storybook/dropdown.md), [Select](storybook/select.md), [Item](storybook/item.md) | `<s-dropdown>` | list items = `s-list-item` |
| [Table](components/table.md) | [Table](storybook/table.md) | `<s-table>` |  |
| [Steps](components/steps.md) | — |  | no public Storybook component |
| [Learn More](components/learn-more.md) | [Panel](storybook/panel.md) | `<s-panel>` | panel with media |
| [Icons/Filled](components/icons-filled.md) | [Icon](storybook/icon.md) | `<s-icon>` | see icons/ |
| [Icons/Outline](components/icons-outline.md) | [Icon](storybook/icon.md) | `<s-icon>` | see icons/ |
| [Illustrations Collection](components/illustrations-collection.md) | [Placeholder](storybook/placeholder.md) | `<s-placeholder>` | empty states |
| [Action Buttons](components/action-buttons.md) | [ButtonsGroup](storybook/buttonsgroup.md) | `<s-buttons-group>` |  |
| [Products Management](components/products-management.md) | [Table](storybook/table.md), [Panel](storybook/panel.md) |  | page composition |
| [Header Primary Tabs](components/header-primary-tabs.md) | — |  | app shell |
| [Flag](components/flag.md) | [Telephone Input](storybook/telephone-input.md) | `<s-tel-input>` | country flags |
| [Social media icons](components/social-media-icons.md) | [Icon](storybook/icon.md) | `<s-icon>` |  |
| [Illustration](components/illustration.md) | [Placeholder](storybook/placeholder.md) | `<s-placeholder>` |  |
