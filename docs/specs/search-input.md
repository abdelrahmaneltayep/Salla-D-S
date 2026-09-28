# SearchInput

- Figma node id: `14952:18116`
- File key: `dnmyqzYKK9dUJjVHuIWMDS`
- Source: `mcp__Figma__get_design_context` (screenshot excluded)

> Note: the original response defined `assetPathPrefix` as a temporary `https://www.figma.com/api/mcp/asset/<uuid>` URL. It has been replaced with the `figma-asset:` placeholder below; everything else is verbatim.

## Returned code

```tsx
const assetPathPrefix = "figma-asset:";
const imgAlertCircleOutline = `${assetPathPrefix}/020c4.svg`;
const imgSearch01Outline = `${assetPathPrefix}/55de9.svg`;

type SearchInputProps = {
  className?: string;
  error?: "False";
  info?: boolean;
  language?: "Arabic";
  placeholder?: string;
  searchIcon?: boolean;
  state?: "--default";
};

function SearchInput({ className, error = "False", info = false, language = "Arabic", placeholder = "بحث", searchIcon = true, state = "--default" }: SearchInputProps) {
  return (
    <div className={className || "content-stretch flex flex-col gap-[var(--spacing\\/5xs,4px)] items-center relative w-[375px]"} data-node-id="14952:18116">
      <div className="bg-[var(--background\/default\/input,white)] border border-[var(--border\/default,#eee)] border-solid content-stretch flex items-center justify-end overflow-clip relative rounded-[var(--radius\/sm,8px)] shrink-0 w-full" data-node-id="14952:18117" data-name="inputContainer">
        <div className="content-stretch flex flex-[1_0_0] gap-[var(--spacing\/sizes\/sm,8px)] items-center justify-end min-h-[40px] min-w-px px-[var(--spacing\/sizes\/lg,12px)] py-[var(--spacing\/sizes\/sm,8px)] relative" data-node-id="14952:18118" data-name="contentContainer">
          {info && (
            <div className="content-stretch flex items-center relative shrink-0 w-[16px]" data-node-id="14952:18120" data-name="_info">
              <div className="flex-[1_0_0] h-[16px] min-w-px relative" data-node-id="14952:18121" data-name="alert-circle-outline">
                <img alt="" className="absolute block inset-0 max-w-none size-full" src={imgAlertCircleOutline} />
              </div>
            </div>
          )}
          <div className="content-stretch flex flex-[1_0_0] items-center justify-end min-w-px relative" data-node-id="14952:18122" data-name="__label">
            <p className="[word-break:break-word] font-[family-name:var(--typography\/family\/font,'Ping_AR_+_LT:Regular')] font-[var(--typography\/weight\/regular,normal)] leading-[var(--typography\/line-height-\(descreptive\)\/5,20px)] relative shrink-0 text-[color:var(--text\/gray\/light,#666)] text-[length:var(--typography\/size\/sm,14px)] text-right whitespace-nowrap" dir="auto" data-node-id="14952:18123">
              {placeholder}
            </p>
          </div>
          {searchIcon && (
            <div className="content-stretch flex items-center relative shrink-0" data-node-id="14952:18820" data-name="__iconStart">
              <div className="relative shrink-0 size-[20px]" data-node-id="14952:18821" data-name="search-01-outline">
                <img alt="" className="absolute block inset-0 max-w-none size-full" src={imgSearch01Outline} />
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
```

## Design tokens / variables used

- `--background/default/input` = `white`
- `--border/default` = `#eee`
- `--radius/sm` = `8px`
- `--spacing/5xs` = `4px`
- `--spacing/sizes/sm` = `8px`
- `--spacing/sizes/lg` = `12px`
- `--typography/family/font` = `Ping AR + LT` (Regular)
- `--typography/weight/regular` = `normal` (400)
- `--typography/size/sm` = `14px`
- `--typography/line-height (Descreptive)/5` = `20px`
- `--text/gray/light` = `#666`
- Search icon size `20px`; info icon `16px`; min-height `40px`; default frame width `375px`

## Text styles in the design

- `Regular/$text-sm`: Font(family: "Typography/Family/Font", style: Typography/Weight/Regular, size: Typography/Size/sm, weight: 400, lineHeight: typography/line-height (Descreptive)/5, letterSpacing: 0)

## Assets (SVG)

- `figma-asset:020c4.svg` — alert-circle-outline (16x16), node 14952:18121
- `figma-asset:55de9.svg` — search-01-outline (20x20), node 14952:18821

## Notes from the response

- Node ids are added to the code as `data-node-id` attributes.
- The generated React+Tailwind is a reference prototype that must be converted to the target stack; do not install Tailwind.
- Assets on the Figma server expire in 7 days (download URLs blocked in this environment; not downloaded).
