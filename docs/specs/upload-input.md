# UploadInput

- Figma node id: `15040:14565`
- File key: `dnmyqzYKK9dUJjVHuIWMDS`
- Source: `mcp__Figma__get_design_context` (screenshot excluded)

> Note: the original response defined `assetPathPrefix` as a temporary `https://www.figma.com/api/mcp/asset/<uuid>` URL. It has been replaced with the `figma-asset:` placeholder below; everything else is verbatim.

## Returned code

```tsx
const assetPathPrefix = "figma-asset:";
const imgImageUpload01Outline = `${assetPathPrefix}/2c531.svg`;
const imgUpload04Outline = `${assetPathPrefix}/a1dba.svg`;

type UploadInputProps = {
  className?: string;
  error?: "false";
  langugae?: "Arabic";
  state?: "--default";
  variant?: "--multiple";
};

function UploadInput({ className, error = "false", langugae = "Arabic", state = "--default", variant = "--multiple" }: UploadInputProps) {
  return (
    <div className={className || "content-end flex flex-wrap gap-[var(--spacing\\/sizes\\/2xl,16px)] gap-y-[16px] items-end justify-end relative w-[848px]"} data-node-id="15040:14565">
      <div className="content-stretch flex flex-[1_0_0] flex-col items-center justify-end min-w-px overflow-clip relative rounded-[var(--radius\/xl,8px)]" data-node-id="15040:14409" data-name="_uploadZone">
        <div className="bg-[var(--fill,white)] border-2 border-[var(--border,#eee)] border-dashed content-stretch flex items-start justify-end overflow-clip relative rounded-[var(--radius\/xl,8px)] shrink-0 w-full" data-node-id="I15040:14409;14973:28015" data-name="inputContainer">
          <div className="content-stretch flex flex-[1_0_0] flex-col gap-[var(--spacing\/sizes\/2xl,16px)] items-center min-w-px p-[var(--spacing\/sizes\/4xl,24px)] relative" data-node-id="I15040:14409;14973:29468" data-name="Placeholder">
            <div className="content-stretch flex items-center justify-end relative shrink-0" data-node-id="I15040:14409;14973:29469" data-name="iconTop">
              <div className="relative shrink-0 size-[32px]" data-node-id="I15040:14409;14973:29470" data-name="image-upload-01-outline">
                <img alt="" className="absolute block inset-0 max-w-none size-full" src={imgImageUpload01Outline} />
              </div>
            </div>
            <div className="[word-break:break-word] content-stretch flex flex-col gap-[var(--spacing\/sizes\/2xs,4px)] items-start relative shrink-0 text-center w-full" data-node-id="I15040:14409;14973:29559" data-name="contentContainer">
              <p className="font-[family-name:var(--typography\/family\/font,'Ping_AR_+_LT:Medium')] font-[var(--typography\/weight\/medium,normal)] leading-[var(--typography\/line-height-\(descreptive\)\/5,20px)] relative shrink-0 text-[color:var(--text\/gray\/dark,#333)] text-[length:var(--typography\/size\/sm,14px)] w-full" dir="auto" data-node-id="I15040:14409;14973:29471">
                اسحب الملفات هنا لرفعها
              </p>
              <div className="font-[family-name:var(--typography\/family\/font,'Ping_AR_+_LT:Regular')] font-[var(--typography\/weight\/regular,normal)] leading-[0] relative shrink-0 text-[color:var(--text\/gray\/lighter,#737373)] text-[length:var(--typography\/size\/xs,12px)] w-full" data-node-id="I15040:14409;14973:29558">
                <p className="leading-[var(--typography\/line-height-\(descreptive\)\/4,16px)] mb-0" dir="auto">
                  اقصى حجم مسموح هو 2MB. انواع الملفات المسموح بها هي:
                </p>
                <p className="leading-[var(--typography\/line-height-\(descreptive\)\/4,16px)]" dir="auto">
                  .JPEG, .JPG, .PNG
                </p>
              </div>
            </div>
            <div className="content-stretch flex flex-col gap-[var(--spacing\/6xs,2px)] items-center relative shrink-0" data-node-id="I15040:14409;21684:32609" data-name="buttons">
              <div className="content-stretch flex flex-col items-start relative shrink-0" data-node-id="I15040:14409;14973:29523" data-name="__buttonEnd">
                <div className="border border-[var(--border\/default,#eee)] border-solid content-stretch flex gap-[var(--spacing\/5xs,4px)] items-center justify-center max-h-[32px] min-h-[32px] px-[var(--spacing\/3xs,8px)] py-[var(--spacing\/xs,12px)] relative rounded-[var(--radius\/xl,8px)] shrink-0" data-node-id="I15040:14409;14973:29524" data-name="Button">
                  <div className="content-stretch flex flex-col items-start relative shrink-0" data-node-id="I15040:14409;14973:29524;14671:7581" data-name="__icon-end">
                    <div className="relative shrink-0 size-[16px]" data-node-id="I15040:14409;14973:29524;14671:7582" data-name="add-01-outline">
                      <img alt="" className="absolute block inset-0 max-w-none size-full" src={imgUpload04Outline} />
                    </div>
                  </div>
                  <div className="content-stretch flex flex-col items-center justify-center relative shrink-0" data-node-id="I15040:14409;14973:29524;14671:7583" data-name="__label">
                    <div className="[word-break:break-word] flex flex-col font-[family-name:var(--typography\/family\/font,'Ping_AR_+_LT:Medium')] font-[var(--typography\/weight\/medium,normal)] justify-center leading-[0] relative shrink-0 text-[color:var(--text\/gray\/dark,#333)] text-[length:var(--typography\/size\/xs,12px)] text-center whitespace-nowrap" data-node-id="I15040:14409;14973:29524;14671:7584">
                      <p className="leading-[var(--typography\/line-height-\(descreptive\)\/4,16px)]" dir="auto">
                        أو تصفح من جهازك
                      </p>
                    </div>
                  </div>
                </div>
              </div>
              <div className="content-stretch flex flex-col items-start relative shrink-0" data-node-id="I15040:14409;21684:32192" data-name="youtube link">
                <div className="content-stretch flex gap-[var(--spacing\/5xs,4px)] items-center justify-center max-h-[32px] min-h-[32px] px-[var(--spacing\/3xs,8px)] py-[var(--spacing\/xs,12px)] relative rounded-[var(--radius\/xl,8px)] shrink-0" data-node-id="I15040:14409;21684:32193" data-name="Button">
                  <div className="content-stretch flex flex-col items-center justify-center relative shrink-0" data-node-id="I15040:14409;21684:32196" data-name="__label">
                    <div className="[word-break:break-word] flex flex-col font-[family-name:var(--typography\/family\/font,'Ping_AR_+_LT:Regular')] font-[var(--typography\/weight\/regular,normal)] justify-center leading-[0] relative shrink-0 text-[0px] text-[color:var(--text\/primary\/link,#004956)] text-center whitespace-nowrap" data-node-id="I15040:14409;21684:32197">
                      <p className="[text-decoration-skip-ink:none] [text-underline-position:from-font] decoration-from-font decoration-solid font-['Ping_AR_+_LT:Regular'] leading-[20px] not-italic text-[14px] underline" dir="auto">
                        او اضف رابط يوتيوب
                      </p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
```

## Design tokens / variables used

- `--fill` = `white` (upload zone background)
- `--border` = `#eee` (2px dashed upload-zone border), `--border/default` = `#eee` (browse button border)
- `--radius/xl` = `8px`
- `--spacing/sizes/2xl` = `16px`, `--spacing/sizes/4xl` = `24px` (zone padding), `--spacing/sizes/2xs` = `4px`
- `--spacing/6xs` = `2px`, `--spacing/5xs` = `4px`, `--spacing/3xs` = `8px`, `--spacing/xs` = `12px`
- `--typography/family/font` = `Ping AR + LT` (Regular / Medium)
- `--typography/weight/regular` = 400, `--typography/weight/medium` = 500
- `--typography/size/xs` = `12px`, `--typography/size/sm` = `14px`
- `--typography/line-height (Descreptive)/4` = `16px`, `/5` = `20px`
- `--text/gray/dark` = `#333`, `--text/gray/lighter` = `#737373`, `--text/primary/link` = `#004956`
- Buttons: min/max height `32px`; top icon `32px`; button icon `16px`; default frame width `848px`

## Text styles in the design

- `Medium/$text-sm`: Font(family: "Typography/Family/Font", style: Typography/Weight/Medium, size: Typography/Size/sm, weight: 500, lineHeight: typography/line-height (Descreptive)/5, letterSpacing: 0)
- `Regular/$text-xs`: Font(family: "Typography/Family/Font", style: Typography/Weight/Regular, size: Typography/Size/xs, weight: 400, lineHeight: typography/line-height (Descreptive)/4, letterSpacing: 0)
- `Medium/$text-xs`: Font(family: "Typography/Family/Font", style: Typography/Weight/Medium, size: Typography/Size/xs, weight: 500, lineHeight: typography/line-height (Descreptive)/4, letterSpacing: 0)
- `Regular/$text-sm`: Font(family: "Typography/Family/Font", style: Typography/Weight/Regular, size: Typography/Size/sm, weight: 400, lineHeight: typography/line-height (Descreptive)/5, letterSpacing: 0)

## Component description (from Figma)

### Button — Node ID: 14526:107536

Keywords: [Action trigger, Clickable element, UI control, Interactive button, Command button, Call-to-action (CTA) button, Press component, زرار]

## Assets (SVG)

- `figma-asset:2c531.svg` — image-upload-01-outline (32x32), node I15040:14409;14973:29470
- `figma-asset:a1dba.svg` — upload-04-outline (16x16; layer named add-01-outline), node I15040:14409;14973:29524;14671:7582

## Notes from the response

- Node ids are added to the code as `data-node-id` attributes.
- The generated React+Tailwind is a reference prototype that must be converted to the target stack; do not install Tailwind.
- Assets on the Figma server expire in 7 days (download URLs blocked in this environment; not downloaded).
