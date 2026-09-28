# Icon

Storybook title `Components/Icon` · source `./src/components/s-icon/s-icon.stories.tsx`

Tags rendered: `<s-icon>`

Use Icon component to display `Hugeicons` or `Sallaicons-light` within a shadowDOM component, such as table, button, uploader, etc when needed.

## Props

| Prop | Type / control | Options | Default | Description |
|---|---|---|---|---|
| `icon` | string |  | `sicon-light-salla` | Icon class name representing the icon to be displayed, you can use `Hugeicons` or `Sallaicons-light` like `hgi-stroke hgi-tick-02`, `s-light-tick-02` or `sicon-light-salla` |
| `size` | string |  | `1rem` | icon size, you can use rem or px, we prefer rem, default is 1rem |

## Stories

### Default

Story id `components-icon--default`

![Default](../../storybook/captures/stories/icon/default.png)

Args:

```json
{
  "icon": "sicon-light-salla",
  "size": "1rem"
}
```

<details><summary>Rendered markup</summary>

```html
<s-icon icon="sicon-light-salla" size="1rem" class="hydrated"></s-icon>
```

</details>
