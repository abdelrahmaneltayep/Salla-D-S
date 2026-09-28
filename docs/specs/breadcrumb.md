# Breadcrumb — count=2, device=Desktop, language=Arabic

- Figma file: `dnmyqzYKK9dUJjVHuIWMDS`
- Figma node id: `15392:76150`
- Parent component set: `15392:76151` (Breadcrumb)
- Item sub-component nodes referenced: `15392:5076` / `15392:5078` (_breadcrumbItem Text default / active), `15392:76108` (arrow separator)

## Code (verbatim from get_design_context)

```tsx
const assetPathPrefix = "figma-asset:";
const imgArrowLeft01Outline = `${assetPathPrefix}/9b1ae.svg`;

type BreadcrumbItemProps = {
  className?: string;
  language?: "Arabic";
  status?: "--default" | "--active";
  type?: "Text";
};

function BreadcrumbItem({ className, language = "Arabic", status = "--default", type = "Text" }: BreadcrumbItemProps) {
  const isArabicAndActiveAndText = language === "Arabic" && status === "--active" && type === "Text";
  return (
    <div className={className || "content-stretch flex items-start p-[var(--spacing\\/5xs,4px)] relative"} id={isArabicAndActiveAndText ? "node-15392_5078" : "node-15392_5076"}>
      <div className={`${String.raw`[word-break:break-word] flex flex-col font-[family-name:var(--typography\/family\/font,"Ping_AR_+_LT:Regular")] font-[var(--typography\/weight\/regular,normal)] justify-center leading-[0] relative shrink-0 text-right whitespace-nowrap `}${isArabicAndActiveAndText ? String.raw`text-[color:var(--text\/primary\/primary,#004956)] text-[length:var(--typography\/size\/sm,14px)]` : String.raw`text-[0px] text-[color:var(--text\/gray\/lighter,#737373)]`}`} id={isArabicAndActiveAndText ? "node-15392_5079" : "node-15392_5077"}>
        <p className={isArabicAndActiveAndText ? String.raw`leading-[var(--typography\/line-height-\(descreptive\)\/5,20px)]` : 'font-["Ping_AR_+_LT:Regular"] leading-[20px] not-italic text-[#737373] text-[14px]'} dir="auto">
          عنوان
        </p>
      </div>
    </div>
  );
}

type BreadcrumbProps = {
  className?: string;
  count?: "2";
  device?: "Desktop";
  language?: "Arabic";
};

function Breadcrumb({ className, count = "2", device = "Desktop", language = "Arabic" }: BreadcrumbProps) {
  return (
    <div className={className || "content-stretch flex gap-[var(--spacing-7xl,24px)] items-center justify-end px-[var(--spacing\\/7xl,56px)] py-[var(--spacing\\/3xs,8px)] relative w-[1536px]"} data-node-id="15392:76150">
      <div className="content-stretch flex flex-[1_0_0] gap-[var(--spacing\/3xs,8px)] items-center justify-end min-w-px relative" data-node-id="15392:73633" data-name="listContainer">
        <BreadcrumbItem className="content-stretch flex items-start p-[var(--spacing\/5xs,4px)] relative shrink-0" status="--active" />
        <div className="content-stretch flex items-start p-[var(--spacing\/5xs,4px)] relative shrink-0" data-node-id="15392:76108" data-name="_breadcrumbItem">
          <div className="relative shrink-0 size-[24px]" data-node-id="I15392:76108;15392:75943" data-name="arrow-left-01-outline">
            <img alt="" className="absolute block inset-0 max-w-none size-full" src={imgArrowLeft01Outline} />
          </div>
        </div>
        <BreadcrumbItem className="content-stretch flex items-start p-[var(--spacing\/5xs,4px)] relative shrink-0" />
      </div>
    </div>
  );
}
```

## Design tokens / variables referenced in the code

| Token (CSS var) | Fallback |
|---|---|
| `--spacing-7xl` | `24px` (outer gap; note hyphen naming) |
| `--spacing/7xl` | `56px` (outer padding-x) |
| `--spacing/3xs` | `8px` (outer padding-y; list gap) |
| `--spacing/5xs` | `4px` (item padding) |
| `--typography/family/font` | `"Ping AR + LT:Regular"` |
| `--typography/weight/regular` | `normal` (400) |
| `--typography/size/sm` | `14px` |
| `--typography/line-height (Descreptive)/5` | `20px` |
| `--text/primary/primary` | `#004956` (active item) |
| `--text/gray/lighter` | `#737373` (default item; the inner `<p>` also hard-codes `#737373` / 14px / 20px) |

Fixed values: container width 1536px (desktop); separator icon 24x24px (arrow-left-01-outline). Items are laid out `justify-end` for RTL, active item first.

## Text styles

- `Regular/$text-sm`: Font(family: "Typography/Family/Font", style: Typography/Weight/Regular, size: Typography/Size/sm, weight: 400, lineHeight: typography/line-height (Descreptive)/5, letterSpacing: 0).

## Component description (from Figma)

**Breadcrumb** — Node ID: 15392:76151. Keywords: [Navigation path, Hierarchy navigation, Location trail, Path-based navigation, Secondary navigation, Clickable links, UI element, Navigation component, مسار التنقل, مسار التصفح, شريط المسار, دليل الموقع, روابط تتبع المسار, عنصر واجهة المستخدم, التنقل الهرمي]

## Assets

- `figma-asset:9b1ae.svg` — arrow-left-01-outline separator (node I15392:76108;15392:75943, 24x24)

## Notes

- Original asset URL prefix `https://www.figma.com/api/mcp/asset/<uuid>/` replaced with `figma-asset:` placeholder.
