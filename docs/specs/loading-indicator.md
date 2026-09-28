# LoadingIndicator — size="xxl- 88px", type=Spinner

- Figma file: `dnmyqzYKK9dUJjVHuIWMDS`
- Figma node id: `27716:13238`

## Code (verbatim from get_design_context)

```tsx
const assetPathPrefix = "figma-asset:";
const imgSizeXxl88PxTypeSpinner = `${assetPathPrefix}/12e59.svg`;

type LoadingIndicatorProps = {
  className?: string;
  size?: "xxl- 88px";
  type?: "Spinner";
};

function LoadingIndicator({ className, size = "xxl- 88px", type = "Spinner" }: LoadingIndicatorProps) {
  return (
    <div className={className || "relative size-[88px]"} data-node-id="27716:13238">
      <img alt="" className="absolute block inset-0 max-w-none size-full" src={imgSizeXxl88PxTypeSpinner} />
    </div>
  );
}
```

## Design tokens / variables

- None exposed in the returned code; the 88x88px spinner is flattened to a single SVG asset.

## Component description (from Figma)

- No component description or text styles were included in the response.

## Assets

- `figma-asset:12e59.svg` — the entire spinner (Size=xxl 88px, Type=Spinner), 88x88

## Notes

- Original asset URL prefix `https://www.figma.com/api/mcp/asset/<uuid>/` replaced with `figma-asset:` placeholder.
