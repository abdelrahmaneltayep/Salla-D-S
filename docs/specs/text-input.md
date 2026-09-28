# TextInput

- Figma node id: `14805:10166`
- File key: `dnmyqzYKK9dUJjVHuIWMDS`
- Source: `mcp__Figma__get_design_context` (screenshot excluded)

> Note: the original response defined `assetPathPrefix` as a temporary `https://www.figma.com/api/mcp/asset/<uuid>` URL. It has been replaced with the `figma-asset:` placeholder below; everything else is verbatim.

## Returned code

```tsx
const assetPathPrefix = "figma-asset:";
const imgSaudiRiyal = `${assetPathPrefix}/595c7.svg`;
const imgAlertCircleOutline = `${assetPathPrefix}/020c4.svg`;
const imgArrowDown01Outline = `${assetPathPrefix}/2f628.svg`;
const imgFile01Outline = `${assetPathPrefix}/940b5.svg`;

type TextInputProps = {
  className?: string;
  error?: "False";
  iconStart?: boolean;
  info?: boolean;
  language?: "Arabic";
  placeholder?: string;
  saudiRiyal?: boolean;
  state?: "--default";
  subtextLabel?: string;
  subtextUnit?: boolean;
  swapIconStart?: React.ReactNode | null;
  translation?: boolean;
};

function TextInput({ className, error = "False", iconStart = true, info = false, language = "Arabic", placeholder = "نص بديل للحقل", saudiRiyal = false, state = "--default", subtextLabel = "وصف مساعد", subtextUnit = true, swapIconStart = null, translation = true }: TextInputProps) {
  return (
    <div className={className || "content-stretch flex items-end justify-center relative w-[375px]"} data-node-id="14805:10166">
      <div className="bg-[var(--background\/default\/input,white)] border border-[var(--border\/default,#eee)] border-solid content-stretch flex flex-[1_0_0] items-center justify-end min-w-px overflow-clip relative rounded-[var(--radius\/xl,8px)]" data-node-id="14805:10170" data-name="inputContainer">
        <div className="content-stretch flex flex-[1_0_0] gap-[var(--spacing\/sizes\/sm,8px)] items-center justify-end min-h-[40px] min-w-px px-[var(--spacing\/sizes\/lg,12px)] py-[var(--spacing\/sizes\/sm,8px)] relative" data-node-id="14900:10667" data-name="contentContainer">
          {saudiRiyal && (
            <div className="relative shrink-0 size-[16px]" data-node-id="24131:22742" data-name="Saudi-Riyal">
              <img alt="" className="absolute block inset-0 max-w-none size-full" src={imgSaudiRiyal} />
            </div>
          )}
          {info && (
            <div className="content-stretch flex items-center relative shrink-0 w-[16px]" data-node-id="14937:16582" data-name="__info">
              <div className="flex-[1_0_0] h-[16px] min-w-px relative" data-node-id="14937:16583" data-name="alert-circle-outline">
                <img alt="" className="absolute block inset-0 max-w-none size-full" src={imgAlertCircleOutline} />
              </div>
            </div>
          )}
          {translation && (
            <div className="content-stretch flex flex-col items-start relative shrink-0" data-node-id="14900:10670" data-name="__translation">
              <div className="border border-[var(--border\/default,#eee)] border-solid content-stretch flex gap-[var(--spacing\/sizes\/3xs,2px)] items-center justify-center px-[var(--spacing\/sizes\/sm,8px)] py-[var(--spacing\/5xs,4px)] relative rounded-[var(--radius\/xl,8px)] shrink-0 w-full" data-node-id="14900:10671" data-name="_Translation">
                <div className="relative shrink-0 size-[16px]" data-node-id="I14900:10671;12364:40387" data-name="arrow-down-01-outline">
                  <img alt="" className="absolute block inset-0 max-w-none size-full" src={imgArrowDown01Outline} />
                </div>
                <p className="[word-break:break-word] font-[family-name:var(--typography\/family\/font,'Ping_AR_+_LT:Regular')] font-[var(--typography\/weight\/regular,normal)] leading-[var(--typography\/line-height-\(descreptive\)\/4,16px)] relative shrink-0 text-[color:var(--text\/gray\/light,#666)] text-[length:var(--typography\/size\/xs,12px)] text-right whitespace-nowrap" data-node-id="I14900:10671;8758:34252">
                  AR
                </p>
              </div>
            </div>
          )}
          {subtextUnit && (
            <div className="content-stretch flex items-center justify-center relative shrink-0" data-node-id="14900:10672" data-name="__subtext">
              <p className="[word-break:break-word] font-[family-name:var(--typography\/family\/font,'Ping_AR_+_LT:Regular')] font-[var(--typography\/weight\/regular,normal)] leading-[var(--typography\/line-height-\(descreptive\)\/4,16px)] relative shrink-0 text-[color:var(--text\/gray\/light,#666)] text-[length:var(--typography\/size\/xs,12px)] text-right whitespace-nowrap" dir="auto" data-node-id="14900:10673">
                {subtextLabel}
              </p>
            </div>
          )}
          <div className="content-stretch flex flex-[1_0_0] items-center justify-end min-w-px relative" data-node-id="14900:10674" data-name="__label">
            <p className="[word-break:break-word] font-[family-name:var(--typography\/family\/font,'Ping_AR_+_LT:Regular')] font-[var(--typography\/weight\/regular,normal)] leading-[var(--typography\/line-height-\(descreptive\)\/5,20px)] relative shrink-0 text-[color:var(--text\/gray\/light,#666)] text-[length:var(--typography\/size\/sm,14px)] text-right whitespace-nowrap" dir="auto" data-node-id="14900:10675">
              {placeholder}
            </p>
          </div>
          {iconStart && (
            <div className="content-stretch flex items-center relative shrink-0 w-[16px]" data-node-id="14900:10676" data-name="__iconStart">
              {swapIconStart || (
                <div className="flex-[1_0_0] h-[16px] min-w-px relative" data-node-id="14900:10677" data-name="file-01-outline">
                  <img alt="" className="absolute block inset-0 max-w-none size-full" src={imgFile01Outline} />
                </div>
              )}
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
- `--radius/xl` = `8px`
- `--spacing/sizes/sm` = `8px`
- `--spacing/sizes/lg` = `12px`
- `--spacing/sizes/3xs` = `2px`
- `--spacing/5xs` = `4px`
- `--typography/family/font` = `Ping AR + LT` (Regular)
- `--typography/weight/regular` = `normal` (400)
- `--typography/size/xs` = `12px`, `--typography/size/sm` = `14px`
- `--typography/line-height (Descreptive)/4` = `16px`, `/5` = `20px`
- `--text/gray/light` = `#666`
- min-height of contentContainer: `40px`; default frame width `375px`

## Text styles in the design

- `Regular/$text-xs`: Font(family: "Typography/Family/Font", style: Typography/Weight/Regular, size: Typography/Size/xs, weight: 400, lineHeight: typography/line-height (Descreptive)/4, letterSpacing: 0)
- `Regular/$text-sm`: Font(family: "Typography/Family/Font", style: Typography/Weight/Regular, size: Typography/Size/sm, weight: 400, lineHeight: typography/line-height (Descreptive)/5, letterSpacing: 0)

## Assets (SVG)

- `figma-asset:595c7.svg` — Saudi-Riyal icon (16x16), node 24131:22742
- `figma-asset:020c4.svg` — alert-circle-outline (16x16), node 14937:16583
- `figma-asset:2f628.svg` — arrow-down-01-outline (16x16), node I14900:10671;12364:40387
- `figma-asset:940b5.svg` — file-01-outline (16x16), node 14900:10677

## Notes from the response

- Node ids are added to the code as `data-node-id` attributes.
- The generated React+Tailwind is a reference prototype that must be converted to the target stack; do not install Tailwind.
- Assets on the Figma server expire in 7 days (download URLs blocked in this environment; not downloaded).
