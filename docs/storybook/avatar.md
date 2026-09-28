# Avatar

Storybook title `Components/Avatar` · source `./src/components/s-avatar/s-avatar.stories.tsx`

Tags rendered: `<s-avatar>`

An avatar is a graphical representation of a user, typically a photo or icon, used to represent a person or entity in a user interface.

## Props

| Prop | Type / control | Options | Default | Description |
|---|---|---|---|---|
| `url` | string |  |  | Image URL |
| `label` | string |  |  | Label displayed next to avatar image |
| `desc` | string |  |  | Description displayed below avatar label |
| `layout` | string | `circular`, `rounded` | `circular` | Layout variant, you can use either circular, rounded |
| `size` | string | `xs`, `sm`, `md`, `lg` | `md` | Avatar size |
| `shadow` | boolean |  | `false` | You can add shadow to the avatar image |
| `outlined` | boolean |  | `false` | You can also add outline to the avatar image |
| `loading` | boolean |  | `false` | Shows loading state for the avatar |
| `initials` | boolean |  | `false` | If you want to show initials instead of an image, you can use this property |
| `initialsLabel` | text |  | `undefined` | Custom text to extract initials from when initials=true. If not provided, will use the label prop. Supports 1-2 characters for direct display or longer text for auto-extraction. |
| `icon` | text |  |  | If you want to show an icon instead of an image, we are using huge icons, so you can use icons classes here like `hgi-stroke hgi-user-multiple-02` |
| `iconSize` | text |  | `md` | Custom icon size |
| `imageFit` | select | `cover`, `contain`, `fit` | `cover` | Image fit type, cover, contain, fit |
| `responsive` | boolean |  | `false` | If set to true, label and description will be hidden on mobile only avatar image will be visible |
| `isActive` | boolean |  | `false` | adds an active indicator to the avatar image to show that the user is active |
| `status` | select | `None`, `info`, `success`, `warning`, `danger` | `undefined` | Predefined status badge shown on the avatar thumbnail. Adds a colored icon badge and a matching border to the thumb. |

## Stories

### Default

Story id `components-avatar--default`

![Default](../../storybook/captures/stories/avatar/default.png)

Args:

```json
{
  "url": "https://i.pravatar.cc/100",
  "label": "James Bond",
  "desc": "Special agent 007",
  "layout": "circular",
  "size": "md",
  "shadow": false,
  "outlined": false,
  "loading": false
}
```

<details><summary>Rendered markup</summary>

```html
<s-avatar label="James Bond" desc="Special agent 007" layout="circular" size="md" url="https://i.pravatar.cc/100" class="s-avatar s-avatar--circular s-avatar--horizontal ltr md hydrated"></s-avatar>
```

</details>

### Circular

Story id `components-avatar--circular`

![Circular](../../storybook/captures/stories/avatar/circular.png)

Args:

```json
{
  "url": "https://i.pravatar.cc/100",
  "label": "James Bond",
  "desc": "Special agent 007",
  "layout": "circular",
  "size": "md",
  "shadow": false,
  "outlined": false,
  "loading": false
}
```

<details><summary>Rendered markup</summary>

```html
<s-avatar label="James Bond" desc="Special agent 007" layout="circular" size="md" url="https://i.pravatar.cc/100" class="s-avatar s-avatar--circular s-avatar--horizontal ltr md hydrated"></s-avatar>
```

</details>

### Rounded

Story id `components-avatar--rounded`

![Rounded](../../storybook/captures/stories/avatar/rounded.png)

Args:

```json
{
  "url": "https://i.pravatar.cc/100",
  "label": "James Bond",
  "desc": "Special agent 007",
  "layout": "rounded",
  "size": "md",
  "shadow": false,
  "outlined": false,
  "loading": false
}
```

<details><summary>Rendered markup</summary>

```html
<s-avatar label="James Bond" desc="Special agent 007" layout="rounded" size="md" url="https://i.pravatar.cc/100" class="s-avatar s-avatar--rounded s-avatar--horizontal ltr md hydrated"></s-avatar>
```

</details>

### Initials

Story id `components-avatar--initials`

![Initials](../../storybook/captures/stories/avatar/initials.png)

<details><summary>Rendered markup</summary>

```html
<div class="flex flex-col gap-6">
      <div class="flex flex-col gap-2">
        <h3 class="text-lg font-semibold">Auto-generated from Label</h3>
        <div class="flex gap-4">
          <s-avatar label="James Bond" desc="Special agent 007" size="md" initials="" class="s-avatar s-avatar--circular s-avatar--horizontal ltr md initials hydrated"></s-avatar>
          <s-avatar label="جيمس بوند" desc="عميل سري 007" size="md" initials="" class="s-avatar s-avatar--circular s-avatar--horizontal ltr md initials hydrated"></s-avatar>
          <s-avatar label="John" desc="Single name" size="md" initials="" class="s-avatar s-avatar--circular s-avatar--horizontal ltr md initials hydrated"></s-avatar>
        </div>
      </div>
      
      <div class="flex flex-col gap-2">
        <h3 class="text-lg font-semibold">Custom Initials (using initialsLabel)</h3>
        <div class="flex gap-4">
          <s-avatar label="Display Name" desc="Custom initials: JD" size="md" initials="" initials-label="JD" class="s-avatar s-avatar--circular s-avatar--horizontal ltr md initials hydrated"></s-avatar>
          <s-avatar label="User Profile" desc="Auto from John Doe" size="md" initials="" initials-label="John Doe" class="s-avatar s-avatar--circular s-avatar--horizontal ltr md initials hydrated"></s-avatar>
          <s-avatar label="Arabic User" desc="Auto from Arabic text" size="md" initials="" initials-label="جون دو" class="s-avatar s-avatar--circular s-avatar--horizontal ltr md initials hydrated"></s-avatar>
          <s-avatar label="Custom Arabic" desc="Direct Arabic initials" size="md" initials="" initials-label="ج د" class="s-avatar s-avatar--circular s-avatar--horizontal ltr md initials hydrated"></s-avatar>
        </div>
      </div>
    </div>
```

</details>

### Icons

Story id `components-avatar--icons`

![Icons](../../storybook/captures/stories/avatar/icons.png)

Args:

```json
{
  "label": "James Bond",
  "desc": "Special agent 007",
  "icon": "hgi-stroke hgi-store-verified-01",
  "iconSize": "md",
  "size": "md",
  "shadow": false,
  "outlined": true
}
```

<details><summary>Rendered markup</summary>

```html
<s-avatar label="James Bond" desc="Special agent 007" size="md" icon="hgi-stroke hgi-store-verified-01" icon-size="md" outlined="" class="s-avatar s-avatar--circular s-avatar--horizontal ltr md hydrated"></s-avatar>
```

</details>

### Icon Size Variants

Story id `components-avatar--icon-size-variants`

![Icon Size Variants](../../storybook/captures/stories/avatar/icon-size-variants.png)

Args:

```json
{
  "label": "James Bond",
  "desc": "Special agent 007",
  "icon": "hgi-stroke hgi-store-verified-01"
}
```

<details><summary>Rendered markup</summary>

```html
<div class="flex flex-wrap gap-4 items-end">
        
          <div class="flex flex-col items-center gap-2">
            <s-avatar label="James Bond" desc="Special agent 007" icon="hgi-stroke hgi-store-verified-01" icon-size="1.25rem" class="s-avatar s-avatar--circular s-avatar--horizontal ltr md hydrated"></s-avatar>
            <span class="text-xs text-dark-100">iconSize: 1.25rem</span>
          </div>
        
          <div class="flex flex-col items-center gap-2">
            <s-avatar label="James Bond" desc="Special agent 007" icon="hgi-stroke hgi-store-verified-01" icon-size="1.5rem" class="s-avatar s-avatar--circular s-avatar--horizontal ltr md hydrated"></s-avatar>
            <span class="text-xs text-dark-100">iconSize: 1.5rem</span>
          </div>
        
          <div class="flex flex-col items-center gap-2">
            <s-avatar label="James Bond" desc="Special agent 007" icon="hgi-stroke hgi-store-verified-01" icon-size="1.75rem" class="s-avatar s-avatar--circular s-avatar--horizontal ltr md hydrated"></s-avatar>
            <span class="text-xs text-dark-100">iconSize: 1.75rem</span>
          </div>
        
          <div class="flex flex-col items-center gap-2">
            <s-avatar label="James Bond" desc="Special agent 007" icon="hgi-stroke hgi-store-verified-01" icon-size="2rem" class="s-avatar s-avatar--circular s-avatar--horizontal ltr md hydrated"></s-avatar>
            <span class="text-xs text-dark-100">iconSize: 2rem</span>
          </div>
        
          <div class="flex flex-col items-center gap-2">
            <s-avatar label="James Bond" desc="Special agent 007" icon="hgi-stroke hgi-store-verified-01" icon-size="2.25rem" class="s-avatar s-avatar--circular s-avatar--horizontal ltr md hydrated"></s-avatar>
            <span class="text-xs text-dark-100">iconSize: 2.25rem</span>
          </div>
        
      </div>
```

</details>

### Shadow And Outline

Story id `components-avatar--shadow-and-outline`

![Shadow And Outline](../../storybook/captures/stories/avatar/shadow-and-outline.png)

<details><summary>Rendered markup</summary>

```html
<div class="flex items-center justify-start gap-4">
      <s-avatar shadow="" url="https://i.pravatar.cc/100" outlined="" class="s-avatar s-avatar--circular s-avatar--horizontal ltr md hydrated"></s-avatar>
      <s-avatar shadow="" url="https://i.pravatar.cc/100" outlined="" class="s-avatar s-avatar--circular s-avatar--horizontal ltr md hydrated"></s-avatar>
      <s-avatar shadow="" url="https://i.pravatar.cc/100" outlined="" class="s-avatar s-avatar--circular s-avatar--horizontal ltr md hydrated"></s-avatar>
    </div>
```

</details>

### Image Cover Fit

Story id `components-avatar--image-cover-fit`

![Image Cover Fit](../../storybook/captures/stories/avatar/image-cover-fit.png)

Args:

```json
{
  "url": "https://i.pravatar.cc/100",
  "label": "James Bond",
  "desc": "Special agent 007",
  "layout": "rounded",
  "size": "md",
  "shadow": false,
  "outlined": false,
  "loading": false,
  "imageFit": "cover"
}
```

<details><summary>Rendered markup</summary>

```html
<s-avatar label="James Bond" desc="Special agent 007" layout="rounded" size="md" image-fit="cover" url="https://i.pravatar.cc/100" class="s-avatar s-avatar--rounded s-avatar--horizontal ltr md hydrated"></s-avatar>
```

</details>

### Image Contain Fit

Story id `components-avatar--image-contain-fit`

![Image Contain Fit](../../storybook/captures/stories/avatar/image-contain-fit.png)

Args:

```json
{
  "url": "https://i.pravatar.cc/100",
  "label": "James Bond",
  "desc": "Special agent 007",
  "layout": "rounded",
  "size": "md",
  "shadow": false,
  "outlined": false,
  "loading": false,
  "imageFit": "contain"
}
```

<details><summary>Rendered markup</summary>

```html
<s-avatar label="James Bond" desc="Special agent 007" layout="rounded" size="md" image-fit="contain" url="https://i.pravatar.cc/100" class="s-avatar s-avatar--rounded s-avatar--horizontal ltr md hydrated"></s-avatar>
```

</details>

### Size Variations

Story id `components-avatar--size-variations`

![Size Variations](../../storybook/captures/stories/avatar/size-variations.png)

<details><summary>Rendered markup</summary>

```html
<div class="flex flex-col gap-4">
      <div class="flex gap-4">
        <s-avatar layout="circular" size="lg" url="https://i.pravatar.cc/150" class="s-avatar s-avatar--circular s-avatar--horizontal ltr lg hydrated"></s-avatar>
        <s-avatar layout="circular" size="md" url="https://i.pravatar.cc/100" class="s-avatar s-avatar--circular s-avatar--horizontal ltr md hydrated"></s-avatar>
        <s-avatar layout="circular" size="sm" url="https://i.pravatar.cc/50" class="s-avatar s-avatar--circular s-avatar--horizontal ltr sm hydrated"></s-avatar>
        <s-avatar layout="circular" size="xs" url="https://i.pravatar.cc/50" class="s-avatar s-avatar--circular s-avatar--horizontal ltr xs hydrated"></s-avatar>
      </div>
    </div>
```

</details>

### Loading State

Story id `components-avatar--loading-state`

![Loading State](../../storybook/captures/stories/avatar/loading-state.png)

Args:

```json
{
  "url": "https://i.pravatar.cc/100",
  "label": "James Bond",
  "desc": "Special agent 007",
  "layout": "rounded",
  "size": "md",
  "shadow": false,
  "outlined": false,
  "loading": true
}
```

<details><summary>Rendered markup</summary>

```html
<s-avatar label="James Bond" desc="Special agent 007" layout="rounded" size="md" url="https://i.pravatar.cc/100" loading="" class="s-avatar s-avatar--rounded s-avatar--horizontal ltr md loading hydrated"></s-avatar>
```

</details>

### Active State

Story id `components-avatar--active-state`

![Active State](../../storybook/captures/stories/avatar/active-state.png)

<details><summary>Rendered markup</summary>

```html
<div class="flex flex-col gap-4">
      <s-avatar label="James Bond" desc="Special agent 007" layout="circular" size="md" url="https://i.pravatar.cc/100" is-active="true" class="s-avatar s-avatar--circular s-avatar--horizontal ltr md hydrated"></s-avatar>
      <s-avatar label="James Bond" desc="Special agent 007" size="md" is-active="true" initials="" class="s-avatar s-avatar--circular s-avatar--horizontal ltr md initials hydrated"></s-avatar>
    </div>
```

</details>

### Responsive

Story id `components-avatar--responsive`

![Responsive](../../storybook/captures/stories/avatar/responsive.png)

Args:

```json
{
  "url": "https://i.pravatar.cc/100",
  "label": "James Bond",
  "desc": "Special agent 007",
  "layout": "rounded",
  "size": "md",
  "shadow": false,
  "outlined": false,
  "loading": false,
  "responsive": true,
  "imageFit": "cover"
}
```

<details><summary>Rendered markup</summary>

```html
<s-avatar label="James Bond" desc="Special agent 007" layout="rounded" size="md" image-fit="cover" url="https://i.pravatar.cc/100" responsive="" class="s-avatar s-avatar--rounded s-avatar--horizontal ltr md hydrated"></s-avatar>
```

</details>

### Without Thumbnail

Story id `components-avatar--without-thumbnail`

![Without Thumbnail](../../storybook/captures/stories/avatar/without-thumbnail.png)

Args:

```json
{
  "label": "James Bond",
  "desc": "Special agent 007"
}
```

<details><summary>Rendered markup</summary>

```html
<s-avatar label="James Bond" desc="Special agent 007" class="s-avatar s-avatar--circular s-avatar--horizontal ltr md hydrated"></s-avatar>
```

</details>

### Status Badge

Story id `components-avatar--status-badge`

![Status Badge](../../storybook/captures/stories/avatar/status-badge.png)

Args:

```json
{
  "url": "https://i.pravatar.cc/100",
  "label": "James Bond",
  "desc": "Special agent 007",
  "layout": "circular",
  "size": "md",
  "status": "info"
}
```

<details><summary>Rendered markup</summary>

```html
<s-avatar label="James Bond" desc="Special agent 007" layout="circular" size="md" url="https://i.pravatar.cc/100" status="info" class="s-avatar s-avatar--circular s-avatar--horizontal ltr md s-avatar--status-info hydrated"></s-avatar>
```

</details>

### Status Variants

Story id `components-avatar--status-variants`

![Status Variants](../../storybook/captures/stories/avatar/status-variants.png)

<details><summary>Rendered markup</summary>

```html
<div class="flex flex-col gap-8">
        
          <div class="flex flex-col gap-2">
            <p class="text-sm font-medium text-dark-100 capitalize">info</p>
            <div class="flex items-center gap-6">
              
                <div class="flex flex-col items-center gap-2">
                  <s-avatar layout="circular" size="xs" url="https://i.pravatar.cc/100" status="info" class="s-avatar s-avatar--circular s-avatar--horizontal ltr xs s-avatar--status-info hydrated"></s-avatar>
                  <span class="text-xs text-dark-100">xs</span>
                </div>
              
                <div class="flex flex-col items-center gap-2">
                  <s-avatar layout="circular" size="sm" url="https://i.pravatar.cc/100" status="info" class="s-avatar s-avatar--circular s-avatar--horizontal ltr sm s-avatar--status-info hydrated"></s-avatar>
                  <span class="text-xs text-dark-100">sm</span>
                </div>
              
                <div class="flex flex-col items-center gap-2">
                  <s-avatar layout="circular" size="md" url="https://i.pravatar.cc/100" status="info" class="s-avatar s-avatar--circular s-avatar--horizontal ltr md s-avatar--status-info hydrated"></s-avatar>
                  <span class="text-xs text-dark-100">md</span>
                </div>
              
                <div class="flex flex-col items-center gap-2">
                  <s-avatar layout="circular" size="lg" url="https://i.pravatar.cc/100" status="info" class="s-avatar s-avatar--circular s-avatar--horizontal ltr lg s-avatar--status-info hydrated"></s-avatar>
                  <span class="text-xs text-dark-100">lg</span>
                </div>
              
            </div>
          </div>
        
          <div class="flex flex-col gap-2">
            <p class="text-sm font-medium text-dark-100 capitalize">success</p>
            <div class="flex items-center gap-6">
              
                <div class="flex flex-col items-center gap-2">
                  <s-avatar layout="circular" size="xs" url="https://i.pravatar.cc/100" status="success" class="s-avatar s-avatar--circular s-avatar--horizontal ltr xs s-avatar--status-success hydrated"></s-avatar>
                  <span class="text-xs text-dark-100">xs</span>
                </div>
              
                <div class="flex flex-col items-center gap-2">
                  <s-avatar layout="circular" size="sm" url="https://i.pravatar.cc/100" status="success" class="s-avatar s-avatar--circular s-avatar--horizontal ltr sm s-avatar--status-success hydrated"></s-avatar>
                  <span class="text-xs text-dark-100">sm</span>
                </div>
              
                <div class="flex flex-col items-center gap-2">
                  <s-avatar layout="circular" size="md" url="https://i.pravatar.cc/100" status="success" class="s-avatar s-avatar--circular s-avatar--horizontal ltr md s-avatar--status-success hydrated"></s-avatar>
                  <span class="text-xs text-dark-100">md</span>
                </div>
              
                <div class="flex flex-col items-center gap-2">
                  <s-avatar layout="circular" size="lg" url="https://i.pravatar.cc/100" status="success" class="s-avatar s-avatar--circular s-avatar--horizontal ltr lg s-avatar--status-success hydrated"></s-avatar>
                  <span class="text-xs text-dark-100">lg</span>
                </div>
              
            </div>
          </div>
        
          <div class="flex flex-col gap-2">
            <p class="text-sm font-medium text-dark-100 capitalize">warning</p>
            <div class="flex items-center gap-6">
              
                <div class="flex flex-col items-center gap-2">
                  <s-avatar layout="circular" size="xs" url="https://i.pravatar.cc/100" status="warning" class="s-avatar s-avatar--circular s-avatar--horizontal ltr xs s-avatar--status-warning hydrated"></s-avatar>
                  <span class="text-xs text-dark-100">xs</span>
                </div>
              
                <div class="flex flex-col items-center gap-2">
                  <s-avatar layout="circular" size="sm" url="https://i.pravatar.cc/100" status="warning" class="s-avatar s-avatar--circular s-avatar--horizontal ltr sm s-avatar--status-warning hydrated"></s-avatar>
                  <span class="text-xs text-dark-100">sm</span>
                </div>
              
                <div class="flex flex-col items-center gap-2">
                  <s-avatar layout="circular" size="md" url="https://i.pravatar.cc/100" status="warning" class="s-avatar s-avatar--circular s-avatar--horizontal ltr md s-avatar--status-warning hydrated"></s-avatar>
                  <span class="text-xs text-dark-100">md</span>
                </div>
              
                <div class="flex flex-col items-center gap-2">
                  <s-avatar layout="circular" size="lg" url="https://i.pravatar.cc/100" status="warning" class="s-avatar s-avatar--circular s-avatar--horizontal ltr lg s-avatar--status-warning hydrated"></s-avatar>
                  <span class="text-xs text-dark-100">lg</span>
                </div>
              
            </div>
          </div>
        
          <div class="flex flex-col gap-2">
            <p class="text-sm font-medium text-dark-100 capitalize">danger</p>
            <div class="flex items-center gap-6">
              
                <div class="flex flex-col items-center gap-2">
                  <s-avatar layout="circular" size="xs" url="https://i.pravatar.cc/100" status="danger" class="s-avatar s-avatar--circular s-avatar--horizontal ltr xs s-avatar--status-danger hydrated"></s-avatar>
                  <span class="text-xs text-dark-100">xs</span>
                </div>
              
                <div class="flex flex-col items-center gap-2">
                  <s-avatar layout="circular" size="sm" url="https://i.pravatar.cc/100" status="danger" class="s-avatar s-avatar--circular s-avatar--horizontal ltr sm s-avatar--status-danger hydrated"></s-avatar>
                  <span class="text-xs text-dark-100">sm</span>
                </div>
              
                <div class="flex flex-col items-center gap-2">
                  <s-avatar layout="circular" size="md" url="https://i.pravatar.cc/100" status="danger" class="s-avatar s-avatar--circular s-avatar--horizontal ltr md s-avatar--status-danger hydrated"></s-avatar>
                  <span class="text-xs text-dark-100">md</span>
                </div>
              
                <div class="flex flex-col items-center gap-2">
                  <s-avatar layout="circular" size="lg" url="https://i.pravatar.cc/100" status="danger" class="s-avatar s-avatar--circular s-avatar--horizontal ltr lg s-avatar--status-danger hydrated"></s-avatar>
                  <span class="text-xs text-dark-100">lg</span>
                </div>
              
            </div>
          </div>
        
      </div>
```

</details>
