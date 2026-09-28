# Radio — active=On, size=--md, status=Default

- Figma file: `dnmyqzYKK9dUJjVHuIWMDS`
- Figma node id: `12459:14981`

## Code (verbatim from get_design_context)

```tsx
const assetPathPrefix = "figma-asset:";
const imgActiveOnStatusDefaultSizeMd = `${assetPathPrefix}/9504d.svg`;

type RadioProps = {
  className?: string;
  active?: "On";
  size?: "--md";
  status?: "Default";
};

function Radio({ className, active = "On", size = "--md", status = "Default" }: RadioProps) {
  return (
    <div className={className || "relative size-[20px]"} data-node-id="12459:14981">
      <img alt="" className="absolute block inset-0 max-w-none size-full" src={imgActiveOnStatusDefaultSizeMd} />
    </div>
  );
}
```

## Design tokens / variables

- None exposed in the returned code; the whole 20x20px radio is flattened to a single SVG asset by Figma (no fill/stroke tokens were surfaced).

## Component description (from Figma)

- No component description was included in the response.

## Assets

- `figma-asset:9504d.svg` — the entire radio (Active=On, Status=Default, Size=md), 20x20

## Notes

- Response was not flagged sparse; it is a single-asset render. The response contained no text styles, no token list and no keywords.
- Original asset URL prefix `https://www.figma.com/api/mcp/asset/<uuid>/` replaced with `figma-asset:` placeholder.
