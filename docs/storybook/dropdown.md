# Dropdown

Storybook title `Components/Dropdown` · source `./src/components/s-dropdown/s-dropdown.stories.tsx`

Tags rendered: `<s-button>`, `<s-dropdown>`

A dropdown component that displays a list of selectable items. It supports various states, search functionality, and different toggle elements.

## Props

| Prop | Type / control | Options | Default | Description |
|---|---|---|---|---|
| `items` | array |  | `[]` | Items for the dropdown menu |
| `active` | boolean |  | `false` | Active state of the dropdown |
| `loading` | boolean |  | `false` | Loading state |
| `layout` | select | `start`, `end`, `expanded` | `start` | Dropdown layout |
| `overlayAlignment` | select | `start`, `end` | `start` | Horizontal alignment preference for the dropdown overlay |
| `sheetTitle` | text |  |  | Optional title shown in the mobile sheet header |
| `disabled` | boolean |  | `false` | Disabled state |
| `selectable` | boolean |  | `false` | Enables item selection |
| `searchable` | boolean |  | `false` | Enables search functionality |
| `autoComplete` | boolean |  | `false` | Enables autocomplete functionality |
| `searchQuery` | text |  | `undefined` | Initial search query |
| `isOnClick` | boolean |  | `false` | Enables click event handling |
| `multiselect` | boolean |  | `false` | Enables multiple item selection |
| `searchPlaceholder` | text |  | `undefined` | Placeholder text for the search input |
| `itemClick` |  |  |  | Event emitted when an item in the dropdown is clicked. Provides the item's route or identifier. |
| `onclick` |  |  |  | Event emitted when the dropdown toggle button is clicked. This is the main click event for opening/closing the dropdown. |
| `onopen` |  |  |  | Event emitted when the dropdown menu is opened. Useful for tracking dropdown visibility state. |
| `onclose` |  |  |  | Event emitted when the dropdown menu is closed. Useful for tracking dropdown visibility state and cleanup operations. |
| `onselected` |  |  |  | Event emitted when an item is selected in the dropdown. Provides comprehensive information about the selected item including id, label, value, and icon. |
| `searchValueChange` |  |  |  | Event emitted when the search input value changes (only when searchable or autocomplete is enabled). Useful for implementing custom search logic or autocomplete functionality. |
| `children` | string |  |  |  |

## Stories

### Default

Story id `components-dropdown--default`

![Default](../../storybook/captures/stories/dropdown/default.png)

Args:

```json
{
  "items": [
    {
      "id": 0,
      "label": "Sort Items",
      "value": "sort",
      "icon": "hgi-stroke hgi-sorting-01"
    },
    {
      "id": 1,
      "label": "Copy Items",
      "value": "copy",
      "icon": "hgi-stroke hgi-copy-01",
      "route": "/"
    },
    {
      "id": 2,
      "label": "Export Items",
      "value": "export",
      "icon": "hgi-stroke hgi-share-05",
      "route": "/"
    },
    {
      "id": 3,
      "label": "Delete Items",
      "value": "delete",
      "icon": "hgi-stroke hgi-delete-02",
      "route": "/"
    },
    {
      "id": 4,
      "label": "Settings",
      "value": "settings",
      "icon": "hgi-stroke hgi-settings-01"
    }
  ]
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    #story--components-dropdown--default--primary-inner {
      height: 25vh !important;
    }
  </style>
  <s-dropdown layout="start" items="[{&quot;id&quot;:0,&quot;label&quot;:&quot;Sort Items&quot;,&quot;value&quot;:&quot;sort&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-sorting-01&quot;},{&quot;id&quot;:1,&quot;label&quot;:&quot;Copy Items&quot;,&quot;value&quot;:&quot;copy&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-copy-01&quot;,&quot;route&quot;:&quot;/&quot;},{&quot;id&quot;:2,&quot;label&quot;:&quot;Export Items&quot;,&quot;value&quot;:&quot;export&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-share-05&quot;,&quot;route&quot;:&quot;/&quot;},{&quot;id&quot;:3,&quot;label&quot;:&quot;Delete Items&quot;,&quot;value&quot;:&quot;delete&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-delete-02&quot;,&quot;route&quot;:&quot;/&quot;},{&quot;id&quot;:4,&quot;label&quot;:&quot;Settings&quot;,&quot;value&quot;:&quot;settings&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-settings-01&quot;}]" class="start ltr hydrated">
    
      <s-button data-toggle="true" slot="dropdown-head" outlined="" class="s-btn s-btn--default default md outlined ltr hydrated" theme="default" target="_self">
        <i class="hgi-stroke hgi-settings-01"></i>
        Options
        <i class="hgi-stroke hgi-arrow-down-01"></i>
      </s-button>
    
  </s-dropdown>
```

</details>

### Selectable

Story id `components-dropdown--selectable`

![Selectable](../../storybook/captures/stories/dropdown/selectable.png)

Args:

```json
{
  "items": [
    {
      "id": 0,
      "label": "Sort Items",
      "value": "sort",
      "icon": "hgi-stroke hgi-sorting-01"
    },
    {
      "id": 1,
      "label": "Copy Items",
      "value": "copy",
      "icon": "hgi-stroke hgi-copy-01",
      "route": "/"
    },
    {
      "id": 2,
      "label": "Export Items",
      "value": "export",
      "icon": "hgi-stroke hgi-share-05",
      "route": "/"
    },
    {
      "id": 3,
      "label": "Delete Items",
      "value": "delete",
      "icon": "hgi-stroke hgi-delete-02",
      "route": "/"
    },
    {
      "id": 4,
      "label": "Settings",
      "value": "settings",
      "icon": "hgi-stroke hgi-settings-01"
    }
  ],
  "selectable": true
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    #story--components-dropdown--default--primary-inner {
      height: 25vh !important;
    }
  </style>
  <s-dropdown selectable="" layout="start" items="[{&quot;id&quot;:0,&quot;label&quot;:&quot;Sort Items&quot;,&quot;value&quot;:&quot;sort&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-sorting-01&quot;},{&quot;id&quot;:1,&quot;label&quot;:&quot;Copy Items&quot;,&quot;value&quot;:&quot;copy&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-copy-01&quot;,&quot;route&quot;:&quot;/&quot;},{&quot;id&quot;:2,&quot;label&quot;:&quot;Export Items&quot;,&quot;value&quot;:&quot;export&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-share-05&quot;,&quot;route&quot;:&quot;/&quot;},{&quot;id&quot;:3,&quot;label&quot;:&quot;Delete Items&quot;,&quot;value&quot;:&quot;delete&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-delete-02&quot;,&quot;route&quot;:&quot;/&quot;},{&quot;id&quot;:4,&quot;label&quot;:&quot;Settings&quot;,&quot;value&quot;:&quot;settings&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-settings-01&quot;}]" class="start ltr hydrated">
    
      <s-button data-toggle="true" slot="dropdown-head" outlined="" class="s-btn s-btn--default default md outlined ltr hydrated" theme="default" target="_self">
        <i class="hgi-stroke hgi-settings-01"></i>
        Options
        <i class="hgi-stroke hgi-arrow-down-01"></i>
      </s-button>
    
  </s-dropdown>
```

</details>

### Searchable

Story id `components-dropdown--searchable`

![Searchable](../../storybook/captures/stories/dropdown/searchable.png)

Args:

```json
{
  "items": [
    {
      "id": 0,
      "label": "Sort Items",
      "value": "sort",
      "icon": "hgi-stroke hgi-sorting-01"
    },
    {
      "id": 1,
      "label": "Copy Items",
      "value": "copy",
      "icon": "hgi-stroke hgi-copy-01",
      "route": "/"
    },
    {
      "id": 2,
      "label": "Export Items",
      "value": "export",
      "icon": "hgi-stroke hgi-share-05",
      "route": "/"
    },
    {
      "id": 3,
      "label": "Delete Items",
      "value": "delete",
      "icon": "hgi-stroke hgi-delete-02",
      "route": "/"
    },
    {
      "id": 4,
      "label": "Settings",
      "value": "settings",
      "icon": "hgi-stroke hgi-settings-01"
    }
  ],
  "searchable": true,
  "searchPlaceholder": "Search for items..."
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    #story--components-dropdown--default--primary-inner {
      height: 25vh !important;
    }
  </style>
  <s-dropdown searchable="" search-placeholder="Search for items..." layout="start" items="[{&quot;id&quot;:0,&quot;label&quot;:&quot;Sort Items&quot;,&quot;value&quot;:&quot;sort&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-sorting-01&quot;},{&quot;id&quot;:1,&quot;label&quot;:&quot;Copy Items&quot;,&quot;value&quot;:&quot;copy&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-copy-01&quot;,&quot;route&quot;:&quot;/&quot;},{&quot;id&quot;:2,&quot;label&quot;:&quot;Export Items&quot;,&quot;value&quot;:&quot;export&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-share-05&quot;,&quot;route&quot;:&quot;/&quot;},{&quot;id&quot;:3,&quot;label&quot;:&quot;Delete Items&quot;,&quot;value&quot;:&quot;delete&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-delete-02&quot;,&quot;route&quot;:&quot;/&quot;},{&quot;id&quot;:4,&quot;label&quot;:&quot;Settings&quot;,&quot;value&quot;:&quot;settings&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-settings-01&quot;}]" class="start ltr hydrated">
    
      <s-button data-toggle="true" slot="dropdown-head" outlined="" class="s-btn s-btn--default default md outlined ltr hydrated" theme="default" target="_self">
        <i class="hgi-stroke hgi-settings-01"></i>
        Options
        <i class="hgi-stroke hgi-arrow-down-01"></i>
      </s-button>
    
  </s-dropdown>
```

</details>

### Layout Start

Story id `components-dropdown--layout-start`

![Layout Start](../../storybook/captures/stories/dropdown/layout-start.png)

Args:

```json
{
  "items": [
    {
      "id": 0,
      "label": "Sort Items",
      "value": "sort",
      "icon": "hgi-stroke hgi-sorting-01"
    },
    {
      "id": 1,
      "label": "Copy Items",
      "value": "copy",
      "icon": "hgi-stroke hgi-copy-01",
      "route": "/"
    },
    {
      "id": 2,
      "label": "Export Items",
      "value": "export",
      "icon": "hgi-stroke hgi-share-05",
      "route": "/"
    },
    {
      "id": 3,
      "label": "Delete Items",
      "value": "delete",
      "icon": "hgi-stroke hgi-delete-02",
      "route": "/"
    },
    {
      "id": 4,
      "label": "Settings",
      "value": "settings",
      "icon": "hgi-stroke hgi-settings-01"
    }
  ],
  "layout": "start"
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    #story--components-dropdown--default--primary-inner {
      height: 25vh !important;
    }
  </style>
  <s-dropdown layout="start" items="[{&quot;id&quot;:0,&quot;label&quot;:&quot;Sort Items&quot;,&quot;value&quot;:&quot;sort&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-sorting-01&quot;},{&quot;id&quot;:1,&quot;label&quot;:&quot;Copy Items&quot;,&quot;value&quot;:&quot;copy&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-copy-01&quot;,&quot;route&quot;:&quot;/&quot;},{&quot;id&quot;:2,&quot;label&quot;:&quot;Export Items&quot;,&quot;value&quot;:&quot;export&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-share-05&quot;,&quot;route&quot;:&quot;/&quot;},{&quot;id&quot;:3,&quot;label&quot;:&quot;Delete Items&quot;,&quot;value&quot;:&quot;delete&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-delete-02&quot;,&quot;route&quot;:&quot;/&quot;},{&quot;id&quot;:4,&quot;label&quot;:&quot;Settings&quot;,&quot;value&quot;:&quot;settings&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-settings-01&quot;}]" class="start ltr hydrated">
    
      <s-button data-toggle="true" slot="dropdown-head" outlined="" class="s-btn s-btn--default default md outlined ltr hydrated" theme="default" target="_self">
        <i class="hgi-stroke hgi-settings-01"></i>
        Options
        <i class="hgi-stroke hgi-arrow-down-01"></i>
      </s-button>
    
  </s-dropdown>
```

</details>

### Layout End

Story id `components-dropdown--layout-end`

![Layout End](../../storybook/captures/stories/dropdown/layout-end.png)

Args:

```json
{
  "items": [
    {
      "id": 0,
      "label": "Sort Items",
      "value": "sort",
      "icon": "hgi-stroke hgi-sorting-01"
    },
    {
      "id": 1,
      "label": "Copy Items",
      "value": "copy",
      "icon": "hgi-stroke hgi-copy-01",
      "route": "/"
    },
    {
      "id": 2,
      "label": "Export Items",
      "value": "export",
      "icon": "hgi-stroke hgi-share-05",
      "route": "/"
    },
    {
      "id": 3,
      "label": "Delete Items",
      "value": "delete",
      "icon": "hgi-stroke hgi-delete-02",
      "route": "/"
    },
    {
      "id": 4,
      "label": "Settings",
      "value": "settings",
      "icon": "hgi-stroke hgi-settings-01"
    }
  ],
  "layout": "end"
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    #story--components-dropdown--default--primary-inner {
      height: 25vh !important;
    }
  </style>
  <s-dropdown layout="end" items="[{&quot;id&quot;:0,&quot;label&quot;:&quot;Sort Items&quot;,&quot;value&quot;:&quot;sort&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-sorting-01&quot;},{&quot;id&quot;:1,&quot;label&quot;:&quot;Copy Items&quot;,&quot;value&quot;:&quot;copy&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-copy-01&quot;,&quot;route&quot;:&quot;/&quot;},{&quot;id&quot;:2,&quot;label&quot;:&quot;Export Items&quot;,&quot;value&quot;:&quot;export&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-share-05&quot;,&quot;route&quot;:&quot;/&quot;},{&quot;id&quot;:3,&quot;label&quot;:&quot;Delete Items&quot;,&quot;value&quot;:&quot;delete&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-delete-02&quot;,&quot;route&quot;:&quot;/&quot;},{&quot;id&quot;:4,&quot;label&quot;:&quot;Settings&quot;,&quot;value&quot;:&quot;settings&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-settings-01&quot;}]" class="end ltr hydrated">
    
      <s-button data-toggle="true" slot="dropdown-head" outlined="" class="s-btn s-btn--default default md outlined ltr hydrated" theme="default" target="_self">
        <i class="hgi-stroke hgi-settings-01"></i>
        Options
        <i class="hgi-stroke hgi-arrow-down-01"></i>
      </s-button>
    
  </s-dropdown>
```

</details>

### Overlay Alignment End

Story id `components-dropdown--overlay-alignment-end`

![Overlay Alignment End](../../storybook/captures/stories/dropdown/overlay-alignment-end.png)

Args:

```json
{
  "items": [
    {
      "id": 0,
      "label": "Sort Items",
      "value": "sort",
      "icon": "hgi-stroke hgi-sorting-01"
    },
    {
      "id": 1,
      "label": "Copy Items",
      "value": "copy",
      "icon": "hgi-stroke hgi-copy-01",
      "route": "/"
    },
    {
      "id": 2,
      "label": "Export Items",
      "value": "export",
      "icon": "hgi-stroke hgi-share-05",
      "route": "/"
    },
    {
      "id": 3,
      "label": "Delete Items",
      "value": "delete",
      "icon": "hgi-stroke hgi-delete-02",
      "route": "/"
    },
    {
      "id": 4,
      "label": "Settings",
      "value": "settings",
      "icon": "hgi-stroke hgi-settings-01"
    },
    {
      "id": 99,
      "label": "Very long option label to show end alignment effect",
      "value": "long-option"
    }
  ],
  "overlayAlignment": "end",
  "searchable": true
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    #story--components-dropdown--default--primary-inner {
      height: 25vh !important;
    }
  </style>
  <s-dropdown searchable="" layout="start" overlay-alignment="end" items="[{&quot;id&quot;:0,&quot;label&quot;:&quot;Sort Items&quot;,&quot;value&quot;:&quot;sort&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-sorting-01&quot;},{&quot;id&quot;:1,&quot;label&quot;:&quot;Copy Items&quot;,&quot;value&quot;:&quot;copy&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-copy-01&quot;,&quot;route&quot;:&quot;/&quot;},{&quot;id&quot;:2,&quot;label&quot;:&quot;Export Items&quot;,&quot;value&quot;:&quot;export&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-share-05&quot;,&quot;route&quot;:&quot;/&quot;},{&quot;id&quot;:3,&quot;label&quot;:&quot;Delete Items&quot;,&quot;value&quot;:&quot;delete&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-delete-02&quot;,&quot;route&quot;:&quot;/&quot;},{&quot;id&quot;:4,&quot;label&quot;:&quot;Settings&quot;,&quot;value&quot;:&quot;settings&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-settings-01&quot;},{&quot;id&quot;:99,&quot;label&quot;:&quot;Very long option label to show end alignment effect&quot;,&quot;value&quot;:&quot;long-option&quot;}]" class="start ltr hydrated">
    
      <s-button data-toggle="true" slot="dropdown-head" outlined="" class="s-btn s-btn--default default md outlined ltr hydrated" theme="default" target="_self">
        <i class="hgi-stroke hgi-settings-01"></i>
        Options
        <i class="hgi-stroke hgi-arrow-down-01"></i>
      </s-button>
    
  </s-dropdown>
```

</details>

### Layout Expanded

Story id `components-dropdown--layout-expanded`

![Layout Expanded](../../storybook/captures/stories/dropdown/layout-expanded.png)

Args:

```json
{
  "items": [
    {
      "id": 0,
      "label": "Sort Items",
      "value": "sort",
      "icon": "hgi-stroke hgi-sorting-01"
    },
    {
      "id": 1,
      "label": "Copy Items",
      "value": "copy",
      "icon": "hgi-stroke hgi-copy-01",
      "route": "/"
    },
    {
      "id": 2,
      "label": "Export Items",
      "value": "export",
      "icon": "hgi-stroke hgi-share-05",
      "route": "/"
    },
    {
      "id": 3,
      "label": "Delete Items",
      "value": "delete",
      "icon": "hgi-stroke hgi-delete-02",
      "route": "/"
    },
    {
      "id": 4,
      "label": "Settings",
      "value": "settings",
      "icon": "hgi-stroke hgi-settings-01"
    }
  ],
  "layout": "expanded"
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    #story--components-dropdown--default--primary-inner {
      height: 25vh !important;
    }
  </style>
  <s-dropdown layout="expanded" items="[{&quot;id&quot;:0,&quot;label&quot;:&quot;Sort Items&quot;,&quot;value&quot;:&quot;sort&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-sorting-01&quot;},{&quot;id&quot;:1,&quot;label&quot;:&quot;Copy Items&quot;,&quot;value&quot;:&quot;copy&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-copy-01&quot;,&quot;route&quot;:&quot;/&quot;},{&quot;id&quot;:2,&quot;label&quot;:&quot;Export Items&quot;,&quot;value&quot;:&quot;export&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-share-05&quot;,&quot;route&quot;:&quot;/&quot;},{&quot;id&quot;:3,&quot;label&quot;:&quot;Delete Items&quot;,&quot;value&quot;:&quot;delete&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-delete-02&quot;,&quot;route&quot;:&quot;/&quot;},{&quot;id&quot;:4,&quot;label&quot;:&quot;Settings&quot;,&quot;value&quot;:&quot;settings&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-settings-01&quot;}]" class="expanded ltr hydrated">
    
      <s-button data-toggle="true" slot="dropdown-head" outlined="" class="s-btn s-btn--default default md outlined ltr hydrated" theme="default" target="_self">
        <i class="hgi-stroke hgi-settings-01"></i>
        Options
        <i class="hgi-stroke hgi-arrow-down-01"></i>
      </s-button>
    
  </s-dropdown>
```

</details>

### Multiselect

Story id `components-dropdown--multiselect`

![Multiselect](../../storybook/captures/stories/dropdown/multiselect.png)

Args:

```json
{
  "items": [
    {
      "id": 0,
      "label": "Sort Items",
      "value": "sort",
      "icon": "hgi-stroke hgi-sorting-01"
    },
    {
      "id": 1,
      "label": "Copy Items",
      "value": "copy",
      "icon": "hgi-stroke hgi-copy-01",
      "route": "/"
    },
    {
      "id": 2,
      "label": "Export Items",
      "value": "export",
      "icon": "hgi-stroke hgi-share-05",
      "route": "/"
    },
    {
      "id": 3,
      "label": "Delete Items",
      "value": "delete",
      "icon": "hgi-stroke hgi-delete-02",
      "route": "/"
    },
    {
      "id": 4,
      "label": "Settings",
      "value": "settings",
      "icon": "hgi-stroke hgi-settings-01"
    }
  ],
  "multiselect": true
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    #story--components-dropdown--default--primary-inner {
      height: 25vh !important;
    }
  </style>
  <s-dropdown multiselect="" layout="start" items="[{&quot;id&quot;:0,&quot;label&quot;:&quot;Sort Items&quot;,&quot;value&quot;:&quot;sort&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-sorting-01&quot;},{&quot;id&quot;:1,&quot;label&quot;:&quot;Copy Items&quot;,&quot;value&quot;:&quot;copy&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-copy-01&quot;,&quot;route&quot;:&quot;/&quot;},{&quot;id&quot;:2,&quot;label&quot;:&quot;Export Items&quot;,&quot;value&quot;:&quot;export&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-share-05&quot;,&quot;route&quot;:&quot;/&quot;},{&quot;id&quot;:3,&quot;label&quot;:&quot;Delete Items&quot;,&quot;value&quot;:&quot;delete&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-delete-02&quot;,&quot;route&quot;:&quot;/&quot;},{&quot;id&quot;:4,&quot;label&quot;:&quot;Settings&quot;,&quot;value&quot;:&quot;settings&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-settings-01&quot;}]" class="start ltr hydrated">
    
      <s-button data-toggle="true" slot="dropdown-head" outlined="" class="s-btn s-btn--default default md outlined ltr hydrated" theme="default" target="_self">
        <i class="hgi-stroke hgi-settings-01"></i>
        Options
        <i class="hgi-stroke hgi-arrow-down-01"></i>
      </s-button>
    
  </s-dropdown>
```

</details>

### With Images

Story id `components-dropdown--with-images`

![With Images](../../storybook/captures/stories/dropdown/with-images.png)

Args:

```json
{
  "selectable": true,
  "items": [
    {
      "id": 0,
      "label": "Avatar (s-avatar)",
      "value": "avatar",
      "avatar": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=80&h=80&fit=crop"
    },
    {
      "id": 1,
      "label": "Plain image (img)",
      "value": "plain-image",
      "image": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=80&h=80&fit=crop"
    },
    {
      "id": 2,
      "label": "Another avatar",
      "value": "avatar-2",
      "avatar": "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=80&h=80&fit=crop"
    },
    {
      "id": 3,
      "label": "Another plain image",
      "value": "plain-image-2",
      "image": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=80&h=80&fit=crop"
    },
    {
      "id": 4,
      "label": "Icon fallback",
      "value": "icon",
      "icon": "hgi-stroke hgi-settings-01"
    }
  ]
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    #story--components-dropdown--default--primary-inner {
      height: 25vh !important;
    }
  </style>
  <s-dropdown selectable="" layout="start" items="[{&quot;id&quot;:0,&quot;label&quot;:&quot;Avatar (s-avatar)&quot;,&quot;value&quot;:&quot;avatar&quot;,&quot;avatar&quot;:&quot;https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=80&amp;h=80&amp;fit=crop&quot;},{&quot;id&quot;:1,&quot;label&quot;:&quot;Plain image (img)&quot;,&quot;value&quot;:&quot;plain-image&quot;,&quot;image&quot;:&quot;https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=80&amp;h=80&amp;fit=crop&quot;},{&quot;id&quot;:2,&quot;label&quot;:&quot;Another avatar&quot;,&quot;value&quot;:&quot;avatar-2&quot;,&quot;avatar&quot;:&quot;https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=80&amp;h=80&amp;fit=crop&quot;},{&quot;id&quot;:3,&quot;label&quot;:&quot;Another plain image&quot;,&quot;value&quot;:&quot;plain-image-2&quot;,&quot;image&quot;:&quot;https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=80&amp;h=80&amp;fit=crop&quot;},{&quot;id&quot;:4,&quot;label&quot;:&quot;Icon fallback&quot;,&quot;value&quot;:&quot;icon&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-settings-01&quot;}]" class="start ltr hydrated">
    
      <s-button data-toggle="true" slot="dropdown-head" outlined="" class="s-btn s-btn--default default md outlined ltr hydrated" theme="default" target="_self">
        <i class="hgi-stroke hgi-settings-01"></i>
        Options
        <i class="hgi-stroke hgi-arrow-down-01"></i>
      </s-button>
    
  </s-dropdown>
```

</details>

### With Descriptions

Story id `components-dropdown--with-descriptions`

![With Descriptions](../../storybook/captures/stories/dropdown/with-descriptions.png)

Args:

```json
{
  "selectable": true,
  "sheetTitle": "Add file",
  "items": [
    {
      "id": 0,
      "label": "Upload file",
      "desc": "Upload the file straight from your device (up to 1024MB)",
      "value": "file",
      "icon": "hgi-stroke hgi-cloud-upload"
    },
    {
      "id": 1,
      "label": "File link",
      "desc": "For larger files, upload them to cloud storage then add the link",
      "value": "link",
      "icon": "hgi-stroke hgi-link-04"
    }
  ]
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    #story--components-dropdown--default--primary-inner {
      height: 25vh !important;
    }
  </style>
  <s-dropdown selectable="" sheet-title="Add file" layout="start" items="[{&quot;id&quot;:0,&quot;label&quot;:&quot;Upload file&quot;,&quot;desc&quot;:&quot;Upload the file straight from your device (up to 1024MB)&quot;,&quot;value&quot;:&quot;file&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-cloud-upload&quot;},{&quot;id&quot;:1,&quot;label&quot;:&quot;File link&quot;,&quot;desc&quot;:&quot;For larger files, upload them to cloud storage then add the link&quot;,&quot;value&quot;:&quot;link&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-link-04&quot;}]" class="start ltr hydrated">
    
      <s-button data-toggle="true" slot="dropdown-head" outlined="" class="s-btn s-btn--default default md outlined ltr hydrated" theme="default" target="_self">
        <i class="hgi-stroke hgi-settings-01"></i>
        Options
        <i class="hgi-stroke hgi-arrow-down-01"></i>
      </s-button>
    
  </s-dropdown>
```

</details>

### Custom Toggle

Story id `components-dropdown--custom-toggle`

![Custom Toggle](../../storybook/captures/stories/dropdown/custom-toggle.png)

Args:

```json
{
  "items": [
    {
      "id": 0,
      "label": "Sort Items",
      "value": "sort",
      "icon": "hgi-stroke hgi-sorting-01"
    },
    {
      "id": 1,
      "label": "Copy Items",
      "value": "copy",
      "icon": "hgi-stroke hgi-copy-01",
      "route": "/"
    },
    {
      "id": 2,
      "label": "Export Items",
      "value": "export",
      "icon": "hgi-stroke hgi-share-05",
      "route": "/"
    },
    {
      "id": 3,
      "label": "Delete Items",
      "value": "delete",
      "icon": "hgi-stroke hgi-delete-02",
      "route": "/"
    },
    {
      "id": 4,
      "label": "Settings",
      "value": "settings",
      "icon": "hgi-stroke hgi-settings-01"
    }
  ],
  "children": "\n      <span data-toggle=\"true\" slot=\"dropdown-head\" class=\"flex w-fit h-[2rem] items-center justify-center cursor-pointer rounded-md p-4 bg-gray-200 hover:bg-gray-300 hover:text-primary\">\n        Toggle\n      </span>\n    "
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    #story--components-dropdown--default--primary-inner {
      height: 25vh !important;
    }
  </style>
  <s-dropdown layout="start" items="[{&quot;id&quot;:0,&quot;label&quot;:&quot;Sort Items&quot;,&quot;value&quot;:&quot;sort&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-sorting-01&quot;},{&quot;id&quot;:1,&quot;label&quot;:&quot;Copy Items&quot;,&quot;value&quot;:&quot;copy&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-copy-01&quot;,&quot;route&quot;:&quot;/&quot;},{&quot;id&quot;:2,&quot;label&quot;:&quot;Export Items&quot;,&quot;value&quot;:&quot;export&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-share-05&quot;,&quot;route&quot;:&quot;/&quot;},{&quot;id&quot;:3,&quot;label&quot;:&quot;Delete Items&quot;,&quot;value&quot;:&quot;delete&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-delete-02&quot;,&quot;route&quot;:&quot;/&quot;},{&quot;id&quot;:4,&quot;label&quot;:&quot;Settings&quot;,&quot;value&quot;:&quot;settings&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-settings-01&quot;}]" class="start ltr hydrated">
    
      <span data-toggle="true" slot="dropdown-head" class="flex w-fit h-[2rem] items-center justify-center cursor-pointer rounded-md p-4 bg-gray-200 hover:bg-gray-300 hover:text-primary">
        Toggle
      </span>
    
  </s-dropdown>
```

</details>

### Loading

Story id `components-dropdown--loading`

![Loading](../../storybook/captures/stories/dropdown/loading.png)

Args:

```json
{
  "items": [
    {
      "id": 0,
      "label": "Sort Items",
      "value": "sort",
      "icon": "hgi-stroke hgi-sorting-01"
    },
    {
      "id": 1,
      "label": "Copy Items",
      "value": "copy",
      "icon": "hgi-stroke hgi-copy-01",
      "route": "/"
    },
    {
      "id": 2,
      "label": "Export Items",
      "value": "export",
      "icon": "hgi-stroke hgi-share-05",
      "route": "/"
    },
    {
      "id": 3,
      "label": "Delete Items",
      "value": "delete",
      "icon": "hgi-stroke hgi-delete-02",
      "route": "/"
    },
    {
      "id": 4,
      "label": "Settings",
      "value": "settings",
      "icon": "hgi-stroke hgi-settings-01"
    }
  ],
  "loading": true
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    #story--components-dropdown--default--primary-inner {
      height: 25vh !important;
    }
  </style>
  <s-dropdown loading="" layout="start" items="[{&quot;id&quot;:0,&quot;label&quot;:&quot;Sort Items&quot;,&quot;value&quot;:&quot;sort&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-sorting-01&quot;},{&quot;id&quot;:1,&quot;label&quot;:&quot;Copy Items&quot;,&quot;value&quot;:&quot;copy&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-copy-01&quot;,&quot;route&quot;:&quot;/&quot;},{&quot;id&quot;:2,&quot;label&quot;:&quot;Export Items&quot;,&quot;value&quot;:&quot;export&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-share-05&quot;,&quot;route&quot;:&quot;/&quot;},{&quot;id&quot;:3,&quot;label&quot;:&quot;Delete Items&quot;,&quot;value&quot;:&quot;delete&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-delete-02&quot;,&quot;route&quot;:&quot;/&quot;},{&quot;id&quot;:4,&quot;label&quot;:&quot;Settings&quot;,&quot;value&quot;:&quot;settings&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-settings-01&quot;}]" class="loading start ltr hydrated">
    
      <s-button data-toggle="true" loading="true" slot="dropdown-head" outlined="" class="s-btn s-btn--default default md outlined loading ltr hydrated" theme="default" target="_self">
        <i class="hgi-stroke hgi-settings-01"></i>
        Options
        <i class="hgi-stroke hgi-arrow-down-01"></i>
      </s-button>
    
  </s-dropdown>
```

</details>

### Disabled

Story id `components-dropdown--disabled`

![Disabled](../../storybook/captures/stories/dropdown/disabled.png)

Args:

```json
{
  "items": [
    {
      "id": 0,
      "label": "Sort Items",
      "value": "sort",
      "icon": "hgi-stroke hgi-sorting-01"
    },
    {
      "id": 1,
      "label": "Copy Items",
      "value": "copy",
      "icon": "hgi-stroke hgi-copy-01",
      "route": "/"
    },
    {
      "id": 2,
      "label": "Export Items",
      "value": "export",
      "icon": "hgi-stroke hgi-share-05",
      "route": "/"
    },
    {
      "id": 3,
      "label": "Delete Items",
      "value": "delete",
      "icon": "hgi-stroke hgi-delete-02",
      "route": "/"
    },
    {
      "id": 4,
      "label": "Settings",
      "value": "settings",
      "icon": "hgi-stroke hgi-settings-01"
    }
  ],
  "disabled": true
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    #story--components-dropdown--default--primary-inner {
      height: 25vh !important;
    }
  </style>
  <s-dropdown disabled="" layout="start" items="[{&quot;id&quot;:0,&quot;label&quot;:&quot;Sort Items&quot;,&quot;value&quot;:&quot;sort&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-sorting-01&quot;},{&quot;id&quot;:1,&quot;label&quot;:&quot;Copy Items&quot;,&quot;value&quot;:&quot;copy&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-copy-01&quot;,&quot;route&quot;:&quot;/&quot;},{&quot;id&quot;:2,&quot;label&quot;:&quot;Export Items&quot;,&quot;value&quot;:&quot;export&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-share-05&quot;,&quot;route&quot;:&quot;/&quot;},{&quot;id&quot;:3,&quot;label&quot;:&quot;Delete Items&quot;,&quot;value&quot;:&quot;delete&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-delete-02&quot;,&quot;route&quot;:&quot;/&quot;},{&quot;id&quot;:4,&quot;label&quot;:&quot;Settings&quot;,&quot;value&quot;:&quot;settings&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-settings-01&quot;}]" class="disabled start ltr hydrated">
    
      <s-button data-toggle="true" slot="dropdown-head" outlined="" class="s-btn s-btn--default default md outlined ltr hydrated" theme="default" target="_self">
        <i class="hgi-stroke hgi-settings-01"></i>
        Options
        <i class="hgi-stroke hgi-arrow-down-01"></i>
      </s-button>
    
  </s-dropdown>
```

</details>
