# OTP

Storybook title `Components/OTP` · source `./src/components/s-otp/s-otp.stories.tsx`

Tags rendered: `<s-otp>`

OTP (One-Time Password) component provides a user-friendly interface for entering and validating OTP codes. It supports configurable number of fields, timer functionality, and various sizes.

## Props

| Prop | Type / control | Options | Default | Description |
|---|---|---|---|---|
| `fields` | number |  | `4` | OTP fields number |
| `hasTimer` | boolean |  | `true` | Enable countdown state |
| `timer` | number |  | `60000` | Timer duration (in milliseconds) |
| `size` | string | `md`, `lg` | `md` | Fields siz |
| `resendLabel` | string |  | `Resend Code` | Resend button label |
| `hasError` | boolean |  | `false` | Error state |
| `canSend` |  |  |  | Emitted when the timer expires and user can resend OTP |
| `otpComplete` |  |  |  | Emitted when all OTP fields are filled with complete values |
| `fieldUpdated` |  |  |  | Emitted when any OTP field value is updated |
| `resendRequest` |  |  |  | Emitted when the resend button is clicked |

## Stories

### Default

Story id `components-otp--default`

![Default](../../storybook/captures/stories/otp/default.png)

Args:

```json
{
  "fields": 4,
  "hasTimer": true,
  "timer": 60000,
  "size": "md",
  "resendLabel": "Resend Code",
  "hasError": false
}
```

<details><summary>Rendered markup</summary>

```html
<s-otp size="md" fields="4" has-timer="true" timer="60000" resend-label="Resend Code" class="flex flex-col items-center justify-center gap-6 hydrated"></s-otp>
```

</details>

### Size Variants

Story id `components-otp--size-variants`

![Size Variants](../../storybook/captures/stories/otp/size-variants.png)

Args:

```json
{
  "fields": 4,
  "hasTimer": true,
  "timer": 60000,
  "size": "md",
  "resendLabel": "Resend Code",
  "hasError": false
}
```

<details><summary>Rendered markup</summary>

```html
<div class="flex flex-col gap-8">
        
          <div class="flex flex-col items-center gap-4">
            <h3 class="text-lg font-semibold">MD</h3>
            <s-otp size="md" fields="4" has-timer="true" timer="60000" resend-label="Resend Code" class="flex flex-col items-center justify-center gap-6 hydrated"></s-otp>
          </div>
        
          <div class="flex flex-col items-center gap-4">
            <h3 class="text-lg font-semibold">LG</h3>
            <s-otp size="lg" fields="4" has-timer="true" timer="60000" resend-label="Resend Code" class="flex flex-col items-center justify-center gap-6 hydrated"></s-otp>
          </div>
        
      </div>
```

</details>

### Field Variants

Story id `components-otp--field-variants`

![Field Variants](../../storybook/captures/stories/otp/field-variants.png)

Args:

```json
{
  "fields": 4,
  "hasTimer": true,
  "timer": 60000,
  "size": "md",
  "resendLabel": "Resend Code",
  "hasError": false
}
```

<details><summary>Rendered markup</summary>

```html
<div class="flex flex-col gap-8">
        
          <div class="flex flex-col items-center gap-4">
            <h3 class="text-lg font-semibold">4 Fields</h3>
            <s-otp size="md" fields="4" has-timer="true" timer="60000" resend-label="Resend Code" class="flex flex-col items-center justify-center gap-6 hydrated"></s-otp>
          </div>
        
          <div class="flex flex-col items-center gap-4">
            <h3 class="text-lg font-semibold">5 Fields</h3>
            <s-otp size="md" fields="5" has-timer="true" timer="60000" resend-label="Resend Code" class="flex flex-col items-center justify-center gap-6 hydrated"></s-otp>
          </div>
        
          <div class="flex flex-col items-center gap-4">
            <h3 class="text-lg font-semibold">6 Fields</h3>
            <s-otp size="md" fields="6" has-timer="true" timer="60000" resend-label="Resend Code" class="flex flex-col items-center justify-center gap-6 hydrated"></s-otp>
          </div>
        
      </div>
```

</details>

### Six Fields

Story id `components-otp--six-fields`

![Six Fields](../../storybook/captures/stories/otp/six-fields.png)

Args:

```json
{
  "fields": 6,
  "hasTimer": true,
  "timer": 60000,
  "size": "md",
  "resendLabel": "Resend Code",
  "hasError": false
}
```

<details><summary>Rendered markup</summary>

```html
<s-otp size="md" fields="6" has-timer="true" timer="60000" resend-label="Resend Code" class="flex flex-col items-center justify-center gap-6 hydrated"></s-otp>
```

</details>

### No Timer

Story id `components-otp--no-timer`

![No Timer](../../storybook/captures/stories/otp/no-timer.png)

Args:

```json
{
  "fields": 4,
  "size": "md",
  "resendLabel": "Resend Code",
  "hasError": false,
  "hasTimer": false
}
```

<details><summary>Rendered markup</summary>

```html
<s-otp size="md" fields="4" has-timer="false" resend-label="Resend Code" class="flex flex-col items-center justify-center gap-6 hydrated"></s-otp>
```

</details>

### Short Timer

Story id `components-otp--short-timer`

![Short Timer](../../storybook/captures/stories/otp/short-timer.png)

Args:

```json
{
  "fields": 4,
  "hasTimer": true,
  "timer": 10000,
  "size": "md",
  "resendLabel": "Resend Code",
  "hasError": false
}
```

<details><summary>Rendered markup</summary>

```html
<s-otp size="md" fields="4" has-timer="true" timer="10000" resend-label="Resend Code" class="flex flex-col items-center justify-center gap-6 hydrated"></s-otp>
```

</details>

### Custom Resend Label

Story id `components-otp--custom-resend-label`

![Custom Resend Label](../../storybook/captures/stories/otp/custom-resend-label.png)

Args:

```json
{
  "fields": 4,
  "hasTimer": true,
  "timer": 60000,
  "size": "md",
  "resendLabel": "Send Again",
  "hasError": false
}
```

<details><summary>Rendered markup</summary>

```html
<s-otp size="md" fields="4" has-timer="true" timer="60000" resend-label="Send Again" class="flex flex-col items-center justify-center gap-6 hydrated"></s-otp>
```

</details>

### Has Error

Story id `components-otp--has-error`

![Has Error](../../storybook/captures/stories/otp/has-error.png)

Args:

```json
{
  "fields": 4,
  "hasTimer": true,
  "timer": 60000,
  "size": "md",
  "resendLabel": "Resend Code",
  "hasError": true
}
```

<details><summary>Rendered markup</summary>

```html
<s-otp size="md" fields="4" has-timer="true" timer="60000" resend-label="Resend Code" has-error="" class="flex flex-col items-center justify-center gap-6 hydrated"></s-otp>
```

</details>
