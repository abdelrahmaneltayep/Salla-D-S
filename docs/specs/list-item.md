# ListItem

- Figma node id: `14952:22458`
- File key: `dnmyqzYKK9dUJjVHuIWMDS`
- Source: `mcp__Figma__get_design_context` (screenshot excluded)

> Note: the original response defined `assetPathPrefix` as a temporary `https://www.figma.com/api/mcp/asset/<uuid>` URL. It has been replaced with the `figma-asset:` placeholder below; everything else is verbatim.

## Returned code

```tsx
const assetPathPrefix = "figma-asset:";
const imgTickMark = `${assetPathPrefix}/5ec58.svg`;
const imgFile02Outline = `${assetPathPrefix}/a6097.svg`;
const imgArrowLeft01Outline = `${assetPathPrefix}/d6b9d.svg`;

type CheckBoxProps = {
  className?: string;
  selected?: boolean;
  size?: "md-20px";
  status?: "--default";
};

function CheckBox({ className, selected = true, size = "md-20px", status = "--default" }: CheckBoxProps) {
  const isNotSelectedAndDefault = !selected && status === "--default";
  return (
    <button className={className || `${String.raw`relative rounded-[var(--radius\/md,4px)] size-[20px] `}${isNotSelectedAndDefault ? String.raw`block border border-[var(--border\/primary,#004956)] border-solid` : String.raw`bg-[var(--background\/primary\/primary,#004956)] content-stretch flex flex-col items-center justify-center p-[var(--spacing\/sizes\/3xs,2px)]`}`} id={isNotSelectedAndDefault ? "node-12411_21812" : "node-12411_21810"}>
      {selected && status === "--default" && (
        <div className="relative shrink-0 size-[14px]" data-node-id="12411:21811" data-name="Tick Mark">
          <img alt="" className="absolute block inset-0 max-w-none size-full" src={imgTickMark} />
        </div>
      )}
    </button>
  );
}

type ListItemProps = {
  className?: string;
  arrow?: boolean;
  checkBox?: boolean;
  danger?: "False";
  disabled?: "false";
  feature?: "false";
  language?: "Arabic";
  selected?: "False";
  startIcon?: boolean;
  swapStartIcon?: React.ReactNode | null;
  variant?: "--item-description";
};

function ListItem({ className, arrow = false, checkBox = true, danger = "False", disabled = "false", feature = "false", language = "Arabic", selected = "False", startIcon = true, swapStartIcon = null, variant = "--item-description" }: ListItemProps) {
  return (
    <div className={className || "bg-[var(--background\\/default\\/cards,white)] content-stretch flex gap-[var(--spacing\\/sizes\\/sm,8px)] h-[60px] items-center justify-end min-h-[44px] p-[var(--spacing\\/sizes\\/lg,12px)] relative w-[286px]"} data-node-id="14952:22458">
      <div className="content-stretch flex flex-[1_0_0] flex-col gap-[var(--spacing\/sizes\/2xs,4px)] items-end min-w-px relative" data-node-id="14952:280022" data-name="textContainer">
        <div className="content-stretch flex items-center justify-center relative shrink-0 w-full" data-node-id="14967:20362" data-name="__label">
          <p className="[word-break:break-word] flex-[1_0_0] font-[family-name:var(--typography\/family\/font,'Ping_AR_+_LT:Bold')] font-[var(--typography\/weight\/bold,normal)] leading-[var(--typography\/line-height-\(descreptive\)\/4,16px)] min-w-px relative text-[color:var(--text\/gray\/dark,#333)] text-[length:var(--typography\/size\/xs,12px)] text-right" dir="auto" data-node-id="14952:22459">
            خيار رقم (1)
          </p>
        </div>
        <div className="content-stretch flex items-center justify-center relative shrink-0 w-[123px]" data-node-id="14967:21131" data-name="__description">
          <p className="[word-break:break-word] flex-[1_0_0] font-[family-name:var(--typography\/family\/font,'Ping_AR_+_LT:Regular')] font-[var(--typography\/weight\/regular,normal)] leading-[var(--typography\/line-height-\(descreptive\)\/4,16px)] min-w-px relative text-[color:var(--text\/gray\/light,#666)] text-[length:var(--typography\/size\/xs,12px)] text-right" dir="auto" data-node-id="14952:280028">
            نص بديل لعرض التفاصيل
          </p>
        </div>
      </div>
      {startIcon && (
        <div className="content-stretch flex items-center relative shrink-0 w-[20px]" data-node-id="14967:21352" data-name="__iconStart">
          {startIcon &&
            (swapStartIcon || (
              <div className="flex-[1_0_0] h-[20px] min-w-px relative" data-node-id="14952:22518" data-name="file-02-outline">
                <img alt="" className="absolute block inset-0 max-w-none size-full" src={imgFile02Outline} />
              </div>
            ))}
        </div>
      )}
      {checkBox && <CheckBox className="block border border-[var(--border\/primary,#004956)] border-solid cursor-pointer relative rounded-[var(--radius\/md,4px)] shrink-0 size-[20px]" selected={false} />}
      {arrow && (
        <div className="content-stretch flex items-center relative shrink-0 w-[20px]" data-node-id="22985:50171" data-name="Arrow">
          <div className="flex-[1_0_0] h-[20px] min-w-px relative" data-node-id="22985:50172" data-name="arrow-left-01-outline">
            <img alt="" className="absolute block inset-0 max-w-none size-full" src={imgArrowLeft01Outline} />
          </div>
        </div>
      )}
    </div>
  );
}
```

## Design tokens / variables used

- `--background/default/cards` = `white`
- `--spacing/sizes/sm` = `8px` (gap), `--spacing/sizes/lg` = `12px` (padding), `--spacing/sizes/2xs` = `4px` (label/description gap), `--spacing/sizes/3xs` = `2px` (checkbox padding)
- `--radius/md` = `4px` (checkbox)
- `--border/primary` = `#004956` (unchecked checkbox border), `--background/primary/primary` = `#004956` (checked checkbox fill)
- `--typography/family/font` = `Ping AR + LT` (Bold / Regular)
- `--typography/weight/bold` = 700, `--typography/weight/regular` = 400
- `--typography/size/xs` = `12px`, `--typography/line-height (Descreptive)/4` = `16px`
- `--text/gray/dark` = `#333` (label), `--text/gray/light` = `#666` (description)
- Item: height `60px` (with description), min-height `44px`, default width `286px`; icons `20px`; checkbox `20px` with `14px` tick

## Text styles in the design

- `Bold/$text-xs`: Font(family: "Typography/Family/Font", style: Typography/Weight/Bold, size: Typography/Size/xs, weight: 700, lineHeight: typography/line-height (Descreptive)/4, letterSpacing: 0)
- `Regular/$text-xs`: Font(family: "Typography/Family/Font", style: Typography/Weight/Regular, size: Typography/Size/xs, weight: 400, lineHeight: typography/line-height (Descreptive)/4, letterSpacing: 0)

## Component descriptions (from Figma)

### checkBox — Node ID: 12411:21809
**Keywords:** [Selection control, Tickbox, Check mark, Boolean input, Multiple choice, On/Off switch, Form element, UI control, مربع اختيار, خانة اختيار, علامة صح, أداة تحديد, اختيار متعدد, عنصر إدخال]

## Assets (SVG)

- `figma-asset:5ec58.svg` — Tick Mark (14x14), node 12411:21811
- `figma-asset:a6097.svg` — file-02-outline (20x20), node 14952:22518
- `figma-asset:d6b9d.svg` — arrow-left-01-outline (20x20), node 22985:50172

## Notes from the response

- Node ids are added to the code as `data-node-id` attributes.
- The generated React+Tailwind is a reference prototype that must be converted to the target stack; do not install Tailwind.
- Assets on the Figma server expire in 7 days (download URLs blocked in this environment; not downloaded).
