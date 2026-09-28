# Button — Variant=--primary, Appearance=--default, State=--default, Size=--lg-48px

- Figma file: `dnmyqzYKK9dUJjVHuIWMDS`
- Figma node id: `14526:107537`
- Parent component set: `14526:107536` (Button)

## Code (verbatim from get_design_context)

```tsx
const assetPathPrefix = "figma-asset:";
const imgAdd01Outline = `${assetPathPrefix}/15789.svg`;
const imgAdd01Outline1 = `${assetPathPrefix}/a8630.svg`;

type ButtonProps = {
  className?: string;
  appearance?: "--default";
  iconEnd?: boolean;
  iconStart?: boolean;
  label?: string;
  label1?: boolean;
  layout?: "--default";
  size?: "--lg-48px";
  state?: "--default";
  swapIconEnd?: React.ReactNode | null;
  swapIconStart?: React.ReactNode | null;
  variant?: "--primary";
};

function Button({ className, appearance = "--default", iconEnd = true, iconStart = true, label = "نص بديل", label1 = true, layout = "--default", size = "--lg-48px", state = "--default", swapIconEnd = null, swapIconStart = null, variant = "--primary" }: ButtonProps) {
  return (
    <div className={className || "bg-[var(--background\\/secondary\\/seconadry,#a4ffe5)] border-2 border-[var(--border\\/seconadry,#a4ffe5)] border-solid content-stretch flex gap-[var(--spacing\\/5xs,4px)] items-center justify-center max-h-[48px] min-h-[48px] px-[var(--spacing\\/sm,14px)] py-[var(--spacing\\/xs,12px)] relative rounded-[var(--radius\\/xl,8px)]"} data-node-id="14526:107537">
      {iconEnd && (
        <div className="content-stretch flex flex-col items-start relative shrink-0" data-node-id="14526:112348" data-name="__icon-end">
          {swapIconEnd || (
            <div className="relative shrink-0 size-[20px]" data-node-id="14526:107538" data-name="add-01-outline">
              <img alt="" className="absolute block inset-0 max-w-none size-full" src={imgAdd01Outline} />
            </div>
          )}
        </div>
      )}
      {label1 && (
        <div className="content-stretch flex flex-col items-center justify-center relative shrink-0" data-node-id="14526:112346" data-name="__label">
          <div className="[word-break:break-word] flex flex-col font-[family-name:var(--typography\/family\/font,'Ping_AR_+_LT:Medium')] font-[var(--typography\/weight\/medium,normal)] justify-center leading-[0] relative shrink-0 text-[color:var(--text\/primary\/primary,#004956)] text-[length:var(--typography\/size\/md,16px)] text-center whitespace-nowrap" data-node-id="14526:107539">
            <p className="leading-[var(--typography\/line-height-\(descreptive\)\/6,24px)]" dir="auto">
              {label}
            </p>
          </div>
        </div>
      )}
      {iconStart && (
        <div className="content-stretch flex flex-col items-start relative shrink-0" data-node-id="14526:112349" data-name="__icon-start">
          {swapIconStart || (
            <div className="relative shrink-0 size-[20px]" data-node-id="14526:107540" data-name="add-01-outline">
              <img alt="" className="absolute block inset-0 max-w-none size-full" src={imgAdd01Outline1} />
            </div>
          )}
        </div>
      )}
    </div>
  );
}
```

## Design tokens / variables referenced in the code

| Token (CSS var) | Fallback |
|---|---|
| `--background/secondary/seconadry` | `#a4ffe5` |
| `--border/seconadry` | `#a4ffe5` (border width 2px) |
| `--spacing/5xs` | `4px` (gap) |
| `--spacing/sm` | `14px` (padding-x) |
| `--spacing/xs` | `12px` (padding-y) |
| `--radius/xl` | `8px` |
| `--typography/family/font` | `'Ping AR + LT:Medium'` |
| `--typography/weight/medium` | `normal` (500) |
| `--typography/size/md` | `16px` |
| `--typography/line-height (Descreptive)/6` | `24px` |
| `--text/primary/primary` | `#004956` |

Fixed sizes: min-height 48px, max-height 48px, icon 20px.

## Text styles

- `Medium/$text-base`: Font(family: "Typography/Family/Font", style: Typography/Weight/Medium, size: Typography/Size/md, weight: 500, lineHeight: typography/line-height (Descreptive)/6, letterSpacing: 0).

## Component description (from Figma)

**Button** — Node ID: 14526:107536. Keywords: [Action trigger, Clickable element, UI control, Interactive button, Command button, Call-to-action (CTA) button, Press component, زرار]

## Assets

- `figma-asset:15789.svg` — add-01-outline (icon-end, node 14526:107538, 20x20)
- `figma-asset:a8630.svg` — add-01-outline (icon-start, node 14526:107540, 20x20)

## Notes

- Original asset URL prefix was `https://www.figma.com/api/mcp/asset/<uuid>/` (replaced with `figma-asset:` placeholder; download URLs blocked in this environment).
- Note the original response used JSX `data-node-id` attributes; the string `figma-asset:` above replaces the original `assetPathPrefix` value only.
