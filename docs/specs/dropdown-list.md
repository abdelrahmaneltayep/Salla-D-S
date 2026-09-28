# Drop Down List

- Figma node id: `14952:281456` (component: Drop Down List `14952:281457`)
- File key: `dnmyqzYKK9dUJjVHuIWMDS`
- Source: `mcp__Figma__get_design_context` (screenshot excluded)

> Note: the original response defined `assetPathPrefix` as a temporary `https://www.figma.com/api/mcp/asset/<uuid>` URL. It has been replaced with the `figma-asset:` placeholder below; everything else is verbatim.

## Returned code

```tsx
const assetPathPrefix = "figma-asset:";
const imgTickMark = `${assetPathPrefix}/5ec58.svg`;
const imgFile02Outline = `${assetPathPrefix}/66325.svg`;

type CheckBoxProps = {
  className?: string;
  selected?: boolean;
  size?: "md-20px";
  status?: "--default";
};

function CheckBox({ className, selected = true, size = "md-20px", status = "--default" }: CheckBoxProps) {
  const isNotSelectedAndDefault = !selected && status === "--default";
  return (
    <button className={className || `${String.raw`relative rounded-[var(--radius\/md,4px)] size-[20px] `}${isNotSelectedAndDefault ? String.raw`block border border-[var(--border\/primary,#004956)] border-solid` : String.raw`bg-[var(--background\/primary\/primary,#004956)] content-stretch flex flex-col items-center justify-center p-[var(--spacing\/sizes\/3xs,2px)]`}`} id={isNotSelectedAndDefault ? "node-12411_21812" : "node-12411_21810"}>
      {selected && status === "--default" && (
        <div className="relative shrink-0 size-[14px]" data-node-id="12411:21811" data-name="Tick Mark">
          <img alt="" className="absolute block inset-0 max-w-none size-full" src={imgTickMark} />
        </div>
      )}
    </button>
  );
}

type DividerContainerProps = {
  className?: string;
  thickness?: "1px";
  type?: "Horizontal";
};

function DividerContainer({ className, thickness = "1px", type = "Horizontal" }: DividerContainerProps) {
  return (
    <div className={className || "content-stretch flex flex-col items-start relative w-[212px]"} data-node-id="12411:21717">
      <div className="bg-[var(--background\/default\/neutrals,#f4f4f4)] h-px relative shrink-0 w-full" data-node-id="12411:21718" data-name="dividerContainer" />
    </div>
  );
}

type ListTitleProps = {
  className?: string;
  language?: "Arabic";
  variant?: "Category" | "Subcategory";
};

function ListTitle({ className, language = "Arabic", variant = "Category" }: ListTitleProps) {
  const isArabicAndSubcategory = language === "Arabic" && variant === "Subcategory";
  return (
    <div className={className || `${String.raw`bg-[var(--background\/default\/cards,white)] content-stretch flex gap-[var(--spacing\/sizes\/sm,8px)] items-center justify-end relative w-[286px] `}${isArabicAndSubcategory ? String.raw`h-[36px] pl-[var(--spacing\/sizes\/lg,12px)] pr-[var(--spacing\/sizes\/3xl,20px)] py-[var(--spacing\/sizes\/sm,8px)]` : String.raw`h-[44px] px-[var(--spacing\/sizes\/lg,12px)]`}`} id={isArabicAndSubcategory ? "node-14967_14636" : "node-14967_14634"}>
      <div className="content-stretch flex flex-[1_0_0] items-center justify-center min-w-px relative" id={isArabicAndSubcategory ? "node-14967_20296" : "node-14967_20297"} data-name="__label">
        <p className={`${String.raw`[word-break:break-word] flex-[1_0_0] leading-[var(--typography\/line-height-\(descreptive\)\/5,20px)] min-w-px relative text-[color:var(--text\/gray\/light,#666)] text-[length:var(--typography\/size\/sm,14px)] text-right `}${isArabicAndSubcategory ? String.raw`font-[family-name:var(--typography\/family\/font,"Ping_AR_+_LT:Medium")] font-[var(--typography\/weight\/medium,normal)]` : String.raw`font-[family-name:var(--typography\/family\/font,"Ping_AR_+_LT:Bold")] font-[var(--typography\/weight\/bold,normal)]`}`} dir="auto" id={isArabicAndSubcategory ? "node-14967_14637" : "node-14967_14635"}>
          {isArabicAndSubcategory ? "الفئة الثانوية" : "الفئة"}
        </p>
      </div>
    </div>
  );
}

type ScrollProps = {
  className?: string;
  layout?: "vertical";
  width?: "--md-4px";
};

function Scroll({ className, layout = "vertical", width = "--md-4px" }: ScrollProps) {
  return (
    <div className={className || "h-[292px] relative rounded-[var(--radius\\/xl,140px)] w-[4px]"} data-node-id="2059:3245">
      <div className="absolute bg-[var(--background\/default\/neutrals,#f4f4f4)] inset-0 rounded-[var(--radius-3xl-2,48px)]" data-node-id="2059:3246" />
      <div className="absolute bg-[var(--background\/primary\/primary,#004956)] bottom-3/4 left-0 right-0 rounded-[30px] top-0" data-node-id="2059:3247" />
    </div>
  );
}

type DropDownListProps = {
  className?: string;
  checkbox?: "True";
  description?: "True";
  icon?: "False";
  language?: "Arabic";
  scroll?: boolean;
  variant?: "Three layers";
};

function DropDownList({ className, checkbox = "True", description = "True", icon = "False", language = "Arabic", scroll = true, variant = "Three layers" }: DropDownListProps) {
  return (
    <div className={className || "bg-[var(--background\\/default\\/cards,white)] border border-[var(--border\\/focus,#5196f3)] border-solid content-stretch flex items-start overflow-clip p-px relative rounded-[var(--radius\\/sm,8px)] shadow-[var(--shadow\\/lg\\/type-1\\/position-x,0px)_var(--shadow\\/lg\\/type-1\\/position-y,10px)_var(--shadow\\/lg\\/type-1\\/blur,15px)_var(--shadow\\/lg\\/type-1\\/spread,-3px)_var(--shadow\\/lg\\/type-1\\/color,rgba(18,18,23,0.08)),var(--shadow\\/lg\\/type-2\\/position-x,0px)_var(--shadow\\/lg\\/type-2\\/position-y,4px)_var(--shadow\\/lg\\/type-2\\/blur,6px)_var(--shadow\\/lg\\/type-2\\/spread,-2px)_var(--shadow\\/lg\\/type-2\\/color,rgba(18,18,23,0.05))] w-[375px]"} data-node-id="14952:281456">
      {scroll && (
        <div className="relative self-stretch shrink-0" data-node-id="14952:281190" data-name="slideContainer">
          <div className="bg-clip-padding border-0 border-[transparent] border-solid content-stretch flex items-start relative size-full">
            <Scroll className="h-full relative rounded-[var(--radius\/xl,140px)] shrink-0 w-[4px]" />
          </div>
        </div>
      )}
      <div className="flex-[1_0_0] min-w-px relative" data-node-id="14952:281192" data-name="listContainer">
        <div className="bg-clip-padding border-0 border-[transparent] border-solid content-stretch flex flex-col items-start relative size-full">
          <ListTitle className="bg-[var(--background\/default\/cards,white)] h-[44px] relative shrink-0 w-full" />
          <DividerContainer className="relative shrink-0 w-full" />
          <ListTitle className="bg-[var(--background\/default\/cards,white)] h-[36px] relative shrink-0 w-full" variant="Subcategory" />
          <DividerContainer className="relative shrink-0 w-full" />
          <div className="bg-[var(--background\/default\/cards,white)] h-[60px] min-h-[44px] relative shrink-0 w-full" data-node-id="14952:281198" data-name="_listItem">
            <div className="bg-clip-padding border-0 border-[transparent] border-solid content-stretch flex gap-[var(--spacing\/sizes\/sm,8px)] items-center justify-end min-h-[inherit] p-[var(--spacing\/sizes\/lg,12px)] relative size-full">
              <div className="content-stretch flex flex-[1_0_0] flex-col gap-[var(--spacing\/sizes\/2xs,4px)] items-end min-w-px relative" data-node-id="I14952:281198;14952:280022" data-name="textContainer">
                <div className="content-stretch flex items-center justify-center relative shrink-0 w-full" data-node-id="I14952:281198;14967:20362" data-name="__label">
                  <p className="[word-break:break-word] flex-[1_0_0] font-[family-name:var(--typography\/family\/font,'Ping_AR_+_LT:Bold')] font-[var(--typography\/weight\/bold,normal)] leading-[var(--typography\/line-height-\(descreptive\)\/4,16px)] min-w-px relative text-[color:var(--text\/gray\/dark,#333)] text-[length:var(--typography\/size\/xs,12px)] text-right" dir="auto" data-node-id="I14952:281198;14952:22459">
                    خيار رقم (1)
                  </p>
                </div>
                <div className="content-stretch flex items-center justify-center relative shrink-0 w-[123px]" data-node-id="I14952:281198;14967:21131" data-name="__description">
                  <p className="[word-break:break-word] flex-[1_0_0] font-[family-name:var(--typography\/family\/font,'Ping_AR_+_LT:Regular')] font-[var(--typography\/weight\/regular,normal)] leading-[var(--typography\/line-height-\(descreptive\)\/4,16px)] min-w-px relative text-[color:var(--text\/gray\/light,#666)] text-[length:var(--typography\/size\/xs,12px)] text-right" dir="auto" data-node-id="I14952:281198;14952:280028">
                    نص بديل لعرض التفاصيل
                  </p>
                </div>
              </div>
              <CheckBox className="block border border-[var(--border\/primary,#004956)] border-solid cursor-pointer relative rounded-[var(--radius\/md,4px)] shrink-0 size-[20px]" selected={false} />
            </div>
          </div>
          <DividerContainer className="relative shrink-0 w-full" />
          <div className="bg-[var(--background\/default\/cards,white)] h-[60px] min-h-[44px] relative shrink-0 w-full" data-node-id="15119:299656" data-name="_listItem">
            <div className="bg-clip-padding border-0 border-[transparent] border-solid content-stretch flex gap-[var(--spacing\/sizes\/sm,8px)] items-center justify-end min-h-[inherit] p-[var(--spacing\/sizes\/lg,12px)] relative size-full">
              <div className="content-stretch flex flex-[1_0_0] flex-col gap-[var(--spacing\/sizes\/2xs,4px)] items-end min-w-px relative" data-node-id="I15119:299656;14952:280022" data-name="textContainer">
                <div className="content-stretch flex items-center justify-center relative shrink-0 w-full" data-node-id="I15119:299656;14967:20362" data-name="__label">
                  <p className="[word-break:break-word] flex-[1_0_0] font-[family-name:var(--typography\/family\/font,'Ping_AR_+_LT:Bold')] font-[var(--typography\/weight\/bold,normal)] leading-[var(--typography\/line-height-\(descreptive\)\/4,16px)] min-w-px relative text-[color:var(--text\/gray\/dark,#333)] text-[length:var(--typography\/size\/xs,12px)] text-right" dir="auto" data-node-id="I15119:299656;14952:22459">
                    خيار رقم (2)
                  </p>
                </div>
                <div className="content-stretch flex items-center justify-center relative shrink-0 w-[123px]" data-node-id="I15119:299656;14967:21131" data-name="__description">
                  <p className="[word-break:break-word] flex-[1_0_0] font-[family-name:var(--typography\/family\/font,'Ping_AR_+_LT:Regular')] font-[var(--typography\/weight\/regular,normal)] leading-[var(--typography\/line-height-\(descreptive\)\/4,16px)] min-w-px relative text-[color:var(--text\/gray\/light,#666)] text-[length:var(--typography\/size\/xs,12px)] text-right" dir="auto" data-node-id="I15119:299656;14952:280028">
                    نص بديل لعرض التفاصيل
                  </p>
                </div>
              </div>
              <CheckBox className="block border border-[var(--border\/primary,#004956)] border-solid cursor-pointer relative rounded-[var(--radius\/md,4px)] shrink-0 size-[20px]" selected={false} />
            </div>
          </div>
          <DividerContainer className="relative shrink-0 w-full" />
          <div className="bg-[var(--background\/default\/cards,white)] h-[44px] min-h-[44px] relative shrink-0 w-full" data-node-id="14952:281202" data-name="_listItem">
            <div className="bg-clip-padding border-0 border-[transparent] border-solid content-stretch flex gap-[var(--spacing\/sizes\/sm,8px)] items-center justify-end min-h-[inherit] p-[var(--spacing\/sizes\/lg,12px)] relative size-full">
              <div className="content-stretch flex flex-[1_0_0] flex-col gap-[var(--spacing\/sizes\/2xs,4px)] items-end min-w-px relative" data-node-id="I14952:281202;14952:280022" data-name="textContainer">
                <div className="content-stretch flex items-center justify-center relative shrink-0 w-full" data-node-id="I14952:281202;14967:20362" data-name="__label">
                  <p className="[word-break:break-word] flex-[1_0_0] font-[family-name:var(--typography\/family\/font,'Ping_AR_+_LT:Bold')] font-[var(--typography\/weight\/bold,normal)] leading-[var(--typography\/line-height-\(descreptive\)\/4,16px)] min-w-px relative text-[color:var(--text\/gray\/dark,#333)] text-[length:var(--typography\/size\/xs,12px)] text-right" dir="auto" data-node-id="I14952:281202;14952:22459">
                    خيار رقم (1)
                  </p>
                </div>
                <div className="content-stretch flex items-center justify-center relative shrink-0 w-[123px]" data-node-id="I14952:281202;14967:21131" data-name="__description">
                  <p className="[word-break:break-word] flex-[1_0_0] font-[family-name:var(--typography\/family\/font,'Ping_AR_+_LT:Regular')] font-[var(--typography\/weight\/regular,normal)] leading-[var(--typography\/line-height-\(descreptive\)\/4,16px)] min-w-px relative text-[color:var(--text\/gray\/light,#666)] text-[length:var(--typography\/size\/xs,12px)] text-right" dir="auto" data-node-id="I14952:281202;14952:280028">
                    نص بديل لعرض التفاصيل
                  </p>
                </div>
              </div>
              <div className="content-stretch flex items-center relative shrink-0 w-[20px]" data-node-id="I14952:281202;14967:21352" data-name="__iconStart">
                <div className="flex-[1_0_0] h-[20px] min-w-px relative" data-node-id="I14952:281202;14952:22518" data-name="file-02-outline">
                  <img alt="" className="absolute block inset-0 max-w-none size-full" src={imgFile02Outline} />
                </div>
              </div>
              <CheckBox className="block border border-[var(--border\/primary,#004956)] border-solid cursor-pointer relative rounded-[var(--radius\/md,4px)] shrink-0 size-[20px]" selected={false} />
            </div>
          </div>
          <DividerContainer className="relative shrink-0 w-full" />
          <div className="bg-[var(--background\/default\/cards,white)] h-[60px] min-h-[44px] relative shrink-0 w-full" data-node-id="14952:281204" data-name="_listItem">
            <div className="bg-clip-padding border-0 border-[transparent] border-solid content-stretch flex gap-[var(--spacing\/sizes\/sm,8px)] items-center justify-end min-h-[inherit] p-[var(--spacing\/sizes\/lg,12px)] relative size-full">
              <div className="content-stretch flex flex-[1_0_0] flex-col gap-[var(--spacing\/sizes\/2xs,4px)] items-end min-w-px relative" data-node-id="I14952:281204;14952:280022" data-name="textContainer">
                <div className="content-stretch flex items-center justify-center relative shrink-0 w-full" data-node-id="I14952:281204;14967:20362" data-name="__label">
                  <p className="[word-break:break-word] flex-[1_0_0] font-[family-name:var(--typography\/family\/font,'Ping_AR_+_LT:Bold')] font-[var(--typography\/weight\/bold,normal)] leading-[var(--typography\/line-height-\(descreptive\)\/4,16px)] min-w-px relative text-[color:var(--text\/gray\/dark,#333)] text-[length:var(--typography\/size\/xs,12px)] text-right" dir="auto" data-node-id="I14952:281204;14952:22459">
                    خيار رقم (1)
                  </p>
                </div>
                <div className="content-stretch flex items-center justify-center relative shrink-0 w-[123px]" data-node-id="I14952:281204;14967:21131" data-name="__description">
                  <p className="[word-break:break-word] flex-[1_0_0] font-[family-name:var(--typography\/family\/font,'Ping_AR_+_LT:Regular')] font-[var(--typography\/weight\/regular,normal)] leading-[var(--typography\/line-height-\(descreptive\)\/4,16px)] min-w-px relative text-[color:var(--text\/gray\/light,#666)] text-[length:var(--typography\/size\/xs,12px)] text-right" dir="auto" data-node-id="I14952:281204;14952:280028">
                    نص بديل لعرض التفاصيل
                  </p>
                </div>
              </div>
              <CheckBox className="block border border-[var(--border\/primary,#004956)] border-solid cursor-pointer relative rounded-[var(--radius\/md,4px)] shrink-0 size-[20px]" selected={false} />
            </div>
          </div>
          <DividerContainer className="relative shrink-0 w-full" />
          <div className="bg-[var(--background\/default\/cards,white)] h-[60px] min-h-[44px] relative shrink-0 w-full" data-node-id="15119:299634" data-name="_listItem">
            <div className="bg-clip-padding border-0 border-[transparent] border-solid content-stretch flex gap-[var(--spacing\/sizes\/sm,8px)] items-center justify-end min-h-[inherit] p-[var(--spacing\/sizes\/lg,12px)] relative size-full">
              <div className="content-stretch flex flex-[1_0_0] flex-col gap-[var(--spacing\/sizes\/2xs,4px)] items-end min-w-px relative" data-node-id="I15119:299634;14952:280022" data-name="textContainer">
                <div className="content-stretch flex items-center justify-center relative shrink-0 w-full" data-node-id="I15119:299634;14967:20362" data-name="__label">
                  <p className="[word-break:break-word] flex-[1_0_0] font-[family-name:var(--typography\/family\/font,'Ping_AR_+_LT:Bold')] font-[var(--typography\/weight\/bold,normal)] leading-[var(--typography\/line-height-\(descreptive\)\/4,16px)] min-w-px relative text-[color:var(--text\/gray\/dark,#333)] text-[length:var(--typography\/size\/xs,12px)] text-right" dir="auto" data-node-id="I15119:299634;14952:22459">
                    خيار رقم (2)
                  </p>
                </div>
                <div className="content-stretch flex items-center justify-center relative shrink-0 w-[123px]" data-node-id="I15119:299634;14967:21131" data-name="__description">
                  <p className="[word-break:break-word] flex-[1_0_0] font-[family-name:var(--typography\/family\/font,'Ping_AR_+_LT:Regular')] font-[var(--typography\/weight\/regular,normal)] leading-[var(--typography\/line-height-\(descreptive\)\/4,16px)] min-w-px relative text-[color:var(--text\/gray\/light,#666)] text-[length:var(--typography\/size\/xs,12px)] text-right" dir="auto" data-node-id="I15119:299634;14952:280028">
                    نص بديل لعرض التفاصيل
                  </p>
                </div>
              </div>
              <CheckBox className="block border border-[var(--border\/primary,#004956)] border-solid cursor-pointer relative rounded-[var(--radius\/md,4px)] shrink-0 size-[20px]" selected={false} />
            </div>
          </div>
          <DividerContainer className="relative shrink-0 w-full" />
          <ListTitle className="bg-[var(--background\/default\/cards,white)] h-[44px] relative shrink-0 w-full" />
          <DividerContainer className="relative shrink-0 w-full" />
          <ListTitle className="bg-[var(--background\/default\/cards,white)] h-[36px] relative shrink-0 w-full" variant="Subcategory" />
          <DividerContainer className="relative shrink-0 w-full" />
          <div className="bg-[var(--background\/default\/cards,white)] h-[60px] min-h-[44px] relative shrink-0 w-full" data-node-id="14952:281212" data-name="_listItem">
            <div className="bg-clip-padding border-0 border-[transparent] border-solid content-stretch flex gap-[var(--spacing\/sizes\/sm,8px)] items-center justify-end min-h-[inherit] p-[var(--spacing\/sizes\/lg,12px)] relative size-full">
              <div className="content-stretch flex flex-[1_0_0] flex-col gap-[var(--spacing\/sizes\/2xs,4px)] items-end min-w-px relative" data-node-id="I14952:281212;14952:280022" data-name="textContainer">
                <div className="content-stretch flex items-center justify-center relative shrink-0 w-full" data-node-id="I14952:281212;14967:20362" data-name="__label">
                  <p className="[word-break:break-word] flex-[1_0_0] font-[family-name:var(--typography\/family\/font,'Ping_AR_+_LT:Bold')] font-[var(--typography\/weight\/bold,normal)] leading-[var(--typography\/line-height-\(descreptive\)\/4,16px)] min-w-px relative text-[color:var(--text\/gray\/dark,#333)] text-[length:var(--typography\/size\/xs,12px)] text-right" dir="auto" data-node-id="I14952:281212;14952:22459">
                    خيار رقم (1)
                  </p>
                </div>
                <div className="content-stretch flex items-center justify-center relative shrink-0 w-[123px]" data-node-id="I14952:281212;14967:21131" data-name="__description">
                  <p className="[word-break:break-word] flex-[1_0_0] font-[family-name:var(--typography\/family\/font,'Ping_AR_+_LT:Regular')] font-[var(--typography\/weight\/regular,normal)] leading-[var(--typography\/line-height-\(descreptive\)\/4,16px)] min-w-px relative text-[color:var(--text\/gray\/light,#666)] text-[length:var(--typography\/size\/xs,12px)] text-right" dir="auto" data-node-id="I14952:281212;14952:280028">
                    نص بديل لعرض التفاصيل
                  </p>
                </div>
              </div>
              <CheckBox className="block border border-[var(--border\/primary,#004956)] border-solid cursor-pointer relative rounded-[var(--radius\/md,4px)] shrink-0 size-[20px]" selected={false} />
            </div>
          </div>
          <DividerContainer className="relative shrink-0 w-full" />
          <div className="bg-[var(--background\/default\/cards,white)] h-[60px] min-h-[44px] relative shrink-0 w-full" data-node-id="14952:281214" data-name="_listItem">
            <div className="bg-clip-padding border-0 border-[transparent] border-solid content-stretch flex gap-[var(--spacing\/sizes\/sm,8px)] items-center justify-end min-h-[inherit] p-[var(--spacing\/sizes\/lg,12px)] relative size-full">
              <div className="content-stretch flex flex-[1_0_0] flex-col gap-[var(--spacing\/sizes\/2xs,4px)] items-end min-w-px relative" data-node-id="I14952:281214;14952:280022" data-name="textContainer">
                <div className="content-stretch flex items-center justify-center relative shrink-0 w-full" data-node-id="I14952:281214;14967:20362" data-name="__label">
                  <p className="[word-break:break-word] flex-[1_0_0] font-[family-name:var(--typography\/family\/font,'Ping_AR_+_LT:Bold')] font-[var(--typography\/weight\/bold,normal)] leading-[var(--typography\/line-height-\(descreptive\)\/4,16px)] min-w-px relative text-[color:var(--text\/gray\/dark,#333)] text-[length:var(--typography\/size\/xs,12px)] text-right" dir="auto" data-node-id="I14952:281214;14952:22459">
                    خيار رقم (2)
                  </p>
                </div>
                <div className="content-stretch flex items-center justify-center relative shrink-0 w-[123px]" data-node-id="I14952:281214;14967:21131" data-name="__description">
                  <p className="[word-break:break-word] flex-[1_0_0] font-[family-name:var(--typography\/family\/font,'Ping_AR_+_LT:Regular')] font-[var(--typography\/weight\/regular,normal)] leading-[var(--typography\/line-height-\(descreptive\)\/4,16px)] min-w-px relative text-[color:var(--text\/gray\/light,#666)] text-[length:var(--typography\/size\/xs,12px)] text-right" dir="auto" data-node-id="I14952:281214;14952:280028">
                    نص بديل لعرض التفاصيل
                  </p>
                </div>
              </div>
              <CheckBox className="block border border-[var(--border\/primary,#004956)] border-solid cursor-pointer relative rounded-[var(--radius\/md,4px)] shrink-0 size-[20px]" selected={false} />
            </div>
          </div>
          <DividerContainer className="relative shrink-0 w-full" />
          <div className="bg-[var(--background\/default\/cards,white)] h-[36px] relative shrink-0 w-full" data-node-id="14952:281216" data-name="listItem/Subcategory/Off/False/Arabic/True">
            <div className="bg-clip-padding border-0 border-[transparent] border-solid content-stretch flex gap-[var(--spacing\/sizes\/sm,8px)] items-center justify-end pl-[var(--spacing\/sizes\/lg,12px)] pr-[var(--spacing\/sizes\/3xl,20px)] py-[var(--spacing\/sizes\/sm,8px)] relative size-full">
              <p className="[word-break:break-word] flex-[1_0_0] font-[family-name:var(--typography\/family\/font,'Ping_AR_+_LT:Medium')] font-[var(--typography\/weight\/medium,normal)] leading-[var(--typography\/line-height-\(descreptive\)\/5,20px)] min-w-px relative text-[color:var(--text\/gray\/dark,#333)] text-[length:var(--typography\/size\/sm,14px)] text-right" dir="auto" data-node-id="I14952:281216;14952:22467">
                الفئة الثانوية
              </p>
            </div>
          </div>
          <DividerContainer className="relative shrink-0 w-full" />
          <div className="bg-[var(--background\/default\/cards,white)] h-[60px] min-h-[44px] relative shrink-0 w-full" data-node-id="14952:281218" data-name="_listItem">
            <div className="bg-clip-padding border-0 border-[transparent] border-solid content-stretch flex gap-[var(--spacing\/sizes\/sm,8px)] items-center justify-end min-h-[inherit] p-[var(--spacing\/sizes\/lg,12px)] relative size-full">
              <div className="content-stretch flex flex-[1_0_0] flex-col gap-[var(--spacing\/sizes\/2xs,4px)] items-end min-w-px relative" data-node-id="I14952:281218;14952:280022" data-name="textContainer">
                <div className="content-stretch flex items-center justify-center relative shrink-0 w-full" data-node-id="I14952:281218;14967:20362" data-name="__label">
                  <p className="[word-break:break-word] flex-[1_0_0] font-[family-name:var(--typography\/family\/font,'Ping_AR_+_LT:Bold')] font-[var(--typography\/weight\/bold,normal)] leading-[var(--typography\/line-height-\(descreptive\)\/4,16px)] min-w-px relative text-[color:var(--text\/gray\/dark,#333)] text-[length:var(--typography\/size\/xs,12px)] text-right" dir="auto" data-node-id="I14952:281218;14952:22459">
                    خيار رقم (1)
                  </p>
                </div>
                <div className="content-stretch flex items-center justify-center relative shrink-0 w-[123px]" data-node-id="I14952:281218;14967:21131" data-name="__description">
                  <p className="[word-break:break-word] flex-[1_0_0] font-[family-name:var(--typography\/family\/font,'Ping_AR_+_LT:Regular')] font-[var(--typography\/weight\/regular,normal)] leading-[var(--typography\/line-height-\(descreptive\)\/4,16px)] min-w-px relative text-[color:var(--text\/gray\/light,#666)] text-[length:var(--typography\/size\/xs,12px)] text-right" dir="auto" data-node-id="I14952:281218;14952:280028">
                    نص بديل لعرض التفاصيل
                  </p>
                </div>
              </div>
              <CheckBox className="block border border-[var(--border\/primary,#004956)] border-solid cursor-pointer relative rounded-[var(--radius\/md,4px)] shrink-0 size-[20px]" selected={false} />
            </div>
          </div>
          <DividerContainer className="relative shrink-0 w-full" />
          <div className="bg-[var(--background\/default\/cards,white)] h-[60px] min-h-[44px] relative shrink-0 w-full" data-node-id="15119:299645" data-name="_listItem">
            <div className="bg-clip-padding border-0 border-[transparent] border-solid content-stretch flex gap-[var(--spacing\/sizes\/sm,8px)] items-center justify-end min-h-[inherit] p-[var(--spacing\/sizes\/lg,12px)] relative size-full">
              <div className="content-stretch flex flex-[1_0_0] flex-col gap-[var(--spacing\/sizes\/2xs,4px)] items-end min-w-px relative" data-node-id="I15119:299645;14952:280022" data-name="textContainer">
                <div className="content-stretch flex items-center justify-center relative shrink-0 w-full" data-node-id="I15119:299645;14967:20362" data-name="__label">
                  <p className="[word-break:break-word] flex-[1_0_0] font-[family-name:var(--typography\/family\/font,'Ping_AR_+_LT:Bold')] font-[var(--typography\/weight\/bold,normal)] leading-[var(--typography\/line-height-\(descreptive\)\/4,16px)] min-w-px relative text-[color:var(--text\/gray\/dark,#333)] text-[length:var(--typography\/size\/xs,12px)] text-right" dir="auto" data-node-id="I15119:299645;14952:22459">
                    خيار رقم (2)
                  </p>
                </div>
                <div className="content-stretch flex items-center justify-center relative shrink-0 w-[123px]" data-node-id="I15119:299645;14967:21131" data-name="__description">
                  <p className="[word-break:break-word] flex-[1_0_0] font-[family-name:var(--typography\/family\/font,'Ping_AR_+_LT:Regular')] font-[var(--typography\/weight\/regular,normal)] leading-[var(--typography\/line-height-\(descreptive\)\/4,16px)] min-w-px relative text-[color:var(--text\/gray\/light,#666)] text-[length:var(--typography\/size\/xs,12px)] text-right" dir="auto" data-node-id="I15119:299645;14952:280028">
                    نص بديل لعرض التفاصيل
                  </p>
                </div>
              </div>
              <CheckBox className="block border border-[var(--border\/primary,#004956)] border-solid cursor-pointer relative rounded-[var(--radius\/md,4px)] shrink-0 size-[20px]" selected={false} />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
```

## Design tokens / variables used

- `--background/default/cards` = `white` (list, titles, items), `--background/default/neutrals` = `#f4f4f4` (dividers, scroll track)
- `--border/focus` = `#5196f3` (1px list outline in this focused sample), `--border/primary` = `#004956` (checkbox)
- `--background/primary/primary` = `#004956` (scroll thumb, checked checkbox)
- `--radius/sm` = `8px` (list), `--radius/md` = `4px` (checkbox), `--radius/xl` = `140px` (scroll, as returned), `--radius-3xl-2` = `48px` (scroll track)
- Shadow `Shadows/lg`: type-1 `0 10px 15px -3px rgba(18,18,23,0.08)`, type-2 `0 4px 6px -2px rgba(18,18,23,0.05)`
- `--spacing/sizes/sm` = `8px`, `--spacing/sizes/lg` = `12px`, `--spacing/sizes/2xs` = `4px`, `--spacing/sizes/3xs` = `2px`, `--spacing/sizes/3xl` = `20px` (subcategory indent, right padding)
- `--typography/family/font` = `Ping AR + LT` (Bold / Medium / Regular); weights 700 / 500 / 400
- `--typography/size/xs` = `12px`, `--typography/size/sm` = `14px`
- `--typography/line-height (Descreptive)/4` = `16px`, `/5` = `20px`
- `--text/gray/dark` = `#333`, `--text/gray/light` = `#666`
- Heights: Category title `44px`, Subcategory title `36px`, item with description `60px` (min `44px`), item without description `44px`; list width `375px`; scroll bar `4px` wide; divider `1px`

## Text styles in the design

- `Bold/$text-sm`: Font(family: "Typography/Family/Font", style: Typography/Weight/Bold, size: Typography/Size/sm, weight: 700, lineHeight: typography/line-height (Descreptive)/5, letterSpacing: 0)
- `Medium/$text-sm`: Font(family: "Typography/Family/Font", style: Typography/Weight/Medium, size: Typography/Size/sm, weight: 500, lineHeight: typography/line-height (Descreptive)/5, letterSpacing: 0)
- `Bold/$text-xs`: Font(family: "Typography/Family/Font", style: Typography/Weight/Bold, size: Typography/Size/xs, weight: 700, lineHeight: typography/line-height (Descreptive)/4, letterSpacing: 0)
- `Regular/$text-xs`: Font(family: "Typography/Family/Font", style: Typography/Weight/Regular, size: Typography/Size/xs, weight: 400, lineHeight: typography/line-height (Descreptive)/4, letterSpacing: 0)
- `Shadows/lg`: Effect(type: DROP_SHADOW, color: shadow/lg/type-2/color, offset: (shadow/lg/type-2/position-x, shadow/lg/type-2/position-y), radius: shadow/lg/type-2/blur, spread: shadow/lg/type-2/spread); Effect(type: DROP_SHADOW, color: shadow/lg/type-1/color, offset: (shadow/lg/type-1/position-x, shadow/lg/type-1/position-y), radius: shadow/lg/type-1/blur, spread: shadow/lg/type-1/spread)

## Component descriptions (from Figma)

### Drop Down List — Node ID: 14952:281457
**Keywords:** [Select menu, Dropdown menu, Pull-down menu, Option list, Selection control, Form element, UI component, Input control, Single-choice selector, Multi-choice selector, قائمة منسدلة, قائمة خيارات, قائمة تحديد, عنصر إدخال, قائمة اختيار, عنصر تحكم]

### Scroll — Node ID: 5648:29927
**Keywords:** [Vertical scrolling, Horizontal scrolling, Page navigation, Content overflow, Infinite scroll, Parallax scrolling, Scrollbar, Scroll indicator, Swipe gesture, Mouse wheel action, تمرير رأسي, تمرير أفقي, تصفح المحتوى, شريط التمرير, التمرير اللانهائي, إشارة التمرير, إيماءة السحب]

### dividerContainer — Node ID: 12411:21716
**Keywords:** [Content separator, Visual divider, Rule line, Horizontal rule, Vertical rule, Section break, Layout spacer, Group divider, فاصل, خط فاصل, مقسم المحتوى, فاصل مرئي, مقسم رأسي, مقسم أفقي, فاصل أقسام, منظم للتخطيط]

### checkBox — Node ID: 12411:21809
**Keywords:** [Selection control, Tickbox, Check mark, Boolean input, Multiple choice, On/Off switch, Form element, UI control, مربع اختيار, خانة اختيار, علامة صح, أداة تحديد, اختيار متعدد, عنصر إدخال]

## Assets (SVG)

- `figma-asset:5ec58.svg` — Tick Mark (14x14), node 12411:21811
- `figma-asset:66325.svg` — file-02-outline (20x20), node I14952:281202;14952:22518

## Notes from the response

- Node ids are added to the code as `data-node-id` attributes.
- The generated React+Tailwind is a reference prototype that must be converted to the target stack; do not install Tailwind.
- Assets on the Figma server expire in 7 days (download URLs blocked in this environment; not downloaded).
