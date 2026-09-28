# Tooltip

Storybook title `Components/Tooltip` · source `./src/components/s-tooltip/s-tooltip.stories.tsx`

Tags rendered: `<s-avatar>`, `<s-button>`, `<s-icon>`, `<s-tag>`, `<s-tooltip>`, `<s-tooltip-action>`

Tooltip component provides contextual information when users hover or click on an element. It displays helpful content in a small overlay positioned relative to the trigger element.

It exposes three slots:

- `toggle`: the trigger element, any element can be used (button, avatar, icon, inline text…).
- `title`: the tooltip heading, it is bolded by the component.
- default: the tooltip body, it accepts any markup, including `<s-tooltip-action>` actions.

## Props

| Prop | Type / control | Options | Default | Description |
|---|---|---|---|---|
| `theme` | string | `default`, `secondary`, `white`, `feature`, `danger` | `default` | Tooltip theme |
| `placement` | string | `bottom`, `bottom-start`, `bottom-end`, `top`, `top-start`, `top-end`, `right`, `right-start`, `right-end`, `left`, `left-start`, `left-end` | `top center` | Tooltip placement |
| `toggleAction` | string | `hover`, `click` | `hover` | Toggle action |
| `width` | string |  | `300px` | Tooltip width |
| `layout` | string | `tight`, `normal`, `relaxed` | `normal` | Tooltip layout |
| `toggle` | string |  |  | `toggle` slot, raw HTML for the trigger element, it must carry `slot="toggle"`. Any element works: `s-button`, `s-avatar`, `s-tag`, an icon or plain inline text. |
| `title` | string |  |  | `title` slot, the content is rendered inside `<h4 slot="title">` so inline markup such as icons is supported. Leave it empty to render a tooltip without a title. |
| `content` | string |  |  | Default slot, raw HTML for the tooltip body. It accepts any markup: paragraphs, lists, media, `s-tooltip-action` or `s-button` actions. |
| `onopen` |  |  |  | Emitted when the tooltip is opened. |
| `onclose` |  |  |  | Emitted when the tooltip is closed. |

## Stories

### Default

Story id `components-tooltip--default`

![Default](../../storybook/captures/stories/tooltip/default.png)

Args:

```json
{
  "theme": "default",
  "placement": "top",
  "toggleAction": "hover",
  "width": "300px",
  "layout": "normal",
  "toggle": "<s-button slot=\"toggle\" theme=\"default\">Show Tooltip</s-button>",
  "title": "Tooltip title",
  "content": "\n  <article>\n    <p>This is the tooltip content that provides helpful information to users.</p>\n    <s-tooltip-action>Click here to learn more</s-tooltip-action>\n  </article>\n"
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    [id*="story--components-tooltip--"] {
      height: 35vh !important;
    }
    </style>
  
  <div style="min-height: 30vh;" class="flex items-center justify-center">
    <s-tooltip theme="default" width="300px" placement="top" toggle-action="hover" layout="normal" class="s-tooltip s-tooltip--default ltr hydrated" data-toggle="hover">
      <s-button slot="toggle" theme="default" class="s-btn s-btn--default default md ltr hydrated" target="_self">Show Tooltip</s-button>
      <h4 slot="title">Tooltip title</h4>
      
  <article>
    <p>This is the tooltip content that provides helpful information to users.</p>
    <s-tooltip-action class="hydrated" theme="default">Click here to learn more</s-tooltip-action>
  </article>

    </s-tooltip>
  </div>
```

</details>

### Secondary

Story id `components-tooltip--secondary`

![Secondary](../../storybook/captures/stories/tooltip/secondary.png)

Args:

```json
{
  "theme": "secondary",
  "placement": "top",
  "toggleAction": "hover",
  "width": "300px",
  "layout": "normal",
  "toggle": "<s-button slot=\"toggle\" theme=\"default\">Show Tooltip</s-button>",
  "title": "Tooltip title",
  "content": "\n  <article>\n    <p>This is the tooltip content that provides helpful information to users.</p>\n    <s-tooltip-action>Click here to learn more</s-tooltip-action>\n  </article>\n"
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    [id*="story--components-tooltip--"] {
      height: 35vh !important;
    }
    </style>
  
  <div style="min-height: 30vh;" class="flex items-center justify-center">
    <s-tooltip theme="secondary" width="300px" placement="top" toggle-action="hover" layout="normal" class="s-tooltip s-tooltip--secondary ltr hydrated" data-toggle="hover">
      <s-button slot="toggle" theme="default" class="s-btn s-btn--default default md ltr hydrated" target="_self">Show Tooltip</s-button>
      <h4 slot="title">Tooltip title</h4>
      
  <article>
    <p>This is the tooltip content that provides helpful information to users.</p>
    <s-tooltip-action class="hydrated" theme="secondary">Click here to learn more</s-tooltip-action>
  </article>

    </s-tooltip>
  </div>
```

</details>

### White

Story id `components-tooltip--white`

![White](../../storybook/captures/stories/tooltip/white.png)

Args:

```json
{
  "theme": "white",
  "placement": "top",
  "toggleAction": "hover",
  "width": "300px",
  "layout": "normal",
  "toggle": "<s-button slot=\"toggle\" theme=\"default\">Show Tooltip</s-button>",
  "title": "Tooltip title",
  "content": "\n  <article>\n    <p>This is the tooltip content that provides helpful information to users.</p>\n    <s-tooltip-action>Click here to learn more</s-tooltip-action>\n  </article>\n"
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    [id*="story--components-tooltip--"] {
      height: 35vh !important;
    }
    </style>
  
  <div style="min-height: 30vh;" class="flex items-center justify-center">
    <s-tooltip theme="white" width="300px" placement="top" toggle-action="hover" layout="normal" class="s-tooltip s-tooltip--white ltr hydrated" data-toggle="hover">
      <s-button slot="toggle" theme="default" class="s-btn s-btn--default default md ltr hydrated" target="_self">Show Tooltip</s-button>
      <h4 slot="title">Tooltip title</h4>
      
  <article>
    <p>This is the tooltip content that provides helpful information to users.</p>
    <s-tooltip-action class="hydrated" theme="white">Click here to learn more</s-tooltip-action>
  </article>

    </s-tooltip>
  </div>
```

</details>

### Danger

Story id `components-tooltip--danger`

![Danger](../../storybook/captures/stories/tooltip/danger.png)

Args:

```json
{
  "theme": "danger",
  "placement": "top",
  "toggleAction": "hover",
  "width": "300px",
  "layout": "normal",
  "toggle": "<s-button slot=\"toggle\" theme=\"default\">Show Tooltip</s-button>",
  "title": "Tooltip title",
  "content": "\n  <article>\n    <p>This is the tooltip content that provides helpful information to users.</p>\n    <s-tooltip-action>Click here to learn more</s-tooltip-action>\n  </article>\n"
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    [id*="story--components-tooltip--"] {
      height: 35vh !important;
    }
    </style>
  
  <div style="min-height: 30vh;" class="flex items-center justify-center">
    <s-tooltip theme="danger" width="300px" placement="top" toggle-action="hover" layout="normal" class="s-tooltip s-tooltip--danger ltr hydrated" data-toggle="hover">
      <s-button slot="toggle" theme="default" class="s-btn s-btn--default default md ltr hydrated" target="_self">Show Tooltip</s-button>
      <h4 slot="title">Tooltip title</h4>
      
  <article>
    <p>This is the tooltip content that provides helpful information to users.</p>
    <s-tooltip-action class="hydrated" theme="danger">Click here to learn more</s-tooltip-action>
  </article>

    </s-tooltip>
  </div>
```

</details>

### Top Start

Story id `components-tooltip--top-start`

![Top Start](../../storybook/captures/stories/tooltip/top-start.png)

Args:

```json
{
  "theme": "default",
  "placement": "top-start",
  "toggleAction": "hover",
  "width": "300px",
  "layout": "normal",
  "toggle": "<s-button slot=\"toggle\" theme=\"default\">Show Tooltip</s-button>",
  "title": "Tooltip title",
  "content": "\n  <article>\n    <p>This is the tooltip content that provides helpful information to users.</p>\n    <s-tooltip-action>Click here to learn more</s-tooltip-action>\n  </article>\n"
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    [id*="story--components-tooltip--"] {
      height: 35vh !important;
    }
    </style>
  
  <div style="min-height: 30vh;" class="flex items-center justify-center">
    <s-tooltip theme="default" width="300px" placement="top-start" toggle-action="hover" layout="normal" class="s-tooltip s-tooltip--default ltr hydrated" data-toggle="hover">
      <s-button slot="toggle" theme="default" class="s-btn s-btn--default default md ltr hydrated" target="_self">Show Tooltip</s-button>
      <h4 slot="title">Tooltip title</h4>
      
  <article>
    <p>This is the tooltip content that provides helpful information to users.</p>
    <s-tooltip-action class="hydrated" theme="default">Click here to learn more</s-tooltip-action>
  </article>

    </s-tooltip>
  </div>
```

</details>

### Top End

Story id `components-tooltip--top-end`

![Top End](../../storybook/captures/stories/tooltip/top-end.png)

Args:

```json
{
  "theme": "default",
  "placement": "top-end",
  "toggleAction": "hover",
  "width": "300px",
  "layout": "normal",
  "toggle": "<s-button slot=\"toggle\" theme=\"default\">Show Tooltip</s-button>",
  "title": "Tooltip title",
  "content": "\n  <article>\n    <p>This is the tooltip content that provides helpful information to users.</p>\n    <s-tooltip-action>Click here to learn more</s-tooltip-action>\n  </article>\n"
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    [id*="story--components-tooltip--"] {
      height: 35vh !important;
    }
    </style>
  
  <div style="min-height: 30vh;" class="flex items-center justify-center">
    <s-tooltip theme="default" width="300px" placement="top-end" toggle-action="hover" layout="normal" class="s-tooltip s-tooltip--default ltr hydrated" data-toggle="hover">
      <s-button slot="toggle" theme="default" class="s-btn s-btn--default default md ltr hydrated" target="_self">Show Tooltip</s-button>
      <h4 slot="title">Tooltip title</h4>
      
  <article>
    <p>This is the tooltip content that provides helpful information to users.</p>
    <s-tooltip-action class="hydrated" theme="default">Click here to learn more</s-tooltip-action>
  </article>

    </s-tooltip>
  </div>
```

</details>

### Bottom Center

Story id `components-tooltip--bottom-center`

![Bottom Center](../../storybook/captures/stories/tooltip/bottom-center.png)

Args:

```json
{
  "theme": "default",
  "placement": "bottom",
  "toggleAction": "hover",
  "width": "300px",
  "layout": "normal",
  "toggle": "<s-button slot=\"toggle\" theme=\"default\">Show Tooltip</s-button>",
  "title": "Tooltip title",
  "content": "\n  <article>\n    <p>This is the tooltip content that provides helpful information to users.</p>\n    <s-tooltip-action>Click here to learn more</s-tooltip-action>\n  </article>\n"
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    [id*="story--components-tooltip--"] {
      height: 35vh !important;
    }
    </style>
  
  <div style="min-height: 30vh;" class="flex items-center justify-center">
    <s-tooltip theme="default" width="300px" placement="bottom" toggle-action="hover" layout="normal" class="s-tooltip s-tooltip--default ltr hydrated" data-toggle="hover">
      <s-button slot="toggle" theme="default" class="s-btn s-btn--default default md ltr hydrated" target="_self">Show Tooltip</s-button>
      <h4 slot="title">Tooltip title</h4>
      
  <article>
    <p>This is the tooltip content that provides helpful information to users.</p>
    <s-tooltip-action class="hydrated" theme="default">Click here to learn more</s-tooltip-action>
  </article>

    </s-tooltip>
  </div>
```

</details>

### Bottom Start

Story id `components-tooltip--bottom-start`

![Bottom Start](../../storybook/captures/stories/tooltip/bottom-start.png)

Args:

```json
{
  "theme": "default",
  "placement": "bottom-start",
  "toggleAction": "hover",
  "width": "300px",
  "layout": "normal",
  "toggle": "<s-button slot=\"toggle\" theme=\"default\">Show Tooltip</s-button>",
  "title": "Tooltip title",
  "content": "\n  <article>\n    <p>This is the tooltip content that provides helpful information to users.</p>\n    <s-tooltip-action>Click here to learn more</s-tooltip-action>\n  </article>\n"
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    [id*="story--components-tooltip--"] {
      height: 35vh !important;
    }
    </style>
  
  <div style="min-height: 30vh;" class="flex items-center justify-center">
    <s-tooltip theme="default" width="300px" placement="bottom-start" toggle-action="hover" layout="normal" class="s-tooltip s-tooltip--default ltr hydrated" data-toggle="hover">
      <s-button slot="toggle" theme="default" class="s-btn s-btn--default default md ltr hydrated" target="_self">Show Tooltip</s-button>
      <h4 slot="title">Tooltip title</h4>
      
  <article>
    <p>This is the tooltip content that provides helpful information to users.</p>
    <s-tooltip-action class="hydrated" theme="default">Click here to learn more</s-tooltip-action>
  </article>

    </s-tooltip>
  </div>
```

</details>

### Bottom End

Story id `components-tooltip--bottom-end`

![Bottom End](../../storybook/captures/stories/tooltip/bottom-end.png)

Args:

```json
{
  "theme": "default",
  "placement": "bottom-end",
  "toggleAction": "hover",
  "width": "300px",
  "layout": "normal",
  "toggle": "<s-button slot=\"toggle\" theme=\"default\">Show Tooltip</s-button>",
  "title": "Tooltip title",
  "content": "\n  <article>\n    <p>This is the tooltip content that provides helpful information to users.</p>\n    <s-tooltip-action>Click here to learn more</s-tooltip-action>\n  </article>\n"
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    [id*="story--components-tooltip--"] {
      height: 35vh !important;
    }
    </style>
  
  <div style="min-height: 30vh;" class="flex items-center justify-center">
    <s-tooltip theme="default" width="300px" placement="bottom-end" toggle-action="hover" layout="normal" class="s-tooltip s-tooltip--default ltr hydrated" data-toggle="hover">
      <s-button slot="toggle" theme="default" class="s-btn s-btn--default default md ltr hydrated" target="_self">Show Tooltip</s-button>
      <h4 slot="title">Tooltip title</h4>
      
  <article>
    <p>This is the tooltip content that provides helpful information to users.</p>
    <s-tooltip-action class="hydrated" theme="default">Click here to learn more</s-tooltip-action>
  </article>

    </s-tooltip>
  </div>
```

</details>

### Center Start

Story id `components-tooltip--center-start`

![Center Start](../../storybook/captures/stories/tooltip/center-start.png)

Args:

```json
{
  "theme": "default",
  "placement": "left",
  "toggleAction": "hover",
  "width": "300px",
  "layout": "normal",
  "toggle": "<s-button slot=\"toggle\" theme=\"default\">Show Tooltip</s-button>",
  "title": "Tooltip title",
  "content": "\n  <article>\n    <p>This is the tooltip content that provides helpful information to users.</p>\n    <s-tooltip-action>Click here to learn more</s-tooltip-action>\n  </article>\n"
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    [id*="story--components-tooltip--"] {
      height: 35vh !important;
    }
    </style>
  
  <div style="min-height: 30vh;" class="flex items-center justify-center">
    <s-tooltip theme="default" width="300px" placement="left" toggle-action="hover" layout="normal" class="s-tooltip s-tooltip--default ltr hydrated" data-toggle="hover">
      <s-button slot="toggle" theme="default" class="s-btn s-btn--default default md ltr hydrated" target="_self">Show Tooltip</s-button>
      <h4 slot="title">Tooltip title</h4>
      
  <article>
    <p>This is the tooltip content that provides helpful information to users.</p>
    <s-tooltip-action class="hydrated" theme="default">Click here to learn more</s-tooltip-action>
  </article>

    </s-tooltip>
  </div>
```

</details>

### Center End

Story id `components-tooltip--center-end`

![Center End](../../storybook/captures/stories/tooltip/center-end.png)

Args:

```json
{
  "theme": "default",
  "placement": "right",
  "toggleAction": "hover",
  "width": "300px",
  "layout": "normal",
  "toggle": "<s-button slot=\"toggle\" theme=\"default\">Show Tooltip</s-button>",
  "title": "Tooltip title",
  "content": "\n  <article>\n    <p>This is the tooltip content that provides helpful information to users.</p>\n    <s-tooltip-action>Click here to learn more</s-tooltip-action>\n  </article>\n"
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    [id*="story--components-tooltip--"] {
      height: 35vh !important;
    }
    </style>
  
  <div style="min-height: 30vh;" class="flex items-center justify-center">
    <s-tooltip theme="default" width="300px" placement="right" toggle-action="hover" layout="normal" class="s-tooltip s-tooltip--default ltr hydrated" data-toggle="hover">
      <s-button slot="toggle" theme="default" class="s-btn s-btn--default default md ltr hydrated" target="_self">Show Tooltip</s-button>
      <h4 slot="title">Tooltip title</h4>
      
  <article>
    <p>This is the tooltip content that provides helpful information to users.</p>
    <s-tooltip-action class="hydrated" theme="default">Click here to learn more</s-tooltip-action>
  </article>

    </s-tooltip>
  </div>
```

</details>

### Click Toggle

Story id `components-tooltip--click-toggle`

![Click Toggle](../../storybook/captures/stories/tooltip/click-toggle.png)

Args:

```json
{
  "theme": "default",
  "placement": "top",
  "toggleAction": "click",
  "width": "300px",
  "layout": "normal",
  "toggle": "<s-button slot=\"toggle\" theme=\"default\">Show Tooltip</s-button>",
  "title": "Tooltip title",
  "content": "\n  <article>\n    <p>This is the tooltip content that provides helpful information to users.</p>\n    <s-tooltip-action>Click here to learn more</s-tooltip-action>\n  </article>\n"
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    [id*="story--components-tooltip--"] {
      height: 35vh !important;
    }
    </style>
  
  <div style="min-height: 30vh;" class="flex items-center justify-center">
    <s-tooltip theme="default" width="300px" placement="top" toggle-action="click" layout="normal" class="s-tooltip s-tooltip--default ltr hydrated" data-toggle="click">
      <s-button slot="toggle" theme="default" class="s-btn s-btn--default default md ltr hydrated" target="_self">Show Tooltip</s-button>
      <h4 slot="title">Tooltip title</h4>
      
  <article>
    <p>This is the tooltip content that provides helpful information to users.</p>
    <s-tooltip-action class="hydrated" theme="default">Click here to learn more</s-tooltip-action>
  </article>

    </s-tooltip>
  </div>
```

</details>

### Tight

Story id `components-tooltip--tight`

![Tight](../../storybook/captures/stories/tooltip/tight.png)

Args:

```json
{
  "theme": "default",
  "placement": "top",
  "toggleAction": "hover",
  "width": "300px",
  "layout": "tight",
  "toggle": "<s-button slot=\"toggle\" theme=\"default\">Show Tooltip</s-button>",
  "title": "Tooltip title",
  "content": "\n  <article>\n    <p>This is the tooltip content that provides helpful information to users.</p>\n    <s-tooltip-action>Click here to learn more</s-tooltip-action>\n  </article>\n"
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    [id*="story--components-tooltip--"] {
      height: 35vh !important;
    }
    </style>
  
  <div style="min-height: 30vh;" class="flex items-center justify-center">
    <s-tooltip theme="default" width="300px" placement="top" toggle-action="hover" layout="tight" class="s-tooltip s-tooltip--default ltr hydrated" data-toggle="hover">
      <s-button slot="toggle" theme="default" class="s-btn s-btn--default default md ltr hydrated" target="_self">Show Tooltip</s-button>
      <h4 slot="title">Tooltip title</h4>
      
  <article>
    <p>This is the tooltip content that provides helpful information to users.</p>
    <s-tooltip-action class="hydrated" theme="default">Click here to learn more</s-tooltip-action>
  </article>

    </s-tooltip>
  </div>
```

</details>

### Relaxed

Story id `components-tooltip--relaxed`

![Relaxed](../../storybook/captures/stories/tooltip/relaxed.png)

Args:

```json
{
  "theme": "default",
  "placement": "top",
  "toggleAction": "hover",
  "width": "300px",
  "layout": "relaxed",
  "toggle": "<s-button slot=\"toggle\" theme=\"default\">Show Tooltip</s-button>",
  "title": "Tooltip title",
  "content": "\n  <article>\n    <p>This is the tooltip content that provides helpful information to users.</p>\n    <s-tooltip-action>Click here to learn more</s-tooltip-action>\n  </article>\n"
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    [id*="story--components-tooltip--"] {
      height: 35vh !important;
    }
    </style>
  
  <div style="min-height: 30vh;" class="flex items-center justify-center">
    <s-tooltip theme="default" width="300px" placement="top" toggle-action="hover" layout="relaxed" class="s-tooltip s-tooltip--default ltr hydrated" data-toggle="hover">
      <s-button slot="toggle" theme="default" class="s-btn s-btn--default default md ltr hydrated" target="_self">Show Tooltip</s-button>
      <h4 slot="title">Tooltip title</h4>
      
  <article>
    <p>This is the tooltip content that provides helpful information to users.</p>
    <s-tooltip-action class="hydrated" theme="default">Click here to learn more</s-tooltip-action>
  </article>

    </s-tooltip>
  </div>
```

</details>

### Custom Width

Story id `components-tooltip--custom-width`

![Custom Width](../../storybook/captures/stories/tooltip/custom-width.png)

Args:

```json
{
  "theme": "default",
  "placement": "top",
  "toggleAction": "hover",
  "width": "500px",
  "layout": "normal",
  "toggle": "<s-button slot=\"toggle\" theme=\"default\">Show Tooltip</s-button>",
  "title": "Tooltip title",
  "content": "\n  <article>\n    <p>This is the tooltip content that provides helpful information to users.</p>\n    <s-tooltip-action>Click here to learn more</s-tooltip-action>\n  </article>\n"
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    [id*="story--components-tooltip--"] {
      height: 35vh !important;
    }
    </style>
  
  <div style="min-height: 30vh;" class="flex items-center justify-center">
    <s-tooltip theme="default" width="500px" placement="top" toggle-action="hover" layout="normal" class="s-tooltip s-tooltip--default ltr hydrated" data-toggle="hover">
      <s-button slot="toggle" theme="default" class="s-btn s-btn--default default md ltr hydrated" target="_self">Show Tooltip</s-button>
      <h4 slot="title">Tooltip title</h4>
      
  <article>
    <p>This is the tooltip content that provides helpful information to users.</p>
    <s-tooltip-action class="hydrated" theme="default">Click here to learn more</s-tooltip-action>
  </article>

    </s-tooltip>
  </div>
```

</details>

### Icon Trigger

Story id `components-tooltip--icon-trigger`

![Icon Trigger](../../storybook/captures/stories/tooltip/icon-trigger.png)

Args:

```json
{
  "theme": "default",
  "placement": "top",
  "toggleAction": "hover",
  "width": "260px",
  "layout": "normal",
  "toggle": "\n      <s-button slot=\"toggle\" layout=\"circular\" theme=\"white\" size=\"sm\">\n        <s-icon icon=\"hgi-stroke hgi-information-circle\"></s-icon>\n      </s-button>\n    ",
  "title": "Help",
  "content": "\n      <article class=\"text-sm\">\n        <p>An icon-only button is the most common trigger for inline help.</p>\n      </article>\n    "
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    [id*="story--components-tooltip--"] {
      height: 35vh !important;
    }
    </style>
  
  <div style="min-height: 30vh;" class="flex items-center justify-center">
    <s-tooltip theme="default" width="260px" placement="top" toggle-action="hover" layout="normal" class="s-tooltip s-tooltip--default ltr hydrated" data-toggle="hover">
      
      <s-button slot="toggle" layout="circular" theme="white" size="sm" class="s-btn s-btn--white circular sm ltr hydrated" target="_self">
        <s-icon icon="hgi-stroke hgi-information-circle" class="hydrated"></s-icon>
      </s-button>
    
      <h4 slot="title">Help</h4>
      
      <article class="text-sm">
        <p>An icon-only button is the most common trigger for inline help.</p>
      </article>
    
    </s-tooltip>
  </div>
```

</details>

### Avatar Trigger

Story id `components-tooltip--avatar-trigger`

![Avatar Trigger](../../storybook/captures/stories/tooltip/avatar-trigger.png)

Args:

```json
{
  "theme": "white",
  "placement": "bottom-start",
  "toggleAction": "hover",
  "width": "280px",
  "layout": "normal",
  "toggle": "\n      <s-avatar\n        slot=\"toggle\"\n        url=\"https://i.pravatar.cc/100\"\n        size=\"sm\"\n        label=\"Sara Ahmed\"\n        desc=\"Store manager\"\n      ></s-avatar>\n    ",
  "title": "Sara Ahmed",
  "content": "\n      <article class=\"text-sm flex flex-col gap-2\">\n        <p>Store manager, joined on 12 Jan 2024.</p>\n        <s-tooltip-action layout=\"btn\" wide>View profile</s-tooltip-action>\n      </article>\n    "
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    [id*="story--components-tooltip--"] {
      height: 35vh !important;
    }
    </style>
  
  <div style="min-height: 30vh;" class="flex items-center justify-center">
    <s-tooltip theme="white" width="280px" placement="bottom-start" toggle-action="hover" layout="normal" class="s-tooltip s-tooltip--white ltr hydrated" data-toggle="hover">
      
      <s-avatar slot="toggle" url="https://i.pravatar.cc/100" size="sm" label="Sara Ahmed" desc="Store manager" class="s-avatar s-avatar--circular s-avatar--horizontal ltr sm hydrated"></s-avatar>
    
      <h4 slot="title">Sara Ahmed</h4>
      
      <article class="text-sm flex flex-col gap-2">
        <p>Store manager, joined on 12 Jan 2024.</p>
        <s-tooltip-action layout="btn" wide="" class="hydrated" theme="white">View profile</s-tooltip-action>
      </article>
    
    </s-tooltip>
  </div>
```

</details>

### Inline Text Trigger

Story id `components-tooltip--inline-text-trigger`

![Inline Text Trigger](../../storybook/captures/stories/tooltip/inline-text-trigger.png)

Args:

```json
{
  "theme": "secondary",
  "placement": "top",
  "toggleAction": "hover",
  "width": "280px",
  "layout": "tight",
  "toggle": "\n      <span slot=\"toggle\" class=\"text-sm text-dark-100 underline decoration-dashed underline-offset-4\">\n        Shipping fees\n      </span>\n    ",
  "title": "",
  "content": "\n      <p class=\"text-xs\">Fees are calculated based on the destination city and the package weight.</p>\n    "
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    [id*="story--components-tooltip--"] {
      height: 35vh !important;
    }
    </style>
  
  <div style="min-height: 30vh;" class="flex items-center justify-center">
    <s-tooltip theme="secondary" width="280px" placement="top" toggle-action="hover" layout="tight" class="s-tooltip s-tooltip--secondary ltr hydrated" data-toggle="hover">
      
      <span slot="toggle" class="text-sm text-dark-100 underline decoration-dashed underline-offset-4">
        Shipping fees
      </span>
    
      
      
      <p class="text-xs">Fees are calculated based on the destination city and the package weight.</p>
    
    </s-tooltip>
  </div>
```

</details>

### Title With Icon

Story id `components-tooltip--title-with-icon`

![Title With Icon](../../storybook/captures/stories/tooltip/title-with-icon.png)

Args:

```json
{
  "theme": "white",
  "placement": "top",
  "toggleAction": "hover",
  "width": "300px",
  "layout": "normal",
  "toggle": "<s-button slot=\"toggle\" theme=\"default\">Show Tooltip</s-button>",
  "title": "\n      <span class=\"flex items-center gap-2\">\n        <s-icon icon=\"hgi-stroke hgi-alert-02\" color=\"hsl(var(--warning))\"></s-icon>\n        Action required\n      </span>\n    ",
  "content": "\n      <article class=\"text-sm\">\n        <p>Verify your store details before publishing your first product.</p>\n        <s-tooltip-action href=\"https://salla.com\" target=\"_blank\">Verify now</s-tooltip-action>\n      </article>\n    "
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    [id*="story--components-tooltip--"] {
      height: 35vh !important;
    }
    </style>
  
  <div style="min-height: 30vh;" class="flex items-center justify-center">
    <s-tooltip theme="white" width="300px" placement="top" toggle-action="hover" layout="normal" class="s-tooltip s-tooltip--white ltr hydrated" data-toggle="hover">
      <s-button slot="toggle" theme="default" class="s-btn s-btn--default default md ltr hydrated" target="_self">Show Tooltip</s-button>
      <h4 slot="title">
      <span class="flex items-center gap-2">
        <s-icon icon="hgi-stroke hgi-alert-02" color="hsl(var(--warning))" class="hydrated"></s-icon>
        Action required
      </span>
    </h4>
      
      <article class="text-sm">
        <p>Verify your store details before publishing your first product.</p>
        <s-tooltip-action href="https://salla.com" target="_blank" class="hydrated" theme="white">Verify now</s-tooltip-action>
      </article>
    
    </s-tooltip>
  </div>
```

</details>

### Without Title

Story id `components-tooltip--without-title`

![Without Title](../../storybook/captures/stories/tooltip/without-title.png)

Args:

```json
{
  "theme": "default",
  "placement": "top",
  "toggleAction": "hover",
  "width": "240px",
  "layout": "tight",
  "toggle": "<s-button slot=\"toggle\" theme=\"default\">Show Tooltip</s-button>",
  "title": "",
  "content": "<p class=\"text-xs\">Copied to clipboard</p>"
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    [id*="story--components-tooltip--"] {
      height: 35vh !important;
    }
    </style>
  
  <div style="min-height: 30vh;" class="flex items-center justify-center">
    <s-tooltip theme="default" width="240px" placement="top" toggle-action="hover" layout="tight" class="s-tooltip s-tooltip--default ltr hydrated" data-toggle="hover">
      <s-button slot="toggle" theme="default" class="s-btn s-btn--default default md ltr hydrated" target="_self">Show Tooltip</s-button>
      
      <p class="text-xs">Copied to clipboard</p>
    </s-tooltip>
  </div>
```

</details>

### List Content

Story id `components-tooltip--list-content`

![List Content](../../storybook/captures/stories/tooltip/list-content.png)

Args:

```json
{
  "theme": "white",
  "placement": "top",
  "toggleAction": "hover",
  "width": "320px",
  "layout": "normal",
  "toggle": "<s-button slot=\"toggle\" theme=\"default\">Show Tooltip</s-button>",
  "title": "Why is this order on hold?",
  "content": "\n      <article class=\"text-sm\">\n        <ul class=\"flex flex-col gap-2 list-disc ps-4\">\n          <li>The payment has not been captured yet.</li>\n          <li>The shipping address is missing a district.</li>\n          <li>One of the products is out of stock.</li>\n        </ul>\n      </article>\n    "
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    [id*="story--components-tooltip--"] {
      height: 35vh !important;
    }
    </style>
  
  <div style="min-height: 30vh;" class="flex items-center justify-center">
    <s-tooltip theme="white" width="320px" placement="top" toggle-action="hover" layout="normal" class="s-tooltip s-tooltip--white ltr hydrated" data-toggle="hover">
      <s-button slot="toggle" theme="default" class="s-btn s-btn--default default md ltr hydrated" target="_self">Show Tooltip</s-button>
      <h4 slot="title">Why is this order on hold?</h4>
      
      <article class="text-sm">
        <ul class="flex flex-col gap-2 list-disc ps-4">
          <li>The payment has not been captured yet.</li>
          <li>The shipping address is missing a district.</li>
          <li>One of the products is out of stock.</li>
        </ul>
      </article>
    
    </s-tooltip>
  </div>
```

</details>

### Key Value Content

Story id `components-tooltip--key-value-content`

![Key Value Content](../../storybook/captures/stories/tooltip/key-value-content.png)

Args:

```json
{
  "theme": "white",
  "placement": "top",
  "toggleAction": "hover",
  "width": "300px",
  "layout": "normal",
  "toggle": "<s-button slot=\"toggle\" theme=\"default\">Show Tooltip</s-button>",
  "title": "Order summary",
  "content": "\n      <article class=\"text-sm flex flex-col gap-2\">\n        <div class=\"flex items-center justify-between gap-4\">\n          <span class=\"text-dark-100\">Subtotal</span>\n          <span class=\"font-bold\">450.00 SAR</span>\n        </div>\n        <div class=\"flex items-center justify-between gap-4\">\n          <span class=\"text-dark-100\">Shipping</span>\n          <span class=\"font-bold\">25.00 SAR</span>\n        </div>\n        <hr class=\"my-1\" />\n        <div class=\"flex items-center justify-between gap-4\">\n          <span class=\"text-dark-100\">Total</span>\n          <span class=\"font-bold\">475.00 SAR</span>\n        </div>\n      </article>\n    "
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    [id*="story--components-tooltip--"] {
      height: 35vh !important;
    }
    </style>
  
  <div style="min-height: 30vh;" class="flex items-center justify-center">
    <s-tooltip theme="white" width="300px" placement="top" toggle-action="hover" layout="normal" class="s-tooltip s-tooltip--white ltr hydrated" data-toggle="hover">
      <s-button slot="toggle" theme="default" class="s-btn s-btn--default default md ltr hydrated" target="_self">Show Tooltip</s-button>
      <h4 slot="title">Order summary</h4>
      
      <article class="text-sm flex flex-col gap-2">
        <div class="flex items-center justify-between gap-4">
          <span class="text-dark-100">Subtotal</span>
          <span class="font-bold">450.00 SAR</span>
        </div>
        <div class="flex items-center justify-between gap-4">
          <span class="text-dark-100">Shipping</span>
          <span class="font-bold">25.00 SAR</span>
        </div>
        <hr class="my-1">
        <div class="flex items-center justify-between gap-4">
          <span class="text-dark-100">Total</span>
          <span class="font-bold">475.00 SAR</span>
        </div>
      </article>
    
    </s-tooltip>
  </div>
```

</details>

### Media Content

Story id `components-tooltip--media-content`

![Media Content](../../storybook/captures/stories/tooltip/media-content.png)

Args:

```json
{
  "theme": "white",
  "placement": "top",
  "toggleAction": "hover",
  "width": "300px",
  "layout": "normal",
  "toggle": "<s-button slot=\"toggle\" theme=\"default\">Show Tooltip</s-button>",
  "title": "Product preview",
  "content": "\n      <article class=\"text-sm flex flex-col gap-3\">\n        <img\n          src=\"https://cdn.salla.network/images/logo/logo-square.png\"\n          alt=\"Product preview\"\n          class=\"w-full h-[120px] object-contain rounded-lg bg-white-200\"\n        />\n        <p>Images, videos or any other media can live inside the tooltip content.</p>\n      </article>\n    "
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    [id*="story--components-tooltip--"] {
      height: 35vh !important;
    }
    </style>
  
  <div style="min-height: 30vh;" class="flex items-center justify-center">
    <s-tooltip theme="white" width="300px" placement="top" toggle-action="hover" layout="normal" class="s-tooltip s-tooltip--white ltr hydrated" data-toggle="hover">
      <s-button slot="toggle" theme="default" class="s-btn s-btn--default default md ltr hydrated" target="_self">Show Tooltip</s-button>
      <h4 slot="title">Product preview</h4>
      
      <article class="text-sm flex flex-col gap-3">
        <img src="https://cdn.salla.network/images/logo/logo-square.png" alt="Product preview" class="w-full h-[120px] object-contain rounded-lg bg-white-200">
        <p>Images, videos or any other media can live inside the tooltip content.</p>
      </article>
    
    </s-tooltip>
  </div>
```

</details>

### Multiple Actions

Story id `components-tooltip--multiple-actions`

![Multiple Actions](../../storybook/captures/stories/tooltip/multiple-actions.png)

Args:

```json
{
  "theme": "white",
  "placement": "top",
  "toggleAction": "click",
  "width": "320px",
  "layout": "normal",
  "toggle": "<s-button slot=\"toggle\" theme=\"default\">Show Tooltip</s-button>",
  "title": "Delete this coupon?",
  "content": "\n      <article class=\"text-sm flex flex-col gap-3\">\n        <p>Deleting the coupon stops it from being applied to any new order.</p>\n        <div class=\"flex items-center gap-2\">\n          <s-tooltip-action layout=\"btn\" theme=\"danger\">Delete</s-tooltip-action>\n          <s-tooltip-action layout=\"btn\" theme=\"white\">Cancel</s-tooltip-action>\n        </div>\n      </article>\n    "
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    [id*="story--components-tooltip--"] {
      height: 35vh !important;
    }
    </style>
  
  <div style="min-height: 30vh;" class="flex items-center justify-center">
    <s-tooltip theme="white" width="320px" placement="top" toggle-action="click" layout="normal" class="s-tooltip s-tooltip--white ltr hydrated" data-toggle="click">
      <s-button slot="toggle" theme="default" class="s-btn s-btn--default default md ltr hydrated" target="_self">Show Tooltip</s-button>
      <h4 slot="title">Delete this coupon?</h4>
      
      <article class="text-sm flex flex-col gap-3">
        <p>Deleting the coupon stops it from being applied to any new order.</p>
        <div class="flex items-center gap-2">
          <s-tooltip-action layout="btn" theme="white" class="hydrated">Delete</s-tooltip-action>
          <s-tooltip-action layout="btn" theme="white" class="hydrated">Cancel</s-tooltip-action>
        </div>
      </article>
    
    </s-tooltip>
  </div>
```

</details>

### Feature Locked

Story id `components-tooltip--feature-locked`

![Feature Locked](../../storybook/captures/stories/tooltip/feature-locked.png)

Args:

```json
{
  "theme": "feature",
  "placement": "top",
  "toggleAction": "hover",
  "width": "300px",
  "layout": "normal",
  "toggle": "\n      <s-button slot=\"toggle\" theme=\"feature\">\n        <s-icon icon=\"hgi-stroke hgi-square-lock-02\"></s-icon>\n        Locked feature\n      </s-button>\n    ",
  "title": "Advanced feature",
  "content": "\n      <article>\n        <p>Upgrade your store plan to unlock this feature.</p>\n        <s-button theme=\"feature\">Upgrade now</s-button>\n      </article>\n    "
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    [id*="story--components-tooltip--"] {
      height: 35vh !important;
    }
    </style>
  
  <div style="min-height: 30vh;" class="flex items-center justify-center">
    <s-tooltip theme="feature" width="300px" placement="top" toggle-action="hover" layout="normal" class="s-tooltip s-tooltip--feature ltr hydrated" data-toggle="hover">
      
      <s-button slot="toggle" theme="feature" class="s-btn s-btn--feature default md ltr hydrated" target="_self">
        <s-icon icon="hgi-stroke hgi-square-lock-02" class="hydrated"></s-icon>
        Locked feature
      </s-button>
    
      <h4 slot="title">Advanced feature</h4>
      
      <article>
        <p>Upgrade your store plan to unlock this feature.</p>
        <s-button theme="feature" class="s-btn s-btn--feature default md ltr hydrated" target="_self">Upgrade now</s-button>
      </article>
    
    </s-tooltip>
  </div>
```

</details>

### Media Card With Image

Story id `components-tooltip--media-card-with-image`

![Media Card With Image](../../storybook/captures/stories/tooltip/media-card-with-image.png)

Args:

```json
{
  "theme": "white",
  "placement": "bottom",
  "toggleAction": "hover",
  "width": "400px",
  "layout": "normal",
  "toggle": "\n      <s-button slot=\"toggle\" outlined>\n        <s-icon icon=\"hgi-stroke hgi-image-01\"></s-icon>\n        Cost price guide\n      </s-button>\n    ",
  "title": "",
  "content": "\n  <article class=\"text-sm flex flex-col gap-3\">\n    \n      <img\n        src=\"https://picsum.photos/seed/salla-cost-price/640/360\"\n        alt=\"Cost price guide\"\n        class=\"w-full h-[170px] object-cover rounded-xl\"\n      />\n    \n    <h4 class=\"font-bold text-base\">Setting the right cost price</h4>\n    <p class=\"text-dark-100\">\n      To set an accurate cost price you have to add up every fixed and variable\n      expense tied to the product, otherwise you end up with hidden losses.\n    </p>\n    <ul class=\"flex flex-col gap-2\">\n      <li class=\"flex items-start gap-2\">\n        <span class=\"mt-[6px] size-2 shrink-0 rounded-full bg-success\"></span>\n        <span><strong>Base purchase price:</strong> the amount you pay the supplier or the factory per unit.</span>\n      </li>\n      <li class=\"flex items-start gap-2\">\n        <span class=\"mt-[6px] size-2 shrink-0 rounded-full bg-warning\"></span>\n        <span><strong>Shipping and import:</strong> international shipping, customs and taxes, divided by the number of units.</span>\n      </li>\n      <li class=\"flex items-start gap-2\">\n        <span class=\"mt-[6px] size-2 shrink-0 rounded-full bg-info\"></span>\n        <span><strong>Packaging materials:</strong> the carton, the tape and the labels of a single unit.</span>\n      </li>\n    </ul>\n    <div class=\"flex flex-wrap items-center gap-2\">\n      <s-tag size=\"sm\" theme=\"white\" outlined>Products</s-tag>\n      <s-tag size=\"sm\" theme=\"white\" outlined>Cost price</s-tag>\n      <s-tag size=\"sm\" theme=\"white\" outlined>Cost calculation</s-tag>\n    </div>\n  </article>\n"
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    [id*="story--components-tooltip--"] {
      height: 35vh !important;
    }
    </style>
  
  <div style="min-height: 30vh;" class="flex items-center justify-center">
    <s-tooltip theme="white" width="400px" placement="bottom" toggle-action="hover" layout="normal" class="s-tooltip s-tooltip--white ltr hydrated" data-toggle="hover">
      
      <s-button slot="toggle" outlined="" class="s-btn s-btn--default default md outlined ltr hydrated" theme="default" target="_self">
        <s-icon icon="hgi-stroke hgi-image-01" class="hydrated"></s-icon>
        Cost price guide
      </s-button>
    
      
      
  <article class="text-sm flex flex-col gap-3">
    
      <img src="https://picsum.photos/seed/salla-cost-price/640/360" alt="Cost price guide" class="w-full h-[170px] object-cover rounded-xl">
    
    <h4 class="font-bold text-base">Setting the right cost price</h4>
    <p class="text-dark-100">
      To set an accurate cost price you have to add up every fixed and variable
      expense tied to the product, otherwise you end up with hidden losses.
    </p>
    <ul class="flex flex-col gap-2">
      <li class="flex items-start gap-2">
        <span class="mt-[6px] size-2 shrink-0 rounded-full bg-success"></span>
        <span><strong>Base purchase price:</strong> the amount you pay the supplier or the factory per unit.</span>
      </li>
      <li class="flex items-start gap-2">
        <span class="mt-[6px] size-2 shrink-0 rounded-full bg-warning"></span>
        <span><strong>Shipping and import:</strong> international shipping, customs and taxes, divided by the number of units.</span>
      </li>
      <li class="flex items-start gap-2">
        <span class="mt-[6px] size-2 shrink-0 rounded-full bg-info"></span>
        <span><strong>Packaging materials:</strong> the carton, the tape and the labels of a single unit.</span>
      </li>
    </ul>
    <div class="flex flex-wrap items-center gap-2">
      <s-tag size="sm" theme="white" outlined="" class="s-tag s-tag--white whitespace-nowrap outlined sm ltr hydrated">Products</s-tag>
      <s-tag size="sm" theme="white" outlined="" class="s-tag s-tag--white whitespace-nowrap outlined sm ltr hydrated">Cost price</s-tag>
      <s-tag size="sm" theme="white" outlined="" class="s-tag s-tag--white whitespace-nowrap outlined sm ltr hydrated">Cost calculation</s-tag>
    </div>
  </article>

    </s-tooltip>
  </div>
```

</details>

### Media Card With Video

Story id `components-tooltip--media-card-with-video`

![Media Card With Video](../../storybook/captures/stories/tooltip/media-card-with-video.png)

Args:

```json
{
  "theme": "white",
  "placement": "bottom",
  "toggleAction": "click",
  "width": "400px",
  "layout": "normal",
  "toggle": "\n      <s-button slot=\"toggle\" outlined>\n        <s-icon icon=\"hgi-stroke hgi-play-circle\"></s-icon>\n        Watch the cost price guide\n      </s-button>\n    ",
  "title": "",
  "content": "\n  <article class=\"text-sm flex flex-col gap-3\">\n    \n      <iframe\n        class=\"w-full h-[170px] rounded-xl border-0\"\n        src=\"https://www.youtube-nocookie.com/embed/aqz-KE-bpKQ\"\n        title=\"Cost price guide\"\n        sandbox=\"allow-scripts allow-same-origin allow-presentation\"\n        referrerpolicy=\"strict-origin-when-cross-origin\"\n        allow=\"encrypted-media; picture-in-picture; fullscreen\"\n        loading=\"lazy\"\n      ></iframe>\n    \n    <h4 class=\"font-bold text-base\">Setting the right cost price</h4>\n    <p class=\"text-dark-100\">\n      To set an accurate cost price you have to add up every fixed and variable\n      expense tied to the product, otherwise you end up with hidden losses.\n    </p>\n    <ul class=\"flex flex-col gap-2\">\n      <li class=\"flex items-start gap-2\">\n        <span class=\"mt-[6px] size-2 shrink-0 rounded-full bg-success\"></span>\n        <span><strong>Base purchase price:</strong> the amount you pay the supplier or the factory per unit.</span>\n      </li>\n      <li class=\"flex items-start gap-2\">\n        <span class=\"mt-[6px] size-2 shrink-0 rounded-full bg-warning\"></span>\n        <span><strong>Shipping and import:</strong> international shipping, customs and taxes, divided by the number of units.</span>\n      </li>\n      <li class=\"flex items-start gap-2\">\n        <span class=\"mt-[6px] size-2 shrink-0 rounded-full bg-info\"></span>\n        <span><strong>Packaging materials:</strong> the carton, the tape and the labels of a single unit.</span>\n      </li>\n    </ul>\n    <div class=\"flex flex-wrap items-center gap-2\">\n      <s-tag size=\"sm\" theme=\"white\" outlined>Products</s-tag>\n      <s-tag size=\"sm\" theme=\"white\" outlined>Cost price</s-tag>\n      <s-tag size=\"sm\" theme=\"white\" outlined>Cost calculation</s-tag>\n    </div>\n  </article>\n"
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    [id*="story--components-tooltip--"] {
      height: 35vh !important;
    }
    </style>
  
  <div style="min-height: 30vh;" class="flex items-center justify-center">
    <s-tooltip theme="white" width="400px" placement="bottom" toggle-action="click" layout="normal" class="s-tooltip s-tooltip--white ltr hydrated" data-toggle="click">
      
      <s-button slot="toggle" outlined="" class="s-btn s-btn--default default md outlined ltr hydrated" theme="default" target="_self">
        <s-icon icon="hgi-stroke hgi-play-circle" class="hydrated"></s-icon>
        Watch the cost price guide
      </s-button>
    
      
      
  <article class="text-sm flex flex-col gap-3">
    
      <iframe class="w-full h-[170px] rounded-xl border-0" src="https://www.youtube-nocookie.com/embed/aqz-KE-bpKQ" title="Cost price guide" sandbox="allow-scripts allow-same-origin allow-presentation" referrerpolicy="strict-origin-when-cross-origin" allow="encrypted-media; picture-in-picture; fullscreen" loading="lazy"></iframe>
    
    <h4 class="font-bold text-base">Setting the right cost price</h4>
    <p class="text-dark-100">
      To set an accurate cost price you have to add up every fixed and variable
      expense tied to the product, otherwise you end up with hidden losses.
    </p>
    <ul class="flex flex-col gap-2">
      <li class="flex items-start gap-2">
        <span class="mt-[6px] size-2 shrink-0 rounded-full bg-success"></span>
        <span><strong>Base purchase price:</strong> the amount you pay the supplier or the factory per unit.</span>
      </li>
      <li class="flex items-start gap-2">
        <span class="mt-[6px] size-2 shrink-0 rounded-full bg-warning"></span>
        <span><strong>Shipping and import:</strong> international shipping, customs and taxes, divided by the number of units.</span>
      </li>
      <li class="flex items-start gap-2">
        <span class="mt-[6px] size-2 shrink-0 rounded-full bg-info"></span>
        <span><strong>Packaging materials:</strong> the carton, the tape and the labels of a single unit.</span>
      </li>
    </ul>
    <div class="flex flex-wrap items-center gap-2">
      <s-tag size="sm" theme="white" outlined="" class="s-tag s-tag--white whitespace-nowrap outlined sm ltr hydrated">Products</s-tag>
      <s-tag size="sm" theme="white" outlined="" class="s-tag s-tag--white whitespace-nowrap outlined sm ltr hydrated">Cost price</s-tag>
      <s-tag size="sm" theme="white" outlined="" class="s-tag s-tag--white whitespace-nowrap outlined sm ltr hydrated">Cost calculation</s-tag>
    </div>
  </article>

    </s-tooltip>
  </div>
```

</details>
