# Loader

Storybook title `Components/Loader` · source `./src/components/s-loader/s-loader.stories.tsx`

Tags rendered: `<s-loader>`

Loader component to show loading state.

## Props

| Prop | Type / control | Options | Default | Description |
|---|---|---|---|---|
| `theme` | string | `default`, `default-force`, `light`, `dark` | `default` | Loader theme |
| `size` | string | `xs`, `sm`, `md`, `lg`, `xlg` | `md` | Loader size |

## Stories

### Default

Story id `components-loader--default`

![Default](../../storybook/captures/stories/loader/default.png)

Args:

```json
{
  "theme": "default",
  "size": "md"
}
```

<details><summary>Rendered markup</summary>

```html
<s-loader theme="default" size="md" role="status" class="s-loader s-loader--default md hydrated"></s-loader>
```

</details>
