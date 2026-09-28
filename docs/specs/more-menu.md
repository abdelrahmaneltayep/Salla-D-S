# More menu

- Figma node id: `19764:6970`
- File key: `dnmyqzYKK9dUJjVHuIWMDS`
- Source: `mcp__Figma__get_design_context` (screenshot excluded)

> Note: the original response defined `assetPathPrefix` as a temporary `https://www.figma.com/api/mcp/asset/<uuid>` URL. It has been replaced with the `figma-asset:` placeholder below; everything else is verbatim.

## Returned code

```tsx
const assetPathPrefix = "figma-asset:";
const imgPrinterOutline = `${assetPathPrefix}/65aaf.svg`;
const imgRoadLocation02Outline = `${assetPathPrefix}/76442.svg`;
const imgShare03Outline = `${assetPathPrefix}/39645.svg`;
const imgMoreItems = `${assetPathPrefix}/d798b.svg`;
const imgFileRemoveOutline = `${assetPathPrefix}/e0eef.svg`;
const imgAlert01Outline = `${assetPathPrefix}/a4ab7.svg`;

type MoreMenuProps = {
  className?: string;
  dir?: "Off";
  type?: "Type1";
};

function MoreMenu({ className, dir = "Off", type = "Type1" }: MoreMenuProps) {
  return (
    <div className={className || "bg-[var(--07--light-theme\\/white\\/color-white-drop-menu,white)] content-stretch flex flex-col items-start overflow-clip relative rounded-[var(--radius\\/xl,8px)] shadow-[var(--shadow\\/lg\\/type-1\\/position-x,0px)_var(--shadow\\/lg\\/type-1\\/position-y,10px)_var(--shadow\\/lg\\/type-1\\/blur,15px)_var(--shadow\\/lg\\/type-1\\/spread,-3px)_var(--shadow\\/lg\\/type-1\\/color,rgba(18,18,23,0.08)),var(--shadow\\/lg\\/type-2\\/position-x,0px)_var(--shadow\\/lg\\/type-2\\/position-y,4px)_var(--shadow\\/lg\\/type-2\\/blur,6px)_var(--shadow\\/lg\\/type-2\\/spread,-2px)_var(--shadow\\/lg\\/type-2\\/color,rgba(18,18,23,0.05))] w-[240px]"} data-node-id="19764:6970">
      <div className="content-stretch flex gap-[var(--spacing\/sizes\/sm,8px)] items-center justify-end px-[var(--spacing\/xs,12px)] py-[var(--spacing\/sizes\/lg,12px)] relative shrink-0 w-full" data-node-id="19764:6871" data-name="_moreItems">
        <div className="content-stretch flex flex-[1_0_0] items-center justify-center min-w-px relative" data-node-id="I19764:6871;19764:2488" data-name="__label">
          <p className="[word-break:break-word] flex-[1_0_0] font-[family-name:var(--typography\/family\/font,'Ping_AR_+_LT:Regular')] font-[var(--typography\/weight\/regular,normal)] leading-[var(--typography\/line-height-\(descreptive\)\/5,20px)] min-w-px relative text-[color:var(--text\/gray\/dark,#333)] text-[length:var(--typography\/size\/sm,14px)] text-right" dir="auto" data-node-id="I19764:6871;19764:2489">
            طباعة بوليصة الشحن
          </p>
        </div>
        <div className="content-stretch flex items-center relative shrink-0 w-[20px]" data-node-id="I19764:6871;19764:6814" data-name="__iconStart">
          <div className="flex-[1_0_0] h-[20px] min-w-px relative" data-node-id="I19764:6871;19764:6815" data-name="file-02-outline">
            <img alt="" className="absolute block inset-0 max-w-none size-full" src={imgPrinterOutline} />
          </div>
        </div>
      </div>
      <div className="content-stretch flex gap-[var(--spacing\/sizes\/sm,8px)] items-center justify-end px-[var(--spacing\/xs,12px)] py-[var(--spacing\/sizes\/lg,12px)] relative shrink-0 w-full" data-node-id="19764:6879" data-name="_moreItems">
        <div className="content-stretch flex flex-[1_0_0] items-center justify-center min-w-px relative" data-node-id="I19764:6879;19764:2488" data-name="__label">
          <p className="[word-break:break-word] flex-[1_0_0] font-[family-name:var(--typography\/family\/font,'Ping_AR_+_LT:Regular')] font-[var(--typography\/weight\/regular,normal)] leading-[var(--typography\/line-height-\(descreptive\)\/5,20px)] min-w-px relative text-[color:var(--text\/gray\/dark,#333)] text-[length:var(--typography\/size\/sm,14px)] text-right" dir="auto" data-node-id="I19764:6879;19764:2489">
            تتبع حالة الشحنة
          </p>
        </div>
        <div className="content-stretch flex items-center relative shrink-0 w-[20px]" data-node-id="I19764:6879;19764:6814" data-name="__iconStart">
          <div className="flex-[1_0_0] h-[20px] min-w-px relative" data-node-id="I19764:6879;19764:6815" data-name="file-02-outline">
            <img alt="" className="absolute block inset-0 max-w-none size-full" src={imgRoadLocation02Outline} />
          </div>
        </div>
      </div>
      <div className="content-stretch flex gap-[var(--spacing\/sizes\/sm,8px)] items-center justify-end px-[var(--spacing\/xs,12px)] py-[var(--spacing\/sizes\/lg,12px)] relative shrink-0 w-full" data-node-id="19764:6960" data-name="_moreItems">
        <div className="content-stretch flex flex-[1_0_0] items-center justify-center min-w-px relative" data-node-id="I19764:6960;19764:2488" data-name="__label">
          <p className="[word-break:break-word] flex-[1_0_0] font-[family-name:var(--typography\/family\/font,'Ping_AR_+_LT:Regular')] font-[var(--typography\/weight\/regular,normal)] leading-[var(--typography\/line-height-\(descreptive\)\/5,20px)] min-w-px relative text-[color:var(--text\/gray\/dark,#333)] text-[length:var(--typography\/size\/sm,14px)] text-right" dir="auto" data-node-id="I19764:6960;19764:2489">
            اصدار بوليصة إرجاع
          </p>
        </div>
        <div className="content-stretch flex items-center relative shrink-0 w-[20px]" data-node-id="I19764:6960;19764:6814" data-name="__iconStart">
          <div className="flex-[1_0_0] h-[20px] min-w-px relative" data-node-id="I19764:6960;19764:6815" data-name="file-02-outline">
            <img alt="" className="absolute block inset-0 max-w-none size-full" src={imgShare03Outline} />
          </div>
        </div>
      </div>
      <div className="h-[8px] relative shrink-0 w-full" data-node-id="19764:6886" data-name="_moreItems">
        <img alt="" className="absolute block inset-0 max-w-none size-full" src={imgMoreItems} />
      </div>
      <div className="content-stretch flex gap-[var(--spacing\/sizes\/sm,8px)] items-center justify-end px-[var(--spacing\/xs,12px)] py-[var(--spacing\/sizes\/lg,12px)] relative shrink-0 w-full" data-node-id="19764:6894" data-name="_moreItems">
        <div className="content-stretch flex flex-[1_0_0] items-center justify-center min-w-px relative" data-node-id="I19764:6894;19764:6828" data-name="__label">
          <p className="[word-break:break-word] flex-[1_0_0] font-[family-name:var(--typography\/family\/font,'Ping_AR_+_LT:Regular')] font-[var(--typography\/weight\/regular,normal)] leading-[var(--typography\/line-height-\(descreptive\)\/5,20px)] min-w-px relative text-[color:var(--text\/status\/danger\/primary,#f55157)] text-[length:var(--typography\/size\/sm,14px)] text-right" dir="auto" data-node-id="I19764:6894;19764:6829">
            الغاء بوليصة الشحن
          </p>
        </div>
        <div className="content-stretch flex items-center relative shrink-0 w-[20px]" data-node-id="I19764:6894;19764:6830" data-name="__iconStart">
          <div className="flex-[1_0_0] h-[20px] min-w-px relative" data-node-id="I19764:6894;19764:6831" data-name="file-02-outline">
            <img alt="" className="absolute block inset-0 max-w-none size-full" src={imgFileRemoveOutline} />
          </div>
        </div>
      </div>
      <div className="content-stretch flex gap-[var(--spacing\/sizes\/sm,8px)] items-center justify-end px-[var(--spacing\/xs,12px)] py-[var(--spacing\/sizes\/lg,12px)] relative shrink-0 w-full" data-node-id="19764:6907" data-name="_moreItems">
        <div className="content-stretch flex flex-[1_0_0] items-center justify-center min-w-px relative" data-node-id="I19764:6907;19764:6828" data-name="__label">
          <p className="[word-break:break-word] flex-[1_0_0] font-[family-name:var(--typography\/family\/font,'Ping_AR_+_LT:Regular')] font-[var(--typography\/weight\/regular,normal)] leading-[var(--typography\/line-height-\(descreptive\)\/5,20px)] min-w-px relative text-[color:var(--text\/status\/danger\/primary,#f55157)] text-[length:var(--typography\/size\/sm,14px)] text-right" dir="auto" data-node-id="I19764:6907;19764:6829">
            رفع شكوى
          </p>
        </div>
        <div className="content-stretch flex items-center relative shrink-0 w-[20px]" data-node-id="I19764:6907;19764:6830" data-name="__iconStart">
          <div className="flex-[1_0_0] h-[20px] min-w-px relative" data-node-id="I19764:6907;19764:6831" data-name="file-02-outline">
            <img alt="" className="absolute block inset-0 max-w-none size-full" src={imgAlert01Outline} />
          </div>
        </div>
      </div>
    </div>
  );
}
```

## Design tokens / variables used

- `--07--light-theme/white/color-white-drop-menu` = `white` (menu background)
- `--radius/xl` = `8px`
- Shadow `Shadows/lg` (two drop shadows):
  - type-1: x `0px`, y `10px`, blur `15px`, spread `-3px`, color `rgba(18,18,23,0.08)` (`--shadow/lg/type-1/*`)
  - type-2: x `0px`, y `4px`, blur `6px`, spread `-2px`, color `rgba(18,18,23,0.05)` (`--shadow/lg/type-2/*`)
- `--spacing/sizes/sm` = `8px` (icon/label gap), `--spacing/xs` = `12px` (horizontal padding), `--spacing/sizes/lg` = `12px` (vertical padding)
- `--typography/family/font` = `Ping AR + LT` (Regular), `--typography/weight/regular` = 400
- `--typography/size/sm` = `14px`, `--typography/line-height (Descreptive)/5` = `20px`
- `--text/gray/dark` = `#333` (normal items), `--text/status/danger/primary` = `#f55157` (danger items)
- Menu width `240px`; icons `20px`; divider row height `8px` (rendered as SVG asset `d798b.svg`)
- Items in sample: طباعة بوليصة الشحن (printer), تتبع حالة الشحنة (road-location), اصدار بوليصة إرجاع (share), [divider], الغاء بوليصة الشحن (file-remove, danger), رفع شكوى (alert, danger)

## Text styles in the design

- `Regular/$text-sm`: Font(family: "Typography/Family/Font", style: Typography/Weight/Regular, size: Typography/Size/sm, weight: 400, lineHeight: typography/line-height (Descreptive)/5, letterSpacing: 0)
- `Shadows/lg`: Effect(type: DROP_SHADOW, color: shadow/lg/type-2/color, offset: (shadow/lg/type-2/position-x, shadow/lg/type-2/position-y), radius: shadow/lg/type-2/blur, spread: shadow/lg/type-2/spread); Effect(type: DROP_SHADOW, color: shadow/lg/type-1/color, offset: (shadow/lg/type-1/position-x, shadow/lg/type-1/position-y), radius: shadow/lg/type-1/blur, spread: shadow/lg/type-1/spread)

## Assets (SVG)

- `figma-asset:65aaf.svg` — printer-outline (20x20), node I19764:6871;19764:6815
- `figma-asset:76442.svg` — road-location-02-outline (20x20), node I19764:6879;19764:6815
- `figma-asset:39645.svg` — share-03-outline (20x20), node I19764:6960;19764:6815
- `figma-asset:d798b.svg` — divider row (240x8), node 19764:6886
- `figma-asset:e0eef.svg` — file-remove-outline (20x20), node I19764:6894;19764:6831
- `figma-asset:a4ab7.svg` — alert-01-outline (20x20), node I19764:6907;19764:6831

## Notes from the response

- Node ids are added to the code as `data-node-id` attributes.
- No component descriptions were returned for this node.
- The generated React+Tailwind is a reference prototype that must be converted to the target stack; do not install Tailwind.
- Assets on the Figma server expire in 7 days (download URLs blocked in this environment; not downloaded).
