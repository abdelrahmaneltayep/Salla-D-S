# Alertbox — variant=--info, type=Inline, language=Arabic, title=On, closable=true, button=false, link=false, trasnparet=Off

- Figma file: `dnmyqzYKK9dUJjVHuIWMDS`
- Figma node id: `15375:52053`

## Code (verbatim from get_design_context)

```tsx
const assetPathPrefix = "figma-asset:";
const imgCancel01Outline = `${assetPathPrefix}/e1aa9.svg`;
const imgInformationCircleOutline = `${assetPathPrefix}/4074b.svg`;

type AlertboxProps = {
  className?: string;
  button?: boolean;
  closable?: boolean;
  language?: "Arabic";
  link?: boolean;
  title?: "On";
  trasnparet?: "Off";
  type?: "Inline";
  variant?: "--info";
};

function Alertbox({ className, button = false, closable = true, language = "Arabic", link = false, title = "On", trasnparet = "Off", type = "Inline", variant = "--info" }: AlertboxProps) {
  return (
    <div className={className || "bg-[var(--background\\/status\\/info\\/lighter,#ecf3fe)] border-[var(--border\\/status\\/info-light,#cbe0fb)] border-r-3 border-solid content-stretch flex gap-[var(--spacing\\/3xs,8px)] items-center justify-end px-[var(--spacing\\/2xl,24px)] py-[var(--spacing\\/base,16px)] relative w-[400px]"} data-node-id="15375:52053">
      {closable && (
        <div className="flex flex-row items-center self-stretch" data-node-id="17999:400755">
          <div className="content-stretch flex flex-col h-full items-center pt-[var(--spacing\/6xs,2px)] relative shrink-0" data-name="__iconClose">
            <div className="relative shrink-0 size-[18px]" data-node-id="17999:400756" data-name="cancel-01-outline">
              <img alt="" className="absolute block inset-0 max-w-none size-full" src={imgCancel01Outline} />
            </div>
          </div>
        </div>
      )}
      {button && (
        <div className="bg-[var(--background\/status\/info\/primary,#5196f3)] border-2 border-[var(--background\/status\/info\/primary,#5196f3)] border-solid content-stretch flex gap-[var(--spacing\/5xs,4px)] items-center justify-center max-h-[32px] min-h-[32px] px-[var(--spacing\/3xs,8px)] py-[var(--spacing\/5xs,4px)] relative rounded-[var(--radius\/xl,8px)] shrink-0" data-node-id="19338:24325" data-name="Button">
          <div className="content-stretch flex flex-col items-center justify-center relative shrink-0" data-node-id="I19338:24325;14671:48453" data-name="__label">
            <div className="[word-break:break-word] flex flex-col font-[family-name:var(--typography\/family\/font,'Ping_AR_+_LT:Medium')] font-[var(--typography\/weight\/medium,normal)] justify-center leading-[0] relative shrink-0 text-[color:var(--text\/gray\/white,white)] text-[length:var(--typography\/size\/xs,12px)] text-center whitespace-nowrap" data-node-id="I19338:24325;14671:48454">
              <p className="leading-[var(--typography\/line-height-\(descreptive\)\/4,16px)]" dir="auto">
                حدث الصفحة
              </p>
            </div>
          </div>
        </div>
      )}
      <div className="content-stretch flex flex-[1_0_0] flex-col gap-[4px] items-start justify-center min-w-px relative" data-node-id="15376:60346" data-name="contentContainer">
        <div className="content-stretch flex flex-col gap-[var(--spacing-xs,2px)] items-end justify-center relative shrink-0 w-full" data-node-id="15375:52002" data-name="__title">
          <p className="[word-break:break-word] font-[family-name:var(--typography\/family\/font,'Ping_AR_+_LT:Bold')] font-[var(--typography\/weight\/bold,normal)] leading-[var(--typography\/line-height-\(descreptive\)\/6,24px)] relative shrink-0 text-[color:var(--text\/status\/info\/darker,#204374)] text-[length:var(--typography\/size\/md,16px)] text-right whitespace-nowrap" dir="auto" data-node-id="15375:52006">
            عنوان التنبه
          </p>
        </div>
        <div className="[word-break:break-word] content-stretch flex gap-[5px] items-center justify-end relative shrink-0 text-[color:var(--text\/status\/info\/darker,#204374)] text-right w-full" data-node-id="15376:60343" data-name="__description">
          {link && (
            <p className="[text-decoration-skip-ink:none] [text-underline-position:from-font] decoration-from-font decoration-solid font-['Ping_AR_+_LT:Bold'] leading-[20px] not-italic relative shrink-0 text-[14px] underline whitespace-nowrap" dir="ltr" data-node-id="15376:60344">
              حدث الصفحة
            </p>
          )}
          <p className="flex-[1_0_0] font-[family-name:var(--typography\/family\/font,'Ping_AR_+_LT:Regular')] font-[var(--typography\/weight\/regular,normal)] leading-[var(--typography\/line-height-\(descreptive\)\/5,20px)] min-w-px relative text-[length:var(--typography\/size\/sm,14px)]" dir="auto" data-node-id="15376:60345">
            لديك 3 طلبات جديدة...
          </p>
        </div>
      </div>
      <div className="flex flex-row items-center self-stretch" data-node-id="15375:52007">
        <div className="content-stretch flex flex-col h-full items-center pt-[var(--spacing\/6xs,2px)] relative shrink-0" data-name="__iconStart">
          <div className="relative shrink-0 size-[18px]" data-node-id="15375:52008" data-name="information-circle-outline">
            <img alt="" className="absolute block inset-0 max-w-none size-full" src={imgInformationCircleOutline} />
          </div>
        </div>
      </div>
    </div>
  );
}
```

## Design tokens / variables referenced in the code

| Token (CSS var) | Fallback |
|---|---|
| `--background/status/info/lighter` | `#ecf3fe` (container background) |
| `--border/status/info-light` | `#cbe0fb` (3px border on the right/start edge, `border-r-3`) |
| `--background/status/info/primary` | `#5196f3` (optional button bg + 2px border) |
| `--text/status/info/darker` | `#204374` (title + description text) |
| `--text/gray/white` | `white` (button label) |
| `--spacing/3xs` | `8px` (gap; button padding-x) |
| `--spacing/2xl` | `24px` (container padding-x) |
| `--spacing/base` | `16px` (container padding-y) |
| `--spacing/6xs` | `2px` (icon top padding) |
| `--spacing/5xs` | `4px` (button gap / padding-y) |
| `--spacing-xs` | `2px` (title column gap; note different naming) |
| `--radius/xl` | `8px` (button) |
| `--typography/family/font` | `'Ping AR + LT'` (Bold / Regular / Medium) |
| `--typography/weight/bold` | `normal` (700) |
| `--typography/weight/regular` | `normal` (400) |
| `--typography/weight/medium` | `normal` (500) |
| `--typography/size/md` | `16px` (title) |
| `--typography/size/sm` | `14px` (description) |
| `--typography/size/xs` | `12px` (button label) |
| `--typography/line-height (Descreptive)/6` | `24px` (title) |
| `--typography/line-height (Descreptive)/5` | `20px` (description) |
| `--typography/line-height (Descreptive)/4` | `16px` (button label) |

Fixed values: container width 400px; icons 18x18px; content column gap 4px; description row gap 5px; button min/max height 32px; link text is hard-coded 14px / 20px bold underlined (no tokens).

## Text styles

- `Bold/$text-base`: Font(family: "Typography/Family/Font", style: Typography/Weight/Bold, size: Typography/Size/md, weight: 700, lineHeight: typography/line-height (Descreptive)/6, letterSpacing: 0)
- `Regular/$text-sm`: Font(family: "Typography/Family/Font", style: Typography/Weight/Regular, size: Typography/Size/sm, weight: 400, lineHeight: typography/line-height (Descreptive)/5, letterSpacing: 0)

## Component description (from Figma)

- No component description was included in the response.

## Assets

- `figma-asset:e1aa9.svg` — cancel-01-outline (close icon, node 17999:400756, 18x18)
- `figma-asset:4074b.svg` — information-circle-outline (start icon, node 15375:52008, 18x18)

## Notes

- Default Arabic copy: title "عنوان التنبه", description "لديك 3 طلبات جديدة...", button/link "حدث الصفحة".
- Original asset URL prefix `https://www.figma.com/api/mcp/asset/<uuid>/` replaced with `figma-asset:` placeholder.
