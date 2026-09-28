# Side menu

- Figma node id: `15572:56380` (component: Side menu `15572:55610`; tab component: sidemenu tab `15572:54629`)
- File key: `dnmyqzYKK9dUJjVHuIWMDS`
- Source: `mcp__Figma__get_design_context` (screenshot excluded)

> Note: the original response defined `assetPathPrefix` as a temporary `https://www.figma.com/api/mcp/asset/<uuid>` URL. It has been replaced with the `figma-asset:` placeholder below; everything else is verbatim.

## Returned code

```tsx
const assetPathPrefix = "figma-asset:";
const imgPencilEdit01Outline = `${assetPathPrefix}/915b4.svg`;

type SidemenuTabProps = {
  className?: string;
  status?: "--default" | "--active";
  variant?: "middle" | "first";
};

function SidemenuTab({ className, status = "--default", variant = "first" }: SidemenuTabProps) {
  const isActiveAndMiddle = status === "--active" && variant === "middle";
  const isDefaultAndFirst = status === "--default" && variant === "first";
  return (
    <div className={className || `${String.raw`border-[var(--border\/default,#eee)] border-b border-solid content-stretch flex gap-[var(--spacing\/sizes\/sm,8px)] h-[56px] items-center justify-end p-[var(--spacing\/sizes\/2xl,16px)] relative w-[225px] `}${isActiveAndMiddle ? String.raw`bg-[var(--background\/secondary\/lighter,#e6fff9)]` : String.raw`bg-[var(--background\/default\/cards,white)]`}`} id={isActiveAndMiddle ? "node-15572_54630" : isDefaultAndFirst ? "node-15572_56529" : "node-15572_54609"}>
      <div className="content-stretch flex flex-[1_0_0] gap-[var(--spacing\/sizes\/sm,8px)] items-center justify-end min-w-px relative" id={isActiveAndMiddle ? "node-21547_8102" : isDefaultAndFirst ? "node-21547_8140" : "node-21547_8121"} data-name="line text row">
        <div className={`content-stretch flex flex-[1_0_0] items-center justify-between min-w-px relative ${isActiveAndMiddle ? "h-[24px]" : ""}`} id={isActiveAndMiddle ? "node-21547_8105" : isDefaultAndFirst ? "node-21547_8143" : "node-21547_8124"} data-name="_1 line text">
          <div className="content-stretch flex gap-[var(--spacing\/5xs,4px)] items-center relative shrink-0" id={isActiveAndMiddle ? "node-I21547_8105-15975_10017" : isDefaultAndFirst ? "node-I21547_8143-15975_10026" : "node-I21547_8124-15975_10026"} data-name="__endingTextContainer">
            <p className={`${String.raw`[word-break:break-word] leading-[var(--typography\/line-height-\(descreptive\)\/6,24px)] relative shrink-0 text-[length:var(--typography\/size\/md,16px)] whitespace-nowrap `}${isActiveAndMiddle ? String.raw`font-[family-name:var(--typography\/family\/font,"Ping_AR_+_LT:Medium")] font-[var(--typography\/weight\/medium,normal)] text-[color:var(--text\/primary\/primary,#004956)]` : String.raw`font-[family-name:var(--typography\/family\/font,"Ping_AR_+_LT:Regular")] font-[var(--typography\/weight\/regular,normal)] text-[color:var(--text\/gray\/lighter,#737373)]`}`} dir="auto" id={isActiveAndMiddle ? "node-I21547_8105-15975_10018" : isDefaultAndFirst ? "node-I21547_8143-15975_10027" : "node-I21547_8124-15975_10027"}>
              15
            </p>
          </div>
          <div className="content-stretch flex gap-[var(--spacing\/5xs,4px)] items-center justify-end relative shrink-0" id={isActiveAndMiddle ? "node-I21547_8105-15975_9959" : isDefaultAndFirst ? "node-I21547_8143-15975_9971" : "node-I21547_8124-15975_9971"} data-name="__startingTextContainer">
            <p className={`${String.raw`[word-break:break-word] leading-[var(--typography\/line-height-\(descreptive\)\/6,24px)] relative shrink-0 text-[length:var(--typography\/size\/md,16px)] text-right whitespace-nowrap `}${isActiveAndMiddle ? String.raw`font-[family-name:var(--typography\/family\/font,"Ping_AR_+_LT:Medium")] font-[var(--typography\/weight\/medium,normal)] text-[color:var(--text\/primary\/primary,#004956)]` : String.raw`font-[family-name:var(--typography\/family\/font,"Ping_AR_+_LT:Regular")] font-[var(--typography\/weight\/regular,normal)] text-[color:var(--text\/gray\/lighter,#737373)]`}`} dir="auto" id={isActiveAndMiddle ? "node-I21547_8105-15975_9960" : isDefaultAndFirst ? "node-I21547_8143-15975_9972" : "node-I21547_8124-15975_9972"}>
              العنوان
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}

type SideMenuProps = {
  className?: string;
  button?: boolean;
  status?: "default";
};

function SideMenu({ className, button = true, status = "default" }: SideMenuProps) {
  return (
    <div className={className || "bg-[var(--background\\/default\\/cards,white)] content-stretch flex flex-col items-start overflow-clip relative rounded-[var(--radius\\/sizes\\/xl,8px)] w-[225px]"} data-node-id="15572:56380">
      <SidemenuTab className="bg-[var(--background\/default\/cards,white)] border-[var(--border\/default,#eee)] border-b border-solid content-stretch flex gap-[var(--spacing\/sizes\/sm,8px)] h-[56px] items-center justify-end p-[var(--spacing\/sizes\/2xl,16px)] relative shrink-0 w-full" />
      <SidemenuTab className="bg-[var(--background\/secondary\/lighter,#e6fff9)] border-[var(--border\/default,#eee)] border-b border-solid content-stretch flex gap-[var(--spacing\/sizes\/sm,8px)] h-[56px] items-center justify-end p-[var(--spacing\/sizes\/2xl,16px)] relative shrink-0 w-full" status="--active" variant="middle" />
      <SidemenuTab className="bg-[var(--background\/default\/cards,white)] border-[var(--border\/default,#eee)] border-b border-solid content-stretch flex gap-[var(--spacing\/sizes\/sm,8px)] h-[56px] items-center justify-end p-[var(--spacing\/sizes\/2xl,16px)] relative shrink-0 w-full" variant="middle" />
      <SidemenuTab className="bg-[var(--background\/default\/cards,white)] border-[var(--border\/default,#eee)] border-b border-solid content-stretch flex gap-[var(--spacing\/sizes\/sm,8px)] h-[56px] items-center justify-end p-[var(--spacing\/sizes\/2xl,16px)] relative shrink-0 w-full" variant="middle" />
      <SidemenuTab className="bg-[var(--background\/default\/cards,white)] border-[var(--border\/default,#eee)] border-b border-solid content-stretch flex gap-[var(--spacing\/sizes\/sm,8px)] h-[56px] items-center justify-end p-[var(--spacing\/sizes\/2xl,16px)] relative shrink-0 w-full" variant="middle" />
      <SidemenuTab className="bg-[var(--background\/default\/cards,white)] border-[var(--border\/default,#eee)] border-b border-solid content-stretch flex gap-[var(--spacing\/sizes\/sm,8px)] h-[56px] items-center justify-end p-[var(--spacing\/sizes\/2xl,16px)] relative shrink-0 w-full" variant="middle" />
      <SidemenuTab className="bg-[var(--background\/default\/cards,white)] border-[var(--border\/default,#eee)] border-b border-solid content-stretch flex gap-[var(--spacing\/sizes\/sm,8px)] h-[56px] items-center justify-end p-[var(--spacing\/sizes\/2xl,16px)] relative shrink-0 w-full" variant="middle" />
      <SidemenuTab className="bg-[var(--background\/default\/cards,white)] border-[var(--border\/default,#eee)] border-b border-solid content-stretch flex gap-[var(--spacing\/sizes\/sm,8px)] h-[56px] items-center justify-end p-[var(--spacing\/sizes\/2xl,16px)] relative shrink-0 w-full" variant="middle" />
      <SidemenuTab className="bg-[var(--background\/default\/cards,white)] border-[var(--border\/default,#eee)] border-b border-solid content-stretch flex gap-[var(--spacing\/sizes\/sm,8px)] h-[56px] items-center justify-end p-[var(--spacing\/sizes\/2xl,16px)] relative shrink-0 w-full" variant="middle" />
      <SidemenuTab className="bg-[var(--background\/default\/cards,white)] border-[var(--border\/default,#eee)] border-b border-solid content-stretch flex gap-[var(--spacing\/sizes\/sm,8px)] h-[56px] items-center justify-end p-[var(--spacing\/sizes\/2xl,16px)] relative shrink-0 w-full" variant="middle" />
      <SidemenuTab className="bg-[var(--background\/default\/cards,white)] border-[var(--border\/default,#eee)] border-b border-solid content-stretch flex gap-[var(--spacing\/sizes\/sm,8px)] h-[56px] items-center justify-end p-[var(--spacing\/sizes\/2xl,16px)] relative shrink-0 w-full" variant="middle" />
      <SidemenuTab className="bg-[var(--background\/default\/cards,white)] border-[var(--border\/default,#eee)] border-b border-solid content-stretch flex gap-[var(--spacing\/sizes\/sm,8px)] h-[56px] items-center justify-end p-[var(--spacing\/sizes\/2xl,16px)] relative shrink-0 w-full" variant="middle" />
      <SidemenuTab className="bg-[var(--background\/default\/cards,white)] border-[var(--border\/default,#eee)] border-b border-solid content-stretch flex gap-[var(--spacing\/sizes\/sm,8px)] h-[56px] items-center justify-end p-[var(--spacing\/sizes\/2xl,16px)] relative shrink-0 w-full" variant="middle" />
      {button && (
        <div className="bg-[var(--background\/default\/cards,white)] content-stretch flex flex-col gap-[var(--spacing\/sizes\/2xl,16px)] items-start p-[var(--spacing\/sizes\/2xl,16px)] relative shrink-0 w-full" data-node-id="15572:56394" data-name="__button">
          <div className="bg-[var(--background\/default\/white,white)] border border-[var(--border\/seconadry,#a4ffe5)] border-solid content-stretch flex gap-[var(--spacing\/5xs,4px)] items-center justify-center max-h-[40px] min-h-[40px] px-[var(--spacing\/xs,12px)] py-[var(--spacing\/3xs,8px)] relative rounded-[var(--radius\/xl,8px)] shrink-0 w-full" data-node-id="15572:56395" data-name="Button">
            <div className="content-stretch flex flex-col items-center justify-center relative shrink-0" data-node-id="I15572:56395;14671:5731" data-name="__label">
              <div className="[word-break:break-word] flex flex-col font-[family-name:var(--typography\/family\/font,'Ping_AR_+_LT:Medium')] font-[var(--typography\/weight\/medium,normal)] justify-center leading-[0] relative shrink-0 text-[color:var(--text\/primary\/link,#004956)] text-[length:var(--typography\/size\/sm,14px)] text-center whitespace-nowrap" data-node-id="I15572:56395;14671:5732">
                <p className="leading-[var(--typography\/line-height-\(descreptive\)\/5,20px)]" dir="auto">
                  تخصيص الحالات
                </p>
              </div>
            </div>
            <div className="content-stretch flex flex-col items-start relative shrink-0" data-node-id="I15572:56395;14671:5733" data-name="__icon-start">
              <div className="relative shrink-0 size-[16px]" data-node-id="I15572:56395;14671:5734" data-name="add-01-outline">
                <img alt="" className="absolute block inset-0 max-w-none size-full" src={imgPencilEdit01Outline} />
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
```

## Design tokens / variables used

- `--background/default/cards` = `white` (menu and default tabs), `--background/secondary/lighter` = `#e6fff9` (active tab), `--background/default/white` = `white` (button)
- `--border/default` = `#eee` (tab bottom border), `--border/seconadry` = `#a4ffe5` (button border; token name as spelled in Figma)
- `--radius/sizes/xl` = `8px` (menu), `--radius/xl` = `8px` (button)
- `--spacing/sizes/sm` = `8px`, `--spacing/sizes/2xl` = `16px` (tab padding, button wrapper padding)
- `--spacing/5xs` = `4px`, `--spacing/xs` = `12px`, `--spacing/3xs` = `8px`
- `--typography/family/font` = `Ping AR + LT` (Regular / Medium)
- `--typography/weight/regular` = 400, `--typography/weight/medium` = 500
- `--typography/size/md` = `16px` (tab text), `--typography/size/sm` = `14px` (button)
- `--typography/line-height (Descreptive)/6` = `24px`, `/5` = `20px`
- `--text/gray/lighter` = `#737373` (default tab), `--text/primary/primary` = `#004956` (active tab), `--text/primary/link` = `#004956` (button)
- Tab height `56px`; menu width `225px`; button min/max height `40px`; 13 tabs in the sample (tab 2 active)
- Tab content: title (`العنوان`, right) and count (`15`, left) with `justify-between`

## Text styles in the design

- `Regular/$text-base`: Font(family: "Typography/Family/Font", style: Typography/Weight/Regular, size: Typography/Size/md, weight: 400, lineHeight: typography/line-height (Descreptive)/6, letterSpacing: 0)
- `Medium/$text-base`: Font(family: "Typography/Family/Font", style: Typography/Weight/Medium, size: Typography/Size/md, weight: 500, lineHeight: typography/line-height (Descreptive)/6, letterSpacing: 0)
- `Medium/$text-sm`: Font(family: "Typography/Family/Font", style: Typography/Weight/Medium, size: Typography/Size/sm, weight: 500, lineHeight: typography/line-height (Descreptive)/5, letterSpacing: 0)

## Component descriptions (from Figma)

### Side menu — Node ID: 15572:55610
**Keywords:** [Right sidebar navigation, Vertical navigation, Category list, Filter menu, Product categories, Side panel filter, Collapsible menu, Off-canvas menu, Flyout menu, Right drawer, قائمة جانبية, شريط جانبي أيمن, قائمة الفئات, فلتر التصنيفات, تنقل عمودي, قائمة منسدلة جانبية, لوحة جانبية]

### sidemenu tab — Node ID: 15572:54629
**Keywords:** [Right sidebar navigation, Vertical navigation, Category list, Filter menu, Product categories, Side panel filter, Collapsible menu, Off-canvas menu, Flyout menu, Right drawer, قائمة جانبية, شريط جانبي أيمن, قائمة الفئات, فلتر التصنيفات, تنقل عمودي, قائمة منسدلة جانبية, لوحة جانبية]

### Button — Node ID: 14526:107536
Keywords: [Action trigger, Clickable element, UI control, Interactive button, Command button, Call-to-action (CTA) button, Press component, زرار]

## Assets (SVG)

- `figma-asset:915b4.svg` — pencil-edit-01-outline (16x16; layer named add-01-outline), node I15572:56395;14671:5734

## Notes from the response

- Node ids are added to the code as `data-node-id` attributes (tab variants use `id="node-…"`).
- The generated React+Tailwind is a reference prototype that must be converted to the target stack; do not install Tailwind.
- Assets on the Figma server expire in 7 days (download URLs blocked in this environment; not downloaded).
