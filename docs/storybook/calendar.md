# Calendar

Storybook title `Components/Calendar` · source `./src/components/s-calendar/s-calendar.stories.tsx`

Tags rendered: `<s-calendar>`

Calendar is a component that provides date or time selection functionality.

## Props

| Prop | Type / control | Options | Default | Description |
|---|---|---|---|---|
| `placeholder` | string |  | `Select value` | Field placeholder |
| `value` | text |  | `[]` | Current value of the calendar (string or array of strings) for multiple values |
| `type` | select | `range`, `time`, `single`, `multiple` | `single` | Calendar type, range, time, single or multiple |
| `layout` | select | `start`, `end` | `start` | Calendar layout |
| `minDate` | text |  | `null` | Minimum date selectable |
| `maxDate` | text |  | `null` | Maximum date selectable |
| `dateFormat` | text |  | `DD-MM-YYYY` | Format used for displaying/parsing dates and disabledDates (e.g. 'DD-MM-YYYY', 'YYYY-MM-DD'). |
| `loading` | boolean |  | `false` | Loading state |
| `disabled` | boolean |  | `false` | Disabled state |
| `required` | boolean |  | `false` | Required field |
| `hasError` | boolean |  | `false` | Error state |
| `inline` | boolean |  | `false` | Inline calendar |
| `is24Hr` | boolean |  | `false` | Enable 24 hour format |
| `isOpen` | boolean |  | `false` | Open calendar popup on start (only works when inline is false) |
| `portal` | boolean |  | `false` | If true, appends the calendar dropdown to the body instead of attaching it to the input. Useful for avoiding overflow issues in containers with overflow: hidden. |
| `disabledDays` | object |  | `[]` | Weekdays to disable selection for. 0 = Sunday, 6 = Saturday. Accepts numbers (0–6) or day names/abbreviations, e.g. ['sun', 'monday'] |
| `disabledDates` | object |  | `[]` | Specific dates to disable. Must match the selected dateFormat. Example (DD-MM-YYYY): ['07-09-2025', '10-09-2025'] |
| `dateRangeChanged` |  |  |  | Emitted when the date range changes. |
| `valueChanged` |  |  |  | Emitted when the calendar value changes. |

## Stories

### Default

Story id `components-calendar--default`

![Default](../../storybook/captures/stories/calendar/default.png)

Args:

```json
{
  "placeholder": "Select value"
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    #story--components-calendar--default--primary-inner {
      height: 25vh !important;
    }
  </style>
  <s-calendar placeholder="Select value" class="s-calendar date ltr start hydrated">
    <i class="hgi-stroke hgi-calendar-03" slot="start"></i>
    </s-calendar>
```

</details>

### Single

Story id `components-calendar--single`

![Single](../../storybook/captures/stories/calendar/single.png)

Args:

```json
{
  "placeholder": "Select a single date",
  "type": "single"
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    #story--components-calendar--default--primary-inner {
      height: 25vh !important;
    }
  </style>
  <s-calendar placeholder="Select a single date" type="single" class="s-calendar date ltr start hydrated">
    <i class="hgi-stroke hgi-calendar-03" slot="start"></i>
    </s-calendar>
```

</details>

### Multiple

Story id `components-calendar--multiple`

![Multiple](../../storybook/captures/stories/calendar/multiple.png)

Args:

```json
{
  "placeholder": "Select multiple dates",
  "type": "multiple"
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    #story--components-calendar--default--primary-inner {
      height: 25vh !important;
    }
  </style>
  <s-calendar placeholder="Select multiple dates" type="multiple" class="s-calendar date ltr start hydrated">
    <i class="hgi-stroke hgi-calendar-03" slot="start"></i>
    </s-calendar>
```

</details>

### Range

Story id `components-calendar--range`

![Range](../../storybook/captures/stories/calendar/range.png)

Args:

```json
{
  "placeholder": "Select date range",
  "type": "range"
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    #story--components-calendar--default--primary-inner {
      height: 25vh !important;
    }
  </style>
  <s-calendar placeholder="Select date range" type="range" class="s-calendar date ltr start hydrated">
    <i class="hgi-stroke hgi-calendar-03" slot="start"></i>
    </s-calendar>
```

</details>

### Time

Story id `components-calendar--time`

![Time](../../storybook/captures/stories/calendar/time.png)

Args:

```json
{
  "placeholder": "Select time",
  "type": "time"
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    #story--components-calendar--default--primary-inner {
      height: 25vh !important;
    }
  </style>
  <s-calendar placeholder="Select time" type="time" class="s-calendar date ltr start hydrated">
    <i class="hgi-stroke hgi-calendar-03" slot="start"></i>
    </s-calendar>
```

</details>

### Initial Value

Story id `components-calendar--initial-value`

![Initial Value](../../storybook/captures/stories/calendar/initial-value.png)

Args:

```json
{
  "placeholder": "Select value",
  "value": "2023-12-15"
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    #story--components-calendar--default--primary-inner {
      height: 25vh !important;
    }
  </style>
  <s-calendar placeholder="Select value" value="2023-12-15" class="s-calendar date ltr start hydrated">
    <i class="hgi-stroke hgi-calendar-03" slot="start"></i>
    </s-calendar>
```

</details>

### Multiple Values

Story id `components-calendar--multiple-values`

![Multiple Values](../../storybook/captures/stories/calendar/multiple-values.png)

Args:

```json
{
  "placeholder": "Select value",
  "type": "multiple",
  "value": [
    "2023-12-15",
    "2023-12-20"
  ]
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    #story--components-calendar--default--primary-inner {
      height: 25vh !important;
    }
  </style>
  <s-calendar placeholder="Select value" type="multiple" value="2023-12-15,2023-12-20" class="s-calendar date ltr start hydrated">
    <i class="hgi-stroke hgi-calendar-03" slot="start"></i>
    </s-calendar>
```

</details>

### Layout End

Story id `components-calendar--layout-end`

![Layout End](../../storybook/captures/stories/calendar/layout-end.png)

Args:

```json
{
  "placeholder": "Select value",
  "layout": "end"
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    #story--components-calendar--default--primary-inner {
      height: 25vh !important;
    }
  </style>
  <s-calendar placeholder="Select value" layout="end" class="s-calendar date ltr end hydrated">
    <i class="hgi-stroke hgi-calendar-03" slot="start"></i>
    </s-calendar>
```

</details>

### Min Max Date

Story id `components-calendar--min-max-date`

![Min Max Date](../../storybook/captures/stories/calendar/min-max-date.png)

Args:

```json
{
  "placeholder": "Select value",
  "minDate": "2025-07-28",
  "maxDate": "2025-08-28"
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    #story--components-calendar--default--primary-inner {
      height: 25vh !important;
    }
  </style>
  <s-calendar placeholder="Select value" min-date="2025-07-28" max-date="2025-08-28" class="s-calendar date ltr start hydrated">
    <i class="hgi-stroke hgi-calendar-03" slot="start"></i>
    </s-calendar>
```

</details>

### Hour Format

Story id `components-calendar--hour-format`

![Hour Format](../../storybook/captures/stories/calendar/hour-format.png)

Args:

```json
{
  "placeholder": "Select value",
  "is24Hr": true
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    #story--components-calendar--default--primary-inner {
      height: 25vh !important;
    }
  </style>
  <s-calendar placeholder="Select value" is24-hr="" class="s-calendar date ltr start hydrated">
    <i class="hgi-stroke hgi-calendar-03" slot="start"></i>
    </s-calendar>
```

</details>

### Loading

Story id `components-calendar--loading`

![Loading](../../storybook/captures/stories/calendar/loading.png)

Args:

```json
{
  "placeholder": "Loading...",
  "loading": true
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    #story--components-calendar--default--primary-inner {
      height: 25vh !important;
    }
  </style>
  <s-calendar placeholder="Loading..." loading="" class="s-calendar loading date ltr start hydrated">
    <i class="hgi-stroke hgi-calendar-03" slot="start"></i>
    </s-calendar>
```

</details>

### Disabled

Story id `components-calendar--disabled`

![Disabled](../../storybook/captures/stories/calendar/disabled.png)

Args:

```json
{
  "placeholder": "Select value",
  "disabled": true
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    #story--components-calendar--default--primary-inner {
      height: 25vh !important;
    }
  </style>
  <s-calendar placeholder="Select value" disabled="" class="s-calendar disabled date ltr start hydrated">
    <i class="hgi-stroke hgi-calendar-03" slot="start"></i>
    </s-calendar>
```

</details>

### Has Error

Story id `components-calendar--has-error`

![Has Error](../../storybook/captures/stories/calendar/has-error.png)

Args:

```json
{
  "placeholder": "Select value",
  "hasError": true
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    #story--components-calendar--default--primary-inner {
      height: 25vh !important;
    }
  </style>
  <s-calendar placeholder="Select value" has-error="" class="s-calendar date has-error ltr start hydrated">
    <i class="hgi-stroke hgi-calendar-03" slot="start"></i>
    </s-calendar>
```

</details>

### Required

Story id `components-calendar--required`

![Required](../../storybook/captures/stories/calendar/required.png)

Args:

```json
{
  "placeholder": "Select value",
  "required": true
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    #story--components-calendar--default--primary-inner {
      height: 25vh !important;
    }
  </style>
  <s-calendar placeholder="Select value" required="" class="s-calendar required date ltr start hydrated">
    <i class="hgi-stroke hgi-calendar-03" slot="start"></i>
    </s-calendar>
```

</details>

### Inline

Story id `components-calendar--inline`

![Inline](../../storybook/captures/stories/calendar/inline.png)

Args:

```json
{
  "placeholder": "Select value",
  "inline": true
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    #story--components-calendar--default--primary-inner {
      height: 25vh !important;
    }
  </style>
  <s-calendar placeholder="Select value" inline="" class="s-calendar s-calendar--inline date ltr start hydrated">
    null
    </s-calendar>
```

</details>

### Disabled Weekends

Story id `components-calendar--disabled-weekends`

![Disabled Weekends](../../storybook/captures/stories/calendar/disabled-weekends.png)

Args:

```json
{
  "placeholder": "Select value (Weekends disabled)",
  "disabledDays": [
    0,
    6
  ]
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    #story--components-calendar--default--primary-inner {
      height: 25vh !important;
    }
  </style>
  <s-calendar placeholder="Select value (Weekends disabled)" disabled-days="[0,6]" class="s-calendar date ltr start hydrated">
    <i class="hgi-stroke hgi-calendar-03" slot="start"></i>
    </s-calendar>
```

</details>

### Disabled Weekdays

Story id `components-calendar--disabled-weekdays`

![Disabled Weekdays](../../storybook/captures/stories/calendar/disabled-weekdays.png)

Args:

```json
{
  "placeholder": "Select value (Weekdays disabled)",
  "disabledDays": [
    1,
    2,
    3,
    4,
    5
  ]
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    #story--components-calendar--default--primary-inner {
      height: 25vh !important;
    }
  </style>
  <s-calendar placeholder="Select value (Weekdays disabled)" disabled-days="[1,2,3,4,5]" class="s-calendar date ltr start hydrated">
    <i class="hgi-stroke hgi-calendar-03" slot="start"></i>
    </s-calendar>
```

</details>

### Disabled Specific Days

Story id `components-calendar--disabled-specific-days`

![Disabled Specific Days](../../storybook/captures/stories/calendar/disabled-specific-days.png)

Args:

```json
{
  "placeholder": "Select value (Wed, Fri disabled)",
  "disabledDays": [
    3,
    5
  ]
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    #story--components-calendar--default--primary-inner {
      height: 25vh !important;
    }
  </style>
  <s-calendar placeholder="Select value (Wed, Fri disabled)" disabled-days="[3,5]" class="s-calendar date ltr start hydrated">
    <i class="hgi-stroke hgi-calendar-03" slot="start"></i>
    </s-calendar>
```

</details>

### Disabled Specific Dates

Story id `components-calendar--disabled-specific-dates`

![Disabled Specific Dates](../../storybook/captures/stories/calendar/disabled-specific-dates.png)

Args:

```json
{
  "placeholder": "Select value (Specific dates disabled)",
  "dateFormat": "DD-MM-YYYY",
  "disabledDates": [
    "07-09-2025",
    "10-09-2025"
  ]
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    #story--components-calendar--default--primary-inner {
      height: 25vh !important;
    }
  </style>
  <s-calendar placeholder="Select value (Specific dates disabled)" date-format="DD-MM-YYYY" disabled-dates="[&quot;07-09-2025&quot;,&quot;10-09-2025&quot;]" class="s-calendar date ltr start hydrated">
    <i class="hgi-stroke hgi-calendar-03" slot="start"></i>
    </s-calendar>
```

</details>

### Disabled Dates Custom Format

Story id `components-calendar--disabled-dates-custom-format`

![Disabled Dates Custom Format](../../storybook/captures/stories/calendar/disabled-dates-custom-format.png)

Args:

```json
{
  "placeholder": "Select value (Custom format & disabled dates)",
  "dateFormat": "YYYY-MM-DD",
  "disabledDates": [
    "2025-09-07",
    "2025-09-10"
  ]
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    #story--components-calendar--default--primary-inner {
      height: 25vh !important;
    }
  </style>
  <s-calendar placeholder="Select value (Custom format &amp; disabled dates)" date-format="YYYY-MM-DD" disabled-dates="[&quot;2025-09-07&quot;,&quot;2025-09-10&quot;]" class="s-calendar date ltr start hydrated">
    <i class="hgi-stroke hgi-calendar-03" slot="start"></i>
    </s-calendar>
```

</details>

### Disabled Days And Dates Combined

Story id `components-calendar--disabled-days-and-dates-combined`

![Disabled Days And Dates Combined](../../storybook/captures/stories/calendar/disabled-days-and-dates-combined.png)

Args:

```json
{
  "placeholder": "Weekends + specific dates disabled",
  "disabledDays": [
    0,
    6
  ],
  "dateFormat": "DD-MM-YYYY",
  "disabledDates": [
    "15-09-2025"
  ]
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    #story--components-calendar--default--primary-inner {
      height: 25vh !important;
    }
  </style>
  <s-calendar placeholder="Weekends + specific dates disabled" date-format="DD-MM-YYYY" disabled-days="[0,6]" disabled-dates="[&quot;15-09-2025&quot;]" class="s-calendar date ltr start hydrated">
    <i class="hgi-stroke hgi-calendar-03" slot="start"></i>
    </s-calendar>
```

</details>

### Disabled Days With Names

Story id `components-calendar--disabled-days-with-names`

![Disabled Days With Names](../../storybook/captures/stories/calendar/disabled-days-with-names.png)

Args:

```json
{
  "placeholder": "Select value (Sun, Mon disabled)",
  "disabledDays": [
    "sunday",
    "monday"
  ]
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    #story--components-calendar--default--primary-inner {
      height: 25vh !important;
    }
  </style>
  <s-calendar placeholder="Select value (Sun, Mon disabled)" disabled-days="[&quot;sunday&quot;,&quot;monday&quot;]" class="s-calendar date ltr start hydrated">
    <i class="hgi-stroke hgi-calendar-03" slot="start"></i>
    </s-calendar>
```

</details>

### Disabled Days With Abbreviations

Story id `components-calendar--disabled-days-with-abbreviations`

![Disabled Days With Abbreviations](../../storybook/captures/stories/calendar/disabled-days-with-abbreviations.png)

Args:

```json
{
  "placeholder": "Select value (Tue, Thu disabled)",
  "disabledDays": [
    "tue",
    "thu"
  ]
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    #story--components-calendar--default--primary-inner {
      height: 25vh !important;
    }
  </style>
  <s-calendar placeholder="Select value (Tue, Thu disabled)" disabled-days="[&quot;tue&quot;,&quot;thu&quot;]" class="s-calendar date ltr start hydrated">
    <i class="hgi-stroke hgi-calendar-03" slot="start"></i>
    </s-calendar>
```

</details>

### Disabled Days Mixed

Story id `components-calendar--disabled-days-mixed`

![Disabled Days Mixed](../../storybook/captures/stories/calendar/disabled-days-mixed.png)

Args:

```json
{
  "placeholder": "Select value (Mixed format)",
  "disabledDays": [
    0,
    "wednesday",
    "fri"
  ]
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    #story--components-calendar--default--primary-inner {
      height: 25vh !important;
    }
  </style>
  <s-calendar placeholder="Select value (Mixed format)" disabled-days="[0,&quot;wednesday&quot;,&quot;fri&quot;]" class="s-calendar date ltr start hydrated">
    <i class="hgi-stroke hgi-calendar-03" slot="start"></i>
    </s-calendar>
```

</details>

### Disabled Days Inline

Story id `components-calendar--disabled-days-inline`

![Disabled Days Inline](../../storybook/captures/stories/calendar/disabled-days-inline.png)

Args:

```json
{
  "placeholder": "Select value",
  "inline": true,
  "disabledDays": [
    0,
    6
  ]
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    #story--components-calendar--default--primary-inner {
      height: 25vh !important;
    }
  </style>
  <s-calendar placeholder="Select value" inline="" disabled-days="[0,6]" class="s-calendar s-calendar--inline date ltr start hydrated">
    null
    </s-calendar>
```

</details>

### Disabled Days Range

Story id `components-calendar--disabled-days-range`

![Disabled Days Range](../../storybook/captures/stories/calendar/disabled-days-range.png)

Args:

```json
{
  "placeholder": "Select date range (Weekends disabled)",
  "type": "range",
  "disabledDays": [
    0,
    6
  ]
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    #story--components-calendar--default--primary-inner {
      height: 25vh !important;
    }
  </style>
  <s-calendar placeholder="Select date range (Weekends disabled)" type="range" disabled-days="[0,6]" class="s-calendar date ltr start hydrated">
    <i class="hgi-stroke hgi-calendar-03" slot="start"></i>
    </s-calendar>
```

</details>

### Disabled Days Multiple

Story id `components-calendar--disabled-days-multiple`

![Disabled Days Multiple](../../storybook/captures/stories/calendar/disabled-days-multiple.png)

Args:

```json
{
  "placeholder": "Select multiple dates (Wed, Fri disabled)",
  "type": "multiple",
  "disabledDays": [
    3,
    5
  ]
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    #story--components-calendar--default--primary-inner {
      height: 25vh !important;
    }
  </style>
  <s-calendar placeholder="Select multiple dates (Wed, Fri disabled)" type="multiple" disabled-days="[3,5]" class="s-calendar date ltr start hydrated">
    <i class="hgi-stroke hgi-calendar-03" slot="start"></i>
    </s-calendar>
```

</details>

### Open On Start

Story id `components-calendar--open-on-start`

![Open On Start](../../storybook/captures/stories/calendar/open-on-start.png)

Args:

```json
{
  "placeholder": "Calendar opens on start",
  "isOpen": true
}
```

<details><summary>Rendered markup</summary>

```html
<style>
    #story--components-calendar--default--primary-inner {
      height: 25vh !important;
    }
  </style>
  <s-calendar placeholder="Calendar opens on start" is-open="" class="s-calendar date ltr start hydrated">
    <i class="hgi-stroke hgi-calendar-03" slot="start"></i>
    </s-calendar>
```

</details>
