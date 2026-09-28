# Status (badge) — appearance=--strong, language=Arabic, type=--warning

- Figma file: `dnmyqzYKK9dUJjVHuIWMDS`
- Figma node id: `15342:59964`
- Parent component set: `15342:59936` (Status)
- Nested base component: `15342:59440` (Base Status Indicator, color=--warning, size=md)

## Code (verbatim from get_design_context)

```tsx
type BaseStatusIndicatorProps = {
  className?: string;
  color?: "--warning";
  size?: "md";
};

function BaseStatusIndicator({ className, color = "--warning", size = "md" }: BaseStatusIndicatorProps) {
  return <div className={className || "bg-[var(--warning\\/warning-dark,#d18f36)] max-h-[10px] max-w-[10px] min-h-[10px] min-w-[10px] overflow-clip relative rounded-[var(--radius\\/full,9999px)] size-[10px]"} data-node-id="15342:59440" />;
}

type StatusProps = {
  className?: string;
  appearance?: "--strong";
  language?: "Arabic";
  statusLabel?: string;
  type?: "--warning";
};

function Status({ className, appearance = "--strong", language = "Arabic", statusLabel = "اسم الحالة", type = "--warning" }: StatusProps) {
  return (
    <div className={className || "bg-[var(--warning\\/warning-lighter,#fff9eb)] content-stretch flex gap-[var(--spacing\\/5xs,4px)] h-[24px] items-center justify-center max-h-[24px] min-h-[24px] overflow-clip px-[var(--spacing\\/sizes\\/sm,8px)] relative rounded-[30px]"} data-node-id="15342:59964">
      <div className="content-stretch flex items-center justify-center relative shrink-0" data-node-id="15345:72869" data-name="__label">
        <p className="[word-break:break-word] font-[family-name:var(--typography\/family\/font,'Ping_AR_+_LT:Medium')] font-[var(--typography\/weight\/medium,normal)] leading-[var(--typography\/line-height-\(descreptive\)\/4,16px)] relative shrink-0 text-[color:var(--warning\/warning-darker,#8f5f22)] text-[length:var(--typography\/size\/xs,12px)] text-right whitespace-nowrap" dir="auto" data-node-id="15342:59965">
          {statusLabel}
        </p>
      </div>
      <BaseStatusIndicator className="bg-[var(--warning\/warning-dark,#d18f36)] max-h-[10px] max-w-[10px] min-h-[10px] min-w-[10px] relative rounded-[var(--radius\/full,9999px)] shrink-0 size-[10px]" />
    </div>
  );
}
```

## Design tokens / variables referenced in the code

| Token (CSS var) | Fallback |
|---|---|
| `--warning/warning-lighter` | `#fff9eb` (badge background) |
| `--warning/warning-dark` | `#d18f36` (10px dot) |
| `--warning/warning-darker` | `#8f5f22` (label text) |
| `--spacing/5xs` | `4px` (gap) |
| `--spacing/sizes/sm` | `8px` (padding-x) |
| `--radius/full` | `9999px` (dot) |
| `--typography/family/font` | `'Ping AR + LT:Medium'` |
| `--typography/weight/medium` | `normal` (500) |
| `--typography/size/xs` | `12px` |
| `--typography/line-height (Descreptive)/4` | `16px` |

Fixed values: height 24px (min/max 24px), badge border-radius 30px (hard-coded, not a token), dot 10x10px.

## Text styles

- `Medium/$text-xs`: Font(family: "Typography/Family/Font", style: Typography/Weight/Medium, size: Typography/Size/xs, weight: 500, lineHeight: typography/line-height (Descreptive)/4, letterSpacing: 0).

## Component description (from Figma)

**Status** — Node ID: 15342:59936. Keywords: [State indicator, Condition marker, Progress tracker, System feedback, Notification badge, Availability status, UI indicator, Information tag, مؤشر الحالة, علامة التنبيه, حالة النظام, مؤشر التقدم, شارة معلومات, رمز الحالة, مؤشر التوفر, بطاقة معلومات]

## Assets

- None (no image/SVG assets; the dot is a pure CSS circle).
