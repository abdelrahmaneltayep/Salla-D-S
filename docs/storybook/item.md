# Item

Storybook title `Components/Item` · source `./src/components/s-list-item/s-list-item.stories.tsx`

Tags rendered: `<s-icon>`, `<s-list-item>`

Items are elements that can contain text, icons, avatars, images, inputs, and any other native or custom elements. Items should only be used as rows in a List with other items.

## Props

| Prop | Type / control | Options | Default | Description |
|---|---|---|---|---|
| `clickable` | boolean |  |  |  |

## Stories

### Default

Story id `components-item--default`

![Default](../../storybook/captures/stories/item/default.png)

Args:

```json
{
  "clickable": false
}
```

<details><summary>Rendered markup</summary>

```html
<div style="display: contents;"><s-list-item role="listitem" class="hydrated">List Item <s-icon slot="end" class="hydrated"></s-icon></s-list-item></div>
```

</details>
