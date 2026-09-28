# Avatar — variant=--avatar, radius=--circular, size=xs, statusIndicator=true

- Figma file: `dnmyqzYKK9dUJjVHuIWMDS`
- Figma node id: `15368:1124`

## Code (verbatim from get_design_context)

```tsx
const assetPathPrefix = "figma-asset:";
const imgAvatarplaholderImages = `${assetPathPrefix}/3f02b.png`;

type AvatarProps = {
  className?: string;
  radius?: "--circular";
  size?: "xs";
  statusIndicator?: boolean;
  variant?: "--avatar";
};

function Avatar({ className, radius = "--circular", size = "xs", statusIndicator = true, variant = "--avatar" }: AvatarProps) {
  return (
    <div className={className || "content-stretch flex items-center relative rounded-[var(--radius\\/full,9999px)]"} data-node-id="15368:1124">
      <div className="bg-[var(--background\/default\/white,white)] border-0 border-[var(--border\/default,#eee)] border-solid overflow-clip relative rounded-[var(--radius\/full,8749.125px)] shrink-0 size-[24px]" data-node-id="15368:1125" data-name="_AvatarplaholderImages">
        <div className="absolute inset-0 overflow-hidden pointer-events-none">
          <img alt="" className="absolute h-[220.09%] left-[-34.37%] max-w-none top-[9.68%] w-[171.88%]" src={imgAvatarplaholderImages} />
        </div>
      </div>
      {statusIndicator && <div className="absolute bg-[var(--success\/success-dark,#008c56)] bottom-0 max-h-[6px] max-w-[6px] min-h-[6px] min-w-[6px] right-0 rounded-[var(--radius\/full,9999px)] size-[6px]" data-node-id="15370:1636" data-name="_Base Status Indicator" />}
    </div>
  );
}
```

## Design tokens / variables referenced in the code

| Token (CSS var) | Fallback |
|---|---|
| `--radius/full` | `9999px` (wrapper, status dot); `8749.125px` on the image container (same token, Figma-resolved value) |
| `--background/default/white` | `white` (image container bg) |
| `--border/default` | `#eee` (border colour; border width is 0 in this variant) |
| `--success/success-dark` | `#008c56` (status indicator dot) |

Fixed values: avatar xs = 24x24px; status dot 6x6px positioned bottom-right; placeholder image cropped (h 220.09%, w 171.88%, left -34.37%, top 9.68%).

## Component description (from Figma)

- No component description or text styles were included in the response.

## Assets

- `figma-asset:3f02b.png` — _AvatarplaholderImages placeholder photo (node 15368:1125)

## Notes

- Original asset URL prefix `https://www.figma.com/api/mcp/asset/<uuid>/` replaced with `figma-asset:` placeholder.
