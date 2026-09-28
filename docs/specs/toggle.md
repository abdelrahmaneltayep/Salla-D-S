# Toggle — language=English, selected=true, disabled=false, loading=false, size=default-24px

- Figma file: `dnmyqzYKK9dUJjVHuIWMDS`
- Figma node id: `12411:21836`
- Parent component set: `12411:21835` (Toggle)

## Code (verbatim from get_design_context)

```tsx
const assetPathPrefix = "figma-asset:";
const imgLanguageEnglishSelectedTrueDisabledFalseLoadingFalseSizeDefault24Px = `${assetPathPrefix}/e141c.svg`;

type ToggleProps = {
  className?: string;
  disabled?: "false";
  language?: "English";
  loading?: "false";
  selected?: "true";
  size?: "default-24px";
};

function Toggle({ className, disabled = "false", language = "English", loading = "false", selected = "true", size = "default-24px" }: ToggleProps) {
  return (
    <div className={className || "h-[24px] relative w-[39px]"} data-node-id="12411:21836">
      <img alt="" className="absolute block inset-0 max-w-none size-full" src={imgLanguageEnglishSelectedTrueDisabledFalseLoadingFalseSizeDefault24Px} />
    </div>
  );
}
```

## Design tokens / variables

- None exposed in the returned code; the toggle (39x24px) is flattened to a single SVG asset by Figma.

## Component description (from Figma)

**Toggle** — Node ID: 12411:21835. Keywords: [On/Off switch, State control, Binary selection, Activation switch, Feature flag, UI control, Interactive element, Power button, مفتاح تبديل, زر تفعيل/إيقاف, التحكم في الحالة, اختيار ثنائي, مفتاح تشغيل, زر الطاقة, عنصر تحكم]

## Assets

- `figma-asset:e141c.svg` — the entire toggle (Language=English, Selected=true, Disabled=false, Loading=false, Size=default-24px), 39x24

## Notes

- Original asset URL prefix `https://www.figma.com/api/mcp/asset/<uuid>/` replaced with `figma-asset:` placeholder.
