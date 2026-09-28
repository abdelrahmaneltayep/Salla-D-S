# Table cell header

- Figma node id: `21566:56151`
- File key: `dnmyqzYKK9dUJjVHuIWMDS`
- Source: `mcp__Figma__get_design_context` (screenshot excluded)

> Note: the original response defined `assetPathPrefix` as a temporary `https://www.figma.com/api/mcp/asset/<uuid>` URL. It has been replaced with the `figma-asset:` placeholder below; everything else is verbatim.

## Returned code

```tsx
const assetPathPrefix = "figma-asset:";
const imgMoreHorizontalFilled = `${assetPathPrefix}/a52ed.svg`;
const imgArrowUpDownOutline = `${assetPathPrefix}/3ab78.svg`;
const imgArrowDown01Outline = `${assetPathPrefix}/903a2.svg`;
const imgInformationCircleOutline = `${assetPathPrefix}/4f5ca.svg`;
const imgDeliveryBox01Outline = `${assetPathPrefix}/01648.svg`;

type TableCellHeaderProps = {
  className?: string;
  checkBox?: boolean;
  dropDown?: boolean;
  icon?: React.ReactNode | null;
  info?: boolean;
  more?: boolean;
  scroll?: "Off";
  sort?: boolean;
  startIcon?: boolean;
  status?: "Default";
  type?: "Start";
};

function TableCellHeader({ className, checkBox = false, dropDown = false, icon = null, info = false, more = false, scroll = "Off", sort = false, startIcon = false, status = "Default", type = "Start" }: TableCellHeaderProps) {
  return (
    <div className={className || "bg-[var(--background\\/default\\/neutrals-light,#fcfcfc)] content-stretch flex gap-[var(--spacing\\/xs,12px)] h-[48px] items-center justify-end pl-[var(--spacing\\/sizes\\/2xl,16px)] pr-[var(--spacing\\/sizes\\/5xl,26px)] py-[var(--spacing\\/sizes\\/2xl,16px)] relative w-[300px]"} data-node-id="21566:56151">
      {more && (
        <div className="relative shrink-0 size-[20px]" data-node-id="22602:44323" data-name="more-horizontal-filled">
          <img alt="" className="absolute block inset-0 max-w-none size-full" src={imgMoreHorizontalFilled} />
        </div>
      )}
      <div className="content-stretch flex flex-[1_0_0] gap-[var(--spacing\/xs,12px)] items-center justify-end min-w-px relative" data-node-id="22602:44876" data-name="Data">
        <div className="content-stretch flex gap-[var(--spacing\/sizes\/2xs,4px)] items-center justify-end relative shrink-0" data-node-id="21566:56152" data-name="Text">
          {sort && (
            <div className="relative shrink-0 size-[16px]" data-node-id="21566:56153" data-name="arrow-up-down-outline">
              <img alt="" className="absolute block inset-0 max-w-none size-full" src={imgArrowUpDownOutline} />
            </div>
          )}
          {dropDown && (
            <div className="relative shrink-0 size-[16px]" data-node-id="21566:56154" data-name="arrow-down-01-outline">
              <img alt="" className="absolute block inset-0 max-w-none size-full" src={imgArrowDown01Outline} />
            </div>
          )}
          {info && (
            <div className="relative shrink-0 size-[16px]" data-node-id="21566:56155" data-name="information-circle-outline">
              <img alt="" className="absolute block inset-0 max-w-none size-full" src={imgInformationCircleOutline} />
            </div>
          )}
          <div className="[word-break:break-word] flex flex-col font-[family-name:var(--typography\/family\/font,'Ping_AR_+_LT:Medium')] font-[var(--typography\/weight\/medium,normal)] justify-center leading-[0] relative shrink-0 text-[color:var(--text\/gray\/dark,#333)] text-[length:var(--typography\/size\/sm,14px)] text-center whitespace-nowrap" data-node-id="21566:56156">
            <p className="leading-[var(--typography\/line-height-\(descreptive\)\/5,20px)]" dir="auto">
              رقم الطلب
            </p>
          </div>
        </div>
        {startIcon &&
          (icon || (
            <div className="relative shrink-0 size-[20px]" data-node-id="22602:41008" data-name="delivery-box-01-outline">
              <img alt="" className="absolute block inset-0 max-w-none size-full" src={imgDeliveryBox01Outline} />
            </div>
          ))}
        {checkBox && <div className="border border-[var(--border\/primary,#004956)] border-solid relative rounded-[var(--radius\/md,4px)] shrink-0 size-[20px]" data-node-id="21566:56157" data-name="checkBox" />}
      </div>
    </div>
  );
}
```

## Design tokens / variables used

- `--background/default/neutrals-light` = `#fcfcfc` (header cell background)
- `--spacing/xs` = `12px` (gap), `--spacing/sizes/2xl` = `16px` (left padding, vertical padding), `--spacing/sizes/5xl` = `26px` (right padding), `--spacing/sizes/2xs` = `4px` (text/icon gap)
- `--border/primary` = `#004956` (checkbox border), `--radius/md` = `4px` (checkbox)
- `--typography/family/font` = `Ping AR + LT` (Medium), `--typography/weight/medium` = 500
- `--typography/size/sm` = `14px`, `--typography/line-height (Descreptive)/5` = `20px`
- `--text/gray/dark` = `#333`
- Cell height `48px`; default width `300px`; inline icons (sort/dropdown/info) `16px`; more / start icon / checkbox `20px`
- Sample label: `رقم الطلب`

## Text styles in the design

- `Medium/$text-sm`: Font(family: "Typography/Family/Font", style: Typography/Weight/Medium, size: Typography/Size/sm, weight: 500, lineHeight: typography/line-height (Descreptive)/5, letterSpacing: 0)

## Assets (SVG)

- `figma-asset:a52ed.svg` — more-horizontal-filled (20x20), node 22602:44323
- `figma-asset:3ab78.svg` — arrow-up-down-outline (16x16), node 21566:56153
- `figma-asset:903a2.svg` — arrow-down-01-outline (16x16), node 21566:56154
- `figma-asset:4f5ca.svg` — information-circle-outline (16x16), node 21566:56155
- `figma-asset:01648.svg` — delivery-box-01-outline (20x20), node 22602:41008

## Notes from the response

- Node ids are added to the code as `data-node-id` attributes.
- No component descriptions were returned for this node.
- The generated React+Tailwind is a reference prototype that must be converted to the target stack; do not install Tailwind.
- Assets on the Figma server expire in 7 days (download URLs blocked in this environment; not downloaded).
