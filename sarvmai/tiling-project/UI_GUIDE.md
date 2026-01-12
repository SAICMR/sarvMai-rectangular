# 🎨 UI/UX Guide & Visual Reference

## 🎯 Application Interface Overview

### Main Layout (1280x720 minimum recommended)

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  🧩 NON-OPTIMAL TILING CALCULATOR                                  │
│  Maximize flooring costs with strategic tile placement              │
│                                                                     │
├─────────────────────┬───────────────────────────────────────────────┤
│                     │                                               │
│  INPUT PANEL        │  RESULTS PANEL                                │
│  ┌───────────────┐  │  ┌──────────────────────────────────────┐    │
│  │ Room Length   │  │  │ Tiles of size A:        0           │    │
│  │ [6_________]  │  │  │ Tiles of size B:        12          │    │
│  │               │  │  │ Tiles of size C:        0           │    │
│  │ Room Width    │  │  │                                      │    │
│  │ [4_________]  │  │  │ Cost (A):              $0.00         │    │
│  │               │  │  │ Cost (B):              $36.00        │    │
│  │ Tile A        │  │  │ Cost (C):              $0.00         │    │
│  │ Size: [1___]  │  │  │                                      │    │
│  │ Cost: [2___]  │  │  │ ┌──────────────────────────────────┐│    │
│  │               │  │  │ │ Total Cost: $36.00              ││    │
│  │ Tile B        │  │  │ └──────────────────────────────────┘│    │
│  │ Size: [2___]  │  │  │                                      │    │
│  │ Cost: [3___]  │  │  │ (Loading spinner if calculating)    │    │
│  │               │  │  │ (Error message if failed)           │    │
│  │ Tile C        │  │  │                                      │    │
│  │ Size: [3___]  │  │  │                                      │    │
│  │ Cost: [6___]  │  │  │                                      │    │
│  │               │  │  └──────────────────────────────────────┘    │
│  │ [Calculate]   │  │                                               │
│  └───────────────┘  │                                               │
│                     │                                               │
└─────────────────────┴───────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│  VISUALIZATION                                                      │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │ Legend:                                                      │  │
│  │ ■ Tile A (1×1)    ■ Tile B (2×2)    ■ Tile C (3×3)        │  │
│  │                                                              │  │
│  │ ASCII Grid:                                                  │  │
│  │ 222222222222                                                │  │
│  │ 222222222222                                                │  │
│  │ 222222222222                                                │  │
│  │ 222222222222                                                │  │
│  └──────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 🎨 Color Scheme

### Brand Colors
- **Primary Purple**: `#667eea` - Main interactive elements
- **Secondary Purple**: `#764ba2` - Gradients, accents
- **White**: `#ffffff` - Background, cards
- **Light Gray**: `#f9f9f9` - Backgrounds
- **Dark Gray**: `#333333` - Text
- **Medium Gray**: `#555555` - Labels

### Tile Colors (Visualization)
- **Tile A**: `#ff6b6b` (Red) - Smallest/cheapest
- **Tile B**: `#4ecdc4` (Teal) - Medium
- **Tile C**: `#ffe66d` (Yellow) - Largest/most expensive

### Status Colors
- **Error**: `#c33333` (Red)
- **Success**: `#33c333` (Green)
- **Warning**: `#ff9800` (Orange)
- **Info**: `#667eea` (Blue)

---

## 📐 Responsive Design Breakpoints

```
Desktop (1280px+)
└─ 2-column layout (input + results side-by-side)

Tablet (768px - 1279px)
└─ 1-column layout
└─ Stacked input and results

Mobile (<768px)
└─ Full-width single column
└─ Optimized touch targets
└─ Vertical scrolling
```

---

## 🖱️ Interactive Elements

### Buttons
```
┌──────────────────┐
│ 🚀 Calculate     │  ← Primary button
│   Solution       │
└──────────────────┘
Color: Gradient purple
Hover: Rises slightly + shadow
Click: Depresses
```

### Input Fields
```
┌────────────────────┐
│ [6________________]│
└────────────────────┘
Border: 2px #ddd
Focused: 2px #667eea + subtle glow
```

### Cards
```
┌──────────────────────┐
│ 📐 Room & Tile      │
│    Configuration    │
├──────────────────────┤
│ (Content)            │
│                      │
└──────────────────────┘
Shadow: 0 10px 30px rgba(0,0,0,0.2)
Border-radius: 10px
```

---

## 📊 Results Display Format

### Standard Result Display
```
┌─ Tile A ──────────────────┐
│ Tiles of size A: 0        │
│ Cost per tile: $2.00      │
│ Total cost: $0.00         │
└────────────────────────────┘

┌─ Tile B ──────────────────┐
│ Tiles of size B: 12       │
│ Cost per tile: $3.00      │
│ Total cost: $36.00        │
└────────────────────────────┘

┌─ Tile C ──────────────────┐
│ Tiles of size C: 0        │
│ Cost per tile: $6.00      │
│ Total cost: $0.00         │
└────────────────────────────┘

┌─ TOTAL ────────────────────┐
│ Total Cost: $36.00         │
└────────────────────────────┘
```

### Loading State
```
┌────────────────────┐
│   ⟳ (spinner)      │
│ Calculating        │
│ optimal solution...│
└────────────────────┘
```

### Error State
```
┌────────────────────────────┐
│ ✗ Error Message            │
│                            │
│ "Please fill in all        │
│  dimensions"               │
└────────────────────────────┘
```

---

## 🎯 Typography

### Headings
- **H1** (Page Title): 40px, bold, #fff, text-shadow
- **H2** (Section Title): 24px, bold, #333, border-bottom
- **H3** (Subsection): 18px, bold, #667eea

### Body Text
- **Regular**: 16px, #555
- **Labels**: 15px, #555, 600 weight
- **Values**: 16px, #667eea, bold
- **Monospace** (Code): 14px, Courier New, #333

---

## 🔄 State Management

### Application States
```
Initial State
  └─ Show form with sample data
  └─ Results hidden
  └─ Visualization hidden

Input Focus State
  └─ Input field highlighted
  └─ Cursor in field
  └─ Previous results still visible

Calculating State
  └─ Spinner visible
  └─ Button disabled
  └─ Form locked (cannot change)
  └─ Results area shows loading

Success State
  └─ Results visible
  └─ Visualization displayed
  └─ No error message
  └─ Button re-enabled

Error State
  └─ Error message visible
  └─ Results hidden
  └─ Visualization hidden
  └─ Button re-enabled
```

---

## ♿ Accessibility Features

### Semantic HTML
```html
<label for="length">Room Length</label>
<input type="number" id="length" aria-describedby="length-help">
```

### Keyboard Navigation
- Tab: Move between inputs
- Enter: Submit form
- Escape: Clear error

### Screen Readers
- Aria labels for all inputs
- Descriptive button text
- Error messages announced
- Results table structure

### Color Contrast
- Text: 4.5:1 contrast ratio minimum
- Interactive elements: 3:1 minimum

---

## 📱 Mobile Optimization

### Touch Targets
- Minimum 48x48px for buttons
- 10px padding around inputs
- Larger fonts: 16px minimum

### Viewport
```html
<meta name="viewport" 
      content="width=device-width, initial-scale=1.0">
```

### Mobile Menu
```
On tablets:
  Sidebar becomes hamburger menu
  Stack inputs vertically
  Full-width buttons

On phones:
  Single column layout
  Large touch buttons (60px+)
  Horizontal scroll for tables
```

---

## 🎬 Animation & Transitions

### Transitions (300ms all)
- Hover effects on buttons
- Color changes on focus
- Fade in/out for modals

### Loading Spinner
```css
animation: spin 1s linear infinite;
```
- Rotates 360° in 1 second
- Infinite loop
- Border top in primary color

### Fade Effects
```css
opacity: 0 → 1 over 300ms (fade in)
opacity: 1 → 0 over 300ms (fade out)
```

---

## 🎭 Visual Hierarchy

### Importance Order
1. **Page Title** - Largest, most prominent
2. **Main Inputs** - Large, visible
3. **Results** - Large, highlighted
4. **Visualizations** - Secondary information
5. **Labels & Help** - Smaller, muted

### Visual Weight
```
Heavy:   Primary buttons, main titles
Medium:  Input fields, results values
Light:   Labels, secondary text
```

---

## 📊 Sample Visualization Output

### Grid with Different Tile Types
```
Room: 10m × 8m
Tiles: 1×1(1), 2×2(3), 4×4(6)

ASCII Output:
1111222222223333
1111222222223333
1111444444443333
1111444444443333
5555444444446666
5555444444446666
7777888888886666
7777888888886666

Legend:
1 = Tile A (1×1) - #ff6b6b
2 = Tile B (2×2) - #4ecdc4
3 = Tile C (4×4) - #ffe66d
```

---

## 🖼️ Screenshots Description

### Before Calculation
```
- Empty or sample results hidden
- All input fields visible
- Focus on input panel
- Calculate button prominent
```

### After Calculation
```
- Results panel populated
- Numbers highlighted in blue
- Total cost in gradient box
- Visualization grid displayed
- Legend showing tile colors
```

### Error State
```
- Red error banner visible
- Error text centered
- Results hidden
- Input fields remain visible
- User can retry
```

---

## 💡 UX Principles Applied

✅ **Clarity** - Clear labels, obvious actions
✅ **Feedback** - Loading states, error messages
✅ **Efficiency** - Sample data pre-filled
✅ **Consistency** - Same styling throughout
✅ **Accessibility** - Color contrast, keyboard nav
✅ **Responsiveness** - Works on all devices
✅ **Aesthetics** - Modern gradient design
✅ **Trust** - Professional appearance

---

## 🎨 Customization Guide

### Change Primary Color
Edit `index.html` CSS:
```css
/* Current: #667eea */
/* Change to: #5e72e4, #6366f1, etc. */
```

### Change Tile Colors
```javascript
// In visualization
const colors = {
  'A': '#ff6b6b',  // Change red
  'B': '#4ecdc4',  // Change teal  
  'C': '#ffe66d'   // Change yellow
};
```

### Adjust Grid Size
```css
.main-content {
  grid-template-columns: 1fr 1fr;  /* Change 1fr 1fr */
}
```

---

**Professional, modern, and user-friendly interface design** 🎨

