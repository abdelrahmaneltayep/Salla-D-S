# Header — device=desktop, subcategories=true, breadcrumb=false, subtitle=false

- Figma file: `dnmyqzYKK9dUJjVHuIWMDS`
- Figma node id: `15895:36794` (component `--device=desktop`)
- Nested components: `15895:35360` (Primary Tabs List - Dashboard only instance; set 15895:35397), `15894:30922` (Title Header), `18204:40931` (Header Subcategory), `15913:38807` (Breadcrumb), `18204:42660` (Page Title)

## Code (verbatim from get_design_context)

```tsx
const assetPathPrefix = "figma-asset:";
const imgPieChartOutline = `${assetPathPrefix}/c022c.svg`;
const imgChartBreakoutSquareOutline = `${assetPathPrefix}/3bc8e.svg`;
const imgMarketingOutline = `${assetPathPrefix}/ea919.svg`;
const imgShirt01Outline = `${assetPathPrefix}/d8363.svg`;
const imgDeliveryBox02Outline = `${assetPathPrefix}/caf0b.svg`;
const imgHome01Outline = `${assetPathPrefix}/ea8cc.svg`;
const imgMenu01Outline = `${assetPathPrefix}/c5d9b.svg`;
const imgAvatarplaholderImages = `${assetPathPrefix}/3f02b.png`;
const imgArrowDown01Outline = `${assetPathPrefix}/77e1d.svg`;
const imgNotification01Outline = `${assetPathPrefix}/8804f.svg`;
const imgMessage01Outline = `${assetPathPrefix}/1c34b.svg`;
const imgSearch01Outline = `${assetPathPrefix}/025eb.svg`;
const imgLogoLightWide1 = `${assetPathPrefix}/fa307.svg`;
const imgHelpCircleOutline = `${assetPathPrefix}/a5c32.svg`;
const imgArrowLeft01Outline = `${assetPathPrefix}/9b1ae.svg`;
const imgAdd01Outline = `${assetPathPrefix}/a24ad.svg`;

type PrimaryTabsListDashboardOnlyProps = {
  className?: string;
  language?: "Arabic";
};

function PrimaryTabsListDashboardOnly({ className, language = "Arabic" }: PrimaryTabsListDashboardOnlyProps) {
  return (
    <div className={className || "content-stretch flex gap-[var(--spacing\\/2xs,10px)] items-center justify-end relative w-[1101.6px]"} data-node-id="15895:35360">
      <div className="content-stretch flex gap-[var(--spacing\/5xs,4px)] items-center justify-center px-[var(--spacing\/base,16px)] py-[var(--spacing\/3xs,8px)] relative rounded-[var(--radius\/md,4px)] shrink-0" data-node-id="15895:35323" data-name="Header Primary Tabs">
        <div className="content-stretch flex flex-col items-center justify-center relative shrink-0" data-node-id="I15895:35323;15412:79814" data-name="__label">
          <div className="[word-break:break-word] flex flex-col font-[family-name:var(--typography\/family\/font,'Ping_AR_+_LT:Medium')] font-[var(--typography\/weight\/medium,normal)] justify-center leading-[0] relative shrink-0 text-[color:var(--text\/gray\/white,white)] text-[length:var(--typography\/size\/md,16px)] text-center whitespace-nowrap" data-node-id="I15895:35323;15412:79815">
            <p className="leading-[var(--typography\/line-height-\(descreptive\)\/6,24px)]" dir="auto">
              التقارير
            </p>
          </div>
        </div>
        <div className="content-stretch flex flex-col items-center justify-center relative shrink-0" data-node-id="I15895:35323;15412:79816" data-name="__icon-start">
          <div className="relative shrink-0 size-[24px]" data-node-id="I15895:35323;15412:79817" data-name="home-01-outline">
            <img alt="" className="absolute block inset-0 max-w-none size-full" src={imgPieChartOutline} />
          </div>
        </div>
      </div>
      <div className="content-stretch flex gap-[var(--spacing\/5xs,4px)] items-center justify-center px-[var(--spacing\/base,16px)] py-[var(--spacing\/3xs,8px)] relative rounded-[var(--radius\/md,4px)] shrink-0" data-node-id="15895:35324" data-name="Header Primary Tabs">
        <div className="content-stretch flex flex-col items-center justify-center relative shrink-0" data-node-id="I15895:35324;15412:79814" data-name="__label">
          <div className="[word-break:break-word] flex flex-col font-[family-name:var(--typography\/family\/font,'Ping_AR_+_LT:Medium')] font-[var(--typography\/weight\/medium,normal)] justify-center leading-[0] relative shrink-0 text-[color:var(--text\/gray\/white,white)] text-[length:var(--typography\/size\/md,16px)] text-center whitespace-nowrap" data-node-id="I15895:35324;15412:79815">
            <p className="leading-[var(--typography\/line-height-\(descreptive\)\/6,24px)]" dir="auto">
              المتجر وقنوات البيع
            </p>
          </div>
        </div>
        <div className="content-stretch flex flex-col items-center justify-center relative shrink-0" data-node-id="I15895:35324;15412:79816" data-name="__icon-start">
          <div className="relative shrink-0 size-[24px]" data-node-id="I15895:35324;15412:79817" data-name="home-01-outline">
            <img alt="" className="absolute block inset-0 max-w-none size-full" src={imgChartBreakoutSquareOutline} />
          </div>
        </div>
      </div>
      <div className="content-stretch flex gap-[var(--spacing\/5xs,4px)] items-center justify-center px-[var(--spacing\/base,16px)] py-[var(--spacing\/3xs,8px)] relative rounded-[var(--radius\/md,4px)] shrink-0" data-node-id="15895:35325" data-name="Header Primary Tabs">
        <div className="content-stretch flex flex-col items-center justify-center relative shrink-0" data-node-id="I15895:35325;15412:79814" data-name="__label">
          <div className="[word-break:break-word] flex flex-col font-[family-name:var(--typography\/family\/font,'Ping_AR_+_LT:Medium')] font-[var(--typography\/weight\/medium,normal)] justify-center leading-[0] relative shrink-0 text-[color:var(--text\/gray\/white,white)] text-[length:var(--typography\/size\/md,16px)] text-center whitespace-nowrap" data-node-id="I15895:35325;15412:79815">
            <p className="leading-[var(--typography\/line-height-\(descreptive\)\/6,24px)]" dir="auto">
              التسويق
            </p>
          </div>
        </div>
        <div className="content-stretch flex flex-col items-center justify-center relative shrink-0" data-node-id="I15895:35325;15412:79816" data-name="__icon-start">
          <div className="relative shrink-0 size-[24px]" data-node-id="I15895:35325;15412:79817" data-name="home-01-outline">
            <img alt="" className="absolute block inset-0 max-w-none size-full" src={imgMarketingOutline} />
          </div>
        </div>
      </div>
      <div className="content-stretch flex gap-[var(--spacing\/5xs,4px)] items-center justify-center px-[var(--spacing\/base,16px)] py-[var(--spacing\/3xs,8px)] relative rounded-[var(--radius\/md,4px)] shrink-0" data-node-id="15895:35326" data-name="Header Primary Tabs">
        <div className="content-stretch flex flex-col items-center justify-center relative shrink-0" data-node-id="I15895:35326;15412:79814" data-name="__label">
          <div className="[word-break:break-word] flex flex-col font-[family-name:var(--typography\/family\/font,'Ping_AR_+_LT:Medium')] font-[var(--typography\/weight\/medium,normal)] justify-center leading-[0] relative shrink-0 text-[color:var(--text\/gray\/white,white)] text-[length:var(--typography\/size\/md,16px)] text-center whitespace-nowrap" data-node-id="I15895:35326;15412:79815">
            <p className="leading-[var(--typography\/line-height-\(descreptive\)\/6,24px)]" dir="auto">
              المنتجات
            </p>
          </div>
        </div>
        <div className="content-stretch flex flex-col items-center justify-center relative shrink-0" data-node-id="I15895:35326;15412:79816" data-name="__icon-start">
          <div className="relative shrink-0 size-[24px]" data-node-id="I15895:35326;15412:79817" data-name="home-01-outline">
            <img alt="" className="absolute block inset-0 max-w-none size-full" src={imgShirt01Outline} />
          </div>
        </div>
      </div>
      <div className="content-stretch flex gap-[var(--spacing\/5xs,4px)] items-center justify-center px-[var(--spacing\/base,16px)] py-[var(--spacing\/3xs,8px)] relative rounded-[var(--radius\/md,4px)] shrink-0" data-node-id="15895:35327" data-name="Header Primary Tabs">
        <div className="content-stretch flex flex-col items-center justify-center relative shrink-0" data-node-id="I15895:35327;15412:79814" data-name="__label">
          <div className="[word-break:break-word] flex flex-col font-[family-name:var(--typography\/family\/font,'Ping_AR_+_LT:Medium')] font-[var(--typography\/weight\/medium,normal)] justify-center leading-[0] relative shrink-0 text-[color:var(--text\/gray\/white,white)] text-[length:var(--typography\/size\/md,16px)] text-center whitespace-nowrap" data-node-id="I15895:35327;15412:79815">
            <p className="leading-[var(--typography\/line-height-\(descreptive\)\/6,24px)]" dir="auto">
              الطلبات
            </p>
          </div>
        </div>
        <div className="content-stretch flex flex-col items-center justify-center relative shrink-0" data-node-id="I15895:35327;15412:79816" data-name="__icon-start">
          <div className="relative shrink-0 size-[24px]" data-node-id="I15895:35327;15412:79817" data-name="home-01-outline">
            <img alt="" className="absolute block inset-0 max-w-none size-full" src={imgDeliveryBox02Outline} />
          </div>
        </div>
      </div>
      <div className="bg-[var(--background\/secondary\/seconadry,#a4ffe5)] content-stretch flex gap-[var(--spacing\/5xs,4px)] items-center justify-center px-[var(--spacing\/base,16px)] py-[var(--spacing\/3xs,8px)] relative rounded-[var(--radius\/md,4px)] shrink-0" data-node-id="15895:35328" data-name="Header Primary Tabs">
        <div className="content-stretch flex flex-col items-center justify-center relative shrink-0" data-node-id="I15895:35328;15412:79736" data-name="__label">
          <div className="[word-break:break-word] flex flex-col font-[family-name:var(--typography\/family\/font,'Ping_AR_+_LT:Bold')] font-[var(--typography\/weight\/bold,normal)] justify-center leading-[0] relative shrink-0 text-[color:var(--text\/primary\/primary,#004956)] text-[length:var(--typography\/size\/md,16px)] text-center whitespace-nowrap" data-node-id="I15895:35328;15412:79737">
            <p className="leading-[var(--typography\/line-height-\(descreptive\)\/6,24px)]" dir="auto">
              الرئيسية
            </p>
          </div>
        </div>
        <div className="content-stretch flex flex-col items-center justify-center relative shrink-0" data-node-id="I15895:35328;15412:79738" data-name="__icon-start">
          <div className="relative shrink-0 size-[24px]" data-node-id="I15895:35328;15412:79739" data-name="home-01-outline">
            <img alt="" className="absolute block inset-0 max-w-none size-full" src={imgHome01Outline} />
          </div>
        </div>
      </div>
      <div className="content-stretch flex gap-[var(--spacing\/5xs,4px)] items-center justify-center px-[var(--spacing\/base,16px)] py-[var(--spacing\/3xs,8px)] relative rounded-[var(--radius\/md,4px)] shrink-0" data-node-id="18162:78061" data-name="Header Primary Tabs">
        <div className="content-stretch flex flex-col items-center justify-center relative shrink-0" data-node-id="I18162:78061;15412:79814" data-name="__label">
          <div className="[word-break:break-word] flex flex-col font-[family-name:var(--typography\/family\/font,'Ping_AR_+_LT:Medium')] font-[var(--typography\/weight\/medium,normal)] justify-center leading-[0] relative shrink-0 text-[color:var(--text\/gray\/white,white)] text-[length:var(--typography\/size\/md,16px)] text-center whitespace-nowrap" data-node-id="I18162:78061;15412:79815">
            <p className="leading-[var(--typography\/line-height-\(descreptive\)\/6,24px)]" dir="auto">
              الكل
            </p>
          </div>
        </div>
        <div className="content-stretch flex flex-col items-center justify-center relative shrink-0" data-node-id="I18162:78061;15412:79816" data-name="__icon-start">
          <div className="relative shrink-0 size-[24px]" data-node-id="I18162:78061;15412:79817" data-name="home-01-outline">
            <img alt="" className="absolute block inset-0 max-w-none size-full" src={imgMenu01Outline} />
          </div>
        </div>
      </div>
    </div>
  );
}

type HeaderProps = {
  className?: string;
  breadcrumb?: boolean;
  device?: "desktop";
  subcategories?: boolean;
  subtitle?: boolean;
};

function Header({ className, breadcrumb = false, device = "desktop", subcategories = true, subtitle = false }: HeaderProps) {
  return (
    <div className={className || "content-stretch flex flex-col items-start relative w-[1536px]"} data-node-id="15895:36794">
      <div className="bg-[var(--background\/primary\/primary,#004956)] content-stretch flex gap-[var(--spacing\/sizes\/3xl,20px)] items-center justify-end px-[var(--spacing\/sizes\/9xl,56px)] py-[var(--spacing\/base,16px)] relative shrink-0 w-full" data-node-id="15894:30922" data-name="Title Header">
        <div className="content-stretch flex gap-[var(--spacing-4xl,16px)] items-center justify-end relative shrink-0" data-node-id="15910:35894" data-name="Info">
          <div className="content-stretch flex gap-[var(--spacing\/sizes\/sm,8px)] items-center px-[var(--spacing\/sizes\/sm,8px)] py-[var(--spacing\/5xs,4px)] relative rounded-[var(--radius\/sm,8px)] shrink-0" data-node-id="15910:35895" data-name="header Avatar">
            <div className="content-stretch flex gap-[var(--spacing-lg,8px)] items-center justify-end relative shrink-0" data-node-id="I15910:35895;15896:31756" data-name="name">
              <div className="relative shrink-0 size-[16px]" data-node-id="I15910:35895;18162:78764" data-name="arrow-down-01-outline">
                <img alt="" className="absolute block inset-0 max-w-none size-full" src={imgArrowDown01Outline} />
              </div>
              <div className="content-stretch flex flex-col items-end justify-center relative shrink-0" data-node-id="I15910:35895;15896:31757" data-name="listContainer">
                <div className="content-stretch flex gap-[var(--spacing-md,6px)] items-center justify-end relative shrink-0" data-node-id="I15910:35895;15896:31758" data-name="Name">
                  <div className="content-stretch flex flex-col gap-[var(--spacing-xs,2px)] items-end relative shrink-0" data-node-id="I15910:35895;15896:31759" data-name="contentContainer">
                    <div className="content-stretch flex gap-[var(--spacing\/5xs,4px)] items-start justify-end relative shrink-0 w-full" data-node-id="I15910:35895;15896:31760" data-name="__title">
                      <div className="[word-break:break-word] flex flex-col font-['Ping_AR_+_LT:Regular'] justify-center leading-[0] not-italic relative shrink-0 text-[14px] text-[color:var(--07--light-theme\/gray\/color-gray-200--\(1\),#f8f8f8)] text-right whitespace-nowrap" data-node-id="I15910:35895;15896:31761">
                        <p className="leading-[normal]" dir="auto">
                          عبدالله
                        </p>
                      </div>
                    </div>
                    <div className="border border-[var(--border\/seconadry-hover,#dbfff6)] border-solid content-stretch flex gap-[var(--spacing\/sizes\/2xs,4px)] items-center justify-center max-h-[24px] min-h-[24px] px-[var(--spacing\/sizes\/sm,8px)] py-[var(--spacing\/sizes\/2xs,4px)] relative rounded-[var(--radius\/xl,140px)] shrink-0" data-node-id="I15910:35895;25057:59673" data-name="tag">
                      <div className="content-stretch flex items-start relative shrink-0" data-node-id="I15910:35895;25057:59675" data-name="textContainer">
                        <div className="[word-break:break-word] flex flex-col font-[family-name:var(--typography\/family\/font,'Ping_AR_+_LT:Regular')] font-[var(--typography\/weight\/regular,normal)] justify-center leading-[0] relative shrink-0 text-[color:var(--text\/gray\/white,white)] text-[length:var(--typography\/size\/xs,12px)] text-center whitespace-nowrap" data-node-id="I15910:35895;25057:59676">
                          <p className="leading-[var(--typography\/line-height-\(descreptive\)\/4,16px)]" dir="auto">
                            جديد
                          </p>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div className="content-stretch flex items-center relative rounded-[var(--radius\/full,9999px)] shrink-0 size-[48px]" data-node-id="I15910:35895;15896:31763" data-name="Avatar">
                <div className="bg-[var(--background\/default\/white,white)] border-0 border-[var(--border\/default,#eee)] border-solid overflow-clip relative rounded-[var(--radius\/full,8749.125px)] shrink-0 size-[48px]" data-node-id="I15910:35895;15896:31764" data-name="_AvatarplaholderImages">
                  <div className="absolute inset-0 overflow-hidden pointer-events-none">
                    <img alt="" className="absolute h-[220.09%] left-[-34.37%] max-w-none top-[9.68%] w-[171.88%]" src={imgAvatarplaholderImages} />
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div className="content-stretch flex gap-[var(--spacing-4xl,16px)] items-center justify-end relative shrink-0" data-node-id="15910:35896" data-name="Icons">
            <div className="relative shrink-0 size-[24px]" data-node-id="15910:35898" data-name="notification-01-outline">
              <img alt="" className="absolute block inset-0 max-w-none size-full" src={imgNotification01Outline} />
            </div>
            <div className="relative shrink-0 size-[24px]" data-node-id="15910:35900" data-name="message-01-outline">
              <img alt="" className="absolute block inset-0 max-w-none size-full" src={imgMessage01Outline} />
            </div>
            <div className="relative shrink-0 size-[24px]" data-node-id="18162:79178" data-name="search-01-outline">
              <img alt="" className="absolute block inset-0 max-w-none size-full" src={imgSearch01Outline} />
            </div>
          </div>
        </div>
        <PrimaryTabsListDashboardOnly className="content-stretch flex flex-[1_0_0] gap-[var(--spacing\/2xs,10px)] items-center justify-end min-w-px relative" />
        <div className="flex flex-row items-center self-stretch" data-node-id="15895:32288">
          <div className="content-stretch flex flex-col h-full items-center justify-center relative shrink-0" data-name="logo">
            <div className="h-[40px] relative shrink-0 w-[95.4px]" data-node-id="15895:32289" data-name="logo-light-wide 1">
              <img alt="" className="absolute block inset-0 max-w-none size-full" src={imgLogoLightWide1} />
            </div>
          </div>
        </div>
      </div>
      {subcategories && (
        <div className="bg-[var(--background\/default\/white,white)] content-stretch flex gap-[24px] h-[64px] items-center justify-end px-[var(--spacing\/sizes\/9xl,56px)] py-[var(--spacing\/xs,12px)] relative shrink-0 w-full" data-node-id="18204:40931" data-name="Header Subcategory">
          <div className="content-stretch flex gap-[var(--spacing\/base,16px)] items-center relative shrink-0" data-node-id="I18204:40931;18204:40863" data-name="Buttons">
            <div className="bg-[var(--background\/default\/white,white)] border border-[var(--border\/seconadry,#a4ffe5)] border-solid content-stretch flex gap-[var(--spacing\/5xs,4px)] items-center justify-center max-h-[32px] min-h-[32px] px-[var(--spacing\/3xs,8px)] py-[var(--spacing\/5xs,4px)] relative rounded-[var(--radius\/xl,8px)] shrink-0" data-node-id="I18204:40931;18204:40864" data-name="Button">
              <div className="content-stretch flex flex-col items-center justify-center relative shrink-0" data-node-id="I18204:40931;18204:40864;14671:6097" data-name="__label">
                <div className="[word-break:break-word] flex flex-col font-[family-name:var(--typography\/family\/font,'Ping_AR_+_LT:Medium')] font-[var(--typography\/weight\/medium,normal)] justify-center leading-[0] relative shrink-0 text-[color:var(--text\/primary\/link,#004956)] text-[length:var(--typography\/size\/xs,12px)] text-center whitespace-nowrap" data-node-id="I18204:40931;18204:40864;14671:6098">
                  <p className="leading-[var(--typography\/line-height-\(descreptive\)\/4,16px)]" dir="auto">
                    مركز المساعدة
                  </p>
                </div>
              </div>
              <div className="content-stretch flex flex-col items-start relative shrink-0" data-node-id="I18204:40931;18204:40864;14671:6099" data-name="__icon-start">
                <div className="relative shrink-0 size-[16px]" data-node-id="I18204:40931;18204:40864;14671:6100" data-name="add-01-outline">
                  <img alt="" className="absolute block inset-0 max-w-none size-full" src={imgHelpCircleOutline} />
                </div>
              </div>
            </div>
          </div>
          <div className="content-stretch flex flex-[1_0_0] gap-[var(--spacing\/base,16px)] items-center justify-end min-w-px relative" data-node-id="I18204:40931;18204:40866" data-name="Secondary Tabs List">
            <div className="border-[var(--border\/primary-link,#004956)] border-b-2 border-solid content-stretch flex gap-[var(--spacing\/5xs,4px)] items-center justify-center px-[var(--spacing\/6xs,2px)] py-[var(--spacing\/3xs,8px)] relative shrink-0" data-node-id="I18204:40931;18204:40866;18204:44550" data-name="Header Secondary Tabs">
              <div className="content-stretch flex flex-col items-center justify-center relative shrink-0" data-node-id="I18204:40931;18204:40866;18204:44550;15456:85669" data-name="__label">
                <div className="[word-break:break-word] flex flex-col font-[family-name:var(--typography\/family\/font,'Ping_AR_+_LT:Bold')] font-[var(--typography\/weight\/bold,normal)] justify-center leading-[0] relative shrink-0 text-[color:var(--text\/primary\/link,#004956)] text-[length:var(--typography\/size\/md,16px)] text-center whitespace-nowrap" data-node-id="I18204:40931;18204:40866;18204:44550;15456:85670">
                  <p className="leading-[var(--typography\/line-height-\(descreptive\)\/6,24px)]" dir="auto">
                    ملخص المتجر
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      )}
      {breadcrumb && (
        <div className="content-stretch flex gap-[var(--spacing-7xl,24px)] items-center justify-end px-[var(--spacing\/7xl,56px)] py-[var(--spacing\/3xs,8px)] relative shrink-0 w-full" data-node-id="15913:38807" data-name="Breadcrumb">
          <div className="content-stretch flex flex-[1_0_0] gap-[var(--spacing\/3xs,8px)] items-center justify-end min-w-px relative" data-node-id="I15913:38807;15392:76153" data-name="listContainer">
            <div className="content-stretch flex items-start p-[var(--spacing\/5xs,4px)] relative shrink-0" data-node-id="I15913:38807;15392:76158" data-name="_breadcrumbItem">
              <div className="[word-break:break-word] flex flex-col font-[family-name:var(--typography\/family\/font,'Ping_AR_+_LT:Regular')] font-[var(--typography\/weight\/regular,normal)] justify-center leading-[0] relative shrink-0 text-[color:var(--text\/primary\/primary,#004956)] text-[length:var(--typography\/size\/sm,14px)] text-right whitespace-nowrap" data-node-id="I15913:38807;15392:76158;15392:5079">
                <p className="leading-[var(--typography\/line-height-\(descreptive\)\/5,20px)]" dir="auto">
                  عنوان
                </p>
              </div>
            </div>
            <div className="content-stretch flex items-start p-[var(--spacing\/5xs,4px)] relative shrink-0" data-node-id="I15913:38807;15392:76159" data-name="_breadcrumbItem">
              <div className="relative shrink-0 size-[24px]" data-node-id="I15913:38807;15392:76159;15392:75943" data-name="arrow-left-01-outline">
                <img alt="" className="absolute block inset-0 max-w-none size-full" src={imgArrowLeft01Outline} />
              </div>
            </div>
            <div className="content-stretch flex items-start p-[var(--spacing\/5xs,4px)] relative shrink-0" data-node-id="I15913:38807;15392:76160" data-name="_breadcrumbItem">
              <div className="[word-break:break-word] flex flex-col font-[family-name:var(--typography\/family\/font,'Ping_AR_+_LT:Regular')] font-[var(--typography\/weight\/regular,normal)] justify-center leading-[0] relative shrink-0 text-[0px] text-[color:var(--text\/gray\/lighter,#737373)] text-right whitespace-nowrap" data-node-id="I15913:38807;15392:76160;15392:5077">
                <p className="font-['Ping_AR_+_LT:Regular'] leading-[20px] not-italic text-[#737373] text-[14px]" dir="auto">
                  عنوان
                </p>
              </div>
            </div>
            <div className="content-stretch flex items-start p-[var(--spacing\/5xs,4px)] relative shrink-0" data-node-id="I15913:38807;15392:76161" data-name="_breadcrumbItem">
              <div className="relative shrink-0 size-[24px]" data-node-id="I15913:38807;15392:76161;15392:75943" data-name="arrow-left-01-outline">
                <img alt="" className="absolute block inset-0 max-w-none size-full" src={imgArrowLeft01Outline} />
              </div>
            </div>
            <div className="content-stretch flex items-start p-[var(--spacing\/5xs,4px)] relative shrink-0" data-node-id="I15913:38807;18859:96989" data-name="_breadcrumbItem">
              <div className="[word-break:break-word] flex flex-col font-[family-name:var(--typography\/family\/font,'Ping_AR_+_LT:Regular')] font-[var(--typography\/weight\/regular,normal)] justify-center leading-[0] relative shrink-0 text-[0px] text-[color:var(--text\/gray\/lighter,#737373)] text-right whitespace-nowrap" data-node-id="I15913:38807;18859:96989;15392:5077">
                <p className="font-['Ping_AR_+_LT:Regular'] leading-[20px] not-italic text-[#737373] text-[14px]" dir="auto">
                  عنوان
                </p>
              </div>
            </div>
          </div>
        </div>
      )}
      {subtitle && (
        <div className="content-stretch flex gap-[var(--spacing\/base,16px)] items-center justify-end px-[var(--spacing\/sizes\/9xl,56px)] py-[var(--spacing\/sizes\/2xl,16px)] relative shrink-0 w-full" data-node-id="18204:42660" data-name="Page Title">
          <div className="content-stretch flex gap-[var(--spacing\/xs,12px)] items-center relative shrink-0" data-node-id="I18204:42660;18204:42566" data-name="Buttons">
            <div className="bg-[var(--background\/secondary\/seconadry,#a4ffe5)] border-2 border-[var(--border\/seconadry,#a4ffe5)] border-solid content-stretch flex gap-[var(--spacing\/5xs,4px)] items-center justify-center max-h-[40px] min-h-[40px] px-[var(--spacing\/xs,12px)] py-[var(--spacing\/3xs,8px)] relative rounded-[var(--radius\/xl,8px)] shrink-0" data-node-id="I18204:42660;18204:42567" data-name="Button">
              <div className="content-stretch flex flex-col items-center justify-center relative shrink-0" data-node-id="I18204:42660;18204:42567;14671:5724" data-name="__label">
                <div className="[word-break:break-word] flex flex-col font-[family-name:var(--typography\/family\/font,'Ping_AR_+_LT:Medium')] font-[var(--typography\/weight\/medium,normal)] justify-center leading-[0] relative shrink-0 text-[color:var(--text\/primary\/primary,#004956)] text-[length:var(--typography\/size\/sm,14px)] text-center whitespace-nowrap" data-node-id="I18204:42660;18204:42567;14671:5725">
                  <p className="leading-[var(--typography\/line-height-\(descreptive\)\/5,20px)]" dir="auto">
                    انشاء طلب
                  </p>
                </div>
              </div>
              <div className="content-stretch flex flex-col items-start relative shrink-0" data-node-id="I18204:42660;18204:42567;14671:5726" data-name="__icon-start">
                <div className="relative shrink-0 size-[16px]" data-node-id="I18204:42660;18204:42567;14671:5727" data-name="add-01-outline">
                  <img alt="" className="absolute block inset-0 max-w-none size-full" src={imgAdd01Outline} />
                </div>
              </div>
            </div>
          </div>
          <div className="content-stretch flex flex-[1_0_0] gap-[var(--spacing\/3xs,8px)] items-center justify-end min-w-px py-[var(--spacing\/5xs,4px)] relative" data-node-id="I18204:42660;18204:42569" data-name="textContainer">
            <p className="[word-break:break-word] font-[family-name:var(--typography\/family\/font,'Ping_AR_+_LT:Bold')] font-[var(--typography\/weight\/bold,normal)] leading-[var(--typography\/line-height-\(descreptive\)\/8,32px)] relative shrink-0 text-[color:var(--text\/primary\/primary,#004956)] text-[length:var(--typography\/size\/2xl,24px)] text-right whitespace-nowrap" dir="auto" data-node-id="I18204:42660;18204:42570">
              عنوان
            </p>
          </div>
        </div>
      )}
    </div>
  );
}
```

## Design tokens / variables referenced in the code

| Token (CSS var) | Fallback | Used for |
|---|---|---|
| `--background/primary/primary` | `#004956` | Title Header bar background |
| `--background/secondary/seconadry` | `#a4ffe5` | active primary tab bg; "انشاء طلب" button bg |
| `--background/default/white` | `white` | Subcategory bar bg; avatar bg; help button bg |
| `--border/seconadry` | `#a4ffe5` | help-center button 1px border; page-title button 2px border |
| `--border/seconadry-hover` | `#dbfff6` | "جديد" tag 1px border |
| `--border/primary-link` | `#004956` | active secondary tab 2px bottom border |
| `--border/default` | `#eee` | avatar border (width 0) |
| `--text/gray/white` | `white` | inactive primary tab labels; tag label |
| `--text/primary/primary` | `#004956` | active primary tab label; page title; buttons; active breadcrumb |
| `--text/primary/link` | `#004956` | help-center button label; secondary tab label |
| `--text/gray/lighter` | `#737373` | inactive breadcrumb items |
| `--07--light-theme/gray/color-gray-200--(1)` | `#f8f8f8` | user name "عبدالله" (legacy token) |
| `--spacing/sizes/3xl` | `20px` | Title Header gap |
| `--spacing/sizes/9xl` | `56px` | Title Header / Subcategory / Page Title padding-x |
| `--spacing/7xl` | `56px` | Breadcrumb padding-x |
| `--spacing-7xl` | `24px` | Breadcrumb gap (hyphen naming) |
| `--spacing-4xl` | `16px` | Info group gap; Icons gap |
| `--spacing-lg` | `8px` | header Avatar name gap |
| `--spacing-md` | `6px` | Name gap |
| `--spacing-xs` | `2px` | contentContainer gap |
| `--spacing/base` | `16px` | Title Header padding-y; tab padding-x; Buttons gap; Page Title gap |
| `--spacing/xs` | `12px` | Subcategory padding-y; page-title button padding-x; Buttons gap |
| `--spacing/2xs` | `10px` | Primary tabs list gap |
| `--spacing/3xs` | `8px` | tab padding-y; breadcrumb padding-y/list gap; help btn padding-x |
| `--spacing/5xs` | `4px` | tab icon gap; button gaps/padding-y; breadcrumb item padding |
| `--spacing/6xs` | `2px` | secondary tab padding-x |
| `--spacing/sizes/sm` | `8px` | header Avatar gap + padding-x; tag padding-x |
| `--spacing/sizes/2xs` | `4px` | tag gap + padding-y |
| `--spacing/sizes/2xl` | `16px` | Page Title padding-y |
| `--radius/md` | `4px` | primary tabs |
| `--radius/sm` | `8px` | header Avatar wrapper |
| `--radius/xl` | `8px` (buttons) / `140px` (tag pill) | buttons; "جديد" tag |
| `--radius/full` | `9999px` / `8749.125px` | avatar |
| `--typography/family/font` | `Ping AR + LT` (Regular / Medium / Bold) | all text |
| `--typography/weight/regular|medium|bold` | `normal` (400/500/700) | |
| `--typography/size/xs` | `12px` | tag; help-center button |
| `--typography/size/sm` | `14px` | page-title button; breadcrumb |
| `--typography/size/md` | `16px` | tabs; secondary tab |
| `--typography/size/2xl` | `24px` | page title |
| `--typography/line-height (Descreptive)/4` | `16px` | xs text |
| `--typography/line-height (Descreptive)/5` | `20px` | sm text |
| `--typography/line-height (Descreptive)/6` | `24px` | md text |
| `--typography/line-height (Descreptive)/8` | `32px` | page title |

Fixed values: header width 1536px; primary tabs list width 1101.6px (flex-1 when placed); Subcategory bar height 64px, gap 24px; logo 95.4x40px; avatar 48px; primary tab icons 24px; header action icons 24px; arrow-down icon 16px; button icons 16px; tag min/max height 24px; help button min/max height 32px; page-title button min/max height 40px.

## Text styles

- `Regular/text-sm`: Font(family: "Ping AR + LT", style: Regular, size: 14, weight: 400, lineHeight: 100, letterSpacing: 0)
- `Regular/$text-xs`: Font(family: "Typography/Family/Font", style: Typography/Weight/Regular, size: Typography/Size/xs, weight: 400, lineHeight: typography/line-height (Descreptive)/4, letterSpacing: 0)
- `Medium/$text-base`: Font(family: "Typography/Family/Font", style: Typography/Weight/Medium, size: Typography/Size/md, weight: 500, lineHeight: typography/line-height (Descreptive)/6, letterSpacing: 0)
- `Bold/$text-base`: Font(family: "Typography/Family/Font", style: Typography/Weight/Bold, size: Typography/Size/md, weight: 700, lineHeight: typography/line-height (Descreptive)/6, letterSpacing: 0)
- `Medium/$text-xs`: Font(family: "Typography/Family/Font", style: Typography/Weight/Medium, size: Typography/Size/xs, weight: 500, lineHeight: typography/line-height (Descreptive)/4, letterSpacing: 0)

## Component descriptions (from Figma)

- **--device=desktop** — Node ID: 15895:36794. Keywords: [Top bar, Navigation bar, Masthead, Site header, Page header, Main navigation, UI container, App bar, رأس الصفحة, الشريط العلوي, شريط التنقل الرئيسي, ترويسة الموقع, حاوية واجهة المستخدم, عنوان الصفحة]
- **header Avatar** — Node ID: 15896:31776. Keywords: [User icon, Profile picture, User thumbnail, Account image, Member photo, Profile avatar, User menu, User profile indicator, صورة المستخدم, أيقونة الملف الشخصي, الصورة الرمزية, صورة الحساب, قائمة المستخدم, رمز المستخدم]
- **Primary Tabs List - Dashboard only** — Node ID: 15895:35397. Keywords: [Main navigation tabs, Top-level tabs, Section navigation, Content switcher, Tabbed interface, UI container, View switcher, Navigation bar, قائمة التبويبات الرئيسية, تبويبات التنقل الأساسية, شريط تبويبات, مقسم المحتوى, واجهة مبوبة, حاوية عرض, محول العرض]
- **Header Primary Tabs** — Node ID: 15412:79584. Keywords: [Content sections, Main navigation tabs, View switcher, Tabbed navigation, Section selector, UI container, Top-level tabs, Interactive tabs, علامات التبويب الرئيسية, تبويبات المحتوى, شريط تبويبات, أقسام المحتوى, محدد العرض, حاوية واجهة المستخدم, تبويبات تفاعلية, قوائم التبويب]
- **Button** — Node ID: 14526:107536. Keywords: [Action trigger, Clickable element, UI control, Interactive button, Command button, Call-to-action (CTA) button, Press component, زرار]
- **Secondary Tabs List** — Node ID: 15895:35465. Keywords: [Sub-tabs, Nested tabs, Inner tabs, Child tabs, Tabbed navigation, Content organizer, UI component, Filter tabs, تبويبات فرعية, تبويبات داخلية, علامات تبويب متداخلة, قائمة تبويبات ثانوية, منظم المحتوى, مكون واجهة المستخدم, تبويبات التصفية]
- **Header Secondary Tabs** — Node ID: 15456:85667. Keywords: [Sub-tabs, Nested tabs, Inner tabs, Sub-navigation, Content grouping, Tabbed navigation, Child tabs, UI container, Related content switcher, علامات تبويب فرعية, تبويبات داخلية, تقسيم المحتوى, تنظيم المحتوى, تبويبات متداخلة, تنقل فرعي, حاوية واجهة المستخدم]

## Assets

| Placeholder | Layer name | Size |
|---|---|---|
| `figma-asset:c022c.svg` | pie-chart-outline (tab "التقارير") | 24x24 |
| `figma-asset:3bc8e.svg` | chart-breakout-square-outline (tab "المتجر وقنوات البيع") | 24x24 |
| `figma-asset:ea919.svg` | marketing-outline (tab "التسويق") | 24x24 |
| `figma-asset:d8363.svg` | shirt-01-outline (tab "المنتجات") | 24x24 |
| `figma-asset:caf0b.svg` | delivery-box-02-outline (tab "الطلبات") | 24x24 |
| `figma-asset:ea8cc.svg` | home-01-outline (tab "الرئيسية", active) | 24x24 |
| `figma-asset:c5d9b.svg` | menu-01-outline (tab "الكل") | 24x24 |
| `figma-asset:3f02b.png` | _AvatarplaholderImages | 48x48 (cropped) |
| `figma-asset:77e1d.svg` | arrow-down-01-outline | 16x16 |
| `figma-asset:8804f.svg` | notification-01-outline | 24x24 |
| `figma-asset:1c34b.svg` | message-01-outline | 24x24 |
| `figma-asset:025eb.svg` | search-01-outline | 24x24 |
| `figma-asset:fa307.svg` | logo-light-wide 1 (Salla logo) | 95.4x40 |
| `figma-asset:a5c32.svg` | help-circle-outline (help-center button) | 16x16 |
| `figma-asset:9b1ae.svg` | arrow-left-01-outline (breadcrumb separator) | 24x24 |
| `figma-asset:a24ad.svg` | add-01-outline ("انشاء طلب" button) | 16x16 |

## Notes

- Sections: Title Header (dark teal bar with logo, primary tabs, action icons, user avatar+tag) is always rendered; Header Subcategory (white bar, secondary tabs + help button) is on by default; Breadcrumb and Page Title are optional (off by default in this variant).
- Default copy: tabs "التقارير", "المتجر وقنوات البيع", "التسويق", "المنتجات", "الطلبات", "الرئيسية" (active), "الكل"; user "عبدالله" with tag "جديد"; secondary tab "ملخص المتجر"; help button "مركز المساعدة"; page-title button "انشاء طلب"; title placeholder "عنوان".
- Original asset URL prefix `https://www.figma.com/api/mcp/asset/<uuid>/` replaced with `figma-asset:` placeholder.
