# Maps

Storybook title `Components/Maps` · source `./src/components/s-maps/s-map.stories.tsx`

Tags rendered: `<s-maps>`

Maps component provides an interactive map interface with search functionality and location services.

## Props

| Prop | Type / control | Options | Default | Description |
|---|---|---|---|---|
| `apiKey` | string |  |  | Google Maps API Key. |
| `hasCurrentLocationButton` | boolean |  | `false` | Show or hide the 'Go to current location' button. |
| `latitude` | number |  | `21.4255186` | The latitude coordinate of the map's center |
| `longitude` | number |  | `39.7858435` | The longitude coordinate of the map's center |
| `searchPlaceholder` | string |  | `Search...` | Search input placeholder. |
| `height` | string |  | `300px` | Map wrapper height. Accepts CSS height property values. |

## Stories

### Default

Story id `components-maps--default`

![Default](../../storybook/captures/stories/maps/default.png)

Args:

```json
{
  "apiKey": "",
  "hasCurrentLocationButton": false,
  "latitude": 21.4255186,
  "longitude": 39.7858435,
  "searchPlaceholder": "Search...",
  "height": "300px"
}
```

<details><summary>Rendered markup</summary>

```html
<s-maps api-key="" has-current-location-button="false" latitude="21.4255186" longitude="39.7858435" height="300px" search-placeholder="Search..." value="21.4255186,39.7858435" class="w-full relative rounded hydrated" style="height: 300px;">
  </s-maps>
```

</details>

### With Current Location Button

Story id `components-maps--with-current-location-button`

![With Current Location Button](../../storybook/captures/stories/maps/with-current-location-button.png)

Args:

```json
{
  "apiKey": "",
  "hasCurrentLocationButton": true,
  "latitude": 21.4255186,
  "longitude": 39.7858435,
  "searchPlaceholder": "Search for a place",
  "height": "300px"
}
```

<details><summary>Rendered markup</summary>

```html
<s-maps api-key="" has-current-location-button="true" latitude="21.4255186" longitude="39.7858435" height="300px" search-placeholder="Search for a place" value="21.4255186,39.7858435" class="w-full relative rounded hydrated" style="height: 300px;">
  </s-maps>
```

</details>

### Custom Coordinates

Story id `components-maps--custom-coordinates`

![Custom Coordinates](../../storybook/captures/stories/maps/custom-coordinates.png)

Args:

```json
{
  "apiKey": "",
  "hasCurrentLocationButton": false,
  "latitude": 34.052235,
  "longitude": -118.243683,
  "searchPlaceholder": "Search...",
  "height": "300px"
}
```

<details><summary>Rendered markup</summary>

```html
<s-maps api-key="" has-current-location-button="false" latitude="34.052235" longitude="-118.243683" height="300px" search-placeholder="Search..." value="34.052235,-118.243683" class="w-full relative rounded hydrated" style="height: 300px;">
  </s-maps>
```

</details>

### Custom Height

Story id `components-maps--custom-height`

![Custom Height](../../storybook/captures/stories/maps/custom-height.png)

Args:

```json
{
  "apiKey": "",
  "hasCurrentLocationButton": false,
  "latitude": 21.4255186,
  "longitude": 39.7858435,
  "searchPlaceholder": "Search...",
  "height": "500px"
}
```

<details><summary>Rendered markup</summary>

```html
<s-maps api-key="" has-current-location-button="false" latitude="21.4255186" longitude="39.7858435" height="500px" search-placeholder="Search..." value="21.4255186,39.7858435" class="w-full relative rounded hydrated" style="height: 500px;">
  </s-maps>
```

</details>
