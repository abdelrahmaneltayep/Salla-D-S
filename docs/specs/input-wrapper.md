# InputWrapper

- Figma node id: `14900:14750` (component set / parent: `14900:14749`)
- File key: `dnmyqzYKK9dUJjVHuIWMDS`
- Source: `mcp__Figma__get_design_context` (screenshot excluded)

> Note: the original response defined `assetPathPrefix` as a temporary `https://www.figma.com/api/mcp/asset/<uuid>` URL. It has been replaced with the `figma-asset:` placeholder below; everything else is verbatim.

## Returned code

```tsx
const assetPathPrefix = "figma-asset:";
const imgFile01Outline = `${assetPathPrefix}/64c65.svg`;

type InputWrapperProps = {
  className?: string;
  inputLabel?: boolean;
  langauge?: "Arabic";
  tip?: boolean;
  variant?: "--text";
};

function InputWrapper({ className, inputLabel = true, langauge = "Arabic", tip = false, variant = "--text" }: InputWrapperProps) {
  return (
    <div className={className || "content-stretch flex flex-col gap-[var(--spacing\\/sizes\\/sm,8px)] items-center justify-end relative w-[375px]"} data-node-id="14900:14750">
      {inputLabel && (
        <div className="content-stretch flex flex-col items-center justify-end relative shrink-0 w-full" data-node-id="14900:14751" data-name="__titleContainer">
          <div className="content-stretch flex gap-[var(--spacing\/3xs,8px)] items-start justify-end relative shrink-0 w-full" data-node-id="14900:14752" data-name="_inputLabel">
            <div className="content-stretch flex flex-[1_0_0] flex-col gap-[var(--spacing\/sizes\/sm,8px)] items-start min-w-px relative" data-node-id="I14900:14752;8765:17201" data-name="bodyContainer">
              <div className="content-stretch flex gap-[var(--spacing\/sizes\/2xs,4px)] items-center justify-end relative shrink-0 w-full" data-node-id="I14900:14752;8765:17202" data-name="titleContainer">
                <div className="content-stretch flex items-start relative shrink-0" data-node-id="I14900:14752;8765:17205" data-name="labelContainer">
                  <p className="[word-break:break-word] font-[family-name:var(--typography\/family\/font,'Ping_AR_+_LT:Regular')] font-[var(--typography\/weight\/regular,normal)] leading-[var(--typography\/line-height-\(descreptive\)\/5,20px)] relative shrink-0 text-[color:var(--text\/gray\/dark,#333)] text-[length:var(--typography\/size\/sm,14px)] text-right whitespace-nowrap" dir="auto" data-node-id="I14900:14752;8765:17206">
                    عنوان الحقل
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      )}
      <div className="content-stretch flex flex-col items-start relative shrink-0 w-full" data-node-id="14900:15171" data-name="__input">
        <div className="content-stretch flex items-end justify-center relative shrink-0 w-full" data-node-id="14900:15048" data-name="_TextInput">
          <div className="bg-[var(--background\/default\/input,white)] border border-[var(--border\/default,#eee)] border-solid content-stretch flex flex-[1_0_0] items-center justify-end min-w-px overflow-clip relative rounded-[var(--radius\/xl,8px)]" data-node-id="I14900:15048;14805:10170" data-name="inputContainer">
            <div className="content-stretch flex flex-[1_0_0] gap-[var(--spacing\/sizes\/sm,8px)] items-center justify-end min-h-[40px] min-w-px px-[var(--spacing\/sizes\/lg,12px)] py-[var(--spacing\/sizes\/sm,8px)] relative" data-node-id="I14900:15048;14900:10667" data-name="contentContainer">
              <div className="content-stretch flex flex-[1_0_0] items-center justify-end min-w-px relative" data-node-id="I14900:15048;14900:10674" data-name="__label">
                <p className="[word-break:break-word] font-[family-name:var(--typography\/family\/font,'Ping_AR_+_LT:Regular')] font-[var(--typography\/weight\/regular,normal)] leading-[var(--typography\/line-height-\(descreptive\)\/5,20px)] relative shrink-0 text-[color:var(--text\/gray\/light,#666)] text-[length:var(--typography\/size\/sm,14px)] text-right whitespace-nowrap" dir="auto" data-node-id="I14900:15048;14900:10675">
                  نص بديل للحقل
                </p>
              </div>
              <div className="content-stretch flex items-center relative shrink-0 w-[16px]" data-node-id="I14900:15048;14900:10676" data-name="__iconStart">
                <div className="flex-[1_0_0] h-[16px] min-w-px relative" data-node-id="I14900:15048;14900:10677" data-name="file-01-outline">
                  <img alt="" className="absolute block inset-0 max-w-none size-full" src={imgFile01Outline} />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      {tip && (
        <div className="content-stretch flex flex-col items-start relative shrink-0 w-full" data-node-id="14900:15132" data-name="__tipContainer">
          <div className="content-stretch flex gap-[var(--spacing\/5xs,4px)] items-center justify-end relative shrink-0 w-full" data-node-id="14900:15073" data-name="_inputTip">
            <p className="[word-break:break-word] flex-[1_0_0] font-[family-name:var(--typography\/family\/font,'Ping_AR_+_LT:Regular')] font-[var(--typography\/weight\/regular,normal)] leading-[var(--typography\/line-height-\(descreptive\)\/4,16px)] min-w-px relative text-[color:var(--text\/gray\/light,#666)] text-[length:var(--typography\/size\/xs,12px)] text-right" dir="auto" data-node-id="I14900:15073;8765:17371">
              نص بديل لمعلومات الحفل
            </p>
          </div>
        </div>
      )}
    </div>
  );
}
```

## Design tokens / variables used

- `--background/default/input` = `white`
- `--border/default` = `#eee`
- `--radius/xl` = `8px`
- `--spacing/sizes/sm` = `8px`, `--spacing/sizes/lg` = `12px`, `--spacing/sizes/2xs` = `4px`
- `--spacing/3xs` = `8px`, `--spacing/5xs` = `4px`
- `--typography/family/font` = `Ping AR + LT` (Regular)
- `--typography/weight/regular` = `normal` (400)
- `--typography/size/xs` = `12px`, `--typography/size/sm` = `14px`
- `--typography/line-height (Descreptive)/4` = `16px`, `/5` = `20px`
- `--text/gray/dark` = `#333` (label), `--text/gray/light` = `#666` (placeholder, tip)
- Structure: `__titleContainer` (label, gap 8) → `__input` (embeds `_TextInput` 14805:10166) → optional `__tipContainer`

## Text styles in the design

- `Regular/$text-sm`: Font(family: "Typography/Family/Font", style: Typography/Weight/Regular, size: Typography/Size/sm, weight: 400, lineHeight: typography/line-height (Descreptive)/5, letterSpacing: 0)

## Component description (from Figma)

### InputWrapper — Node ID: 14900:14749

- **Keywords:** [Text input, Text field, Text box, String input, Standard input, Single-line input, حقل نصي, خانة نصية, مربع نص, إدخال نصي]
- **Keywords:** [Dropdown, Select, Drop-down menu, Select menu, Picker, Combo box, Option list, Selection field, قائمة منسدلة, قائمة اختيار, مربع تحديد, عنصر اختيار, تحديد من قائمة]
- **Keywords:** [Textarea, Multi-line text input, Comment box, Large text field, Free text area, مساحة نصية, حقل نصي كبير, مربع تعليقات, إدخال نصي متعدد الأسطر]
- **Keywords:** [Phone input, Phone number field, Telephone input, Mobile number field, Contact number, Country code picker, حقل هاتف, إدخال رقم الجوال, خانة رقم الهاتف, رمز الدولة]
- **Keywords:** [Password input, Password field, Secure input, Masked text, Authentication field, Show/Hide toggle, حقل كلمة المرور, خانة كلمة السر, إدخال سري, إظهار/إخفاء كلمة المرور]
- **Keywords:** [Email input, Email address field, Mail input, Contact email, Email validation, حقل البريد الإلكتروني, خانة الإيميل, إدخال البريد الإلكتروني]
- **Keywords:** [Amount input, Number input, Currency input, Price field, Numeric field, Decimal input, Input stepper, حقل المبلغ, إدخال رقمي, خانة السعر, حقل عملة, إدخال قيمة مالية]
- **Keywords:** [File uploader, File input, File select, Upload component, Attachment field, Drag and drop uploader, Choose file, رافع ملفات, حقل تحميل, اختيار ملف, زر رفع, إرفاق ملف, سحب وإفلات]

## Assets (SVG)

- `figma-asset:64c65.svg` — file-01-outline (16x16), node I14900:15048;14900:10677

## Notes from the response

- Node ids are added to the code as `data-node-id` attributes.
- The generated React+Tailwind is a reference prototype that must be converted to the target stack; do not install Tailwind.
- Assets on the Figma server expire in 7 days (download URLs blocked in this environment; not downloaded).
