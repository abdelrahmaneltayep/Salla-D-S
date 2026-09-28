# ColorPicker

Storybook title `Components/ColorPicker` · source `./src/components/s-color-picker/s-color-picker.stories.tsx`

Tags rendered: `<s-color-picker>`, `<s-icon>`

A color picker field component that allows users to select colors using a color input. It supports various states and configurations for different use cases.

## Props

| Prop | Type / control | Options | Default | Description |
|---|---|---|---|---|
| `value` | string |  | `#000000` | Field value |
| `required` | boolean |  | `false` | Required state |
| `disabled` | boolean |  | `false` | Disabled state |
| `hasError` | boolean |  | `false` | Error state |
| `noLabel` | boolean |  | `false` | Label-less field ( required in certain cases) |
| `noBorder` | boolean |  | `false` | Border-less field ( required in certain cases) |
| `colorChanged` |  |  |  | Emitted when the color changes. |

## Stories

### Default

Story id `components-colorpicker--default`

![Default](../../storybook/captures/stories/colorpicker/default.png)

Args:

```json
{
  "value": "#000000"
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    #story--components-colorpicker--default--primary-inner {
      height: 25vh !important;
    }
  </style>
  <s-color-picker value="#000000" @colorchanged="ev=&gt;console.log(" color="" changed:",ev.detail)"="" class="ltr hydrated">
    <s-icon icon="hgi-stroke hgi-color-picker" slot="start" class="hydrated"></s-icon>
  </s-color-picker>
```

</details>

### Initial Value

Story id `components-colorpicker--initial-value`

![Initial Value](../../storybook/captures/stories/colorpicker/initial-value.png)

Args:

```json
{
  "value": "#ab1c1c"
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    #story--components-colorpicker--default--primary-inner {
      height: 25vh !important;
    }
  </style>
  <s-color-picker value="#ab1c1c" @colorchanged="ev=&gt;console.log(" color="" changed:",ev.detail)"="" class="ltr hydrated">
    <s-icon icon="hgi-stroke hgi-color-picker" slot="start" class="hydrated"></s-icon>
  </s-color-picker>
```

</details>

### Has Error

Story id `components-colorpicker--has-error`

![Has Error](../../storybook/captures/stories/colorpicker/has-error.png)

Args:

```json
{
  "value": "#000000",
  "hasError": true
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    #story--components-colorpicker--default--primary-inner {
      height: 25vh !important;
    }
  </style>
  <s-color-picker value="#000000" has-error="" @colorchanged="ev=&gt;console.log(" color="" changed:",ev.detail)"="" class="has-error ltr hydrated">
    <s-icon icon="hgi-stroke hgi-color-picker" slot="start" class="hydrated"></s-icon>
  </s-color-picker>
```

</details>

### Label Less

Story id `components-colorpicker--label-less`

![Label Less](../../storybook/captures/stories/colorpicker/label-less.png)

Args:

```json
{
  "value": "#000000",
  "noLabel": true
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    #story--components-colorpicker--default--primary-inner {
      height: 25vh !important;
    }
  </style>
  <s-color-picker value="#000000" no-label="" @colorchanged="ev=&gt;console.log(" color="" changed:",ev.detail)"="" class="ltr hydrated">
    <s-icon icon="hgi-stroke hgi-color-picker" slot="start" class="hydrated"></s-icon>
  </s-color-picker>
```

</details>

### Border Less

Story id `components-colorpicker--border-less`

![Border Less](../../storybook/captures/stories/colorpicker/border-less.png)

Args:

```json
{
  "value": "#000000",
  "noBorder": true
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    #story--components-colorpicker--default--primary-inner {
      height: 25vh !important;
    }
  </style>
  <s-color-picker value="#000000" no-border="" @colorchanged="ev=&gt;console.log(" color="" changed:",ev.detail)"="" class="ltr hydrated">
    <s-icon icon="hgi-stroke hgi-color-picker" slot="start" class="hydrated"></s-icon>
  </s-color-picker>
```

</details>

### Disabled

Story id `components-colorpicker--disabled`

![Disabled](../../storybook/captures/stories/colorpicker/disabled.png)

Args:

```json
{
  "value": "#000000",
  "disabled": true
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    #story--components-colorpicker--default--primary-inner {
      height: 25vh !important;
    }
  </style>
  <s-color-picker value="#000000" disabled="" @colorchanged="ev=&gt;console.log(" color="" changed:",ev.detail)"="" class="disabled ltr hydrated">
    <s-icon icon="hgi-stroke hgi-color-picker" slot="start" class="hydrated"></s-icon>
  </s-color-picker>
```

</details>
