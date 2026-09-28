# Breadcrumbs

Storybook title `Components/Breadcrumbs` · source `./src/components/s-breadcrumbs/s-breadcrumbs.stories.tsx`

Tags rendered: `<s-breadcrumbs>`

A breadcrumb is a navigation component that allows users to track their location within a website or application.

## Props

| Prop | Type / control | Options | Default | Description |
|---|---|---|---|---|
| `items` | string |  | `[]` | Breadcrumbs items |
| `loading` | boolean |  | `false` | Specifies if the breadcrumbs are in a loading state |
| `maxVisibleItems` | number |  | `5` | Maximum number of visible items, the rest will be hidden in a dropdown |
| `isOnClick` | boolean |  | `false` | Specifies if the breadcrumbs are clickable, if true, the breadcrumbClick event will be emitted |
| `breadcrumbClick` |  |  |  | Emitted when a breadcrumb is clicked. Provides the clicked breadcrumb value. |

## Stories

### Default

Story id `components-breadcrumbs--default`

![Default](../../storybook/captures/stories/breadcrumbs/default.png)

Args:

```json
{
  "items": "[{\"id\":0,\"label\":\"Home\",\"route\":\"/\"},{\"id\":1,\"label\":\"Category\",\"route\":\"/category\"},{\"id\":2,\"label\":\"Subcategory\",\"route\":\"/subcategory\"}]",
  "loading": false,
  "maxVisibleItems": 5,
  "isOnClick": false
}
```

<details><summary>Rendered markup</summary>

```html
<s-breadcrumbs items="[{&quot;id&quot;:0,&quot;label&quot;:&quot;Home&quot;,&quot;route&quot;:&quot;/&quot;},{&quot;id&quot;:1,&quot;label&quot;:&quot;Category&quot;,&quot;route&quot;:&quot;/category&quot;},{&quot;id&quot;:2,&quot;label&quot;:&quot;Subcategory&quot;,&quot;route&quot;:&quot;/subcategory&quot;}]" max-visible-items="5" class="s-breadcrumbs ltr hydrated"></s-breadcrumbs>
```

</details>

### Array Format

Story id `components-breadcrumbs--array-format`

![Array Format](../../storybook/captures/stories/breadcrumbs/array-format.png)

Args:

```json
{
  "items": [
    {
      "id": 0,
      "label": "Home",
      "route": "/"
    },
    {
      "id": 1,
      "label": "Category",
      "route": "/category"
    },
    {
      "id": 2,
      "label": "Subcategory",
      "route": "/subcategory"
    }
  ],
  "loading": false,
  "maxVisibleItems": 5,
  "isOnClick": false
}
```

<details><summary>Rendered markup</summary>

```html
<s-breadcrumbs items="[{&quot;id&quot;:0,&quot;label&quot;:&quot;Home&quot;,&quot;route&quot;:&quot;/&quot;},{&quot;id&quot;:1,&quot;label&quot;:&quot;Category&quot;,&quot;route&quot;:&quot;/category&quot;},{&quot;id&quot;:2,&quot;label&quot;:&quot;Subcategory&quot;,&quot;route&quot;:&quot;/subcategory&quot;}]" max-visible-items="5" class="s-breadcrumbs ltr hydrated"></s-breadcrumbs>
```

</details>

### Max Visible Items

Story id `components-breadcrumbs--max-visible-items`

![Max Visible Items](../../storybook/captures/stories/breadcrumbs/max-visible-items.png)

Args:

```json
{
  "items": "[{\"id\":0,\"label\":\"Home\",\"route\":\"/\"},{\"id\":1,\"label\":\"Products\",\"route\":\"/products\"},{\"id\":2,\"label\":\"Categories\",\"route\":\"/categories\"},{\"id\":3,\"label\":\"Electronics\",\"route\":\"/electronics\"},{\"id\":4,\"label\":\"Phones\",\"route\":\"/phones\"},{\"id\":5,\"label\":\"Smartphones\",\"route\":\"/smartphones\"},{\"id\":6,\"label\":\"iPhone\",\"route\":\"/iphone\"}]",
  "maxVisibleItems": 3,
  "loading": false,
  "isOnClick": false
}
```

<details><summary>Rendered markup</summary>

```html
<s-breadcrumbs items="[{&quot;id&quot;:0,&quot;label&quot;:&quot;Home&quot;,&quot;route&quot;:&quot;/&quot;},{&quot;id&quot;:1,&quot;label&quot;:&quot;Products&quot;,&quot;route&quot;:&quot;/products&quot;},{&quot;id&quot;:2,&quot;label&quot;:&quot;Categories&quot;,&quot;route&quot;:&quot;/categories&quot;},{&quot;id&quot;:3,&quot;label&quot;:&quot;Electronics&quot;,&quot;route&quot;:&quot;/electronics&quot;},{&quot;id&quot;:4,&quot;label&quot;:&quot;Phones&quot;,&quot;route&quot;:&quot;/phones&quot;},{&quot;id&quot;:5,&quot;label&quot;:&quot;Smartphones&quot;,&quot;route&quot;:&quot;/smartphones&quot;},{&quot;id&quot;:6,&quot;label&quot;:&quot;iPhone&quot;,&quot;route&quot;:&quot;/iphone&quot;}]" max-visible-items="3" class="s-breadcrumbs ltr hydrated"></s-breadcrumbs>
```

</details>

### Loading

Story id `components-breadcrumbs--loading`

![Loading](../../storybook/captures/stories/breadcrumbs/loading.png)

Args:

```json
{
  "items": "[{\"id\":0,\"label\":\"Home\",\"route\":\"/\"},{\"id\":1,\"label\":\"Category\",\"route\":\"/category\"},{\"id\":2,\"label\":\"Subcategory\",\"route\":\"/subcategory\"}]",
  "loading": true,
  "maxVisibleItems": 5,
  "isOnClick": false
}
```

<details><summary>Rendered markup</summary>

```html
<s-breadcrumbs items="[{&quot;id&quot;:0,&quot;label&quot;:&quot;Home&quot;,&quot;route&quot;:&quot;/&quot;},{&quot;id&quot;:1,&quot;label&quot;:&quot;Category&quot;,&quot;route&quot;:&quot;/category&quot;},{&quot;id&quot;:2,&quot;label&quot;:&quot;Subcategory&quot;,&quot;route&quot;:&quot;/subcategory&quot;}]" loading="" max-visible-items="5" class="s-breadcrumbs ltr loading hydrated"></s-breadcrumbs>
```

</details>

### With Click Handler

Story id `components-breadcrumbs--with-click-handler`

![With Click Handler](../../storybook/captures/stories/breadcrumbs/with-click-handler.png)

Args:

```json
{
  "items": "[{\"id\":0,\"label\":\"Home\",\"route\":\"/\"},{\"id\":1,\"label\":\"Category\",\"route\":\"/category\"},{\"id\":2,\"label\":\"Subcategory\",\"route\":\"/subcategory\"}]",
  "isOnClick": true,
  "loading": false,
  "maxVisibleItems": 5
}
```

<details><summary>Rendered markup</summary>

```html
<s-breadcrumbs items="[{&quot;id&quot;:0,&quot;label&quot;:&quot;Home&quot;,&quot;route&quot;:&quot;/&quot;},{&quot;id&quot;:1,&quot;label&quot;:&quot;Category&quot;,&quot;route&quot;:&quot;/category&quot;},{&quot;id&quot;:2,&quot;label&quot;:&quot;Subcategory&quot;,&quot;route&quot;:&quot;/subcategory&quot;}]" max-visible-items="5" is-on-click="true" class="s-breadcrumbs ltr hydrated"></s-breadcrumbs>
```

</details>
