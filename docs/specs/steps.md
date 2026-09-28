# Steps

- Figma node id: `24006:17191`
- File key: `dnmyqzYKK9dUJjVHuIWMDS`
- Source: `mcp__Figma__get_design_context` (screenshot excluded)

> Note: the original response defined `assetPathPrefix` as a temporary `https://www.figma.com/api/mcp/asset/<uuid>` URL. It has been replaced with the `figma-asset:` placeholder below; everything else is verbatim.

## Returned code

```tsx
const assetPathPrefix = "figma-asset:";
const imgLine2 = `${assetPathPrefix}/7813f.svg`;

type StepsProps = {
  className?: string;
  count?: "2";
  language?: "Arabic";
  type?: "Desktop";
};

function Steps({ className, count = "2", language = "Arabic", type = "Desktop" }: StepsProps) {
  return (
    <div className={className || "bg-[var(--background\\/default\\/cards,white)] content-stretch flex gap-[var(--spacing\\/sizes\\/2xl,16px)] items-center overflow-clip p-[var(--spacing\\/sizes\\/4xl,24px)] relative rounded-[var(--radius\\/sizes\\/xl,8px)] w-[1166px]"} data-node-id="24006:17191">
      <div className="content-stretch flex gap-[var(--spacing\/sizes\/sm,8px)] items-center justify-center relative shrink-0" data-node-id="24006:17193" data-name="_Step base">
        <div className="[word-break:break-word] flex flex-col font-[family-name:var(--typography\/family\/font,'Ping_AR_+_LT:Medium')] font-[var(--typography\/weight\/medium,normal)] justify-end leading-[0] relative shrink-0 text-[color:var(--text\/gray\/light,#666)] text-[length:var(--typography\/size\/sm,14px)] text-right whitespace-nowrap" data-node-id="I24006:17193;24531:23021">
          <p className="leading-[var(--typography\/line-height-\(descreptive\)\/5,20px)]" dir="auto">
            تصميم الإعلان
          </p>
        </div>
        <div className="bg-[var(--background\/default\/white,white)] border border-[var(--border\/default,#eee)] border-solid content-stretch flex flex-col items-center justify-center overflow-clip relative rounded-[var(--radius\/sizes\/xl,8px)] shrink-0 size-[32px]" data-node-id="I24006:17193;24531:23022" data-name="progress number">
          <div className="[word-break:break-word] flex flex-col font-[family-name:var(--typography\/family\/font,'Ping_AR_+_LT:Medium')] font-[var(--typography\/weight\/medium,normal)] h-[28px] justify-center leading-[0] relative shrink-0 text-[color:var(--07--light-theme\/dark\/color-dark-200,#666)] text-[length:var(--typography\/size\/md,16px)] text-center w-[9px]" data-node-id="I24006:17193;24531:23023">
            <p className="leading-[var(--typography\/line-height-\(descreptive\)\/6,24px)]">2</p>
          </div>
        </div>
      </div>
      <div className="content-stretch flex flex-[1_0_0] gap-[var(--spacing\/sizes\/sm,8px)] items-center justify-center min-w-px relative" data-node-id="24006:17194" data-name="_Step base">
        <div className="flex-[1_0_0] h-0 min-w-px relative" data-node-id="I24006:17194;24531:23082">
          <div className="absolute inset-[-1px_0_0_0]">
            <img alt="" className="block max-w-none size-full" src={imgLine2} />
          </div>
        </div>
        <p className="[word-break:break-word] font-[family-name:var(--typography\/family\/font,'Ping_AR_+_LT:Medium')] font-[var(--typography\/weight\/medium,normal)] leading-[var(--typography\/line-height-\(descreptive\)\/5,20px)] relative shrink-0 text-[color:var(--text\/primary\/primary,#004956)] text-[length:var(--typography\/size\/sm,14px)] text-right whitespace-nowrap" dir="auto" data-node-id="I24006:17194;24006:17146">
          تصميم الإعلان
        </p>
        <div className="bg-[var(--background\/default\/white,white)] border-2 border-[var(--border\/seconadry,#a4ffe5)] border-solid content-stretch flex flex-col items-center justify-center overflow-clip relative rounded-[var(--radius\/sizes\/xl,8px)] shrink-0 size-[32px]" data-node-id="I24006:17194;24006:17147" data-name="progress number">
          <div className="[word-break:break-word] flex flex-col font-[family-name:var(--typography\/family\/font,'Ping_AR_+_LT:Bold')] font-[var(--typography\/weight\/bold,normal)] h-[28px] justify-center leading-[0] relative shrink-0 text-[color:var(--01--primary\/primary-700,#003c47)] text-[length:var(--typography\/size\/md,16px)] text-center w-[9px]" data-node-id="I24006:17194;24006:17148">
            <p className="leading-[var(--typography\/line-height-\(descreptive\)\/6,24px)]">1</p>
          </div>
        </div>
      </div>
    </div>
  );
}
```

## Design tokens / variables used

- `--background/default/cards` = `white` (container), `--background/default/white` = `white` (step number badge)
- `--radius/sizes/xl` = `8px` (container and badge)
- `--spacing/sizes/2xl` = `16px` (gap between steps), `--spacing/sizes/4xl` = `24px` (container padding), `--spacing/sizes/sm` = `8px` (badge/label gap)
- Inactive step: badge `1px` border `--border/default` = `#eee`; number text `--07--light-theme/dark/color-dark-200` = `#666` Medium; label `--text/gray/light` = `#666` Medium
- Active step: badge `2px` border `--border/seconadry` = `#a4ffe5` (token name as spelled in Figma); number text `--01--primary/primary-700` = `#003c47` Bold; label `--text/primary/primary` = `#004956` Medium
- `--typography/family/font` = `Ping AR + LT`; `--typography/weight/medium` = 500, `--typography/weight/bold` = 700
- `--typography/size/sm` = `14px` (labels), `--typography/size/md` = `16px` (numbers)
- `--typography/line-height (Descreptive)/5` = `20px`, `/6` = `24px`
- Badge size `32px`; connector line (`Line 2`) is a 1px horizontal SVG that fills the remaining width; container width `1166px` (Desktop)
- Order is RTL: step 1 (active) on the right, step 2 (upcoming) on the left; sample labels both `تصميم الإعلان`

## Text styles in the design

- `Medium/$text-sm`: Font(family: "Typography/Family/Font", style: Typography/Weight/Medium, size: Typography/Size/sm, weight: 500, lineHeight: typography/line-height (Descreptive)/5, letterSpacing: 0)
- `Medium/$text-base`: Font(family: "Typography/Family/Font", style: Typography/Weight/Medium, size: Typography/Size/md, weight: 500, lineHeight: typography/line-height (Descreptive)/6, letterSpacing: 0)
- `Bold/$text-base`: Font(family: "Typography/Family/Font", style: Typography/Weight/Bold, size: Typography/Size/md, weight: 700, lineHeight: typography/line-height (Descreptive)/6, letterSpacing: 0)

## Assets (SVG)

- `figma-asset:7813f.svg` — Line 2 (connector line between steps, 1px tall), node I24006:17194;24531:23082

## Notes from the response

- Node ids are added to the code as `data-node-id` attributes.
- No component descriptions were returned for this node.
- The generated React+Tailwind is a reference prototype that must be converted to the target stack; do not install Tailwind.
- Assets on the Figma server expire in 7 days (download URLs blocked in this environment; not downloaded).
