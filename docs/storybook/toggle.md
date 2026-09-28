# Toggle

Storybook title `Components/Toggle` · source `./src/components/s-toggle/s-toggle.stories.tsx`

Tags rendered: `<s-toggle>`

Toggle component is used to switch between two states, typically on/off or enabled/disabled. It provides a clear visual indication of the current state and allows users to toggle between states with a single interaction.

## Props

| Prop | Type / control | Options | Default | Description |
|---|---|---|---|---|
| `label` | string |  | `Toggle option` | Toggle label |
| `desc` | string |  |  | Toggle description |
| `size` | string |  |  |  |
| `layout` | string |  | `start` | Layout position, start or end |
| `checked` | boolean |  | `false` | Checked state |
| `ischecked` | boolean |  | `false` | Checked state (deprecated, and will be removed soon) |
| `wide` | boolean |  | `true` | Full width |
| `disabled` | boolean |  | `false` | Disabled state |
| `hasError` | boolean |  | `false` | Error state |
| `required` | boolean |  | `false` | Required state |
| `loading` | boolean |  | `false` | Loading state |
| `feature` | text |  | `true (omitted in HTML when unset)` | Feature guard: `true` (default), `false` to show gated UI + tag, a flag key string, or JSON for structured state (same as the `feature` attribute on the component). |
| `valueChanged` |  |  |  | Emitted when the value of the toggle switch changes. |

## Stories

### Default

Story id `components-toggle--default`

![Default](../../storybook/captures/stories/toggle/default.png)

Args:

```json
{
  "label": "Toggle option",
  "desc": "This is a description for the toggle",
  "size": "md",
  "layout": "start",
  "checked": false,
  "ischecked": false,
  "wide": true,
  "disabled": false,
  "hasError": false,
  "required": false,
  "loading": false
}
```

<details><summary>Rendered markup</summary>

```html
<s-toggle label="Toggle option" desc="This is a description for the toggle" size="md" layout="start" wide="" class="s-toggle w-full start md ltr hydrated"></s-toggle>
```

</details>

### Checked

Story id `components-toggle--checked`

![Checked](../../storybook/captures/stories/toggle/checked.png)

Args:

```json
{
  "label": "Toggle option",
  "desc": "",
  "size": "md",
  "layout": "start",
  "checked": true,
  "ischecked": false,
  "wide": true,
  "disabled": false,
  "hasError": false,
  "required": false,
  "loading": false
}
```

<details><summary>Rendered markup</summary>

```html
<s-toggle label="Toggle option" desc="" size="md" layout="start" checked="" wide="" class="s-toggle w-full start md ltr active hydrated"></s-toggle>
```

</details>

### Layout End

Story id `components-toggle--layout-end`

![Layout End](../../storybook/captures/stories/toggle/layout-end.png)

Args:

```json
{
  "label": "Toggle option",
  "desc": "This is a description for the toggle",
  "size": "md",
  "layout": "end",
  "checked": false,
  "ischecked": false,
  "wide": true,
  "disabled": false,
  "hasError": false,
  "required": false,
  "loading": false
}
```

<details><summary>Rendered markup</summary>

```html
<s-toggle label="Toggle option" desc="This is a description for the toggle" size="md" layout="end" wide="" class="s-toggle w-full end md ltr hydrated"></s-toggle>
```

</details>

### Required

Story id `components-toggle--required`

![Required](../../storybook/captures/stories/toggle/required.png)

Args:

```json
{
  "label": "Toggle option",
  "desc": "",
  "size": "md",
  "layout": "start",
  "checked": false,
  "ischecked": false,
  "wide": true,
  "disabled": false,
  "hasError": false,
  "required": true,
  "loading": false
}
```

<details><summary>Rendered markup</summary>

```html
<s-toggle label="Toggle option" desc="" size="md" layout="start" wide="" required="" class="s-toggle required w-full start md ltr hydrated"></s-toggle>
```

</details>

### Has Description

Story id `components-toggle--has-description`

![Has Description](../../storybook/captures/stories/toggle/has-description.png)

Args:

```json
{
  "label": "Toggle option",
  "desc": "This is a description for the toggle",
  "size": "md",
  "layout": "start",
  "checked": false,
  "ischecked": false,
  "wide": true,
  "disabled": false,
  "hasError": false,
  "required": false,
  "loading": false
}
```

<details><summary>Rendered markup</summary>

```html
<s-toggle label="Toggle option" desc="This is a description for the toggle" size="md" layout="start" wide="" class="s-toggle w-full start md ltr hydrated"></s-toggle>
```

</details>

### Loading

Story id `components-toggle--loading`

![Loading](../../storybook/captures/stories/toggle/loading.png)

Args:

```json
{
  "label": "Toggle option",
  "desc": "",
  "size": "md",
  "layout": "start",
  "checked": false,
  "ischecked": false,
  "wide": true,
  "disabled": false,
  "hasError": false,
  "required": false,
  "loading": true
}
```

<details><summary>Rendered markup</summary>

```html
<s-toggle label="Toggle option" desc="" size="md" layout="start" wide="" loading="" class="s-toggle w-full loading start md ltr hydrated"></s-toggle>
```

</details>

### Is Checked Property

Story id `components-toggle--is-checked-property`

![Is Checked Property](../../storybook/captures/stories/toggle/is-checked-property.png)

Args:

```json
{
  "label": "Toggle option",
  "desc": "",
  "size": "md",
  "layout": "start",
  "checked": false,
  "ischecked": true,
  "wide": true,
  "disabled": false,
  "hasError": false,
  "required": false,
  "loading": false
}
```

<details><summary>Rendered markup</summary>

```html
<s-toggle label="Toggle option" desc="" size="md" layout="start" ischecked="" wide="" class="s-toggle w-full start md ltr active hydrated" checked=""></s-toggle>
```

</details>

### Disabled

Story id `components-toggle--disabled`

![Disabled](../../storybook/captures/stories/toggle/disabled.png)

Args:

```json
{
  "label": "Toggle option",
  "desc": "",
  "size": "md",
  "layout": "start",
  "checked": false,
  "ischecked": false,
  "wide": true,
  "disabled": true,
  "hasError": false,
  "required": false,
  "loading": false
}
```

<details><summary>Rendered markup</summary>

```html
<s-toggle label="Toggle option" desc="" size="md" layout="start" wide="" disabled="" class="s-toggle disabled w-full start md ltr hydrated"></s-toggle>
```

</details>

### Disabled Checked

Story id `components-toggle--disabled-checked`

![Disabled Checked](../../storybook/captures/stories/toggle/disabled-checked.png)

Args:

```json
{
  "label": "Toggle option",
  "desc": "",
  "size": "md",
  "layout": "start",
  "checked": true,
  "ischecked": false,
  "wide": true,
  "disabled": true,
  "hasError": false,
  "required": false,
  "loading": false
}
```

<details><summary>Rendered markup</summary>

```html
<s-toggle label="Toggle option" desc="" size="md" layout="start" checked="" wide="" disabled="" class="s-toggle disabled w-full start md ltr active hydrated"></s-toggle>
```

</details>

### Has Error

Story id `components-toggle--has-error`

![Has Error](../../storybook/captures/stories/toggle/has-error.png)

Args:

```json
{
  "label": "Toggle option",
  "desc": "",
  "size": "md",
  "layout": "start",
  "checked": false,
  "ischecked": false,
  "wide": true,
  "disabled": false,
  "hasError": true,
  "required": false,
  "loading": false
}
```

<details><summary>Rendered markup</summary>

```html
<s-toggle label="Toggle option" desc="" size="md" layout="start" wide="" has-error="" class="s-toggle w-full start has-error md ltr hydrated"></s-toggle>
```

</details>

### Feature Gated

Story id `components-toggle--feature-gated`

![Feature Gated](../../storybook/captures/stories/toggle/feature-gated.png)

Args:

```json
{
  "label": "Toggle option",
  "desc": "This is a description for the toggle",
  "size": "md",
  "layout": "start",
  "checked": false,
  "ischecked": false,
  "wide": true,
  "disabled": false,
  "hasError": false,
  "required": false,
  "loading": false,
  "feature": false
}
```

<details><summary>Rendered markup</summary>

```html
<s-toggle label="Toggle option" desc="This is a description for the toggle" size="md" layout="start" wide="" feature="false" class="s-toggle is-feature w-full start md ltr hydrated"></s-toggle>
```

</details>
