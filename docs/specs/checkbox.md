# checkBox — selected=true, size=md-20px, status=--default

- Figma file: `dnmyqzYKK9dUJjVHuIWMDS`
- Figma node id: `12411:21810`
- Parent component set: `12411:21809` (checkBox)

## Code (verbatim from get_design_context)

```tsx
const assetPathPrefix = "figma-asset:";
const imgTickMark = `${assetPathPrefix}/5ec58.svg`;

type CheckBoxProps = {
  className?: string;
  selected?: boolean;
  size?: "md-20px";
  status?: "--default";
};

function CheckBox({ className, selected = true, size = "md-20px", status = "--default" }: CheckBoxProps) {
  return (
    <button className={className || "bg-[var(--background\\/primary\\/primary,#004956)] content-stretch flex flex-col items-center justify-center p-[var(--spacing\\/sizes\\/3xs,2px)] relative rounded-[var(--radius\\/md,4px)] size-[20px]"} data-node-id="12411:21810">
      <div className="relative shrink-0 size-[14px]" data-node-id="12411:21811" data-name="Tick Mark">
        <img alt="" className="absolute block inset-0 max-w-none size-full" src={imgTickMark} />
      </div>
    </button>
  );
}
```

## Design tokens / variables referenced in the code

| Token (CSS var) | Fallback |
|---|---|
| `--background/primary/primary` | `#004956` |
| `--spacing/sizes/3xs` | `2px` (padding) |
| `--radius/md` | `4px` |

Fixed sizes: box 20x20px, tick mark 14x14px.

## Component description (from Figma)

**checkBox** — Node ID: 12411:21809. Keywords: [Selection control, Tickbox, Check mark, Boolean input, Multiple choice, On/Off switch, Form element, UI control, مربع اختيار, خانة اختيار, علامة صح, أداة تحديد, اختيار متعدد, عنصر إدخال]

## Assets

- `figma-asset:5ec58.svg` — Tick Mark (node 12411:21811, 14x14)

## Notes

- Original asset URL prefix `https://www.figma.com/api/mcp/asset/<uuid>/` replaced with `figma-asset:` placeholder.
