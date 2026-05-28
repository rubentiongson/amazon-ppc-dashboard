codex/create-amazon-ppc-dashboard-web-app-dvy9h2

codex/create-amazon-ppc-dashboard-web-app-0hrlu9
 main
# Amazon PPC Dashboard — UI Build Instructions

This document explains how to implement and iterate the UI for the Streamlit dashboard in this repository.

## 1) Goal
Create a Streamlit UI that visually matches your approved dashboard design:
- Left navigation rail
- Top app bar with account/date controls
- KPI cards row
- Performance trends chart
- Insights & Alerts panel
- Top-performing campaigns table

## 2) File Structure
Use this structure so Streamlit Cloud works reliably:

- `app.py` → entrypoint shim only
- `streamlit_app.py` → main dashboard UI code
- `design.md` → this UI implementation guide

## 3) Streamlit Cloud Settings
In Streamlit Cloud, set:
- **Repository**: `rubentiongson/amazon-ppc-dashboard`
- **Branch**: `main` (or your active release branch)
- **Main file path**: `app.py`

Why: `app.py` imports `streamlit_app.py`, so either local or cloud entry works.

## 4) UI Implementation Checklist

### A. Global Theming
- Inject CSS via `st.markdown(CUSTOM_CSS, unsafe_allow_html=True)`.
- Keep brand palette/tokens in one `:root` block.
- Keep typography set to Inter and monospace fallback for numeric data.

### B. Sidebar (Left Rail)
Include:
- Brand: `Ads Console`
- Subtitle: `Seller Central API`
- Navigation list:
  - Dashboard
  - Campaigns
  - Products
  - Match Type
  - Keywords
  - Search Terms
  - ASIN Targets
  - ASIN from STR
  - Auto Campaigns
  - Category Targets
  - Wasted Ad Spend
- Buttons:
  - Sync Data
  - Help Center
  - Log Out

### C. Top Bar
Include:
- Title: `PPC Insights`
- Account selection chip/dropdown
- Date range chip (`Last 30 Days`)
- Notification/help/user placeholders

### D. KPI Cards
Use four cards:
- TOTAL SPEND: `$12,450.00` (+5%)
- TOTAL SALES: `$84,200.00` (+12%)
- ACoS: `14.78%` (-2%)
- ROAS: `6.76x` (+8%)

### E. Main Chart Area
- Title: `Performance Trends`
- Two series: Spend and Sales
- Keep simple static sample data initially
- Use consistent colors and light grid

### F. Insights Panel
Include cards/alerts for:
- Budget Alert
- Optimization Tip
- Unlock AI Insights
- CTA button: `UPGRADE PRO`

### G. Campaigns Table
Title row:
- `Top Performing Campaigns`
- `VIEW ALL REPORTS` action text

Columns:
- CAMPAIGN NAME
- STATUS
- SPEND
- SALES
- ACoS
- ACTION

## 5) Data Layer (Next Step)
After layout lock:
1. Add a data loader module (CSV first, API later).
2. Replace static KPI/chart/table data with real transformed data.
3. Add filters (date, campaign type, status) wired to dataframe.

## 6) Deployment Flow
1. Commit UI changes.
2. Push to GitHub branch.
3. Merge to `main`.
4. Streamlit Cloud auto-redeploys.
5. If stale: reboot app from Streamlit settings.

## 7) Common Pitfalls
- Do not leave merge-conflict markers in `app.py` or `streamlit_app.py`.
- Avoid mixing multiple duplicated CSS blocks.
- Keep only one source of UI logic (`streamlit_app.py`).
- Ensure `requirements.txt` includes `streamlit` and `pandas`.

## 8) Definition of Done (UI Phase)
- App loads without syntax/runtime errors.
- Layout visually matches approved mock.
- Sidebar + topbar + KPI + chart + insights + table all visible.
- Deploy preview reflects latest `main` commit.
 codex/create-amazon-ppc-dashboard-web-app-dvy9h2


<!-- Design System -->
<!DOCTYPE html><html class="light" lang="en"><head>
<meta charset="utf-8">
<meta content="width=device-width, initial-scale=1.0" name="viewport">
<title>PPC Insights Dashboard</title>
<!-- Fonts & Icons -->
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&amp;family=JetBrains+Mono:wght@500&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<!-- Tailwind Config -->
<script id="tailwind-config">
        tailwind.config = {
            darkMode: "class",
            theme: {
                extend: {
                    "colors": {
                        "surface-bright": "#f8fafa",
                        "on-tertiary-container": "#004b59",
                        "inverse-on-surface": "#eff1f1",
                        "error": "#ba1a1a",
                        "surface-container-low": "#f2f4f4",
                        "outline": "#887361",
                        "on-tertiary-fixed": "#001f26",
                        "on-error": "#ffffff",
                        "surface-container-high": "#e6e8e8",
                        "surface-variant": "#e1e3e3",
                        "on-secondary": "#ffffff",
                        "surface": "#f8fafa",
                        "surface-container-lowest": "#ffffff",
                        "on-primary-container": "#653a00",
                        "on-error-container": "#93000a",
                        "outline-variant": "#dbc2ad",
                        "secondary": "#535f70",
                        "primary-container": "#ff9900",
                        "secondary-container": "#d4e1f5",
                        "on-secondary-container": "#576474",
                        "inverse-primary": "#ffb86f",
                        "on-tertiary": "#ffffff",
                        "tertiary-container": "#6abdd3",
                        "inverse-surface": "#2e3131",
                        "surface-tint": "#8a5100",
                        "error-container": "#ffdad6",
                        "on-primary-fixed-variant": "#693c00",
                        "primary-fixed": "#ffdcbd",
                        "primary": "#8a5100",
                        "surface-container": "#eceeee",
                        "primary-fixed-dim": "#ffb86f",
                        "tertiary-fixed-dim": "#80d2e9",
                        "tertiary": "#00687a",
                        "surface-dim": "#d8dada",
                        "on-surface": "#191c1d",
                        "on-surface-variant": "#554434",
                        "background": "#f8fafa",
                        "tertiary-fixed": "#adecff",
                        "on-background": "#191c1d",
                        "secondary-fixed": "#d7e3f7",
                        "on-primary-fixed": "#2c1600",
                        "on-secondary-fixed": "#101c2b",
                        "on-tertiary-fixed-variant": "#004e5d",
                        "on-secondary-fixed-variant": "#3c4858",
                        "surface-container-highest": "#e1e3e3",
                        "on-primary": "#ffffff",
                        "secondary-fixed-dim": "#bbc7db"
                    },
                    "borderRadius": {
                        "DEFAULT": "0.125rem",
                        "lg": "0.25rem",
                        "xl": "0.5rem",
                        "full": "0.75rem"
                    },
                    "spacing": {
                        "margin-mobile": "16px",
                        "max-width": "1440px",
                        "unit": "4px",
                        "margin-desktop": "32px",
                        "gutter": "16px",
                        "container-padding": "24px"
                    },
                    "fontFamily": {
                        "headline-sm": ["Inter"],
                        "display-md": ["Inter"],
                        "body-lg": ["Inter"],
                        "data-mono": ["JetBrains Mono"],
                        "body-sm": ["Inter"],
                        "label-caps": ["Inter"],
                        "display-lg": ["Inter"],
                        "body-md": ["Inter"]
                    },
                    "fontSize": {
                        "headline-sm": ["18px", {"lineHeight": "24px", "fontWeight": "600"}],
                        "display-md": ["24px", {"lineHeight": "32px", "letterSpacing": "-0.01em", "fontWeight": "600"}],
                        "body-lg": ["16px", {"lineHeight": "24px", "fontWeight": "400"}],
                        "data-mono": ["13px", {"lineHeight": "18px", "fontWeight": "500"}],
                        "body-sm": ["12px", {"lineHeight": "16px", "fontWeight": "400"}],
                        "label-caps": ["11px", {"lineHeight": "16px", "letterSpacing": "0.05em", "fontWeight": "700"}],
                        "display-lg": ["32px", {"lineHeight": "40px", "letterSpacing": "-0.02em", "fontWeight": "700"}],
                        "body-md": ["14px", {"lineHeight": "20px", "fontWeight": "400"}]
                    }
                },
            },
        }
    </script>
<style>
        body { background-color: #f8fafa; }
        .material-symbols-outlined {
            font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
        }
        .zebra-table tr:nth-child(even) {
            background-color: #f8fafa;
        }
        .chart-grid {
            background-image: linear-gradient(to right, #f0f2f2 1px, transparent 1px),
                              linear-gradient(to bottom, #f0f2f2 1px, transparent 1px);
            background-size: 40px 40px;
        }
    </style>
</head>
<body class="font-body-md text-on-surface">
<!-- SideNavBar Shell -->
<aside class="h-screen w-64 fixed left-0 top-0 bg-surface-container-low dark:bg-surface-dim border-r border-outline-variant dark:border-outline flex flex-col py-6 px-4 gap-y-2 z-50">
<div class="mb-8 px-2">
<h1 class="font-headline-sm text-headline-sm font-bold text-primary dark:text-primary-fixed">Ads Console</h1>
<p class="font-label-caps text-label-caps text-on-surface-variant opacity-70">Seller Central API</p>
</div>
<nav class="flex-grow flex flex-col gap-y-1 overflow-y-auto"><!-- Dashboard Active -->
<a class="bg-secondary-container dark:bg-secondary text-on-secondary-container dark:text-on-secondary font-semibold rounded-xl flex items-center gap-3 px-4 py-3 transition-all" href="#">
<span class="material-symbols-outlined" data-icon="dashboard">dashboard</span>
<span class="font-body-md">Dashboard</span>
</a>
<a class="text-on-surface-variant dark:text-surface-variant hover:bg-surface-container-highest flex items-center gap-3 px-4 py-3 rounded-xl transition-all" href="#">
<span class="material-symbols-outlined" data-icon="ads_click">ads_click</span>
<span class="font-body-md">Campaigns</span>
</a>
<a class="text-on-surface-variant dark:text-surface-variant hover:bg-surface-container-highest flex items-center gap-3 px-4 py-3 rounded-xl transition-all" href="#">
<span class="material-symbols-outlined" data-icon="inventory_2">inventory_2</span>
<span class="font-body-md">Products</span>
</a>
<a class="text-on-surface-variant dark:text-surface-variant hover:bg-surface-container-highest flex items-center gap-3 px-4 py-3 rounded-xl transition-all" href="#">
<span class="material-symbols-outlined" data-icon="architecture">architecture</span>
<span class="font-body-md">Match Type</span>
</a>
<a class="text-on-surface-variant dark:text-surface-variant hover:bg-surface-container-highest flex items-center gap-3 px-4 py-3 rounded-xl transition-all" href="#">
<span class="material-symbols-outlined" data-icon="key">key</span>
<span class="font-body-md">Keywords</span>
</a>
<a class="text-on-surface-variant dark:text-surface-variant hover:bg-surface-container-highest flex items-center gap-3 px-4 py-3 rounded-xl transition-all" href="#">
<span class="material-symbols-outlined" data-icon="search">search</span>
<span class="font-body-md">Search Terms</span>
</a>
<a class="text-on-surface-variant dark:text-surface-variant hover:bg-surface-container-highest flex items-center gap-3 px-4 py-3 rounded-xl transition-all" href="#">
<span class="material-symbols-outlined" data-icon="target">target</span>
<span class="font-body-md">ASIN Targets</span>
</a>
<a class="text-on-surface-variant dark:text-surface-variant hover:bg-surface-container-highest flex items-center gap-3 px-4 py-3 rounded-xl transition-all" href="#">
<span class="material-symbols-outlined" data-icon="psychology">psychology</span>
<span class="font-body-md">ASIN from STR</span>
</a>
<a class="text-on-surface-variant dark:text-surface-variant hover:bg-surface-container-highest flex items-center gap-3 px-4 py-3 rounded-xl transition-all" href="#">
<span class="material-symbols-outlined" data-icon="autorenew">autorenew</span>
<span class="font-body-md">Auto Campaigns</span>
</a>
<a class="text-on-surface-variant dark:text-surface-variant hover:bg-surface-container-highest flex items-center gap-3 px-4 py-3 rounded-xl transition-all" href="#">
<span class="material-symbols-outlined" data-icon="category">category</span>
<span class="font-body-md">Category Targets</span>
</a>
<a class="text-on-surface-variant dark:text-surface-variant hover:bg-surface-container-highest flex items-center gap-3 px-4 py-3 rounded-xl transition-all" href="#">
<span class="material-symbols-outlined" data-icon="delete_sweep">delete_sweep</span>
<span class="font-body-md">Wasted Ad Spend</span>
</a></nav>
<button class="mt-4 mb-8 bg-primary-container text-on-primary-container font-bold py-3 px-4 rounded-xl flex items-center justify-center gap-2 hover:opacity-90 active:scale-95 transition-all">
<span class="material-symbols-outlined" data-icon="sync">sync</span>
<span class="">Sync Data</span>
</button>
<div class="flex flex-col gap-y-1 pt-4 border-t border-outline-variant">
<a class="text-on-surface-variant hover:bg-surface-container-highest flex items-center gap-3 px-4 py-2 rounded-xl transition-all" href="#">
<span class="material-symbols-outlined" data-icon="contact_support">contact_support</span>
<span class="font-body-md">Help Center</span>
</a>
<a class="text-on-surface-variant hover:bg-surface-container-highest flex items-center gap-3 px-4 py-2 rounded-xl transition-all" href="#">
<span class="material-symbols-outlined" data-icon="logout">logout</span>
<span class="font-body-md">Log Out</span>
</a>
</div>
</aside>
<!-- Main Content Canvas -->
<main class="ml-64 flex flex-col min-h-screen">
<!-- TopAppBar Shell -->
<header class="h-16 bg-surface-container-lowest border-b border-outline-variant flex justify-between items-center px-margin-desktop sticky top-0 z-40">
<div class="flex items-center gap-6">
<h2 class="font-display-md text-display-md font-bold text-primary">PPC Insights</h2>
<div class="flex items-center bg-surface-container-low px-4 py-1.5 rounded-full border border-outline-variant">
<span class="material-symbols-outlined text-sm mr-2" data-icon="account_balance">account_balance</span>
<span class="font-label-caps text-label-caps uppercase tracking-wider">Account Selection</span>
<span class="material-symbols-outlined ml-2 text-sm" data-icon="arrow_drop_down">arrow_drop_down</span>
</div>
</div>
<div class="flex items-center gap-4">
<div class="flex items-center bg-surface-container-high px-4 py-1.5 rounded-full cursor-pointer hover:bg-surface-variant transition-colors">
<span class="material-symbols-outlined text-sm mr-2" data-icon="calendar_today">calendar_today</span>
<span class="font-label-caps text-label-caps">Date Range: Last 30 Days</span>
</div>
<div class="flex items-center gap-3 text-on-surface-variant">
<button class="p-2 hover:bg-surface-container-high rounded-full transition-colors">
<span class="material-symbols-outlined" data-icon="notifications">notifications</span>
</button>
<button class="p-2 hover:bg-surface-container-high rounded-full transition-colors">
<span class="material-symbols-outlined" data-icon="help_outline">help_outline</span>
</button>
<div class="h-8 w-8 rounded-full overflow-hidden border border-outline-variant bg-secondary-container">
<img alt="User profile" class="w-full h-full object-cover" data-alt="A professional headshot of a business executive with a warm, confident expression. The lighting is soft and natural, against a clean, blurred office background. The overall aesthetic is high-fidelity and modern, using a balanced color palette of soft greys and blues to match a corporate light-mode UI." src="https://lh3.googleusercontent.com/aida-public/AB6AXuBvbC5cctS68RJ7qBkQzGz3kZMygkuqDPURlkuvgzeCruaw6W7n7KlDnEiIeHjIoPmxVRrkfJKFrcOYUO4aJUISd1TI6-ZkcVq1gvZ782JJtpdNi0ynKU8UAz1nSizQcYeeeWZ6H36KcqqL58CVC_wUZruFOYE-Bi46FC95_kTRoo5xdupRCNzIEVzhobFJk47vPUiA5nB88RaJQonbnrr-lESfShpXG3TW2DugPvRf49zn3GpTq_dVbbSSLnOgMbDudhngppGp">
</div>
</div>
</div>
</header>
<!-- Scrollable Content Area -->
<div class="p-margin-desktop max-w-max-width mx-auto w-full grid grid-cols-12 gap-gutter">
<!-- KPI Section -->
<section class="col-span-12 grid grid-cols-1 md:grid-cols-4 gap-gutter mb-4">
<!-- KPI 1 -->
<div class="bg-surface-container-lowest border border-outline-variant p-5 rounded-lg">
<p class="font-label-caps text-label-caps text-on-surface-variant mb-1">TOTAL SPEND</p>
<div class="flex items-end justify-between">
<h3 class="font-display-md text-display-md text-primary">$12,450.00</h3>
<div class="flex items-center text-error bg-error-container/20 px-2 py-0.5 rounded text-xs font-bold">
<span class="material-symbols-outlined text-sm" data-icon="trending_up">trending_up</span>
<span class="">+5%</span>
</div>
</div>
</div>
<!-- KPI 2 -->
<div class="bg-surface-container-lowest border border-outline-variant p-5 rounded-lg">
<p class="font-label-caps text-label-caps text-on-surface-variant mb-1">TOTAL SALES</p>
<div class="flex items-end justify-between">
<h3 class="font-display-md text-display-md text-primary">$84,200.00</h3>
<div class="flex items-center text-[#2e7d32] bg-[#e8f5e9] px-2 py-0.5 rounded text-xs font-bold">
<span class="material-symbols-outlined text-sm" data-icon="trending_up">trending_up</span>
<span class="">+12%</span>
</div>
</div>
</div>
<!-- KPI 3 -->
<div class="bg-surface-container-lowest border border-outline-variant p-5 rounded-lg">
<p class="font-label-caps text-label-caps text-on-surface-variant mb-1">ACoS</p>
<div class="flex items-end justify-between">
<h3 class="font-display-md text-display-md text-primary">14.78%</h3>
<div class="flex items-center text-[#2e7d32] bg-[#e8f5e9] px-2 py-0.5 rounded text-xs font-bold">
<span class="material-symbols-outlined text-sm" data-icon="trending_down">trending_down</span>
<span class="">-2%</span>
</div>
</div>
</div>
<!-- KPI 4 -->
<div class="bg-surface-container-lowest border border-outline-variant p-5 rounded-lg">
<p class="font-label-caps text-label-caps text-on-surface-variant mb-1">ROAS</p>
<div class="flex items-end justify-between">
<h3 class="font-display-md text-display-md text-primary">6.76x</h3>
<div class="flex items-center text-[#2e7d32] bg-[#e8f5e9] px-2 py-0.5 rounded text-xs font-bold">
<span class="material-symbols-outlined text-sm" data-icon="trending_up">trending_up</span>
<span class="">+8%</span>
</div>
</div>
</div>
</section>
<!-- Main Performance Chart Area -->
<section class="col-span-12 lg:col-span-9">
<div class="bg-surface-container-lowest border border-outline-variant rounded-lg p-6 h-full">
<div class="flex justify-between items-center mb-6">
<h4 class="font-headline-sm text-headline-sm">Performance Trends</h4>
<div class="flex gap-4">
<div class="flex items-center gap-2">
<span class="w-3 h-3 rounded-full bg-primary"></span>
<span class="text-xs font-medium uppercase tracking-wider">Spend</span>
</div>
<div class="flex items-center gap-2">
<span class="w-3 h-3 rounded-full bg-tertiary"></span>
<span class="text-xs font-medium uppercase tracking-wider">Sales</span>
</div>
</div>
</div>
<!-- Mock Chart -->
<div class="relative h-64 w-full chart-grid border-b border-l border-outline-variant/30">
<svg class="absolute top-0 left-0 w-full h-full" viewBox="0 0 1000 250">
<!-- Sales Path -->
<path d="M0,200 Q100,180 200,120 T400,100 T600,60 T800,40 T1000,20" fill="none" stroke="#00687a" stroke-width="2"></path>
<!-- Spend Path -->
<path d="M0,230 Q100,220 200,200 T400,210 T600,190 T800,185 T1000,180" fill="none" stroke="#8a5100" stroke-width="2"></path>
</svg>
<!-- Chart Labels -->
<div class="absolute bottom-0 left-0 w-full flex justify-between px-2 pt-2 -mb-6">
<span class="font-data-mono text-[10px] text-on-surface-variant">OCT 01</span>
<span class="font-data-mono text-[10px] text-on-surface-variant">OCT 10</span>
<span class="font-data-mono text-[10px] text-on-surface-variant">OCT 20</span>
<span class="font-data-mono text-[10px] text-on-surface-variant">OCT 30</span>
</div>
</div>
</div>
</section>
<!-- Insights Sidebar -->
<aside class="col-span-12 lg:col-span-3">
<div class="bg-surface-container-lowest border border-outline-variant rounded-lg p-5 h-full flex flex-col gap-4">
<h4 class="font-headline-sm text-headline-sm">Insights &amp; Alerts</h4>
<div class="bg-secondary-container/30 border-l-4 border-secondary p-3 rounded-r-lg">
<div class="flex items-center gap-2 mb-1">
<span class="material-symbols-outlined text-sm text-secondary" data-icon="error_outline">error_outline</span>
<span class="font-label-caps text-[10px]">BUDGET ALERT</span>
</div>
<p class="font-body-sm text-body-sm text-on-secondary-container font-medium">3 campaigns are nearing daily budget limit.</p>
<button class="mt-2 text-primary text-[10px] font-bold hover:underline">VIEW CAMPAIGNS</button>
</div>
<div class="bg-primary-container/10 border-l-4 border-primary p-3 rounded-r-lg">
<div class="flex items-center gap-2 mb-1">
<span class="material-symbols-outlined text-sm text-primary" data-icon="lightbulb">lightbulb</span>
<span class="font-label-caps text-[10px]">OPTIMIZATION TIP</span>
</div>
<p class="font-body-sm text-body-sm text-on-primary-container font-medium">Lowering bids on "keyword_x" could save $45/day.</p>
</div>
<div class="mt-auto">
<div class="bg-tertiary-container/20 p-4 rounded-xl text-center border border-tertiary/20">
<span class="material-symbols-outlined text-3xl text-tertiary mb-2" data-icon="auto_awesome">auto_awesome</span>
<p class="font-body-sm text-on-tertiary-container font-bold">Unlock AI Insights</p>
<p class="text-[10px] text-on-tertiary-container/70 mb-3">Get predictive keyword scaling advice.</p>
<button class="w-full bg-tertiary text-white py-2 rounded-lg font-label-caps">UPGRADE PRO</button>
</div>
</div>
</div>
</aside>
<!-- Campaign Performance Table -->
<section class="col-span-12">
<div class="bg-surface-container-lowest border border-outline-variant rounded-lg overflow-hidden">
<div class="px-6 py-4 border-b border-outline-variant flex justify-between items-center">
<h4 class="font-headline-sm text-headline-sm">Top Performing Campaigns</h4>
<button class="text-primary font-label-caps text-label-caps hover:bg-surface-container-high px-3 py-1 rounded transition-colors">VIEW ALL REPORTS</button>
</div>
<div class="overflow-x-auto">
<table class="w-full text-left border-collapse zebra-table">
<thead>
<tr class="bg-surface-container-low text-on-surface-variant font-label-caps text-label-caps">
<th class="px-6 py-3 border-b border-outline-variant">CAMPAIGN NAME</th>
<th class="px-6 py-3 border-b border-outline-variant text-center">STATUS</th>
<th class="px-6 py-3 border-b border-outline-variant text-right">SPEND</th>
<th class="px-6 py-3 border-b border-outline-variant text-right">SALES</th>
<th class="px-6 py-3 border-b border-outline-variant text-right">ACoS</th>
<th class="px-6 py-3 border-b border-outline-variant text-center">ACTION</th>
</tr>
</thead>
<tbody class="text-on-surface">
<tr class="border-b border-outline-variant hover:bg-surface-container-high/50 transition-colors h-10">
<td class="px-6 py-3 font-medium">Summer_Collection_Manual_2023</td>
<td class="px-6 py-3 text-center">
<span class="px-2 py-0.5 bg-[#e8f5e9] text-[#2e7d32] text-[10px] font-bold rounded-full border border-[#c8e6c9]">ACTIVE</span>
</td>
<td class="px-6 py-3 text-right font-data-mono">$1,420.50</td>
<td class="px-6 py-3 text-right font-data-mono">$12,500.00</td>
<td class="px-6 py-3 text-right font-data-mono">11.36%</td>
<td class="px-6 py-3 text-center">
<button class="material-symbols-outlined text-on-surface-variant hover:text-primary transition-colors" data-icon="more_horiz">more_horiz</button>
</td>
</tr>
<tr class="border-b border-outline-variant hover:bg-surface-container-high/50 transition-colors h-10">
<td class="px-6 py-3 font-medium">Prime_Day_Headphones_Auto</td>
<td class="px-6 py-3 text-center">
<span class="px-2 py-0.5 bg-[#e8f5e9] text-[#2e7d32] text-[10px] font-bold rounded-full border border-[#c8e6c9]">ACTIVE</span>
</td>
<td class="px-6 py-3 text-right font-data-mono">$2,105.00</td>
<td class="px-6 py-3 text-right font-data-mono">$18,450.00</td>
<td class="px-6 py-3 text-right font-data-mono">11.41%</td>
<td class="px-6 py-3 text-center">
<button class="material-symbols-outlined text-on-surface-variant hover:text-primary transition-colors" data-icon="more_horiz">more_horiz</button>
</td>
</tr>
<tr class="border-b border-outline-variant hover:bg-surface-container-high/50 transition-colors h-10">
<td class="px-6 py-3 font-medium">Competitor_Targeting_Bags</td>
<td class="px-6 py-3 text-center">
<span class="px-2 py-0.5 bg-secondary-container text-on-secondary-container text-[10px] font-bold rounded-full border border-outline-variant">PAUSED</span>
</td>
<td class="px-6 py-3 text-right font-data-mono">$850.40</td>
<td class="px-6 py-3 text-right font-data-mono">$6,120.00</td>
<td class="px-6 py-3 text-right font-data-mono">13.89%</td>
<td class="px-6 py-3 text-center">
<button class="material-symbols-outlined text-on-surface-variant hover:text-primary transition-colors" data-icon="more_horiz">more_horiz</button>
</td>
</tr>
<tr class="border-b border-outline-variant hover:bg-surface-container-high/50 transition-colors h-10">
<td class="px-6 py-3 font-medium">Brand_Defense_Keywords</td>
<td class="px-6 py-3 text-center">
<span class="px-2 py-0.5 bg-[#e8f5e9] text-[#2e7d32] text-[10px] font-bold rounded-full border border-[#c8e6c9]">ACTIVE</span>
</td>
<td class="px-6 py-3 text-right font-data-mono">$3,200.00</td>
<td class="px-6 py-3 text-right font-data-mono">$24,800.00</td>
<td class="px-6 py-3 text-right font-data-mono">12.90%</td>
<td class="px-6 py-3 text-center">
<button class="material-symbols-outlined text-on-surface-variant hover:text-primary transition-colors" data-icon="more_horiz">more_horiz</button>
</td>
</tr>
<tr class="border-b border-outline-variant hover:bg-surface-container-high/50 transition-colors h-10">
<td class="px-6 py-3 font-medium">Home_Office_Desk_Lamp_Manual</td>
<td class="px-6 py-3 text-center">
<span class="px-2 py-0.5 bg-error-container/20 text-error text-[10px] font-bold rounded-full border border-error/30">OUT OF BUDGET</span>
</td>
<td class="px-6 py-3 text-right font-data-mono">$680.00</td>
<td class="px-6 py-3 text-right font-data-mono">$3,450.00</td>
<td class="px-6 py-3 text-right font-data-mono">19.71%</td>
<td class="px-6 py-3 text-center">
<button class="material-symbols-outlined text-on-surface-variant hover:text-primary transition-colors" data-icon="more_horiz">more_horiz</button>
</td>
</tr>
</tbody>
</table>
</div>
</div>
</section>
</div>
</main>
<script>
        // Simple interactivity for demonstration
        document.querySelectorAll('nav a').forEach(link => {
            link.addEventListener('click', (e) => {
                if (!e.currentTarget.classList.contains('bg-secondary-container')) {
                    // Logic to handle tab switching would go here
                }
            });
        });
    </script>


</body></html>

<!-- Dashboard - Performance Overview -->
<!DOCTYPE html><html class="light" lang="en" style=""><head>
<meta charset="utf-8">
<meta content="width=device-width, initial-scale=1.0" name="viewport">
<title>Campaigns | PPC Insights</title>
<!-- Tailwind CSS -->
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<!-- Material Symbols -->
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<!-- Google Fonts -->
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&amp;family=JetBrains+Mono:wght@500&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<script id="tailwind-config">
        tailwind.config = {
            darkMode: "class",
            theme: {
                extend: {
                    "colors": {
                        "primary-container": "#ff9900",
                        "outline-variant": "#dbc2ad",
                        "on-primary-container": "#653a00",
                        "secondary": "#535f70",
                        "tertiary-fixed": "#adecff",
                        "surface-variant": "#e1e3e3",
                        "surface-bright": "#f8fafa",
                        "error-container": "#ffdad6",
                        "surface-container-highest": "#e1e3e3",
                        "background": "#f8fafa",
                        "surface-container": "#eceeee",
                        "on-tertiary-container": "#004b59",
                        "inverse-on-surface": "#eff1f1",
                        "outline": "#887361",
                        "tertiary-fixed-dim": "#80d2e9",
                        "primary-fixed": "#ffdcbd",
                        "on-tertiary-fixed-variant": "#004e5d",
                        "on-primary-fixed-variant": "#693c00",
                        "on-primary-fixed": "#2c1600",
                        "on-secondary": "#ffffff",
                        "surface": "#f8fafa",
                        "on-surface": "#191c1d",
                        "on-primary": "#ffffff",
                        "on-error-container": "#93000a",
                        "on-secondary-fixed-variant": "#3c4858",
                        "on-secondary-fixed": "#101c2b",
                        "secondary-fixed": "#d7e3f7",
                        "secondary-container": "#d4e1f5",
                        "error": "#ba1a1a",
                        "surface-container-high": "#e6e8e8",
                        "tertiary-container": "#6abdd3",
                        "on-secondary-container": "#576474",
                        "on-error": "#ffffff",
                        "surface-dim": "#d8dada",
                        "surface-container-low": "#f2f4f4",
                        "surface-container-lowest": "#ffffff",
                        "secondary-fixed-dim": "#bbc7db",
                        "primary": "#8a5100",
                        "on-tertiary-fixed": "#001f26",
                        "primary-fixed-dim": "#ffb86f",
                        "surface-tint": "#8a5100",
                        "tertiary": "#00687a",
                        "on-tertiary": "#ffffff",
                        "inverse-surface": "#2e3131",
                        "on-background": "#191c1d"
                    },
                    "borderRadius": {
                        "DEFAULT": "0.125rem",
                        "lg": "0.25rem",
                        "xl": "0.5rem",
                        "full": "0.75rem"
                    },
                    "spacing": {
                        "margin-mobile": "16px",
                        "unit": "4px",
                        "margin-desktop": "32px",
                        "container-padding": "24px",
                        "max-width": "1440px",
                        "gutter": "16px"
                    },
                    "fontFamily": {
                        "data-mono": ["JetBrains Mono"],
                        "body-md": ["Inter"],
                        "body-sm": ["Inter"],
                        "label-caps": ["Inter"],
                        "headline-sm": ["Inter"],
                        "display-md": ["Inter"],
                        "display-lg": ["Inter"],
                        "body-lg": ["Inter"]
                    },
                    "fontSize": {
                        "data-mono": ["13px", {"lineHeight": "18px", "fontWeight": "500"}],
                        "body-md": ["14px", {"lineHeight": "20px", "fontWeight": "400"}],
                        "body-sm": ["12px", {"lineHeight": "16px", "fontWeight": "400"}],
                        "label-caps": ["11px", {"lineHeight": "16px", "letterSpacing": "0.05em", "fontWeight": "700"}],
                        "headline-sm": ["18px", {"lineHeight": "24px", "fontWeight": "600"}],
                        "display-md": ["24px", {"lineHeight": "32px", "letterSpacing": "-0.01em", "fontWeight": "600"}],
                        "display-lg": ["32px", {"lineHeight": "40px", "letterSpacing": "-0.02em", "fontWeight": "700"}],
                        "body-lg": ["16px", {"lineHeight": "24px", "fontWeight": "400"}]
                    }
                },
            },
        }
    </script>
<style>
        .material-symbols-outlined {
            font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
            vertical-align: middle;
        }
        ::-webkit-scrollbar { width: 6px; height: 6px; }
        ::-webkit-scrollbar-track { background: transparent; }
        ::-webkit-scrollbar-thumb { background: #d8dada; border-radius: 10px; }
        ::-webkit-scrollbar-thumb:hover { background: #887361; }
    </style>
</head>
<body class="bg-background text-on-background font-body-md overflow-x-hidden">
<!-- SideNavBar -->
<aside class="h-screen w-64 fixed left-0 top-0 bg-surface-container-low dark:bg-surface-dim border-r border-outline-variant dark:border-outline flex flex-col py-6 px-4 gap-y-2 z-50">
<div class="mb-8 px-2">
<h1 class="font-headline-sm text-headline-sm font-bold text-primary dark:text-primary-fixed">Ads Console</h1>
<p class="text-on-surface-variant font-label-caps text-[10px] tracking-widest">SELLER CENTRAL API</p>
</div>
<nav class="flex flex-col gap-y-1 overflow-y-auto flex-1"><a class="text-on-surface-variant dark:text-surface-variant hover:bg-surface-container-high flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-200" href="#">
    <span class="material-symbols-outlined">dashboard</span>
    <span class="">Dashboard</span>
</a>
<a class="bg-secondary-container dark:bg-secondary text-on-secondary-container dark:text-on-secondary font-semibold rounded-xl flex items-center gap-3 px-4 py-3 shadow-sm" href="#">
    <span class="material-symbols-outlined">ads_click</span>
    <span class="">Campaigns</span>
</a>
<a class="text-on-surface-variant dark:text-surface-variant hover:bg-surface-container-high flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-200" href="#">
    <span class="material-symbols-outlined">inventory_2</span>
    <span class="">Products</span>
</a>
<a class="text-on-surface-variant dark:text-surface-variant hover:bg-surface-container-high flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-200" href="#">
    <span class="material-symbols-outlined">layers</span>
    <span class="">Match Type</span>
</a>
<a class="text-on-surface-variant dark:text-surface-variant hover:bg-surface-container-high flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-200" href="#">
    <span class="material-symbols-outlined">key</span>
    <span class="">Keywords</span>
</a>
<a class="text-on-surface-variant dark:text-surface-variant hover:bg-surface-container-high flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-200" href="#">
    <span class="material-symbols-outlined">search</span>
    <span class="">Search Terms</span>
</a>
<a class="text-on-surface-variant dark:text-surface-variant hover:bg-surface-container-high flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-200" href="#">
    <span class="material-symbols-outlined">target</span>
    <span class="">ASIN Targets</span>
</a>
<a class="text-on-surface-variant dark:text-surface-variant hover:bg-surface-container-high flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-200" href="#">
    <span class="material-symbols-outlined">track_changes</span>
    <span class="">ASIN from STR</span>
</a>
<a class="text-on-surface-variant dark:text-surface-variant hover:bg-surface-container-high flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-200" href="#">
    <span class="material-symbols-outlined">auto_awesome</span>
    <span class="">Auto Campaigns</span>
</a>
<a class="text-on-surface-variant dark:text-surface-variant hover:bg-surface-container-high flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-200" href="#">
    <span class="material-symbols-outlined">category</span>
    <span class="">Category Targets</span>
</a>
<a class="text-on-surface-variant dark:text-surface-variant hover:bg-surface-container-high flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-200" href="#">
    <span class="material-symbols-outlined">delete_sweep</span>
    <span class="">Wasted Ad Spend</span>
</a></nav>
<div class="mt-auto flex flex-col gap-y-1">
<button class="bg-primary-container text-on-primary-container font-bold py-3 rounded-xl flex items-center justify-center gap-2 mb-4 hover:opacity-90 active:scale-95 transition-all">
<span class="material-symbols-outlined">sync</span>
                Sync Data
            </button>
<a class="text-on-surface-variant dark:text-surface-variant hover:bg-surface-container-high flex items-center gap-3 px-4 py-2 rounded-xl text-sm" href="#">
<span class="material-symbols-outlined">contact_support</span>
<span class="">Help Center</span>
</a>
<a class="text-on-surface-variant dark:text-surface-variant hover:bg-surface-container-high flex items-center gap-3 px-4 py-2 rounded-xl text-sm" href="#" style="transform: translateY(0px); box-shadow: none; transition: 0.2s ease-out;">
<span class="material-symbols-outlined">logout</span>
<span class="">Log Out</span>
</a>
</div>
</aside>
<!-- Main Wrapper -->
<div class="ml-64 flex flex-col min-h-screen">
<!-- TopAppBar -->
<header class="bg-surface-container-lowest dark:bg-surface-dim border-b border-outline-variant dark:border-outline h-16 sticky top-0 z-40 w-full">
<div class="flex justify-between items-center h-full px-margin-desktop max-w-max-width mx-auto">
<div class="flex items-center gap-8">
<span class="font-display-md text-display-md font-bold text-primary dark:text-primary-fixed">PPC Insights</span>
<div class="hidden md:flex items-center gap-1 bg-surface-container px-3 py-1.5 rounded-lg border border-outline-variant/30">
<span class="material-symbols-outlined text-on-surface-variant text-sm">search</span>
<input class="bg-transparent border-none focus:ring-0 text-body-sm w-48" placeholder="Search campaign name..." type="text">
</div>
</div>
<div class="flex items-center gap-4">
<div class="flex flex-col items-end mr-2">
<span class="font-label-caps text-label-caps text-on-surface-variant">DATE RANGE</span>
<span class="font-data-mono text-data-mono text-primary">Last 30 Days</span>
</div>
<div class="h-8 w-px bg-outline-variant"></div>
<div class="flex items-center gap-3">
<button class="p-2 rounded-full hover:bg-surface-container-high transition-colors">
<span class="material-symbols-outlined text-on-surface-variant">notifications</span>
</button>
<button class="p-2 rounded-full hover:bg-surface-container-high transition-colors">
<span class="material-symbols-outlined text-on-surface-variant">help_outline</span>
</button>
<button class="flex items-center gap-2 p-1 pl-3 rounded-full border border-outline-variant hover:bg-surface-container-high transition-colors">
<span class="font-label-caps text-label-caps text-on-surface">ACCOUNT</span>
<span class="material-symbols-outlined text-primary">account_circle</span>
</button>
</div>
</div>
</div>
</header>
<!-- Main Content Canvas -->
<main class="flex-1 p-margin-desktop max-w-max-width mx-auto w-full space-y-8">
<!-- KPI Summary Bento Grid -->
<section class="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-13 gap-3">
<!-- Impressions -->
<div class="bg-surface-container-lowest border border-outline-variant p-4 rounded-lg flex flex-col justify-between col-span-1 min-w-[100px]">
<span class="font-label-caps text-[10px] text-on-surface-variant uppercase">Impressions</span>
<div class="mt-2">
<span class="font-data-mono text-lg text-on-surface">1.2M</span>
<div class="flex items-center gap-1 text-[10px] text-error">
<span class="material-symbols-outlined text-xs">trending_down</span>
<span class="">4.2%</span>
</div>
</div>
</div>
<!-- Clicks -->
<div class="bg-surface-container-lowest border border-outline-variant p-4 rounded-lg flex flex-col justify-between">
<span class="font-label-caps text-[10px] text-on-surface-variant uppercase">Clicks</span>
<div class="mt-2">
<span class="font-data-mono text-lg text-on-surface">24.5K</span>
<div class="flex items-center gap-1 text-[10px] text-primary">
<span class="material-symbols-outlined text-xs">trending_up</span>
<span class="">12.1%</span>
</div>
</div>
</div>
<!-- CTR -->
<div class="bg-surface-container-lowest border border-outline-variant p-4 rounded-lg flex flex-col justify-between">
<span class="font-label-caps text-[10px] text-on-surface-variant uppercase">CTR</span>
<div class="mt-2">
<span class="font-data-mono text-lg text-on-surface">2.04%</span>
<div class="flex items-center gap-1 text-[10px] text-primary">
<span class="material-symbols-outlined text-xs">trending_up</span>
<span class="">0.5%</span>
</div>
</div>
</div>
<!-- CVR -->
<div class="bg-surface-container-lowest border border-outline-variant p-4 rounded-lg flex flex-col justify-between">
<span class="font-label-caps text-[10px] text-on-surface-variant uppercase">CVR</span>
<div class="mt-2">
<span class="font-data-mono text-lg text-on-surface">8.12%</span>
<div class="flex items-center gap-1 text-[10px] text-error">
<span class="material-symbols-outlined text-xs">trending_down</span>
<span class="">1.2%</span>
</div>
</div>
</div>
<!-- CPC -->
<div class="bg-surface-container-lowest border border-outline-variant p-4 rounded-lg flex flex-col justify-between">
<span class="font-label-caps text-[10px] text-on-surface-variant uppercase">CPC</span>
<div class="mt-2">
<span class="font-data-mono text-lg text-on-surface">$0.82</span>
<div class="flex items-center gap-1 text-[10px] text-primary">
<span class="material-symbols-outlined text-xs">trending_down</span>
<span class="">0.04</span>
</div>
</div>
</div>
<!-- Spend -->
<div class="bg-surface-container-lowest border border-outline-variant p-4 rounded-lg flex flex-col justify-between col-span-1 md:col-span-1">
<span class="font-label-caps text-[10px] text-on-surface-variant uppercase">Spend</span>
<div class="mt-2">
<span class="font-data-mono text-lg text-on-surface">$20.1K</span>
</div>
</div>
<!-- Sales -->
<div class="bg-surface-container-lowest border border-outline-variant p-4 rounded-lg flex flex-col justify-between">
<span class="font-label-caps text-[10px] text-on-surface-variant uppercase">Sales</span>
<div class="mt-2">
<span class="font-data-mono text-lg text-on-surface">$84.2K</span>
</div>
</div>
<!-- Orders -->
<div class="bg-surface-container-lowest border border-outline-variant p-4 rounded-lg flex flex-col justify-between">
<span class="font-label-caps text-[10px] text-on-surface-variant uppercase">Orders</span>
<div class="mt-2">
<span class="font-data-mono text-lg text-on-surface">1,984</span>
</div>
</div>
<!-- Units -->
<div class="bg-surface-container-lowest border border-outline-variant p-4 rounded-lg flex flex-col justify-between">
<span class="font-label-caps text-[10px] text-on-surface-variant uppercase">Units</span>
<div class="mt-2">
<span class="font-data-mono text-lg text-on-surface">2,142</span>
</div>
</div>
<!-- ACOS -->
<div class="bg-surface-container-lowest border border-primary/20 p-4 rounded-lg flex flex-col justify-between bg-primary-container/5">
<span class="font-label-caps text-[10px] text-primary uppercase">ACOS</span>
<div class="mt-2">
<span class="font-data-mono text-lg font-bold text-primary">23.8%</span>
</div>
</div>
<!-- ROAS -->
<div class="bg-surface-container-lowest border border-primary/20 p-4 rounded-lg flex flex-col justify-between bg-primary-container/5">
<span class="font-label-caps text-[10px] text-primary uppercase">ROAS</span>
<div class="mt-2">
<span class="font-data-mono text-lg font-bold text-primary">4.19x</span>
</div>
</div>
<!-- Spend Split -->
<div class="bg-surface-container-lowest border border-outline-variant p-4 rounded-lg flex flex-col justify-between">
<span class="font-label-caps text-[10px] text-on-surface-variant uppercase">Spend %</span>
<div class="mt-2">
<span class="font-data-mono text-lg text-on-surface">62%</span>
</div>
</div>
<!-- Sales Split -->
<div class="bg-surface-container-lowest border border-outline-variant p-4 rounded-lg flex flex-col justify-between">
<span class="font-label-caps text-[10px] text-on-surface-variant uppercase">Sales %</span>
<div class="mt-2">
<span class="font-data-mono text-lg text-on-surface">58%</span>
</div>
</div>
</section>
<!-- Table Controls Row -->
<div class="flex flex-col md:flex-row gap-4 justify-between items-center">
<!-- Campaign Type Filters -->
<div class="flex bg-surface-container-low p-1 rounded-xl border border-outline-variant/30" style="transform: translateY(0px); box-shadow: none; transition: 0.2s ease-out;">
<button class="px-6 py-2 rounded-lg text-body-sm font-semibold bg-white shadow-sm text-primary">All Campaigns</button>
<button class="px-6 py-2 rounded-lg text-body-sm text-on-surface-variant hover:text-on-surface transition-colors" style="transform: translateY(0px); box-shadow: none; transition: 0.2s ease-out;">Sponsored Products</button>
<button class="px-6 py-2 rounded-lg text-body-sm text-on-surface-variant hover:text-on-surface transition-colors" style="transform: translateY(0px); box-shadow: none; transition: 0.2s ease-out;">Sponsored Brands</button>
<button class="px-6 py-2 rounded-lg text-body-sm text-on-surface-variant hover:text-on-surface transition-colors">Sponsored Display</button>
</div>
<div class="flex items-center gap-2">
<button class="flex items-center gap-2 px-4 py-2 bg-surface-container-lowest border border-outline-variant rounded-lg text-body-sm font-medium hover:bg-surface-container-high transition-colors">
<span class="material-symbols-outlined text-sm">filter_list</span>
                        Advanced Filters
                    </button>
<button class="flex items-center gap-2 px-4 py-2 bg-surface-container-lowest border border-outline-variant rounded-lg text-body-sm font-medium hover:bg-surface-container-high transition-colors">
<span class="material-symbols-outlined text-sm">download</span>
                        Export
                    </button>
</div>
</div>
<!-- Campaign Table Card -->
<div class="bg-surface-container-lowest border border-outline-variant rounded-xl overflow-hidden shadow-sm" style="transform: translateY(0px); box-shadow: none; transition: 0.2s ease-out;">
<div class="overflow-x-auto">
<table class="w-full text-left border-collapse">
<thead>
<tr class="bg-surface-container-low border-b border-outline-variant">
<th class="px-6 py-3 font-label-caps text-label-caps text-on-surface-variant uppercase tracking-wider">Campaign Name</th>
<th class="px-6 py-3 font-label-caps text-label-caps text-on-surface-variant uppercase tracking-wider">Status</th>
<th class="px-6 py-3 font-label-caps text-label-caps text-on-surface-variant uppercase tracking-wider">Type</th>
<th class="px-6 py-3 font-label-caps text-label-caps text-on-surface-variant uppercase tracking-wider text-right">Impressions</th>
<th class="px-6 py-3 font-label-caps text-label-caps text-on-surface-variant uppercase tracking-wider text-right">Clicks</th>
<th class="px-6 py-3 font-label-caps text-label-caps text-on-surface-variant uppercase tracking-wider text-right">Spend</th>
<th class="px-6 py-3 font-label-caps text-label-caps text-on-surface-variant uppercase tracking-wider text-right">Sales</th>
<th class="px-6 py-3 font-label-caps text-label-caps text-on-surface-variant uppercase tracking-wider text-right">ACoS</th>
<th class="px-6 py-3 font-label-caps text-label-caps text-on-surface-variant uppercase tracking-wider text-right">ROAS</th>
</tr>
</thead>
<tbody class="divide-y divide-outline-variant/30">
<!-- Row 1 -->
<tr class="hover:bg-surface-container transition-colors h-10">
<td class="px-6 py-3 font-body-md text-on-surface font-medium">SP_HighVolume_Generic_US</td>
<td class="px-6 py-3">
<span class="inline-flex items-center gap-1.5 px-2 py-0.5 rounded-full bg-green-100 text-green-700 text-[10px] font-bold">
<span class="w-1.5 h-1.5 rounded-full bg-green-600"></span> ACTIVE
                                    </span>
</td>
<td class="px-6 py-3 text-body-sm text-on-surface-variant">Sponsored Products</td>
<td class="px-6 py-3 font-data-mono text-data-mono text-right">245,820</td>
<td class="px-6 py-3 font-data-mono text-data-mono text-right">1,240</td>
<td class="px-6 py-3 font-data-mono text-data-mono text-right">$1,024.50</td>
<td class="px-6 py-3 font-data-mono text-data-mono text-right">$4,820.00</td>
<td class="px-6 py-3 font-data-mono text-data-mono text-right text-primary font-bold">21.2%</td>
<td class="px-6 py-3 font-data-mono text-data-mono text-right">4.7x</td>
</tr>
<!-- Row 2 -->
<tr class="bg-surface-container-low/30 hover:bg-surface-container transition-colors h-10">
<td class="px-6 py-3 font-body-md text-on-surface font-medium">SB_BrandDefense_Q3</td>
<td class="px-6 py-3">
<span class="inline-flex items-center gap-1.5 px-2 py-0.5 rounded-full bg-yellow-100 text-yellow-700 text-[10px] font-bold">
<span class="w-1.5 h-1.5 rounded-full bg-yellow-600"></span> OUT OF BUDGET
                                    </span>
</td>
<td class="px-6 py-3 text-body-sm text-on-surface-variant">Sponsored Brands</td>
<td class="px-6 py-3 font-data-mono text-data-mono text-right">82,100</td>
<td class="px-6 py-3 font-data-mono text-data-mono text-right">542</td>
<td class="px-6 py-3 font-data-mono text-data-mono text-right">$640.20</td>
<td class="px-6 py-3 font-data-mono text-data-mono text-right">$3,120.50</td>
<td class="px-6 py-3 font-data-mono text-data-mono text-right text-primary font-bold">20.5%</td>
<td class="px-6 py-3 font-data-mono text-data-mono text-right">4.8x</td>
</tr>
<!-- Row 3 -->
<tr class="hover:bg-surface-container transition-colors h-10">
<td class="px-6 py-3 font-body-md text-on-surface font-medium">SD_Remarketing_L7D</td>
<td class="px-6 py-3">
<span class="inline-flex items-center gap-1.5 px-2 py-0.5 rounded-full bg-gray-100 text-gray-700 text-[10px] font-bold">
<span class="w-1.5 h-1.5 rounded-full bg-gray-400"></span> PAUSED
                                    </span>
</td>
<td class="px-6 py-3 text-body-sm text-on-surface-variant">Sponsored Display</td>
<td class="px-6 py-3 font-data-mono text-data-mono text-right">12,400</td>
<td class="px-6 py-3 font-data-mono text-data-mono text-right">88</td>
<td class="px-6 py-3 font-data-mono text-data-mono text-right">$112.40</td>
<td class="px-6 py-3 font-data-mono text-data-mono text-right">$450.00</td>
<td class="px-6 py-3 font-data-mono text-data-mono text-right text-primary font-bold">25.0%</td>
<td class="px-6 py-3 font-data-mono text-data-mono text-right">4.0x</td>
</tr>
<!-- Row 4 -->
<tr class="bg-surface-container-low/30 hover:bg-surface-container transition-colors h-10">
<td class="px-6 py-3 font-body-md text-on-surface font-medium">SP_Auto_Harvesting_01</td>
<td class="px-6 py-3">
<span class="inline-flex items-center gap-1.5 px-2 py-0.5 rounded-full bg-green-100 text-green-700 text-[10px] font-bold">
<span class="w-1.5 h-1.5 rounded-full bg-green-600"></span> ACTIVE
                                    </span>
</td>
<td class="px-6 py-3 text-body-sm text-on-surface-variant">Sponsored Products</td>
<td class="px-6 py-3 font-data-mono text-data-mono text-right">412,050</td>
<td class="px-6 py-3 font-data-mono text-data-mono text-right">2,840</td>
<td class="px-6 py-3 font-data-mono text-data-mono text-right">$2,410.00</td>
<td class="px-6 py-3 font-data-mono text-data-mono text-right">$12,050.00</td>
<td class="px-6 py-3 font-data-mono text-data-mono text-right text-primary font-bold">20.0%</td>
<td class="px-6 py-3 font-data-mono text-data-mono text-right">5.0x</td>
</tr>
<!-- Row 5 -->
<tr class="hover:bg-surface-container transition-colors h-10">
<td class="px-6 py-3 font-body-md text-on-surface font-medium">SP_CompetitorConquesting_Bissell</td>
<td class="px-6 py-3">
<span class="inline-flex items-center gap-1.5 px-2 py-0.5 rounded-full bg-green-100 text-green-700 text-[10px] font-bold">
<span class="w-1.5 h-1.5 rounded-full bg-green-600"></span> ACTIVE
                                    </span>
</td>
<td class="px-6 py-3 text-body-sm text-on-surface-variant">Sponsored Products</td>
<td class="px-6 py-3 font-data-mono text-data-mono text-right">65,400</td>
<td class="px-6 py-3 font-data-mono text-data-mono text-right">312</td>
<td class="px-6 py-3 font-data-mono text-data-mono text-right">$410.80</td>
<td class="px-6 py-3 font-data-mono text-data-mono text-right">$820.00</td>
<td class="px-6 py-3 font-data-mono text-data-mono text-right text-error font-bold">50.1%</td>
<td class="px-6 py-3 font-data-mono text-data-mono text-right">2.0x</td>
</tr>
</tbody>
</table>
</div>
<!-- Pagination -->
<div class="px-6 py-4 border-t border-outline-variant flex justify-between items-center bg-surface-container-low">
<span class="text-body-sm text-on-surface-variant">Showing 1 to 5 of 42 campaigns</span>
<div class="flex items-center gap-2">
<button class="p-1 rounded hover:bg-surface-container-high text-on-surface-variant disabled:opacity-30" disabled="">
<span class="material-symbols-outlined">chevron_left</span>
</button>
<button class="px-3 py-1 rounded bg-primary text-white text-body-sm font-bold">1</button>
<button class="px-3 py-1 rounded hover:bg-surface-container-high text-on-surface-variant text-body-sm font-medium">2</button>
<button class="px-3 py-1 rounded hover:bg-surface-container-high text-on-surface-variant text-body-sm font-medium">3</button>
<span class="text-on-surface-variant px-1">...</span>
<button class="px-3 py-1 rounded hover:bg-surface-container-high text-on-surface-variant text-body-sm font-medium">9</button>
<button class="p-1 rounded hover:bg-surface-container-high text-on-surface-variant">
<span class="material-symbols-outlined">chevron_right</span>
</button>
</div>
</div>
</div>
<!-- Contextual Insights Section -->
<div class="grid grid-cols-1 md:grid-cols-3 gap-8">
<div class="col-span-1 md:col-span-2 bg-surface-container-lowest border border-outline-variant p-6 rounded-xl flex items-center justify-between overflow-hidden relative group">
<div class="relative z-10">
<h3 class="font-headline-sm text-headline-sm text-primary mb-2">Maximize your ROI</h3>
<p class="text-body-md text-on-surface-variant max-w-md">Our AI analysis identified 14 keywords that are spending but not converting. Pausing these could save you up to $420/week.</p>
<button class="mt-4 px-6 py-2 bg-primary text-white font-bold rounded-lg hover:opacity-90 transition-all active:scale-95">View Suggestions</button>
</div>
<div class="hidden lg:block w-48 h-48 opacity-10 group-hover:opacity-20 transition-opacity">
<img alt="Campaign Optimization Illustration" class="w-full h-full object-contain" data-alt="A clean, minimalist 3D rendering of floating geometric bar charts and professional analytics symbols in Amazon orange and deep navy. The lighting is bright and high-key, creating a professional and analytical atmosphere suitable for a corporate dashboard. The overall style is modern tech-focused digital art with a focus on data growth." src="https://lh3.googleusercontent.com/aida-public/AB6AXuCwrBS4vkbqnXqsJqXGqVv5CfBj8ejHEpgtOfZiH7pnGAuzU9cvFyfZ9TFHczOkEen7ojj3MbeMA1_to4Msfu79tKIpUT_ImOUywdLz8DXNnEyaiwqGfXlSdN7KsWuMuCECq4c_UDoL7LEb9XBjGceYCtbURE18GK210jPR6yRlhGR7CcKPoNkvzQxWBZXxrTI86APU8S5YPq57YaGhWYJUFMYoBmbog4OMX3-tzPmGijo53Z8S3oPwGKEqCPLJYmOyvqzXnx29">
</div>
</div>
<div class="col-span-1 bg-surface-container-lowest border border-outline-variant p-6 rounded-xl">
<h3 class="font-label-caps text-label-caps text-on-surface-variant mb-4">BUDGET ALLOCATION</h3>
<div class="space-y-4">
<div class="space-y-1">
<div class="flex justify-between text-body-sm">
<span class="">Sponsored Products</span>
<span class="font-data-mono">65%</span>
</div>
<div class="w-full bg-surface-container-high h-2 rounded-full overflow-hidden">
<div class="bg-primary h-full" style="width: 65%"></div>
</div>
</div>
<div class="space-y-1">
<div class="flex justify-between text-body-sm">
<span class="">Sponsored Brands</span>
<span class="font-data-mono">25%</span>
</div>
<div class="w-full bg-surface-container-high h-2 rounded-full overflow-hidden">
<div class="bg-secondary h-full" style="width: 25%"></div>
</div>
</div>
<div class="space-y-1">
<div class="flex justify-between text-body-sm">
<span class="">Sponsored Display</span>
<span class="font-data-mono">10%</span>
</div>
<div class="w-full bg-surface-container-high h-2 rounded-full overflow-hidden">
<div class="bg-tertiary h-full" style="width: 10%"></div>
</div>
</div>
</div>
</div>
</div>
</main>
<!-- Footer -->
<footer class="mt-auto px-margin-desktop py-6 border-t border-outline-variant bg-surface-container-lowest">
<div class="max-w-max-width mx-auto flex justify-between items-center text-body-sm text-on-surface-variant">
<span class="">© 2024 PPC Insights. All rights reserved.</span>
<div class="flex gap-6">
<a class="hover:text-primary transition-colors" href="#">Privacy Policy</a>
<a class="hover:text-primary transition-colors" href="#">Terms of Service</a>
<a class="hover:text-primary transition-colors" href="#">Contact Support</a>
</div>
</div>
</footer>
</div>
<!-- Micro-interaction Scripts -->
<script>
        // Simple hover lift effect for cards
        document.querySelectorAll('.rounded-lg, .rounded-xl').forEach(card => {
            card.addEventListener('mouseenter', () => {
                if(!card.classList.contains('border-primary')) {
                    card.style.transform = 'translateY(-2px)';
                    card.style.boxShadow = '0 4px 12px rgba(0,0,0,0.05)';
                    card.style.transition = 'all 0.2s ease-out';
                }
            });
            card.addEventListener('mouseleave', () => {
                card.style.transform = 'translateY(0)';
                card.style.boxShadow = 'none';
            });
        });
    </script>


</body></html>

<!-- Campaigns - Performance Management -->
<!DOCTYPE html><html class="light" lang="en"><head>
<meta charset="utf-8">
<meta content="width=device-width, initial-scale=1.0" name="viewport">
<title>Products Performance - PPC Insights</title>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&amp;family=JetBrains+Mono:wght@500&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<style>
        .material-symbols-outlined {
            font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
            vertical-align: middle;
        }
        /* Custom scrollbar for data-heavy sections */
        ::-webkit-scrollbar { width: 6px; height: 6px; }
        ::-webkit-scrollbar-track { background: #f1f1f1; }
        ::-webkit-scrollbar-thumb { background: #d1d5db; border-radius: 10px; }
        ::-webkit-scrollbar-thumb:hover { background: #9ca3af; }
    </style>
<script id="tailwind-config">
        tailwind.config = {
            darkMode: "class",
            theme: {
                extend: {
                    "colors": {
                        "surface-container-high": "#e6e8e8",
                        "tertiary": "#00687a",
                        "secondary-container": "#d4e1f5",
                        "primary-fixed": "#ffdcbd",
                        "outline-variant": "#dbc2ad",
                        "on-tertiary-container": "#004b59",
                        "on-primary-fixed": "#2c1600",
                        "on-error-container": "#93000a",
                        "surface": "#f8fafa",
                        "surface-dim": "#d8dada",
                        "surface-container": "#eceeee",
                        "surface-container-low": "#f2f4f4",
                        "surface-container-highest": "#e1e3e3",
                        "tertiary-container": "#6abdd3",
                        "tertiary-fixed-dim": "#80d2e9",
                        "on-secondary": "#ffffff",
                        "on-surface": "#191c1d",
                        "surface-tint": "#8a5100",
                        "on-tertiary-fixed-variant": "#004e5d",
                        "inverse-on-surface": "#eff1f1",
                        "inverse-surface": "#2e3131",
                        "on-secondary-fixed-variant": "#3c4858",
                        "on-error": "#ffffff",
                        "secondary-fixed-dim": "#bbc7db",
                        "primary-container": "#ff9900",
                        "tertiary-fixed": "#adecff",
                        "surface-container-lowest": "#ffffff",
                        "surface-bright": "#f8fafa",
                        "error": "#ba1a1a",
                        "background": "#f8fafa",
                        "on-primary": "#ffffff",
                        "inverse-primary": "#ffb86f",
                        "secondary-fixed": "#d7e3f7",
                        "secondary": "#535f70",
                        "on-secondary-fixed": "#101c2b",
                        "on-secondary-container": "#576474",
                        "on-surface-variant": "#554434",
                        "on-tertiary": "#ffffff",
                        "error-container": "#ffdad6",
                        "surface-variant": "#e1e3e3",
                        "primary-fixed-dim": "#ffb86f",
                        "on-primary-fixed-variant": "#693c00",
                        "on-background": "#191c1d",
                        "primary": "#8a5100",
                        "outline": "#887361",
                        "on-primary-container": "#653a00",
                        "on-tertiary-fixed": "#001f26"
                    },
                    "borderRadius": {
                        "DEFAULT": "0.125rem",
                        "lg": "0.25rem",
                        "xl": "0.5rem",
                        "full": "0.75rem"
                    },
                    "spacing": {
                        "gutter": "16px",
                        "unit": "4px",
                        "max-width": "1440px",
                        "margin-desktop": "32px",
                        "margin-mobile": "16px",
                        "container-padding": "24px"
                    },
                    "fontFamily": {
                        "body-md": ["Inter"],
                        "body-lg": ["Inter"],
                        "headline-sm": ["Inter"],
                        "label-caps": ["Inter"],
                        "display-lg": ["Inter"],
                        "data-mono": ["JetBrains Mono"],
                        "display-md": ["Inter"],
                        "body-sm": ["Inter"]
                    },
                    "fontSize": {
                        "body-md": ["14px", {"lineHeight": "20px", "fontWeight": "400"}],
                        "body-lg": ["16px", {"lineHeight": "24px", "fontWeight": "400"}],
                        "headline-sm": ["18px", {"lineHeight": "24px", "fontWeight": "600"}],
                        "label-caps": ["11px", {"lineHeight": "16px", "letterSpacing": "0.05em", "fontWeight": "700"}],
                        "display-lg": ["32px", {"lineHeight": "40px", "letterSpacing": "-0.02em", "fontWeight": "700"}],
                        "data-mono": ["13px", {"lineHeight": "18px", "fontWeight": "500"}],
                        "display-md": ["24px", {"lineHeight": "32px", "letterSpacing": "-0.01em", "fontWeight": "600"}],
                        "body-sm": ["12px", {"lineHeight": "16px", "fontWeight": "400"}]
                    }
                }
            }
        }
    </script>
</head>
<body class="bg-background text-on-surface font-body-md overflow-hidden">
<!-- SideNavBar -->
<aside class="h-screen w-64 fixed left-0 top-0 bg-surface-container-low dark:bg-surface-dim border-r border-outline-variant dark:border-outline flex flex-col py-6 px-4 gap-y-2 z-50">
<div class="mb-8 px-2 flex items-center gap-3">
<div class="w-10 h-10 bg-primary-container rounded-lg flex items-center justify-center text-on-primary-container">
<span class="material-symbols-outlined" data-icon="insights">insights</span>
</div>
<div>
<h1 class="font-headline-sm text-headline-sm font-bold text-primary dark:text-primary-fixed">Ads Console</h1>
<p class="font-label-caps text-[9px] uppercase tracking-wider text-on-surface-variant">Seller Central API</p>
</div>
</div>
<nav class="flex-1 space-y-1 overflow-y-auto pr-2">
<a class="text-on-surface-variant dark:text-surface-variant hover:bg-surface-container-highest flex items-center gap-3 px-4 py-2.5 rounded-xl transition-all duration-200" href="#">
<span class="material-symbols-outlined text-[20px]" data-icon="dashboard">dashboard</span>
<span class="font-body-md">Dashboard</span>
</a>
<a class="text-on-surface-variant dark:text-surface-variant hover:bg-surface-container-highest flex items-center gap-3 px-4 py-2.5 rounded-xl transition-all duration-200" href="#">
<span class="material-symbols-outlined text-[20px]" data-icon="ads_click">ads_click</span>
<span class="font-body-md">Campaigns</span>
</a>
<a class="bg-secondary-container dark:bg-secondary text-on-secondary-container dark:text-on-secondary font-semibold rounded-xl flex items-center gap-3 px-4 py-2.5 transition-all" href="#">
<span class="material-symbols-outlined text-[20px]" data-icon="inventory_2">inventory_2</span>
<span class="font-body-md">Products</span>
</a>
<a class="text-on-surface-variant dark:text-surface-variant hover:bg-surface-container-highest flex items-center gap-3 px-4 py-2.5 rounded-xl transition-all duration-200" href="#">
<span class="material-symbols-outlined text-[20px]" data-icon="join_inner">join_inner</span>
<span class="font-body-md">Match Type</span>
</a>
<a class="text-on-surface-variant dark:text-surface-variant hover:bg-surface-container-highest flex items-center gap-3 px-4 py-2.5 rounded-xl transition-all duration-200" href="#">
<span class="material-symbols-outlined text-[20px]" data-icon="key">key</span>
<span class="font-body-md">Keywords</span>
</a>
<a class="text-on-surface-variant dark:text-surface-variant hover:bg-surface-container-highest flex items-center gap-3 px-4 py-2.5 rounded-xl transition-all duration-200" href="#">
<span class="material-symbols-outlined text-[20px]" data-icon="search">search</span>
<span class="font-body-md">Search Terms</span>
</a>
<a class="text-on-surface-variant dark:text-surface-variant hover:bg-surface-container-highest flex items-center gap-3 px-4 py-2.5 rounded-xl transition-all duration-200" href="#">
<span class="material-symbols-outlined text-[20px]" data-icon="target">target</span>
<span class="font-body-md">ASIN Targets</span>
</a>
<a class="text-on-surface-variant dark:text-surface-variant hover:bg-surface-container-highest flex items-center gap-3 px-4 py-2.5 rounded-xl transition-all duration-200" href="#">
<span class="material-symbols-outlined text-[20px]" data-icon="query_stats">query_stats</span>
<span class="font-body-md">ASIN from STR</span>
</a>
<a class="text-on-surface-variant dark:text-surface-variant hover:bg-surface-container-highest flex items-center gap-3 px-4 py-2.5 rounded-xl transition-all duration-200" href="#">
<span class="material-symbols-outlined text-[20px]" data-icon="precision_manufacturing">precision_manufacturing</span>
<span class="font-body-md">Auto Campaigns</span>
</a>
<a class="text-on-surface-variant dark:text-surface-variant hover:bg-surface-container-highest flex items-center gap-3 px-4 py-2.5 rounded-xl transition-all duration-200" href="#">
<span class="material-symbols-outlined text-[20px]" data-icon="category">category</span>
<span class="font-body-md">Category Targets</span>
</a>
<a class="text-on-surface-variant dark:text-surface-variant hover:bg-surface-container-highest flex items-center gap-3 px-4 py-2.5 rounded-xl transition-all duration-200" href="#">
<span class="material-symbols-outlined text-[20px]" data-icon="monetization_on">monetization_on</span>
<span class="font-body-md">Wasted Ad Spend</span>
</a>
</nav>
<div class="mt-auto border-t border-outline-variant pt-4 space-y-1">
<button class="w-full mb-4 bg-primary text-on-primary font-bold py-2.5 rounded-lg flex items-center justify-center gap-2 hover:opacity-90 active:scale-95 transition-all">
<span class="material-symbols-outlined text-[18px]" data-icon="sync">sync</span>
                Sync Data
            </button>
<a class="text-on-surface-variant hover:bg-surface-container-highest flex items-center gap-3 px-4 py-2.5 rounded-xl" href="#">
<span class="material-symbols-outlined text-[20px]" data-icon="contact_support">contact_support</span>
<span class="font-body-md">Help Center</span>
</a>
<a class="text-on-surface-variant hover:bg-surface-container-highest flex items-center gap-3 px-4 py-2.5 rounded-xl" href="#">
<span class="material-symbols-outlined text-[20px]" data-icon="logout">logout</span>
<span class="font-body-md">Log Out</span>
</a>
</div>
</aside>
<!-- Main Content Area -->
<main class="ml-64 flex-1 h-screen flex flex-col">
<!-- TopAppBar -->
<header class="h-16 bg-surface-container-lowest dark:bg-surface-dim border-b border-outline-variant dark:border-outline flex justify-between items-center px-8 z-40 sticky top-0">
<div class="flex items-center gap-4 flex-1 max-w-xl">
<div class="relative w-full">
<span class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-on-surface-variant text-[20px]" data-icon="search">search</span>
<input class="w-full bg-surface-container-low border-none rounded-full pl-10 pr-4 py-2 text-body-md focus:ring-2 focus:ring-tertiary" placeholder="Search insights, products, campaigns..." type="text">
</div>
</div>
<div class="flex items-center gap-4">
<button class="flex items-center gap-2 px-3 py-1.5 rounded-lg border border-outline-variant hover:bg-surface-container-high transition-colors text-body-sm font-medium">
<span class="material-symbols-outlined text-[18px]" data-icon="calendar_today">calendar_today</span>
                    Date Range: Last 30 Days
                </button>
<div class="h-6 w-px bg-outline-variant mx-1"></div>
<button class="p-2 rounded-full hover:bg-surface-container-high relative">
<span class="material-symbols-outlined" data-icon="notifications">notifications</span>
<span class="absolute top-2 right-2 w-2 h-2 bg-error rounded-full border-2 border-white"></span>
</button>
<button class="p-2 rounded-full hover:bg-surface-container-high">
<span class="material-symbols-outlined" data-icon="help_outline">help_outline</span>
</button>
<div class="flex items-center gap-3 pl-2 border-l border-outline-variant">
<div class="text-right">
<p class="font-label-caps text-on-surface leading-tight">North America</p>
<p class="text-[10px] text-on-surface-variant font-medium">Apex Seller Account</p>
</div>
<img alt="User" class="w-8 h-8 rounded-full border border-outline" data-alt="A professional headshot of a business executive in a high-key, modern office setting. The person has a friendly but confident expression. The background is softly blurred with neutral corporate tones and bright, clean natural lighting from a nearby window, maintaining a light-mode aesthetic." src="https://lh3.googleusercontent.com/aida-public/AB6AXuDZ5t5fZnUWdoiJzOnc4OaHlG61tkKXYra9CEC1_NGuv1__RFhM6Whq3mUFGWRJwSbn26VK3rqUHuRyT6NOIJMo2T0cm88MZHYGYV-O4LUfEF3qwuUa0kyEYwSosb9gINjNmW12Hho0c7P3hGfJ3uosvIQVFiPCtJWqlqgJO4-d4ex7T2UDSJfJgEno3Zs8-9Z8kRz881XUUB_iya2qEPmMlYbv4JhV8ukAgzOGabPDIEAzWBwG37WL1_Ib2mVAKIWsWtx8WvLn">
</div>
</div>
</header>
<!-- Canvas Body -->
<div class="flex-1 overflow-y-auto bg-surface p-8">
<div class="max-w-max-width mx-auto space-y-6">
<!-- KPI Grid Section -->
<section>
<div class="flex items-center justify-between mb-4">
<h2 class="font-headline-sm text-headline-sm text-on-surface">Product Performance Overview</h2>
<span class="text-body-sm text-on-surface-variant">Real-time data from 2,491 items</span>
</div>
<div class="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-7 gap-3">
<!-- Primary KPIs -->
<div class="bg-surface-container-lowest border border-outline-variant p-3 rounded-lg hover:shadow-sm transition-all group">
<p class="font-label-caps text-on-surface-variant mb-1 uppercase">Impressions</p>
<p class="font-data-mono text-display-md text-on-surface tracking-tighter">1.2M</p>
<div class="flex items-center gap-1 mt-1 text-tertiary">
<span class="material-symbols-outlined text-[14px]" data-icon="trending_up">trending_up</span>
<span class="font-body-sm font-semibold">+12.4%</span>
</div>
</div>
<div class="bg-surface-container-lowest border border-outline-variant p-3 rounded-lg hover:shadow-sm transition-all group">
<p class="font-label-caps text-on-surface-variant mb-1 uppercase">Clicks</p>
<p class="font-data-mono text-display-md text-on-surface tracking-tighter">48.2K</p>
<div class="flex items-center gap-1 mt-1 text-tertiary">
<span class="material-symbols-outlined text-[14px]" data-icon="trending_up">trending_up</span>
<span class="font-body-sm font-semibold">+8.1%</span>
</div>
</div>
<div class="bg-surface-container-lowest border border-outline-variant p-3 rounded-lg hover:shadow-sm transition-all group">
<p class="font-label-caps text-on-surface-variant mb-1 uppercase">CTR</p>
<p class="font-data-mono text-display-md text-on-surface tracking-tighter">4.01%</p>
<div class="flex items-center gap-1 mt-1 text-error">
<span class="material-symbols-outlined text-[14px]" data-icon="trending_down">trending_down</span>
<span class="font-body-sm font-semibold">-0.4%</span>
</div>
</div>
<div class="bg-surface-container-lowest border border-outline-variant p-3 rounded-lg hover:shadow-sm transition-all group">
<p class="font-label-caps text-on-surface-variant mb-1 uppercase">CVR</p>
<p class="font-data-mono text-display-md text-on-surface tracking-tighter">12.5%</p>
<div class="flex items-center gap-1 mt-1 text-tertiary">
<span class="material-symbols-outlined text-[14px]" data-icon="trending_up">trending_up</span>
<span class="font-body-sm font-semibold">+2.1%</span>
</div>
</div>
<div class="bg-surface-container-lowest border border-outline-variant p-3 rounded-lg hover:shadow-sm transition-all group">
<p class="font-label-caps text-on-surface-variant mb-1 uppercase">CPC</p>
<p class="font-data-mono text-display-md text-on-surface tracking-tighter">$1.12</p>
<div class="flex items-center gap-1 mt-1 text-on-surface-variant">
<span class="material-symbols-outlined text-[14px]" data-icon="horizontal_rule">horizontal_rule</span>
<span class="font-body-sm font-semibold">0.0%</span>
</div>
</div>
<div class="bg-surface-container-lowest border border-outline-variant p-3 rounded-lg hover:shadow-sm transition-all group">
<p class="font-label-caps text-on-surface-variant mb-1 uppercase">Spend</p>
<p class="font-data-mono text-display-md text-on-surface tracking-tighter">$54.1K</p>
<div class="flex items-center gap-1 mt-1 text-error">
<span class="material-symbols-outlined text-[14px]" data-icon="trending_up">trending_up</span>
<span class="font-body-sm font-semibold">+15%</span>
</div>
</div>
<div class="bg-surface-container-lowest border border-outline-variant p-3 rounded-lg hover:shadow-sm transition-all group">
<p class="font-label-caps text-on-surface-variant mb-1 uppercase">Sales</p>
<p class="font-data-mono text-display-md text-on-surface tracking-tighter">$245K</p>
<div class="flex items-center gap-1 mt-1 text-tertiary">
<span class="material-symbols-outlined text-[14px]" data-icon="trending_up">trending_up</span>
<span class="font-body-sm font-semibold">+18%</span>
</div>
</div>
<!-- Secondary Row for specific Metrics -->
<div class="bg-surface-container-lowest border border-outline-variant p-3 rounded-lg hover:shadow-sm transition-all group">
<p class="font-label-caps text-on-surface-variant mb-1 uppercase">Orders</p>
<p class="font-data-mono text-display-md text-on-surface tracking-tighter">6,025</p>
</div>
<div class="bg-surface-container-lowest border border-outline-variant p-3 rounded-lg hover:shadow-sm transition-all group">
<p class="font-label-caps text-on-surface-variant mb-1 uppercase">Units</p>
<p class="font-data-mono text-display-md text-on-surface tracking-tighter">6,810</p>
</div>
<div class="bg-surface-container-lowest border border-outline-variant p-3 rounded-lg hover:shadow-sm transition-all group bg-primary-container/5">
<p class="font-label-caps text-primary mb-1 uppercase">ACOS</p>
<p class="font-data-mono text-display-md text-primary tracking-tighter">22.1%</p>
</div>
<div class="bg-surface-container-lowest border border-outline-variant p-3 rounded-lg hover:shadow-sm transition-all group">
<p class="font-label-caps text-on-surface-variant mb-1 uppercase">ROAS</p>
<p class="font-data-mono text-display-md text-on-surface tracking-tighter">4.52</p>
</div>
<div class="bg-surface-container-lowest border border-outline-variant p-3 rounded-lg hover:shadow-sm transition-all group">
<p class="font-label-caps text-on-surface-variant mb-1 uppercase">Spend % Split</p>
<p class="font-data-mono text-display-md text-on-surface tracking-tighter">32%</p>
</div>
<div class="bg-surface-container-lowest border border-outline-variant p-3 rounded-lg hover:shadow-sm transition-all group">
<p class="font-label-caps text-on-surface-variant mb-1 uppercase">Sales % Split</p>
<p class="font-data-mono text-display-md text-on-surface tracking-tighter">41%</p>
</div>
<div class="bg-surface-container-low border border-dashed border-outline-variant p-3 rounded-lg flex items-center justify-center opacity-60">
<span class="material-symbols-outlined text-on-surface-variant" data-icon="add">add</span>
</div>
</div>
</section>
<!-- Filter Bar -->
<section class="bg-surface-container-low p-4 rounded-xl flex items-center gap-4 border border-outline-variant shadow-sm">
<div class="flex-1 flex gap-2">
<div class="relative w-full max-w-sm">
<span class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-on-surface-variant text-[18px]" data-icon="search">search</span>
<input class="w-full h-10 bg-surface-container-lowest border border-outline-variant rounded-lg pl-10 pr-4 text-body-sm focus:border-tertiary focus:ring-1 focus:ring-tertiary outline-none" placeholder="Product Name, ASIN, SKU..." type="text">
</div>
<div class="relative min-w-[160px]">
<select class="w-full h-10 bg-surface-container-lowest border border-outline-variant rounded-lg pl-3 pr-10 text-body-sm appearance-none focus:border-tertiary focus:ring-1 focus:ring-tertiary outline-none">
<option>Tags Filter: All</option>
<option>Top Sellers</option>
<option>Low Inventory</option>
<option>High ACOS</option>
</select>
<span class="material-symbols-outlined absolute right-3 top-1/2 -translate-y-1/2 pointer-events-none text-on-surface-variant" data-icon="expand_more">expand_more</span>
</div><div class="relative min-w-[140px]"><span class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-on-surface-variant text-[18px]" data-icon="date_range">date_range</span><input class="w-full h-10 bg-surface-container-lowest border border-outline-variant rounded-lg pl-10 pr-3 text-body-sm focus:border-tertiary focus:ring-1 focus:ring-tertiary outline-none" max="52" min="1" placeholder="Compare (wks)" type="number" value="1"><p class="absolute -top-2 left-2 bg-surface-container-low px-1 text-[9px] font-bold text-on-surface-variant uppercase">Comp. Weeks</p></div>
</div>
<div class="flex items-center gap-2">
<button class="h-10 px-4 border border-outline-variant rounded-lg flex items-center gap-2 bg-surface-container-lowest text-body-sm font-medium hover:bg-surface-container-high transition-colors">
<span class="material-symbols-outlined text-[18px]" data-icon="filter_list">filter_list</span>
                            Columns
                        </button>
<button class="h-10 px-4 border border-outline-variant rounded-lg flex items-center gap-2 bg-surface-container-lowest text-body-sm font-medium hover:bg-surface-container-high transition-colors">
<span class="material-symbols-outlined text-[18px]" data-icon="download">download</span>
                            Export
                        </button>
</div>
</section>
<!-- High-Density Product Table -->
<section class="bg-surface-container-lowest rounded-xl border border-outline-variant shadow-sm overflow-hidden">
<div class="overflow-x-auto">
<table class="w-full text-left border-collapse">
<thead>
<tr class="bg-surface-container text-on-surface font-label-caps border-b border-outline-variant">
<th class="px-4 py-3 w-12"><input class="rounded border-outline-variant text-primary focus:ring-primary" type="checkbox"></th>
<th class="px-4 py-3 min-w-[280px]">Product Details</th>
<th class="px-4 py-3">Status</th>
<th class="px-4 py-3 text-right">Impressions</th>
<th class="px-4 py-3 text-right">Clicks</th>
<th class="px-4 py-3 text-right">Spend</th>
<th class="px-4 py-3 text-right">Sales</th>
<th class="px-4 py-3 text-right">ACOS</th>
<th class="px-4 py-3 text-right">ROAS</th>
<th class="px-4 py-3 w-10"></th>
</tr>
</thead>
<tbody class="divide-y divide-outline-variant">
<!-- Table Row 1 -->
<tr class="hover:bg-surface-container-low transition-colors h-14 group">
<td class="px-4 py-2"><input class="rounded border-outline-variant text-primary focus:ring-primary" type="checkbox"></td>
<td class="px-4 py-2">
<div class="flex items-center gap-3">
<div class="w-10 h-10 rounded bg-surface-container-high flex-shrink-0 overflow-hidden">
<img alt="Product" class="w-full h-full object-cover" data-alt="A close-up studio shot of a high-performance orange running shoe, presented on a minimalist platform with sharp, clean lighting. The product is the central focus against a neutral gray background, reflecting a modern, high-end e-commerce photography style with professional clarity and vibrant color accuracy." src="https://lh3.googleusercontent.com/aida-public/AB6AXuCY9Ov8Jg3JuN7P-CZkNMcfdAs4mRWe-X_SCjKDkb-RHjaFOKWtldiVtJkSJ5QDljfpWSBfSpF9aeL4gE_frVkY5Xz7f2ixd7g3Iuql0I_RFtijYTiFpLP4Uie3mTPYo9mFpY_uc1W9rsV-AmYpCVi_z0pw1s8A98ZvTC_yPrQ31_6fOk2WbnSMc0RYROW4xf5DTJRKZi5rCwRAKv4HuoJI6I3mHMVliEbXrjWajHmK47eNJrh69il7_aJ_lIuFcBFigiarsUn-">
</div>
<div class="overflow-hidden">
<p class="font-body-sm font-bold text-on-surface truncate">Apex Stealth Ultra-Light Running Shoes - V2 Pro Edition</p>
<p class="text-[10px] text-on-surface-variant font-data-mono">ASIN: B07N1J1K9 | SKU: SH-AST-01-OR</p>
</div>
</div>
</td>
<td class="px-4 py-2">
<span class="inline-flex items-center gap-1.5 px-2 py-0.5 rounded-full bg-tertiary/10 text-tertiary text-[10px] font-bold uppercase">
<span class="w-1.5 h-1.5 rounded-full bg-tertiary"></span>
                                            Active
                                        </span>
</td>
<td class="px-4 py-2 text-right font-data-mono text-body-sm">412,402<div class="flex items-center justify-end gap-1 text-[10px] text-tertiary mt-0.5"><span class="material-symbols-outlined text-[12px]" data-icon="arrow_drop_up">arrow_drop_up</span><span class="">12.4%</span></div></td>
<td class="px-4 py-2 text-right font-data-mono text-body-sm">18,291<div class="flex items-center justify-end gap-1 text-[10px] text-tertiary mt-0.5"><span class="material-symbols-outlined text-[12px]" data-icon="arrow_drop_up">arrow_drop_up</span><span class="">8.1%</span></div></td>
<td class="px-4 py-2 text-right font-data-mono text-body-sm font-semibold">$14,291.50<div class="flex items-center justify-end gap-1 text-[10px] text-error mt-0.5"><span class="material-symbols-outlined text-[12px]" data-icon="arrow_drop_up">arrow_drop_up</span><span class="">+ $1,864.12</span></div></td>
<td class="px-4 py-2 text-right font-data-mono text-body-sm font-semibold">$89,401.00<div class="flex items-center justify-end gap-1 text-[10px] text-tertiary mt-0.5"><span class="material-symbols-outlined text-[12px]" data-icon="arrow_drop_up">arrow_drop_up</span><span class="">+ $13,820.00</span></div></td>
<td class="px-4 py-2 text-right font-data-mono text-body-sm">
<span class="px-2 py-0.5 rounded bg-tertiary/10 text-tertiary font-bold">15.9%</span>
</td>
<td class="px-4 py-2 text-right font-data-mono text-body-sm">6.25</td>
<td class="px-4 py-2 text-right">
<button class="p-1 rounded hover:bg-surface-container-high opacity-0 group-hover:opacity-100 transition-opacity">
<span class="material-symbols-outlined text-[18px]" data-icon="more_vert">more_vert</span>
</button>
</td>
</tr>
<!-- Table Row 2 (Zebra) -->
<tr class="bg-surface-container-low/30 hover:bg-surface-container-low transition-colors h-14 group">
<td class="px-4 py-2"><input class="rounded border-outline-variant text-primary focus:ring-primary" type="checkbox"></td>
<td class="px-4 py-2">
<div class="flex items-center gap-3">
<div class="w-10 h-10 rounded bg-surface-container-high flex-shrink-0 overflow-hidden">
<img alt="Product" class="w-full h-full object-cover" data-alt="A sleek, professional-grade minimalist watch with a white face and silver band, photographed in a crisp, bright setting with soft diffuse lighting. The shot emphasizes the precision of the watch's craftsmanship. The environment is uncluttered, echoing a sophisticated corporate aesthetic with high-key lighting." src="https://lh3.googleusercontent.com/aida-public/AB6AXuDSiBVuHBUK3s699VNjY1yB18THeo67VGKWWX7BchofXDRETT1CjFp2Iu_YpHWXBosfywttElFSA9jo_dOOFl4_59lj0idaFe3c1WiiSeu7R98r3sOXcyLc4F9byQdYiLXAM7Wh-azQVJNokEuBz6ZwEmJVtCc9zPcYS26ZI00iqkw0wyHevkmhbasYjgiw3c2CZCyr5dYNrAchtSZCBMnMoJLFPMiX9UDy9X8UejWvtKUn5xKIlB28b9tetDSvPa2Abu-rQP5D">
</div>
<div class="overflow-hidden">
<p class="font-body-sm font-bold text-on-surface truncate">Zenith Chronograph - Minimalist Steel Series 40mm</p>
<p class="text-[10px] text-on-surface-variant font-data-mono">ASIN: B09M2P9X1 | SKU: WT-ZNC-ST-40</p>
</div>
</div>
</td>
<td class="px-4 py-2">
<span class="inline-flex items-center gap-1.5 px-2 py-0.5 rounded-full bg-surface-container-highest text-on-surface-variant text-[10px] font-bold uppercase">
<span class="w-1.5 h-1.5 rounded-full bg-on-surface-variant"></span>
                                            Paused
                                        </span>
</td>
<td class="px-4 py-2 text-right font-data-mono text-body-sm">82,109<div class="flex items-center justify-end gap-1 text-[10px] text-error mt-0.5"><span class="material-symbols-outlined text-[12px]" data-icon="arrow_drop_down">arrow_drop_down</span><span class="">5.2%</span></div></td>
<td class="px-4 py-2 text-right font-data-mono text-body-sm">2,310<div class="flex items-center justify-end gap-1 text-[10px] text-error mt-0.5"><span class="material-symbols-outlined text-[12px]" data-icon="arrow_drop_down">arrow_drop_down</span><span class="">2.1%</span></div></td>
<td class="px-4 py-2 text-right font-data-mono text-body-sm font-semibold">$2,105.20<div class="flex items-center justify-end gap-1 text-[10px] text-tertiary mt-0.5"><span class="material-symbols-outlined text-[12px]" data-icon="arrow_drop_down">arrow_drop_down</span><span class="">- $176.80</span></div></td>
<td class="px-4 py-2 text-right font-data-mono text-body-sm font-semibold">$5,402.00<div class="flex items-center justify-end gap-1 text-[10px] text-error mt-0.5"><span class="material-symbols-outlined text-[12px]" data-icon="arrow_drop_down">arrow_drop_down</span><span class="">- $654.00</span></div></td>
<td class="px-4 py-2 text-right font-data-mono text-body-sm">
<span class="px-2 py-0.5 rounded bg-error/10 text-error font-bold">38.9%</span>
</td>
<td class="px-4 py-2 text-right font-data-mono text-body-sm">2.57</td>
<td class="px-4 py-2 text-right">
<button class="p-1 rounded hover:bg-surface-container-high opacity-0 group-hover:opacity-100 transition-opacity">
<span class="material-symbols-outlined text-[18px]" data-icon="more_vert">more_vert</span>
</button>
</td>
</tr>
<!-- Table Row 3 -->
<tr class="hover:bg-surface-container-low transition-colors h-14 group">
<td class="px-4 py-2"><input class="rounded border-outline-variant text-primary focus:ring-primary" type="checkbox"></td>
<td class="px-4 py-2">
<div class="flex items-center gap-3">
<div class="w-10 h-10 rounded bg-surface-container-high flex-shrink-0 overflow-hidden">
<img alt="Product" class="w-full h-full object-cover" data-alt="Modern high-fidelity wireless headphones in a deep matte black finish, positioned on a sleek white desk with soft, focused accent lighting. The background is a clean, bright minimalist studio, creating a sophisticated product display that highlights ergonomic design and premium materials." src="https://lh3.googleusercontent.com/aida-public/AB6AXuCSKDEtFx2MuSKmmAxfno9VN7frde00BSkWXWXuVwceDPBxD8NTowsRw0IDIx_tcDDTGLkzkgshNKrwmgM5Uec8Q48yFIKwjlLgiVzmReZ6sFVSGEpNnfjLhEt3cErzBR3UxIQxLBfXbi2mESv7IhkKK14EhXSgqsgjmm6QB795VIyke5C6Vh__TGynvGawg-V9dljYpD-QVYC8OdbOvNY3Or-USp1cANzFR3vN_T3DNrum7u64UdVz0ukHQOkxWNwxZfIc3m3N">
</div>
<div class="overflow-hidden">
<p class="font-body-sm font-bold text-on-surface truncate">Sonic-Wave Noise Cancelling Wireless Headphones</p>
<p class="text-[10px] text-on-surface-variant font-data-mono">ASIN: B08K5L2R4 | SKU: AU-SWN-BK-WF</p>
</div>
</div>
</td>
<td class="px-4 py-2">
<span class="inline-flex items-center gap-1.5 px-2 py-0.5 rounded-full bg-tertiary/10 text-tertiary text-[10px] font-bold uppercase">
<span class="w-1.5 h-1.5 rounded-full bg-tertiary"></span>
                                            Active
                                        </span>
</td>
<td class="px-4 py-2 text-right font-data-mono text-body-sm">259,381</td>
<td class="px-4 py-2 text-right font-data-mono text-body-sm">9,482</td>
<td class="px-4 py-2 text-right font-data-mono text-body-sm font-semibold">$8,940.30</td>
<td class="px-4 py-2 text-right font-data-mono text-body-sm font-semibold">$42,910.00</td>
<td class="px-4 py-2 text-right font-data-mono text-body-sm">
<span class="px-2 py-0.5 rounded bg-tertiary/10 text-tertiary font-bold">20.8%</span>
</td>
<td class="px-4 py-2 text-right font-data-mono text-body-sm">4.80</td>
<td class="px-4 py-2 text-right">
<button class="p-1 rounded hover:bg-surface-container-high opacity-0 group-hover:opacity-100 transition-opacity">
<span class="material-symbols-outlined text-[18px]" data-icon="more_vert">more_vert</span>
</button>
</td>
</tr>
<!-- Table Row 4 -->
<tr class="bg-surface-container-low/30 hover:bg-surface-container-low transition-colors h-14 group">
<td class="px-4 py-2"><input class="rounded border-outline-variant text-primary focus:ring-primary" type="checkbox"></td>
<td class="px-4 py-2">
<div class="flex items-center gap-3">
<div class="w-10 h-10 rounded bg-surface-container-high flex-shrink-0 overflow-hidden">
<img alt="Product" class="w-full h-full object-cover" data-alt="Premium polarized sunglasses with a designer frame, resting on a reflective surface that catches soft, warm light. The image style is bright and luxury-focused, with a clean white backdrop. Professional lighting highlights the clarity of the lenses and the elegant texture of the frames, suggesting high quality and style." src="https://lh3.googleusercontent.com/aida-public/AB6AXuBEDT7d1jY13NMBijiQgHEHb86aiU2mJWT6Nj_Kqj6hu7BpI5-77wjP2YvIf5W33PpQ9GR_rB4IkAOWWm1jhvbfCto3Ogb8Wmtx1q1bcHaqOi4PQJWEz_YW3gh3YPHsRS3TTj4bnOGHDvcspZIDIQ7NvLom_4Pv97GYtdBeGkL8Da4ICZEgsz7JCs71B79aLoq-Ea0u9oZbnwOFO5GEsxDtimBvCaFkUPAK3_PjhYt1uIVAPgvT0MMPYq4PE5nat6ecd_sJKLYV">
</div>
<div class="overflow-hidden">
<p class="font-body-sm font-bold text-on-surface truncate">Vanguard Polarized Aviators - Classic Gold Series</p>
<p class="text-[10px] text-on-surface-variant font-data-mono">ASIN: B0CF9W2M8 | SKU: EY-VPA-GL-CL</p>
</div>
</div>
</td>
<td class="px-4 py-2">
<span class="inline-flex items-center gap-1.5 px-2 py-0.5 rounded-full bg-tertiary/10 text-tertiary text-[10px] font-bold uppercase">
<span class="w-1.5 h-1.5 rounded-full bg-tertiary"></span>
                                            Active
                                        </span>
</td>
<td class="px-4 py-2 text-right font-data-mono text-body-sm">114,028</td>
<td class="px-4 py-2 text-right font-data-mono text-body-sm">3,821</td>
<td class="px-4 py-2 text-right font-data-mono text-body-sm font-semibold">$3,109.80</td>
<td class="px-4 py-2 text-right font-data-mono text-body-sm font-semibold">$12,490.00</td>
<td class="px-4 py-2 text-right font-data-mono text-body-sm">
<span class="px-2 py-0.5 rounded bg-tertiary/10 text-tertiary font-bold">24.9%</span>
</td>
<td class="px-4 py-2 text-right font-data-mono text-body-sm">4.02</td>
<td class="px-4 py-2 text-right">
<button class="p-1 rounded hover:bg-surface-container-high opacity-0 group-hover:opacity-100 transition-opacity">
<span class="material-symbols-outlined text-[18px]" data-icon="more_vert">more_vert</span>
</button>
</td>
</tr>
</tbody>
</table>
</div>
<!-- Table Footer / Pagination -->
<div class="p-4 bg-surface-container flex justify-between items-center border-t border-outline-variant">
<div class="text-body-sm text-on-surface-variant">
                            Showing <span class="font-bold">1-4</span> of <span class="font-bold">2,491</span> products
                        </div>
<div class="flex items-center gap-2">
<button class="w-8 h-8 flex items-center justify-center rounded-lg hover:bg-surface-container-highest disabled:opacity-30" disabled="">
<span class="material-symbols-outlined" data-icon="chevron_left">chevron_left</span>
</button>
<button class="w-8 h-8 flex items-center justify-center rounded-lg bg-primary text-on-primary font-bold text-body-sm">1</button>
<button class="w-8 h-8 flex items-center justify-center rounded-lg hover:bg-surface-container-highest text-body-sm">2</button>
<button class="w-8 h-8 flex items-center justify-center rounded-lg hover:bg-surface-container-highest text-body-sm">3</button>
<span class="text-on-surface-variant">...</span>
<button class="w-8 h-8 flex items-center justify-center rounded-lg hover:bg-surface-container-highest text-body-sm">623</button>
<button class="w-8 h-8 flex items-center justify-center rounded-lg hover:bg-surface-container-highest">
<span class="material-symbols-outlined" data-icon="chevron_right">chevron_right</span>
</button>
</div>
</div>
</section>
<!-- Floating Insights Banner -->
<section class="bg-secondary-container dark:bg-secondary rounded-xl p-4 flex items-center gap-6 border border-outline-variant">
<div class="w-12 h-12 rounded-full bg-white/20 flex items-center justify-center text-on-secondary-container">
<span class="material-symbols-outlined text-[28px]" data-icon="auto_awesome">auto_awesome</span>
</div>
<div class="flex-1">
<h3 class="font-body-md font-bold text-on-secondary-container">AI Smart Recommendation</h3>
<p class="text-body-sm text-on-secondary-container/80">3 products in your "Running Shoes" category are losing Buy Box prominence. Increase bid for "Apex Stealth" to regain 15% estimated daily impressions.</p>
</div>
<button class="px-4 py-2 bg-on-secondary-container text-white font-bold rounded-lg text-body-sm hover:opacity-90 transition-opacity">
                        Apply Adjustments
                    </button>
</section>
</div>
</div>
</main>
<script>
        // Simple interactivity for demonstration
        document.querySelectorAll('tbody tr').forEach(row => {
            row.addEventListener('click', (e) => {
                if (e.target.tagName !== 'INPUT' && e.target.tagName !== 'BUTTON' && !e.target.closest('button')) {
                    // Simulation of row selection or detail view
                    console.log('Product selected:', row.querySelector('.font-bold').innerText);
                }
            });
        });
    </script>


</body></html>

<!-- Products - WoW Performance Comparison -->
<!DOCTYPE html><html class="light" lang="en"><head>
<meta charset="utf-8">
<meta content="width=device-width, initial-scale=1.0" name="viewport">
<title>Match Type Performance | PPC Insights</title>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&amp;family=JetBrains+Mono:wght@500&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<!-- Tailwind Configuration -->
<script id="tailwind-config">
      tailwind.config = {
        darkMode: "class",
        theme: {
          extend: {
            "colors": {
                "surface-bright": "#f8fafa",
                "on-error": "#ffffff",
                "on-tertiary": "#ffffff",
                "inverse-surface": "#2e3131",
                "background": "#f8fafa",
                "on-surface": "#191c1d",
                "error-container": "#ffdad6",
                "tertiary-fixed": "#adecff",
                "surface-tint": "#8a5100",
                "on-secondary": "#ffffff",
                "on-background": "#191c1d",
                "outline-variant": "#dbc2ad",
                "secondary-fixed": "#d7e3f7",
                "on-error-container": "#93000a",
                "secondary": "#535f70",
                "primary-container": "#ff9900",
                "on-tertiary-fixed-variant": "#004e5d",
                "error": "#ba1a1a",
                "on-primary-container": "#653a00",
                "on-secondary-container": "#576474",
                "on-primary": "#ffffff",
                "surface-variant": "#e1e3e3",
                "surface-container-low": "#f2f4f4",
                "on-primary-fixed": "#2c1600",
                "on-secondary-fixed-variant": "#3c4858",
                "outline": "#887361",
                "tertiary-container": "#6abdd3",
                "primary-fixed-dim": "#ffb86f",
                "surface": "#f8fafa",
                "surface-container-highest": "#e1e3e3",
                "primary": "#8a5100",
                "on-primary-fixed-variant": "#693c00",
                "inverse-primary": "#ffb86f",
                "surface-container-high": "#e6e8e8",
                "tertiary-fixed-dim": "#80d2e9",
                "surface-container-lowest": "#ffffff",
                "on-tertiary-container": "#004b59",
                "secondary-fixed-dim": "#bbc7db",
                "on-tertiary-fixed": "#001f26",
                "on-surface-variant": "#554434",
                "on-secondary-fixed": "#101c2b",
                "primary-fixed": "#ffdcbd",
                "inverse-on-surface": "#eff1f1",
                "surface-container": "#eceeee",
                "surface-dim": "#d8dada",
                "tertiary": "#00687a",
                "secondary-container": "#d4e1f5"
            },
            "borderRadius": {
                "DEFAULT": "0.125rem",
                "lg": "0.25rem",
                "xl": "0.5rem",
                "full": "0.75rem"
            },
            "spacing": {
                "unit": "4px",
                "margin-desktop": "32px",
                "margin-mobile": "16px",
                "max-width": "1440px",
                "container-padding": "24px",
                "gutter": "16px"
            },
            "fontFamily": {
                "label-caps": ["Inter"],
                "headline-sm": ["Inter"],
                "data-mono": ["JetBrains Mono"],
                "body-md": ["Inter"],
                "display-lg": ["Inter"],
                "body-lg": ["Inter"],
                "display-md": ["Inter"],
                "body-sm": ["Inter"]
            },
            "fontSize": {
                "label-caps": ["11px", {"lineHeight": "16px", "letterSpacing": "0.05em", "fontWeight": "700"}],
                "headline-sm": ["18px", {"lineHeight": "24px", "fontWeight": "600"}],
                "data-mono": ["13px", {"lineHeight": "18px", "fontWeight": "500"}],
                "body-md": ["14px", {"lineHeight": "20px", "fontWeight": "400"}],
                "display-lg": ["32px", {"lineHeight": "40px", "letterSpacing": "-0.02em", "fontWeight": "700"}],
                "body-lg": ["16px", {"lineHeight": "24px", "fontWeight": "400"}],
                "display-md": ["24px", {"lineHeight": "32px", "letterSpacing": "-0.01em", "fontWeight": "600"}],
                "body-sm": ["12px", {"lineHeight": "16px", "fontWeight": "400"}]
            }
          },
        },
      }
    </script>
<style>
        body {
            background-color: #f8fafa;
            color: #191c1d;
            font-family: 'Inter', sans-serif;
            -webkit-font-smoothing: antialiased;
        }
        .material-symbols-outlined {
            font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
        }
        .custom-scrollbar::-webkit-scrollbar {
            width: 4px;
        }
        .custom-scrollbar::-webkit-scrollbar-track {
            background: transparent;
        }
        .custom-scrollbar::-webkit-scrollbar-thumb {
            background: #e1e3e3;
            border-radius: 10px;
        }
        .zebra-row:nth-child(even) {
            background-color: #f2f4f4;
        }
        .card-shadow {
            border: 1px solid #E0E3E3;
        }
    </style>
</head>
<body class="flex min-h-screen">
<!-- SideNavBar -->
<aside class="h-screen w-64 fixed left-0 top-0 bg-surface-container-low border-r border-outline-variant flex flex-col py-6 px-4 gap-y-2 z-50">
<div class="mb-8 px-4">
<h1 class="font-headline-sm text-headline-sm font-bold text-primary">Ads Console</h1>
<p class="text-[10px] font-label-caps text-on-surface-variant uppercase tracking-widest">Seller Central API</p>
</div>
<nav class="flex-1 space-y-1 overflow-y-auto custom-scrollbar">
<a class="text-on-surface-variant hover:bg-surface-container-high flex items-center gap-3 px-4 py-3 rounded-xl transition-all" href="#">
<span class="material-symbols-outlined">dashboard</span>
<span class="font-body-md text-body-md">Dashboard</span>
</a>
<a class="text-on-surface-variant hover:bg-surface-container-high flex items-center gap-3 px-4 py-3 rounded-xl transition-all" href="#">
<span class="material-symbols-outlined">ads_click</span>
<span class="font-body-md text-body-md">Campaigns</span>
</a>
<a class="text-on-surface-variant hover:bg-surface-container-high flex items-center gap-3 px-4 py-3 rounded-xl transition-all" href="#">
<span class="material-symbols-outlined">inventory_2</span>
<span class="font-body-md text-body-md">Products</span>
</a>
<!-- Active State -->
<a class="bg-secondary-container text-on-secondary-container font-semibold rounded-xl flex items-center gap-3 px-4 py-3 transition-all" href="#">
<span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">target</span>
<span class="font-body-md text-body-md">Match Type</span>
</a>
<a class="text-on-surface-variant hover:bg-surface-container-high flex items-center gap-3 px-4 py-3 rounded-xl transition-all" href="#">
<span class="material-symbols-outlined">key</span>
<span class="font-body-md text-body-md">Keywords</span>
</a>
<a class="text-on-surface-variant hover:bg-surface-container-high flex items-center gap-3 px-4 py-3 rounded-xl transition-all" href="#">
<span class="material-symbols-outlined">search</span>
<span class="font-body-md text-body-md">Search Terms</span>
</a>
<a class="text-on-surface-variant hover:bg-surface-container-high flex items-center gap-3 px-4 py-3 rounded-xl transition-all" href="#">
<span class="material-symbols-outlined">dataset</span>
<span class="font-body-md text-body-md">ASIN Targets</span>
</a>
<a class="text-on-surface-variant hover:bg-surface-container-high flex items-center gap-3 px-4 py-3 rounded-xl transition-all" href="#">
<span class="material-symbols-outlined">conversion_path</span>
<span class="font-body-md text-body-md">ASIN from STR</span>
</a>
<a class="text-on-surface-variant hover:bg-surface-container-high flex items-center gap-3 px-4 py-3 rounded-xl transition-all" href="#">
<span class="material-symbols-outlined">smart_toy</span>
<span class="font-body-md text-body-md">Auto Campaigns</span>
</a>
<a class="text-on-surface-variant hover:bg-surface-container-high flex items-center gap-3 px-4 py-3 rounded-xl transition-all" href="#">
<span class="material-symbols-outlined">category</span>
<span class="font-body-md text-body-md">Category Targets</span>
</a>
<a class="text-on-surface-variant hover:bg-surface-container-high flex items-center gap-3 px-4 py-3 rounded-xl transition-all" href="#">
<span class="material-symbols-outlined">trending_down</span>
<span class="font-body-md text-body-md">Wasted Ad Spend</span>
</a>
</nav>
<div class="mt-auto pt-4 border-t border-outline-variant space-y-1">
<button class="w-full bg-primary text-white font-bold py-3 px-4 rounded-xl mb-4 hover:opacity-90 active:scale-95 transition-all">
                Sync Data
            </button>
<a class="text-on-surface-variant hover:bg-surface-container-high flex items-center gap-3 px-4 py-2 rounded-xl transition-all" href="#">
<span class="material-symbols-outlined">contact_support</span>
<span class="font-body-md text-body-md">Help Center</span>
</a>
<a class="text-on-surface-variant hover:bg-surface-container-high flex items-center gap-3 px-4 py-2 rounded-xl transition-all" href="#">
<span class="material-symbols-outlined">logout</span>
<span class="font-body-md text-body-md">Log Out</span>
</a>
</div>
</aside>
<!-- Main Content Area -->
<main class="flex-1 ml-64 flex flex-col">
<!-- TopAppBar -->
<header class="h-16 bg-surface-container-lowest border-b border-outline-variant sticky top-0 z-40 flex justify-between items-center px-margin-desktop w-full">
<div class="flex items-center gap-6 flex-1">
<div class="relative w-96">
<span class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-on-surface-variant">search</span>
<input class="w-full pl-10 pr-4 py-2 bg-surface-container-low border-none rounded-lg text-body-md focus:ring-2 focus:ring-tertiary transition-all" placeholder="Search campaigns or keywords..." type="text">
</div>
</div>
<div class="flex items-center gap-4">
<div class="flex items-center gap-2 px-3 py-2 bg-surface-container-low rounded-lg border border-outline-variant">
<span class="material-symbols-outlined text-on-surface-variant">calendar_today</span>
<span class="font-data-mono text-data-mono">Last 30 Days</span>
</div>
<div class="flex items-center gap-3 border-l border-outline-variant pl-4">
<button class="p-2 hover:bg-surface-container-high rounded-full transition-colors relative">
<span class="material-symbols-outlined">notifications</span>
<span class="absolute top-2 right-2 w-2 h-2 bg-primary rounded-full"></span>
</button>
<button class="p-2 hover:bg-surface-container-high rounded-full transition-colors">
<span class="material-symbols-outlined">help_outline</span>
</button>
<div class="flex items-center gap-3 ml-2 cursor-pointer hover:bg-surface-container-high p-1 rounded-lg transition-all">
<div class="text-right hidden xl:block">
<p class="font-label-caps text-label-caps text-on-surface leading-none">Apex Seller Account</p>
<p class="font-body-sm text-body-sm text-on-surface-variant">North America</p>
</div>
<img alt="User profile" class="w-8 h-8 rounded-full border border-outline-variant" data-alt="A professional studio headshot of a business executive with a friendly expression. The lighting is bright and even, against a clean, modern workspace background with neutral gray and white tones. The overall aesthetic is corporate, precise, and high-quality." src="https://lh3.googleusercontent.com/aida-public/AB6AXuBqsVTvcGVM3QuCVKe1JUrxryknFohjzd-6lOQ_-rzIq1ViqSxmgIgMO_zXwDJQN-M6XW0ZeTw-DzO9DWqlIPlqHdjTCZ_Iyor-BBcY872UVw7uC2WJi74Naj0QcvRVc3a3LAqcUIosACjtEfG3u2oSgt-Zw-ZC4Pbl0GhVnyf4azSEkzmbsLnnduT_lYdJqwKdII_KrZgpJ2FKh23Vj7bcSqaMd-e7LDEeyNjnwdb7fLs6yZ4HisS_qeNWETEeOX5m12irrRMF">
</div>
</div>
</div>
</header>
<!-- Page Content -->
<div class="p-margin-desktop space-y-8 max-w-max-width mx-auto w-full">
<!-- Header Section -->
<div class="flex justify-between items-end">
<div>
<h2 class="font-display-lg text-display-lg text-on-surface">Match Type Performance Overview</h2>
<p class="font-body-md text-body-md text-on-surface-variant mt-1">Real-time data from all active and historical campaigns across all marketplaces.</p>
</div>
<div class="flex gap-2">
<button class="flex items-center gap-2 px-4 py-2 border border-outline text-on-surface-variant font-semibold rounded-lg hover:bg-surface-container-high transition-all">
<span class="material-symbols-outlined">download</span> Export
                    </button>
<button class="flex items-center gap-2 px-4 py-2 bg-[#007185] text-white font-semibold rounded-lg hover:opacity-90 transition-all">
<span class="material-symbols-outlined">sync</span> Refresh Data
                    </button>
</div>
</div>
<!-- Metric Summary Grid (13 Cards) -->
<div class="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-7 xl:grid-cols-13 gap-2">
<!-- Card Template -->
<div class="bg-surface-container-lowest p-4 card-shadow rounded-lg">
<p class="font-label-caps text-label-caps text-on-surface-variant uppercase mb-2">Impressions</p>
<p class="font-display-md text-display-md text-on-surface">1.2M</p>
<p class="flex items-center gap-1 font-data-mono text-[10px] text-green-600 mt-1">
<span class="material-symbols-outlined text-[12px]">trending_up</span> 12%
                    </p>
</div>
<div class="bg-surface-container-lowest p-4 card-shadow rounded-lg">
<p class="font-label-caps text-label-caps text-on-surface-variant uppercase mb-2">Clicks</p>
<p class="font-display-md text-display-md text-on-surface">45.2K</p>
<p class="flex items-center gap-1 font-data-mono text-[10px] text-green-600 mt-1">
<span class="material-symbols-outlined text-[12px]">trending_up</span> 8.4%
                    </p>
</div>
<div class="bg-surface-container-lowest p-4 card-shadow rounded-lg">
<p class="font-label-caps text-label-caps text-on-surface-variant uppercase mb-2">CTR</p>
<p class="font-display-md text-display-md text-on-surface">3.76%</p>
<p class="flex items-center gap-1 font-data-mono text-[10px] text-red-600 mt-1">
<span class="material-symbols-outlined text-[12px]">trending_down</span> 0.2%
                    </p>
</div>
<div class="bg-surface-container-lowest p-4 card-shadow rounded-lg">
<p class="font-label-caps text-label-caps text-on-surface-variant uppercase mb-2">CVR</p>
<p class="font-display-md text-display-md text-on-surface">12.4%</p>
<p class="flex items-center gap-1 font-data-mono text-[10px] text-green-600 mt-1">
<span class="material-symbols-outlined text-[12px]">trending_up</span> 1.1%
                    </p>
</div>
<div class="bg-surface-container-lowest p-4 card-shadow rounded-lg">
<p class="font-label-caps text-label-caps text-on-surface-variant uppercase mb-2">CPC</p>
<p class="font-display-md text-display-md text-on-surface">$0.92</p>
<p class="flex items-center gap-1 font-data-mono text-[10px] text-red-600 mt-1">
<span class="material-symbols-outlined text-[12px]">trending_up</span> $0.05
                    </p>
</div>
<div class="bg-surface-container-lowest p-4 card-shadow rounded-lg">
<p class="font-label-caps text-label-caps text-on-surface-variant uppercase mb-2">Spend</p>
<p class="font-display-md text-display-md text-on-surface">$41.5K</p>
<p class="flex items-center gap-1 font-data-mono text-[10px] text-red-600 mt-1">
<span class="material-symbols-outlined text-[12px]">trending_up</span> $2.1K
                    </p>
</div>
<div class="bg-surface-container-lowest p-4 card-shadow rounded-lg">
<p class="font-label-caps text-label-caps text-on-surface-variant uppercase mb-2">Sales</p>
<p class="font-display-md text-display-md text-on-surface">$182K</p>
<p class="flex items-center gap-1 font-data-mono text-[10px] text-green-600 mt-1">
<span class="material-symbols-outlined text-[12px]">trending_up</span> $15K
                    </p>
</div>
<div class="bg-surface-container-lowest p-4 card-shadow rounded-lg">
<p class="font-label-caps text-label-caps text-on-surface-variant uppercase mb-2">Orders</p>
<p class="font-display-md text-display-md text-on-surface">5,604</p>
<p class="flex items-center gap-1 font-data-mono text-[10px] text-green-600 mt-1">
<span class="material-symbols-outlined text-[12px]">trending_up</span> 422
                    </p>
</div>
<div class="bg-surface-container-lowest p-4 card-shadow rounded-lg">
<p class="font-label-caps text-label-caps text-on-surface-variant uppercase mb-2">Units</p>
<p class="font-display-md text-display-md text-on-surface">6,120</p>
<p class="flex items-center gap-1 font-data-mono text-[10px] text-green-600 mt-1">
<span class="material-symbols-outlined text-[12px]">trending_up</span> 480
                    </p>
</div>
<div class="bg-surface-container-lowest p-4 card-shadow rounded-lg">
<p class="font-label-caps text-label-caps text-on-surface-variant uppercase mb-2">ACOS</p>
<p class="font-display-md text-display-md text-on-surface">22.8%</p>
<p class="flex items-center gap-1 font-data-mono text-[10px] text-green-600 mt-1">
<span class="material-symbols-outlined text-[12px]">trending_down</span> 2.4%
                    </p>
</div>
<div class="bg-surface-container-lowest p-4 card-shadow rounded-lg">
<p class="font-label-caps text-label-caps text-on-surface-variant uppercase mb-2">ROAS</p>
<p class="font-display-md text-display-md text-on-surface">4.38</p>
<p class="flex items-center gap-1 font-data-mono text-[10px] text-green-600 mt-1">
<span class="material-symbols-outlined text-[12px]">trending_up</span> 0.42
                    </p>
</div>
<div class="bg-surface-container-lowest p-4 card-shadow rounded-lg">
<p class="font-label-caps text-label-caps text-on-surface-variant uppercase mb-2">Spend %</p>
<p class="font-display-md text-display-md text-on-surface">100%</p>
<p class="flex items-center gap-1 font-data-mono text-[10px] text-on-surface-variant mt-1">
                        Baseline
                    </p>
</div>
<div class="bg-surface-container-lowest p-4 card-shadow rounded-lg">
<p class="font-label-caps text-label-caps text-on-surface-variant uppercase mb-2">Sales %</p>
<p class="font-display-md text-display-md text-on-surface">100%</p>
<p class="flex items-center gap-1 font-data-mono text-[10px] text-on-surface-variant mt-1">
                        Baseline
                    </p>
</div>
</div>
<!-- Main Data Section -->
<div class="bg-surface-container-lowest card-shadow rounded-xl overflow-hidden" style="transform: translateY(0px); transition: 0.2s;">
<!-- Filter Bar -->
<div class="px-6 py-4 flex flex-col md:flex-row gap-4 items-center justify-between border-b border-outline-variant bg-surface-container-low/50">
<div class="flex flex-1 gap-4 w-full">
<div class="relative flex-1 max-w-md">
<span class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-on-surface-variant text-sm">search</span>
<input class="w-full pl-9 pr-4 py-2 border border-outline-variant rounded-lg text-body-md bg-white focus:ring-1 focus:ring-primary outline-none transition-all" placeholder="Filter by Campaign or Targeting Name..." type="text">
</div>
<div class="relative">
<select class="appearance-none pl-4 pr-10 py-2 border border-outline-variant rounded-lg text-body-md bg-white focus:ring-1 focus:ring-primary outline-none transition-all">
<option value="all">All Match Types</option>
<option value="exact">Exact</option>
<option value="phrase">Phrase</option>
<option value="broad">Broad</option>
<option value="auto">Auto</option>
</select>
<span class="material-symbols-outlined absolute right-3 top-1/2 -translate-y-1/2 pointer-events-none text-on-surface-variant">expand_more</span>
</div>
</div>
<div class="flex items-center gap-3">
<span class="text-body-sm font-semibold text-on-surface-variant">Viewing: 1-4 of 4 match types</span>
<div class="flex gap-1">
<button class="p-1 border border-outline-variant rounded hover:bg-surface-container-high transition-colors disabled:opacity-50" disabled="">
<span class="material-symbols-outlined">chevron_left</span>
</button>
<button class="p-1 border border-outline-variant rounded hover:bg-surface-container-high transition-colors">
<span class="material-symbols-outlined">chevron_right</span>
</button>
</div>
</div>
</div>
<!-- Data Table -->
<div class="overflow-x-auto">
<table class="w-full text-left border-collapse">
<thead>
<tr class="bg-surface-container-low">
<th class="px-6 py-3 font-label-caps text-label-caps text-on-surface-variant border-b border-outline-variant uppercase">Match Type</th>
<th class="px-6 py-3 font-label-caps text-label-caps text-on-surface-variant border-b border-outline-variant uppercase">Status</th>
<th class="px-6 py-3 font-label-caps text-label-caps text-on-surface-variant border-b border-outline-variant uppercase text-right">Impressions</th>
<th class="px-6 py-3 font-label-caps text-label-caps text-on-surface-variant border-b border-outline-variant uppercase text-right">Clicks</th>
<th class="px-6 py-3 font-label-caps text-label-caps text-on-surface-variant border-b border-outline-variant uppercase text-right">Spend (WoW)</th>
<th class="px-6 py-3 font-label-caps text-label-caps text-on-surface-variant border-b border-outline-variant uppercase text-right">Sales (WoW)</th>
<th class="px-6 py-3 font-label-caps text-label-caps text-on-surface-variant border-b border-outline-variant uppercase text-right">ACOS</th>
<th class="px-6 py-3 font-label-caps text-label-caps text-on-surface-variant border-b border-outline-variant uppercase text-right">ROAS</th>
<th class="px-6 py-3 font-label-caps text-label-caps text-on-surface-variant border-b border-outline-variant uppercase text-center">Trend</th>
</tr>
</thead>
<tbody class="divide-y divide-outline-variant">
<!-- Exact Row -->
<tr class="zebra-row hover:bg-surface-container-high transition-colors group">
<td class="px-6 py-4">
<div class="flex items-center gap-3">
<div class="w-8 h-8 rounded bg-blue-100 flex items-center justify-center text-blue-700">
<span class="material-symbols-outlined text-[18px]" style="font-variation-settings: 'FILL' 1;">bolt</span>
</div>
<div>
<p class="font-body-md font-bold text-on-surface">Exact Match</p>
<p class="text-[10px] text-on-surface-variant">High Precision / Fixed Bids</p>
</div>
</div>
</td>
<td class="px-6 py-4">
<span class="px-2 py-1 rounded-full bg-green-100 text-green-700 text-[10px] font-bold uppercase">Active</span>
</td>
<td class="px-6 py-4 text-right font-data-mono text-data-mono">420,532</td>
<td class="px-6 py-4 text-right font-data-mono text-data-mono">18,245</td>
<td class="px-6 py-4 text-right">
<div class="font-data-mono text-data-mono">$15,420.00</div>
<div class="text-[10px] text-red-600">+$840.50</div>
</td>
<td class="px-6 py-4 text-right">
<div class="font-data-mono text-data-mono">$84,320.00</div>
<div class="text-[10px] text-green-600">+$12,450.00</div>
</td>
<td class="px-6 py-4 text-right">
<div class="font-data-mono text-data-mono">18.28%</div>
<div class="w-full bg-surface-container-high h-1 rounded-full mt-1 overflow-hidden">
<div class="bg-green-500 h-full w-[18%]"></div>
</div>
</td>
<td class="px-6 py-4 text-right font-data-mono text-data-mono">5.47</td>
<td class="px-6 py-4">
<div class="flex justify-center">
<canvas class="w-20 h-8 sparkline" data-values="10,12,11,14,16,15,18"></canvas>
</div>
</td>
</tr>
<!-- Phrase Row -->
<tr class="zebra-row hover:bg-surface-container-high transition-colors group">
<td class="px-6 py-4">
<div class="flex items-center gap-3">
<div class="w-8 h-8 rounded bg-purple-100 flex items-center justify-center text-purple-700">
<span class="material-symbols-outlined text-[18px]" style="font-variation-settings: 'FILL' 1;">format_quote</span>
</div>
<div>
<p class="font-body-md font-bold text-on-surface">Phrase Match</p>
<p class="text-[10px] text-on-surface-variant">Core Variation / Balanced</p>
</div>
</div>
</td>
<td class="px-6 py-4">
<span class="px-2 py-1 rounded-full bg-green-100 text-green-700 text-[10px] font-bold uppercase">Active</span>
</td>
<td class="px-6 py-4 text-right font-data-mono text-data-mono">312,110</td>
<td class="px-6 py-4 text-right font-data-mono text-data-mono">12,402</td>
<td class="px-6 py-4 text-right">
<div class="font-data-mono text-data-mono">$12,180.00</div>
<div class="text-[10px] text-green-600">-$210.30</div>
</td>
<td class="px-6 py-4 text-right">
<div class="font-data-mono text-data-mono">$48,220.00</div>
<div class="text-[10px] text-red-600">-$1,100.00</div>
</td>
<td class="px-6 py-4 text-right">
<div class="font-data-mono text-data-mono">25.26%</div>
<div class="w-full bg-surface-container-high h-1 rounded-full mt-1 overflow-hidden">
<div class="bg-yellow-500 h-full w-[25%]"></div>
</div>
</td>
<td class="px-6 py-4 text-right font-data-mono text-data-mono">3.96</td>
<td class="px-6 py-4">
<div class="flex justify-center">
<canvas class="w-20 h-8 sparkline" data-values="15,14,13,12,13,11,10"></canvas>
</div>
</td>
</tr>
<!-- Broad Row -->
<tr class="zebra-row hover:bg-surface-container-high transition-colors group">
<td class="px-6 py-4">
<div class="flex items-center gap-3">
<div class="w-8 h-8 rounded bg-orange-100 flex items-center justify-center text-orange-700">
<span class="material-symbols-outlined text-[18px]" style="font-variation-settings: 'FILL' 1;">explore</span>
</div>
<div>
<p class="font-body-md font-bold text-on-surface">Broad Match</p>
<p class="text-[10px] text-on-surface-variant">Discovery / High Volume</p>
</div>
</div>
</td>
<td class="px-6 py-4">
<span class="px-2 py-1 rounded-full bg-green-100 text-green-700 text-[10px] font-bold uppercase">Active</span>
</td>
<td class="px-6 py-4 text-right font-data-mono text-data-mono">380,421</td>
<td class="px-6 py-4 text-right font-data-mono text-data-mono">11,040</td>
<td class="px-6 py-4 text-right">
<div class="font-data-mono text-data-mono">$10,480.00</div>
<div class="text-[10px] text-red-600">+$1,420.00</div>
</td>
<td class="px-6 py-4 text-right">
<div class="font-data-mono text-data-mono">$36,840.00</div>
<div class="text-[10px] text-green-600">+$4,210.00</div>
</td>
<td class="px-6 py-4 text-right">
<div class="font-data-mono text-data-mono">28.45%</div>
<div class="w-full bg-surface-container-high h-1 rounded-full mt-1 overflow-hidden">
<div class="bg-orange-500 h-full w-[28%]"></div>
</div>
</td>
<td class="px-6 py-4 text-right font-data-mono text-data-mono">3.52</td>
<td class="px-6 py-4">
<div class="flex justify-center">
<canvas class="w-20 h-8 sparkline" data-values="8,10,9,12,11,14,13"></canvas>
</div>
</td>
</tr>
<!-- Auto Row -->

</tbody>
</table>
</div>
<!-- Footer Stats -->
<div class="px-6 py-4 bg-surface-container-low border-t border-outline-variant flex justify-end gap-12">
<div class="text-right">
<p class="text-[10px] font-label-caps text-on-surface-variant uppercase">Total Spend</p>
<p class="font-display-md text-display-md text-on-surface">$41,500.00</p>
</div>
<div class="text-right">
<p class="text-[10px] font-label-caps text-on-surface-variant uppercase">Total Sales</p>
<p class="font-display-md text-display-md text-on-surface">$182,000.00</p>
</div>
<div class="text-right">
<p class="text-[10px] font-label-caps text-on-surface-variant uppercase">Avg. ACOS</p>
<p class="font-display-md text-display-md text-primary">22.8%</p>
</div>
</div>
</div>
</div>
</main>
<script>
        // Simple Sparkline Drawer
        document.querySelectorAll('.sparkline').forEach(canvas => {
            const ctx = canvas.getContext('2d');
            const values = canvas.dataset.values.split(',').map(Number);
            const width = canvas.width;
            const height = canvas.height;
            const padding = 2;
            
            const max = Math.max(...values);
            const min = Math.min(...values);
            const range = max - min || 1;
            
            ctx.beginPath();
            ctx.lineWidth = 2;
            ctx.lineJoin = 'round';
            ctx.lineCap = 'round';
            
            // Check trend for color
            const first = values[0];
            const last = values[values.length - 1];
            ctx.strokeStyle = last >= first ? '#16a34a' : '#dc2626';

            values.forEach((val, i) => {
                const x = padding + (i / (values.length - 1)) * (width - padding * 2);
                const y = (height - padding * 2) - ((val - min) / range) * (height - padding * 2) + padding;
                
                if (i === 0) ctx.moveTo(x, y);
                else ctx.lineTo(x, y);
            });
            
            ctx.stroke();
            
            // Gradient Fill
            ctx.lineTo(width - padding, height);
            ctx.lineTo(padding, height);
            ctx.closePath();
            const gradient = ctx.createLinearGradient(0, 0, 0, height);
            gradient.addColorStop(0, last >= first ? 'rgba(22, 163, 74, 0.1)' : 'rgba(220, 38, 38, 0.1)');
            gradient.addColorStop(1, 'transparent');
            ctx.fillStyle = gradient;
            ctx.fill();
        });

        // Interactive states for metric cards
        document.querySelectorAll('.card-shadow').forEach(card => {
            card.addEventListener('mouseenter', () => {
                card.classList.add('shadow-sm');
                card.style.transform = 'translateY(-2px)';
                card.style.transition = 'all 0.2s ease';
            });
            card.addEventListener('mouseleave', () => {
                card.classList.remove('shadow-sm');
                card.style.transform = 'translateY(0)';
            });
        });
    </script>


</body></html>

<!-- Match Type - Performance Management -->
<!DOCTYPE html>

<html class="light" lang="en"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>AdTracker Pro - Keywords Performance</title>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&amp;family=JetBrains+Mono:wght@500&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<script id="tailwind-config">
      tailwind.config = {
        darkMode: "class",
        theme: {
          extend: {
            "colors": {
                    "error": "#ba1a1a",
                    "on-tertiary": "#ffffff",
                    "on-secondary-container": "#576474",
                    "tertiary-fixed": "#adecff",
                    "primary": "#8a5100",
                    "secondary-fixed-dim": "#bbc7db",
                    "on-primary-container": "#653a00",
                    "surface-dim": "#d8dada",
                    "surface-container-lowest": "#ffffff",
                    "inverse-surface": "#2e3131",
                    "on-primary-fixed-variant": "#693c00",
                    "surface-tint": "#8a5100",
                    "surface-container-high": "#e6e8e8",
                    "on-secondary-fixed-variant": "#3c4858",
                    "on-tertiary-container": "#004b59",
                    "tertiary-fixed-dim": "#80d2e9",
                    "on-surface-variant": "#554434",
                    "on-surface": "#191c1d",
                    "on-error-container": "#93000a",
                    "surface": "#f8fafa",
                    "on-tertiary-fixed": "#001f26",
                    "surface-bright": "#f8fafa",
                    "on-primary": "#ffffff",
                    "on-secondary": "#ffffff",
                    "inverse-on-surface": "#eff1f1",
                    "surface-variant": "#e1e3e3",
                    "inverse-primary": "#ffb86f",
                    "on-error": "#ffffff",
                    "tertiary-container": "#6abdd3",
                    "on-primary-fixed": "#2c1600",
                    "secondary-fixed": "#d7e3f7",
                    "surface-container-highest": "#e1e3e3",
                    "tertiary": "#00687a",
                    "secondary-container": "#d4e1f5",
                    "primary-fixed-dim": "#ffb86f",
                    "primary-fixed": "#ffdcbd",
                    "secondary": "#535f70",
                    "background": "#f8fafa",
                    "surface-container": "#eceeee",
                    "primary-container": "#ff9900",
                    "on-secondary-fixed": "#101c2b",
                    "error-container": "#ffdad6",
                    "on-background": "#191c1d",
                    "surface-container-low": "#f2f4f4",
                    "on-tertiary-fixed-variant": "#004e5d",
                    "outline-variant": "#dbc2ad",
                    "outline": "#887361"
            },
            "borderRadius": {
                    "DEFAULT": "0.125rem",
                    "lg": "0.25rem",
                    "xl": "0.5rem",
                    "full": "0.75rem"
            },
            "spacing": {
                    "margin-mobile": "16px",
                    "unit": "4px",
                    "gutter": "16px",
                    "container-padding": "24px",
                    "max-width": "1440px",
                    "margin-desktop": "32px"
            },
            "fontFamily": {
                    "body-md": ["Inter"],
                    "data-mono": ["JetBrains Mono"],
                    "body-lg": ["Inter"],
                    "display-md": ["Inter"],
                    "display-lg": ["Inter"],
                    "label-caps": ["Inter"],
                    "headline-sm": ["Inter"],
                    "body-sm": ["Inter"]
            },
            "fontSize": {
                    "body-md": ["14px", {"lineHeight": "20px", "fontWeight": "400"}],
                    "data-mono": ["13px", {"lineHeight": "18px", "fontWeight": "500"}],
                    "body-lg": ["16px", {"lineHeight": "24px", "fontWeight": "400"}],
                    "display-md": ["24px", {"lineHeight": "32px", "letterSpacing": "-0.01em", "fontWeight": "600"}],
                    "display-lg": ["32px", {"lineHeight": "40px", "letterSpacing": "-0.02em", "fontWeight": "700"}],
                    "label-caps": ["11px", {"lineHeight": "16px", "letterSpacing": "0.05em", "fontWeight": "700"}],
                    "headline-sm": ["18px", {"lineHeight": "24px", "fontWeight": "600"}],
                    "body-sm": ["12px", {"lineHeight": "16px", "fontWeight": "400"}]
            }
          },
        },
      }
    </script>
<style>
        .material-symbols-outlined {
            font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
            vertical-align: middle;
        }
        .zebra-table tr:nth-child(even) {
            background-color: #f8fafa;
        }
        .custom-scrollbar::-webkit-scrollbar {
            width: 6px;
            height: 6px;
        }
        .custom-scrollbar::-webkit-scrollbar-thumb {
            background: #dbc2ad;
            border-radius: 10px;
        }
        .custom-scrollbar::-webkit-scrollbar-track {
            background: transparent;
        }
    </style>
</head>
<body class="bg-background text-on-surface font-body-md overflow-hidden">
<!-- TopNavBar -->
<header class="fixed top-0 left-0 right-0 z-50 flex items-center justify-between px-margin-desktop h-16 bg-surface border-b border-outline-variant">
<div class="flex items-center gap-8">
<span class="font-display-md text-display-md font-bold text-primary">AdTracker Pro</span>
<div class="relative hidden md:block">
<span class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-on-secondary-container">search</span>
<input class="pl-10 pr-4 py-2 bg-surface-container-low border border-outline-variant rounded-lg w-96 text-body-md focus:outline-none focus:ring-2 focus:ring-tertiary/20" placeholder="Search keywords..." type="text"/>
</div>
</div>
<div class="flex items-center gap-4">
<button class="p-2 hover:bg-surface-container-low transition-colors rounded-full text-on-secondary-container">
<span class="material-symbols-outlined">notifications</span>
</button>
<button class="p-2 hover:bg-surface-container-low transition-colors rounded-full text-on-secondary-container">
<span class="material-symbols-outlined">settings</span>
</button>
<button class="p-2 hover:bg-surface-container-low transition-colors rounded-full text-on-secondary-container">
<span class="material-symbols-outlined">help</span>
</button>
<div class="h-8 w-[1px] bg-outline-variant mx-2"></div>
<div class="flex items-center gap-2 cursor-pointer active:opacity-80">
<img alt="User Avatar" class="h-8 w-8 rounded-full object-cover" data-alt="A professional headshot of a smiling male executive with clean-cut features and professional attire, shot against a soft-focus office background with high-key corporate lighting. The aesthetic is clean, sharp, and optimistic, matching a high-end SaaS dashboard interface with a neutral and warm tone." src="https://lh3.googleusercontent.com/aida-public/AB6AXuAtp0wi8ymRQxt1iA7mrfw4pndXLp68JD5UQUY0lXNw3pQtPfJ3z7933rWfRgR0-ahHacSOc4GQ9Yui9XQDTPg3HChbDeIF3H8iVGJRV2xYO4DEERQEaY8EA7D0wLL_crLWKWlYSA5eLa1UYdYf_s2O9eI26gBU0fjMo8v489drHcwIgA_njogGe1M00e0gCbd3Kb4MkGvoGiG4t4aO4no9NYzjWDv7GoBmRHX33JDQx2r9tYksomd0QnibQE25CxL7A6XNM1_e"/>
<span class="font-body-md text-on-surface-variant font-medium">Account Selector</span>
<span class="material-symbols-outlined text-on-secondary-container">expand_more</span>
</div>
</div>
</header>
<!-- SideNavBar -->
<aside class="fixed left-0 top-16 bottom-0 w-64 bg-white border-r border-outline-variant flex flex-col h-full py-4 overflow-y-auto">
<div class="px-6 py-4 border-b border-outline-variant mb-4">
<div class="flex items-center gap-3">
<div class="w-10 h-10 bg-primary-fixed flex items-center justify-center rounded-lg shadow-sm">
<span class="material-symbols-outlined text-primary" style="font-variation-settings: 'FILL' 1;">storefront</span>
</div>
<div class="flex flex-col">
<span class="font-headline-sm text-headline-sm text-on-surface">Brand Performance</span>
<span class="text-[10px] text-on-secondary-container font-bold tracking-widest uppercase">Professional Seller</span>
</div>
</div>
</div>
<nav class="flex-1 px-3 space-y-1">
<div class="flex items-center gap-3 px-4 py-2 my-1 rounded-lg text-on-secondary-container hover:bg-surface-container-low transition-all cursor-pointer">
<span class="material-symbols-outlined">dashboard</span>
<span class="font-label-caps text-label-caps">Dashboard</span>
</div>
<div class="flex items-center gap-3 px-4 py-2 my-1 rounded-lg text-on-secondary-container hover:bg-surface-container-low transition-all cursor-pointer">
<span class="material-symbols-outlined">campaign</span>
<span class="font-label-caps text-label-caps">Campaigns</span>
</div>
<div class="flex items-center gap-3 px-4 py-2 my-1 rounded-lg text-on-secondary-container hover:bg-surface-container-low transition-all cursor-pointer">
<span class="material-symbols-outlined">inventory_2</span>
<span class="font-label-caps text-label-caps">Products</span>
</div>
<div class="flex items-center gap-3 px-4 py-2 my-1 rounded-lg text-on-secondary-container hover:bg-surface-container-low transition-all cursor-pointer">
<span class="material-symbols-outlined">analytics</span>
<span class="font-label-caps text-label-caps">Match Type</span>
</div>
<!-- ACTIVE TAB -->
<div class="flex items-center gap-3 px-4 py-2 my-1 rounded-lg bg-secondary-container text-on-secondary-container font-bold transition-all cursor-pointer">
<span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">key</span>
<span class="font-label-caps text-label-caps">Keywords</span>
</div>
<div class="flex items-center gap-3 px-4 py-2 my-1 rounded-lg text-on-secondary-container hover:bg-surface-container-low transition-all cursor-pointer">
<span class="material-symbols-outlined">search</span>
<span class="font-label-caps text-label-caps">Search Terms</span>
</div>
<div class="flex items-center gap-3 px-4 py-2 my-1 rounded-lg text-on-secondary-container hover:bg-surface-container-low transition-all cursor-pointer">
<span class="material-symbols-outlined">target</span>
<span class="font-label-caps text-label-caps">ASIN Targets</span>
</div>
<div class="flex items-center gap-3 px-4 py-2 my-1 rounded-lg text-on-secondary-container hover:bg-surface-container-low transition-all cursor-pointer">
<span class="material-symbols-outlined">query_stats</span>
<span class="font-label-caps text-label-caps">ASIN from STR</span>
</div>
<div class="flex items-center gap-3 px-4 py-2 my-1 rounded-lg text-on-secondary-container hover:bg-surface-container-low transition-all cursor-pointer">
<span class="material-symbols-outlined">smart_toy</span>
<span class="font-label-caps text-label-caps">Auto Campaigns</span>
</div>
<div class="flex items-center gap-3 px-4 py-2 my-1 rounded-lg text-on-secondary-container hover:bg-surface-container-low transition-all cursor-pointer">
<span class="material-symbols-outlined">category</span>
<span class="font-label-caps text-label-caps">Category Targets</span>
</div>
<div class="flex items-center gap-3 px-4 py-2 my-1 rounded-lg text-on-secondary-container hover:bg-surface-container-low transition-all cursor-pointer">
<span class="material-symbols-outlined">money_off</span>
<span class="font-label-caps text-label-caps">Wasted Ad Spend</span>
</div>
</nav>
<div class="px-3 mt-4 border-t border-outline-variant pt-4">
<button class="w-full bg-primary-container text-on-primary-fixed font-bold py-3 rounded-lg flex items-center justify-center gap-2 hover:opacity-90 transition-opacity">
<span class="material-symbols-outlined">download</span>
<span class="font-label-caps text-label-caps">Export Report</span>
</button>
<div class="mt-4">
<div class="flex items-center gap-3 px-4 py-2 text-on-secondary-container hover:bg-surface-container-low rounded-lg transition-all cursor-pointer">
<span class="material-symbols-outlined">contact_support</span>
<span class="font-label-caps text-label-caps">Support</span>
</div>
<div class="flex items-center gap-3 px-4 py-2 text-on-secondary-container hover:bg-surface-container-low rounded-lg transition-all cursor-pointer">
<span class="material-symbols-outlined">settings</span>
<span class="font-label-caps text-label-caps">Settings</span>
</div>
</div>
</div>
</aside>
<!-- Main Content Area -->
<main class="ml-64 mt-16 p-margin-desktop h-[calc(100vh-64px)] overflow-y-auto custom-scrollbar">
<!-- Header Section -->
<div class="flex flex-col md:flex-row md:items-center justify-between mb-8 gap-4">
<div>
<h1 class="font-display-lg text-display-lg text-on-surface">Keyword Performance Overview</h1>
<p class="text-body-md text-on-surface-variant">Real-time keyword analysis and optimization for active campaigns.</p>
</div>
<div class="flex items-center gap-3">
<div class="bg-white border border-outline-variant rounded px-4 py-2 flex items-center gap-2 cursor-pointer hover:bg-surface-container-low transition-all">
<span class="material-symbols-outlined text-on-secondary-container">calendar_today</span>
<span class="font-body-md">Last 30 Days</span>
<span class="material-symbols-outlined text-on-secondary-container">expand_more</span>
</div>
<button class="bg-white border border-secondary text-secondary font-bold px-6 py-2 rounded flex items-center gap-2 hover:bg-secondary-container transition-all">
<span class="material-symbols-outlined">upload_file</span>
<span class="font-label-caps text-label-caps">Export</span>
</button>
</div>
</div>
<!-- Metric Grid -->
<div class="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-7 gap-4 mb-8">
<!-- Metric Card 1 -->
<div class="bg-white p-4 border border-outline-variant rounded-lg shadow-sm">
<p class="text-label-caps font-label-caps text-on-secondary-container mb-2">Impressions</p>
<div class="flex items-end justify-between">
<span class="font-display-md text-display-md text-on-surface">1.2M</span>
<span class="text-xs font-bold text-green-600 bg-green-50 px-1 rounded flex items-center">
<span class="material-symbols-outlined text-[14px]">trending_up</span> 12%
                    </span>
</div>
</div>
<!-- Metric Card 2 -->
<div class="bg-white p-4 border border-outline-variant rounded-lg shadow-sm">
<p class="text-label-caps font-label-caps text-on-secondary-container mb-2">Clicks</p>
<div class="flex items-end justify-between">
<span class="font-display-md text-display-md text-on-surface">45.8K</span>
<span class="text-xs font-bold text-green-600 bg-green-50 px-1 rounded flex items-center">
<span class="material-symbols-outlined text-[14px]">trending_up</span> 8.4%
                    </span>
</div>
</div>
<!-- Metric Card 3 -->
<div class="bg-white p-4 border border-outline-variant rounded-lg shadow-sm">
<p class="text-label-caps font-label-caps text-on-secondary-container mb-2">CTR</p>
<div class="flex items-end justify-between">
<span class="font-display-md text-display-md text-on-surface">3.82%</span>
<span class="text-xs font-bold text-error bg-red-50 px-1 rounded flex items-center">
<span class="material-symbols-outlined text-[14px]">trending_down</span> 0.5%
                    </span>
</div>
</div>
<!-- Metric Card 4 -->
<div class="bg-white p-4 border border-outline-variant rounded-lg shadow-sm">
<p class="text-label-caps font-label-caps text-on-secondary-container mb-2">CVR</p>
<div class="flex items-end justify-between">
<span class="font-display-md text-display-md text-on-surface">12.4%</span>
<span class="text-xs font-bold text-green-600 bg-green-50 px-1 rounded flex items-center">
<span class="material-symbols-outlined text-[14px]">trending_up</span> 2.1%
                    </span>
</div>
</div>
<!-- Metric Card 5 -->
<div class="bg-white p-4 border border-outline-variant rounded-lg shadow-sm">
<p class="text-label-caps font-label-caps text-on-secondary-container mb-2">CPC</p>
<div class="flex items-end justify-between">
<span class="font-display-md text-display-md text-on-surface">$1.24</span>
<span class="text-xs font-bold text-on-surface-variant">Stable</span>
</div>
</div>
<!-- Metric Card 6 -->
<div class="bg-white p-4 border border-outline-variant rounded-lg shadow-sm">
<p class="text-label-caps font-label-caps text-on-secondary-container mb-2">Spend</p>
<div class="flex items-end justify-between">
<span class="font-display-md text-display-md text-on-surface">$56.7K</span>
<span class="text-xs font-bold text-error bg-red-50 px-1 rounded flex items-center">
<span class="material-symbols-outlined text-[14px]">trending_up</span> 15%
                    </span>
</div>
</div>
<!-- Metric Card 7 -->
<div class="bg-white p-4 border border-outline-variant rounded-lg shadow-sm">
<p class="text-label-caps font-label-caps text-on-secondary-container mb-2">Sales</p>
<div class="flex items-end justify-between">
<span class="font-display-md text-display-md text-on-surface">$212K</span>
<span class="text-xs font-bold text-green-600 bg-green-50 px-1 rounded flex items-center">
<span class="material-symbols-outlined text-[14px]">trending_up</span> 24%
                    </span>
</div>
</div>
</div>
<div class="grid grid-cols-2 md:grid-cols-6 gap-4 mb-8">
<!-- Metric Card 8 -->
<div class="bg-white p-4 border border-outline-variant rounded-lg shadow-sm">
<p class="text-label-caps font-label-caps text-on-secondary-container mb-2">Orders</p>
<span class="font-display-md text-display-md text-on-surface">5,672</span>
</div>
<!-- Metric Card 9 -->
<div class="bg-white p-4 border border-outline-variant rounded-lg shadow-sm">
<p class="text-label-caps font-label-caps text-on-secondary-container mb-2">Units</p>
<span class="font-display-md text-display-md text-on-surface">6,104</span>
</div>
<!-- Metric Card 10 -->
<div class="bg-white p-4 border border-outline-variant rounded-lg shadow-sm">
<p class="text-label-caps font-label-caps text-on-secondary-container mb-2">ACOS</p>
<div class="flex items-end justify-between">
<span class="font-display-md text-display-md text-green-600">26.7%</span>
<span class="text-xs text-on-surface-variant">Efficient</span>
</div>
</div>
<!-- Metric Card 11 -->
<div class="bg-white p-4 border border-outline-variant rounded-lg shadow-sm">
<p class="text-label-caps font-label-caps text-on-secondary-container mb-2">ROAS</p>
<div class="flex items-end justify-between">
<span class="font-display-md text-display-md text-on-surface">3.74x</span>
<span class="text-xs text-on-surface-variant">+0.2x</span>
</div>
</div>
<!-- Metric Card 12 -->
<div class="bg-white p-4 border border-outline-variant rounded-lg shadow-sm">
<p class="text-label-caps font-label-caps text-on-secondary-container mb-2">Spend % Split</p>
<div class="w-full bg-surface-container h-2 rounded-full mt-2">
<div class="bg-primary w-[65%] h-full rounded-full"></div>
</div>
<p class="text-[10px] mt-1 text-on-secondary-container text-right">65% Top Keywords</p>
</div>
<!-- Metric Card 13 -->
<div class="bg-white p-4 border border-outline-variant rounded-lg shadow-sm">
<p class="text-label-caps font-label-caps text-on-secondary-container mb-2">Sales % Split</p>
<div class="w-full bg-surface-container h-2 rounded-full mt-2">
<div class="bg-tertiary w-[82%] h-full rounded-full"></div>
</div>
<p class="text-[10px] mt-1 text-on-secondary-container text-right">82% Top Keywords</p>
</div>
</div>
<!-- Filter Bar -->
<div class="bg-white border border-outline-variant rounded-lg p-4 mb-6 flex flex-wrap items-center gap-4">
<div class="flex-1 min-w-[200px] relative">
<span class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-on-secondary-container">search</span>
<input class="w-full pl-10 pr-4 py-2 border border-outline-variant rounded focus:outline-none focus:ring-1 focus:ring-primary text-body-md" placeholder="Search Keywords..." type="text"/>
</div>
<div class="flex items-center gap-3">
<select class="bg-white border border-outline-variant rounded px-3 py-2 text-body-md focus:outline-none min-w-[120px]">
<option>Match Type</option>
<option>Exact</option>
<option>Phrase</option>
<option>Broad</option>
</select>
<select class="bg-white border border-outline-variant rounded px-3 py-2 text-body-md focus:outline-none min-w-[180px]">
<option>Performance Metrics</option>
<option>High ACOS (&gt;35%)</option>
<option>Low CTR (&lt;0.5%)</option>
<option>Zero Sales</option>
</select>
<select class="bg-white border border-outline-variant rounded px-3 py-2 text-body-md focus:outline-none min-w-[150px]">
<option>Portfolio</option>
<option>Winter Collection</option>
<option>Summer Specials</option>
<option>Main Line</option>
</select>
<button class="bg-primary text-white font-bold px-4 py-2 rounded flex items-center gap-2 hover:opacity-90 transition-all">
<span class="material-symbols-outlined">filter_list</span>
<span class="font-label-caps text-label-caps">Apply Filters</span>
</button>
<button class="text-on-secondary-container font-label-caps text-label-caps hover:underline px-2">Clear</button>
</div>
</div>
<!-- Data Table Section -->
<div class="bg-white border border-outline-variant rounded-lg overflow-hidden shadow-sm">
<div class="overflow-x-auto custom-scrollbar">
<table class="w-full text-left zebra-table min-w-[1600px]">
<thead class="bg-surface-container-low border-b border-outline-variant">
<tr>
<th class="px-4 py-3 font-label-caps text-label-caps text-on-secondary-container sticky left-0 bg-surface-container-low z-10">Keyword</th>
<th class="px-4 py-3 font-label-caps text-label-caps text-on-secondary-container">Match Type</th>
<th class="px-4 py-3 font-label-caps text-label-caps text-on-secondary-container">Campaign</th>
<th class="px-4 py-3 font-label-caps text-label-caps text-on-secondary-container">Portfolio</th>
<th class="px-4 py-3 font-label-caps text-label-caps text-on-secondary-container text-right">Impr.</th>
<th class="px-4 py-3 font-label-caps text-label-caps text-on-secondary-container text-right">Clicks</th>
<th class="px-4 py-3 font-label-caps text-label-caps text-on-secondary-container text-right">CTR</th>
<th class="px-4 py-3 font-label-caps text-label-caps text-on-secondary-container text-right">CVR</th>
<th class="px-4 py-3 font-label-caps text-label-caps text-on-secondary-container text-right">CPC</th>
<th class="px-4 py-3 font-label-caps text-label-caps text-on-secondary-container text-right">Spend</th>
<th class="px-4 py-3 font-label-caps text-label-caps text-on-secondary-container text-right">Sales</th>
<th class="px-4 py-3 font-label-caps text-label-caps text-on-secondary-container text-right">Orders</th>
<th class="px-4 py-3 font-label-caps text-label-caps text-on-secondary-container text-right">ACOS</th>
<th class="px-4 py-3 font-label-caps text-label-caps text-on-secondary-container text-right">ROAS</th>
<th class="px-4 py-3 font-label-caps text-label-caps text-on-secondary-container text-center">Trend</th>
</tr>
</thead>
<tbody class="divide-y divide-outline-variant">
<!-- Row 1 -->
<tr class="group hover:bg-surface-container-low transition-colors">
<td class="px-4 py-3 font-medium text-on-surface sticky left-0 bg-white group-hover:bg-surface-container-low z-10">running shoes</td>
<td class="px-4 py-3 text-body-sm"><span class="px-2 py-1 bg-secondary-container text-on-secondary-fixed text-[10px] font-bold rounded uppercase">Exact</span></td>
<td class="px-4 py-3 text-body-sm text-on-surface-variant">SP_Auto_Footwear_01</td>
<td class="px-4 py-3 text-body-sm text-on-surface-variant">Winter 2024</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">245,102</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">8,452</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">3.45%</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">14.2%</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">$0.85</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">$7,184.20</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">$32,450.00</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">412</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono font-bold text-green-600">22.1%</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">4.52</td>
<td class="px-4 py-3 text-center">
<span class="material-symbols-outlined text-green-600 text-[18px]">trending_up</span>
</td>
</tr>
<!-- Row 2 -->
<tr class="group hover:bg-surface-container-low transition-colors">
<td class="px-4 py-3 font-medium text-on-surface sticky left-0 bg-white group-hover:bg-surface-container-low z-10">wireless headphones</td>
<td class="px-4 py-3 text-body-sm"><span class="px-2 py-1 bg-surface-variant text-on-surface-variant text-[10px] font-bold rounded uppercase">Phrase</span></td>
<td class="px-4 py-3 text-body-sm text-on-surface-variant">SB_Tech_Audio_Primary</td>
<td class="px-4 py-3 text-body-sm text-on-surface-variant">Electronics</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">512,045</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">12,104</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">2.36%</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">8.1%</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">$1.42</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">$17,187.68</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">$48,210.50</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">980</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono font-bold text-error">35.6%</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">2.81</td>
<td class="px-4 py-3 text-center">
<span class="material-symbols-outlined text-error text-[18px]">trending_down</span>
</td>
</tr>
<!-- Row 3 -->
<tr class="group hover:bg-surface-container-low transition-colors">
<td class="px-4 py-3 font-medium text-on-surface sticky left-0 bg-white group-hover:bg-surface-container-low z-10">minimalist watch</td>
<td class="px-4 py-3 text-body-sm"><span class="px-2 py-1 bg-primary-fixed-dim text-on-primary-fixed text-[10px] font-bold rounded uppercase">Broad</span></td>
<td class="px-4 py-3 text-body-sm text-on-surface-variant">SP_Keyword_Accessories_04</td>
<td class="px-4 py-3 text-body-sm text-on-surface-variant">Lifestyle</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">89,450</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">3,120</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">3.49%</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">11.4%</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">$0.92</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">$2,870.40</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">$10,254.00</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">355</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono font-bold text-green-600">27.9%</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">3.57</td>
<td class="px-4 py-3 text-center">
<span class="material-symbols-outlined text-on-surface-variant text-[18px]">remove</span>
</td>
</tr>
<!-- Row 4 -->
<tr class="group hover:bg-surface-container-low transition-colors">
<td class="px-4 py-3 font-medium text-on-surface sticky left-0 bg-white group-hover:bg-surface-container-low z-10">leather sneakers</td>
<td class="px-4 py-3 text-body-sm"><span class="px-2 py-1 bg-secondary-container text-on-secondary-fixed text-[10px] font-bold rounded uppercase">Exact</span></td>
<td class="px-4 py-3 text-body-sm text-on-surface-variant">SP_Brand_Footwear_Main</td>
<td class="px-4 py-3 text-body-sm text-on-surface-variant">Winter 2024</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">124,000</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">5,600</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">4.51%</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">15.8%</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">$1.15</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">$6,440.00</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">$42,560.00</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">884</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono font-bold text-green-600">15.1%</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">6.61</td>
<td class="px-4 py-3 text-center">
<span class="material-symbols-outlined text-green-600 text-[18px]">trending_up</span>
</td>
</tr>
<!-- Row 5 -->
<tr class="group hover:bg-surface-container-low transition-colors">
<td class="px-4 py-3 font-medium text-on-surface sticky left-0 bg-white group-hover:bg-surface-container-low z-10">gym duffel bag</td>
<td class="px-4 py-3 text-body-sm"><span class="px-2 py-1 bg-surface-variant text-on-surface-variant text-[10px] font-bold rounded uppercase">Phrase</span></td>
<td class="px-4 py-3 text-body-sm text-on-surface-variant">SD_Fitness_Accessories</td>
<td class="px-4 py-3 text-body-sm text-on-surface-variant">Fitness</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">45,210</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">1,020</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">2.26%</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">4.2%</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">$2.10</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">$2,142.00</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">$3,840.00</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">43</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono font-bold text-error">55.8%</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">1.79</td>
<td class="px-4 py-3 text-center">
<span class="material-symbols-outlined text-error text-[18px]">trending_down</span>
</td>
</tr>
</tbody>
</table>
</div>
<div class="px-4 py-4 border-t border-outline-variant flex items-center justify-between bg-surface-container-lowest">
<span class="text-body-sm text-on-surface-variant">Showing 5 of 1,248 keywords</span>
<div class="flex items-center gap-2">
<button class="p-2 border border-outline-variant rounded hover:bg-surface-container-low disabled:opacity-50" disabled="">
<span class="material-symbols-outlined">chevron_left</span>
</button>
<div class="flex items-center gap-1">
<button class="w-8 h-8 rounded bg-primary text-white font-bold text-sm">1</button>
<button class="w-8 h-8 rounded hover:bg-surface-container-low text-sm">2</button>
<button class="w-8 h-8 rounded hover:bg-surface-container-low text-sm">3</button>
<span class="px-1">...</span>
<button class="w-8 h-8 rounded hover:bg-surface-container-low text-sm">42</button>
</div>
<button class="p-2 border border-outline-variant rounded hover:bg-surface-container-low">
<span class="material-symbols-outlined">chevron_right</span>
</button>
</div>
</div>
</div>
<div class="mt-8 grid grid-cols-1 lg:grid-cols-3 gap-6">
<div class="bg-white p-6 border border-outline-variant rounded-lg">
<h3 class="font-headline-sm text-headline-sm mb-4">Ad Spend Optimization</h3>
<p class="text-body-md text-on-surface-variant mb-6">Recommendations based on last 7 days of performance trends.</p>
<div class="space-y-4">
<div class="flex items-start gap-4 p-3 bg-green-50 border border-green-100 rounded">
<span class="material-symbols-outlined text-green-600">arrow_upward</span>
<div>
<p class="font-bold text-sm text-green-800">Increase Bid</p>
<p class="text-xs text-green-700">"running shoes" is under-bidding for top of search with high conversion rate.</p>
</div>
</div>
<div class="flex items-start gap-4 p-3 bg-red-50 border border-red-100 rounded">
<span class="material-symbols-outlined text-error">block</span>
<div>
<p class="font-bold text-sm text-red-800">Negative Keyword</p>
<p class="text-xs text-red-700">"cheap headphones" has 25 clicks and 0 sales in "wireless headphones" phrase match.</p>
</div>
</div>
</div>
</div>
<div class="lg:col-span-2 bg-white p-6 border border-outline-variant rounded-lg">
<h3 class="font-headline-sm text-headline-sm mb-4">Match Type Distribution</h3>
<div class="h-48 flex items-center justify-around">
<!-- Manual Chart Representation -->
<div class="flex flex-col items-center gap-2">
<div class="w-16 bg-secondary-container rounded-t" style="height: 120px;"></div>
<span class="text-label-caps font-label-caps">Exact (42%)</span>
</div>
<div class="flex flex-col items-center gap-2">
<div class="w-16 bg-surface-variant rounded-t" style="height: 80px;"></div>
<span class="text-label-caps font-label-caps">Phrase (28%)</span>
</div>
<div class="flex flex-col items-center gap-2">
<div class="w-16 bg-primary-fixed-dim rounded-t" style="height: 40px;"></div>
<span class="text-label-caps font-label-caps">Broad (15%)</span>
</div>
<div class="flex flex-col items-center gap-2">
<div class="w-16 bg-outline-variant rounded-t" style="height: 50px;"></div>
<span class="text-label-caps font-label-caps">Other (15%)</span>
</div>
</div>
</div>
</div>
</main>
<script>
        // Simple interactive demo logic
        document.querySelectorAll('select').forEach(select => {
            select.addEventListener('change', () => {
                const toast = document.createElement('div');
                toast.className = 'fixed bottom-8 right-8 bg-inverse-surface text-inverse-on-surface px-6 py-3 rounded-lg shadow-xl animate-bounce flex items-center gap-3 z-[100]';
                toast.innerHTML = '<span class="material-symbols-outlined">refresh</span> Filters applied successfully';
                document.body.appendChild(toast);
                setTimeout(() => toast.remove(), 2500);
            });
        });
    </script>
</body></html>

<!-- Keywords - Performance Management -->
<!DOCTYPE html><html class="light" lang="en"><head>
<meta charset="utf-8">
<meta content="width=device-width, initial-scale=1.0" name="viewport">
<title>Search Terms Performance - AdTracker Pro</title>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&amp;family=JetBrains+Mono:wght@500&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<script id="tailwind-config">
      tailwind.config = {
        darkMode: "class",
        theme: {
          extend: {
            "colors": {
                    "surface-bright": "#f8fafa",
                    "tertiary-fixed": "#adecff",
                    "secondary-container": "#d4e1f5",
                    "primary-fixed-dim": "#ffb86f",
                    "on-primary": "#ffffff",
                    "surface": "#f8fafa",
                    "on-surface-variant": "#554434",
                    "inverse-on-surface": "#eff1f1",
                    "on-error-container": "#93000a",
                    "error-container": "#ffdad6",
                    "on-primary-fixed-variant": "#693c00",
                    "on-primary-fixed": "#2c1600",
                    "surface-container-highest": "#e1e3e3",
                    "outline": "#887361",
                    "on-tertiary-fixed-variant": "#004e5d",
                    "on-primary-container": "#653a00",
                    "surface-container-low": "#f2f4f4",
                    "on-secondary-fixed-variant": "#3c4858",
                    "on-secondary-container": "#576474",
                    "on-secondary-fixed": "#101c2b",
                    "background": "#f8fafa",
                    "secondary-fixed": "#d7e3f7",
                    "surface-container": "#eceeee",
                    "secondary": "#535f70",
                    "inverse-primary": "#ffb86f",
                    "error": "#ba1a1a",
                    "surface-container-lowest": "#ffffff",
                    "surface-tint": "#8a5100",
                    "on-tertiary": "#ffffff",
                    "primary-container": "#ff9900",
                    "on-tertiary-fixed": "#001f26",
                    "on-secondary": "#ffffff",
                    "tertiary-fixed-dim": "#80d2e9",
                    "primary": "#8a5100",
                    "surface-dim": "#d8dada",
                    "on-background": "#191c1d",
                    "surface-variant": "#e1e3e3",
                    "primary-fixed": "#ffdcbd",
                    "on-tertiary-container": "#004b59",
                    "tertiary-container": "#6abdd3",
                    "tertiary": "#00687a",
                    "on-surface": "#191c1d",
                    "secondary-fixed-dim": "#bbc7db",
                    "outline-variant": "#dbc2ad",
                    "on-error": "#ffffff",
                    "surface-container-high": "#e6e8e8",
                    "inverse-surface": "#2e3131"
            },
            "borderRadius": {
                    "DEFAULT": "0.125rem",
                    "lg": "0.25rem",
                    "xl": "0.5rem",
                    "full": "0.75rem"
            },
            "spacing": {
                    "margin-desktop": "32px",
                    "unit": "4px",
                    "margin-mobile": "16px",
                    "container-padding": "24px",
                    "max-width": "1440px",
                    "gutter": "16px"
            },
            "fontFamily": {
                    "headline-sm": ["Inter"],
                    "display-lg": ["Inter"],
                    "data-mono": ["JetBrains Mono"],
                    "label-caps": ["Inter"],
                    "body-sm": ["Inter"],
                    "body-md": ["Inter"],
                    "body-lg": ["Inter"],
                    "display-md": ["Inter"]
            },
            "fontSize": {
                    "headline-sm": ["18px", {"lineHeight": "24px", "fontWeight": "600"}],
                    "display-lg": ["32px", {"lineHeight": "40px", "letterSpacing": "-0.02em", "fontWeight": "700"}],
                    "data-mono": ["13px", {"lineHeight": "18px", "fontWeight": "500"}],
                    "label-caps": ["11px", {"lineHeight": "16px", "letterSpacing": "0.05em", "fontWeight": "700"}],
                    "body-sm": ["12px", {"lineHeight": "16px", "fontWeight": "400"}],
                    "body-md": ["14px", {"lineHeight": "20px", "fontWeight": "400"}],
                    "body-lg": ["16px", {"lineHeight": "24px", "fontWeight": "400"}],
                    "display-md": ["24px", {"lineHeight": "32px", "letterSpacing": "-0.01em", "fontWeight": "600"}]
            }
          },
        },
      }
    </script>
<style>
        body {
            font-family: 'Inter', sans-serif;
            background-color: #f8fafa;
            color: #191c1d;
        }
        .material-symbols-outlined {
            font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
            vertical-align: middle;
        }
        .custom-scrollbar::-webkit-scrollbar {
            width: 4px;
            height: 4px;
        }
        .custom-scrollbar::-webkit-scrollbar-track {
            background: #f1f1f1;
        }
        .custom-scrollbar::-webkit-scrollbar-thumb {
            background: #888;
            border-radius: 10px;
        }
        .zebra-stripe:nth-child(even) {
            background-color: #f8fafa;
        }
        .kpi-card {
            border: 1px solid #E0E3E3;
            transition: all 0.2s ease;
        }
        .kpi-card:hover {
            box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);
        }
    </style>
</head>
<body class="bg-surface">
<!-- Sidebar Navigation -->
<aside class="w-64 h-full fixed left-0 top-0 border-r border-outline-variant bg-surface-container-lowest flex flex-col py-6 px-4 z-20">
<div class="mb-8 px-2">
<h1 class="font-headline-sm text-headline-sm font-bold text-primary">AdTracker Pro</h1>
<p class="text-[10px] text-secondary tracking-widest uppercase font-bold mt-1">Precision Performance System</p>
</div>
<nav class="flex-1 space-y-1 overflow-y-auto custom-scrollbar">
<!-- Navigation Items Mapping -->
<a class="flex items-center gap-3 px-3 py-2 rounded text-secondary hover:bg-surface-container transition-colors group" href="#">
<span class="material-symbols-outlined text-[20px]">dashboard</span>
<span class="font-body-md text-body-md">Dashboard</span>
</a>
<a class="flex items-center gap-3 px-3 py-2 rounded text-secondary hover:bg-surface-container transition-colors group" href="#">
<span class="material-symbols-outlined text-[20px]">campaign</span>
<span class="font-body-md text-body-md">Campaigns</span>
</a>
<a class="flex items-center gap-3 px-3 py-2 rounded text-secondary hover:bg-surface-container transition-colors group" href="#">
<span class="material-symbols-outlined text-[20px]">inventory_2</span>
<span class="font-body-md text-body-md">Products</span>
</a>
<a class="flex items-center gap-3 px-3 py-2 rounded text-secondary hover:bg-surface-container transition-colors group" href="#">
<span class="material-symbols-outlined text-[20px]">analytics</span>
<span class="font-body-md text-body-md">Match Type</span>
</a>
<a class="flex items-center gap-3 px-3 py-2 rounded text-secondary hover:bg-surface-container transition-colors group" href="#">
<span class="material-symbols-outlined text-[20px]">key</span>
<span class="font-body-md text-body-md">Keywords</span>
</a>
<!-- Active State: Search Terms -->
<a class="flex items-center gap-3 px-3 py-2 rounded bg-secondary-container text-on-secondary-container font-semibold transition-colors group" href="#">
<span class="material-symbols-outlined text-[20px]">search</span>
<span class="font-body-md text-body-md">Search Terms</span>
</a>
<a class="flex items-center gap-3 px-3 py-2 rounded text-secondary hover:bg-surface-container transition-colors group" href="#">
<span class="material-symbols-outlined text-[20px]">target</span>
<span class="font-body-md text-body-md">ASIN Targets</span>
</a>
<a class="flex items-center gap-3 px-3 py-2 rounded text-secondary hover:bg-surface-container transition-colors group" href="#">
<span class="material-symbols-outlined text-[20px]">query_stats</span>
<span class="font-body-md text-body-md">ASIN from STR</span>
</a>
<a class="flex items-center gap-3 px-3 py-2 rounded text-secondary hover:bg-surface-container transition-colors group" href="#">
<span class="material-symbols-outlined text-[20px]">smart_toy</span>
<span class="font-body-md text-body-md">Auto Campaigns</span>
</a>
<a class="flex items-center gap-3 px-3 py-2 rounded text-secondary hover:bg-surface-container transition-colors group" href="#">
<span class="material-symbols-outlined text-[20px]">category</span>
<span class="font-body-md text-body-md">Category Targets</span>
</a>
<a class="flex items-center gap-3 px-3 py-2 rounded text-secondary hover:bg-surface-container transition-colors group" href="#">
<span class="material-symbols-outlined text-[20px]">leak_add</span>
<span class="font-body-md text-body-md">Wasted Ad Spend</span>
</a>
</nav>
<div class="mt-auto pt-4 border-t border-outline-variant flex items-center gap-3 px-2">
<div class="w-8 h-8 rounded-full bg-primary-fixed flex items-center justify-center overflow-hidden">
<img alt="User Profile" class="w-full h-full object-cover" src="https://lh3.googleusercontent.com/aida-public/AB6AXuA6ixSIfnT0YBEe6I6fy8TVWflfZv8VRjcWdSYOZaJIPuvcwoMLwAyRCaDu_b5TmTfGKog_c0p-8uL25nh-_JsElv2aqEF27PNjRFNzjXqFXrlQoupAtetcxXOO3F6Y1driqvA_d476QA09KTyHpxaBHIQAcvHaoMUbsBaCNkwISR0cAIJ-3vObJZj1ItA12UWqUvIqBmtAHG9pUaBZhPq3qD0SfIp30taMIiTUIDTwR6dXLW7fZrIihQWxr4SneBaQZkIQBfed">
</div>
<div class="overflow-hidden">
<p class="font-body-sm text-body-sm font-semibold truncate">Alex Strategy</p>
<p class="text-[10px] text-secondary truncate uppercase">Senior Optimizer</p>
</div>
</div>
</aside>
<!-- Main Content Area -->
<main class="ml-64 min-h-screen flex flex-col">
<!-- Top Navbar -->
<header class="h-16 bg-surface px-margin-desktop flex items-center justify-between border-b border-outline-variant sticky top-0 z-10">
<div class="flex items-center gap-4 flex-1 max-w-xl">
<div class="relative w-full">
<span class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-secondary text-sm">search</span>
<input class="w-full bg-surface-container-low border border-outline-variant rounded-lg pl-10 pr-4 py-2 text-body-sm focus:ring-2 focus:ring-tertiary-container outline-none transition-all" placeholder="Search Global Campaigns..." type="text">
</div>
</div>
<div class="flex items-center gap-6">
<button class="relative text-secondary hover:text-primary transition-colors">
<span class="material-symbols-outlined">notifications</span>
<span class="absolute -top-1 -right-1 w-2 h-2 bg-error rounded-full"></span>
</button>
<button class="text-secondary hover:text-primary transition-colors">
<span class="material-symbols-outlined">help</span>
</button>
<button class="text-secondary hover:text-primary transition-colors">
<span class="material-symbols-outlined">settings</span>
</button>
<div class="h-8 w-px bg-outline-variant"></div>
<div class="flex items-center gap-2">
<span class="material-symbols-outlined text-primary">account_circle</span>
</div>
</div>
</header>
<!-- Page Content -->
<div class="p-margin-desktop space-y-6">
<!-- Header Section -->
<div class="flex flex-col md:flex-row md:items-center justify-between gap-4">
<div>
<h2 class="font-display-md text-display-md text-on-surface">Search Terms Performance Overview</h2>
<p class="font-body-sm text-body-sm text-secondary mt-1 tracking-wide">Last updated: Today, 08:42 AM</p>
</div>
<div class="flex items-center gap-3">
<div class="flex items-center gap-2 bg-surface-container-lowest border border-outline-variant px-4 py-2 rounded-lg">
<span class="material-symbols-outlined text-secondary text-sm">calendar_today</span>
<span class="font-body-sm text-body-sm font-medium">Oct 01, 2023 - Oct 31, 2023</span>
</div>
<button class="flex items-center gap-2 bg-primary-container text-on-primary-container px-4 py-2 rounded-lg font-body-sm font-semibold hover:opacity-90 transition-all">
<span class="material-symbols-outlined text-sm">download</span>
                        Export Report
                    </button>
</div>
</div>
<!-- Metric Grid (13 Metrics) -->
<div class="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-7 gap-4">
<!-- KPI Card 1 -->
<div class="kpi-card bg-surface-container-lowest p-4 rounded-xl flex flex-col justify-between min-h-[100px]">
<span class="font-label-caps text-label-caps text-secondary uppercase">Impressions</span>
<div class="flex flex-col mt-2">
<span class="font-display-md text-display-md font-bold">1.2M</span>
<span class="font-body-sm text-body-sm text-green-600 flex items-center gap-1">
<span class="material-symbols-outlined text-[14px]">arrow_upward</span> 12%
                        </span>
</div>
</div>
<!-- KPI Card 2 -->
<div class="kpi-card bg-surface-container-lowest p-4 rounded-xl flex flex-col justify-between min-h-[100px]">
<span class="font-label-caps text-label-caps text-secondary uppercase">Clicks</span>
<div class="flex flex-col mt-2">
<span class="font-display-md text-display-md font-bold">45.8K</span>
<span class="font-body-sm text-body-sm text-green-600 flex items-center gap-1">
<span class="material-symbols-outlined text-[14px]">arrow_upward</span> 8.4%
                        </span>
</div>
</div>
<!-- KPI Card 3 -->
<div class="kpi-card bg-surface-container-lowest p-4 rounded-xl flex flex-col justify-between min-h-[100px]">
<span class="font-label-caps text-label-caps text-secondary uppercase">CTR</span>
<div class="flex flex-col mt-2">
<span class="font-display-md text-display-md font-bold">3.82%</span>
<span class="font-body-sm text-body-sm text-error flex items-center gap-1">
<span class="material-symbols-outlined text-[14px]">arrow_downward</span> 0.5%
                        </span>
</div>
</div>
<!-- KPI Card 4 -->
<div class="kpi-card bg-surface-container-lowest p-4 rounded-xl flex flex-col justify-between min-h-[100px]">
<span class="font-label-caps text-label-caps text-secondary uppercase">CVR</span>
<div class="flex flex-col mt-2">
<span class="font-display-md text-display-md font-bold">12.4%</span>
<span class="font-body-sm text-body-sm text-green-600 flex items-center gap-1">
<span class="material-symbols-outlined text-[14px]">arrow_upward</span> 2.1%
                        </span>
</div>
</div>
<!-- KPI Card 5 -->
<div class="kpi-card bg-surface-container-lowest p-4 rounded-xl flex flex-col justify-between min-h-[100px]">
<span class="font-label-caps text-label-caps text-secondary uppercase">CPC</span>
<div class="flex flex-col mt-2">
<span class="font-display-md text-display-md font-bold">$1.24</span>
<span class="font-body-sm text-body-sm text-secondary flex items-center gap-1">
                            Stable
                        </span>
</div>
</div>
<!-- KPI Card 6 -->
<div class="kpi-card bg-surface-container-lowest p-4 rounded-xl flex flex-col justify-between min-h-[100px]">
<span class="font-label-caps text-label-caps text-secondary uppercase">Spend</span>
<div class="flex flex-col mt-2">
<span class="font-display-md text-display-md font-bold text-primary">$56.7K</span>
<span class="font-body-sm text-body-sm text-error flex items-center gap-1">
<span class="material-symbols-outlined text-[14px]">arrow_upward</span> 15%
                        </span>
</div>
</div>
<!-- KPI Card 7 -->
<div class="kpi-card bg-surface-container-lowest p-4 rounded-xl flex flex-col justify-between min-h-[100px]">
<span class="font-label-caps text-label-caps text-secondary uppercase">Sales</span>
<div class="flex flex-col mt-2">
<span class="font-display-md text-display-md font-bold">$212K</span>
<span class="font-body-sm text-body-sm text-green-600 flex items-center gap-1">
<span class="material-symbols-outlined text-[14px]">arrow_upward</span> 24%
                        </span>
</div>
</div>
</div>
<!-- Row 2 Metrics & Progress Cards -->
<div class="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-6 gap-4">
<div class="kpi-card bg-surface-container-lowest p-4 rounded-xl flex flex-col justify-between min-h-[100px]">
<span class="font-label-caps text-label-caps text-secondary uppercase">Orders</span>
<span class="font-display-md text-display-md font-bold mt-2">5,672</span>
</div>
<div class="kpi-card bg-surface-container-lowest p-4 rounded-xl flex flex-col justify-between min-h-[100px]">
<span class="font-label-caps text-label-caps text-secondary uppercase">Units</span>
<span class="font-display-md text-display-md font-bold mt-2">6,104</span>
</div>
<div class="kpi-card bg-surface-container-lowest p-4 rounded-xl flex flex-col justify-between min-h-[100px]">
<span class="font-label-caps text-label-caps text-secondary uppercase">ACOS</span>
<div class="flex flex-col mt-2">
<span class="font-display-md text-display-md font-bold">26.7%</span>
<span class="font-body-sm text-body-sm text-green-600 px-2 bg-green-50 rounded-full w-max mt-1">Efficient</span>
</div>
</div>
<div class="kpi-card bg-surface-container-lowest p-4 rounded-xl flex flex-col justify-between min-h-[100px]">
<span class="font-label-caps text-label-caps text-secondary uppercase">ROAS</span>
<div class="flex flex-col mt-2">
<span class="font-display-md text-display-md font-bold">3.74x</span>
<span class="font-body-sm text-body-sm text-green-600 flex items-center gap-1">
<span class="material-symbols-outlined text-[14px]">add</span> 0.2x
                        </span>
</div>
</div>
<!-- Progress Split Card -->
<div class="md:col-span-2 kpi-card bg-surface-container-lowest p-4 rounded-xl grid grid-cols-2 gap-6 items-center">
<div>
<span class="font-label-caps text-label-caps text-secondary uppercase">Spend % Split</span>
<div class="mt-2 flex items-center gap-3">
<div class="flex-1 h-2 bg-surface-container rounded-full overflow-hidden">
<div class="bg-primary h-full rounded-full" style="width: 65%"></div>
</div>
<span class="font-data-mono text-data-mono font-bold">65%</span>
</div>
</div>
<div>
<span class="font-label-caps text-label-caps text-secondary uppercase">Sales % Split</span>
<div class="mt-2 flex items-center gap-3">
<div class="flex-1 h-2 bg-surface-container rounded-full overflow-hidden">
<div class="bg-[#007185] h-full rounded-full" style="width: 82%"></div>
</div>
<span class="font-data-mono text-data-mono font-bold">82%</span>
</div>
</div>
</div>
</div>
<!-- Filter Bar -->
<div class="bg-surface-container-lowest border border-outline-variant rounded-xl p-4 flex flex-wrap items-center gap-4">
<div class="flex-1 min-w-[240px] relative">
<span class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-secondary text-sm">search</span>
<input class="w-full bg-surface border border-outline-variant rounded-lg pl-10 pr-4 py-2 text-body-sm outline-none focus:border-primary transition-all" placeholder="Search Terms..." type="text">
</div>
<div class="flex items-center gap-3">
<select class="bg-surface border border-outline-variant rounded-lg px-4 py-2 text-body-sm font-medium focus:ring-1 focus:ring-primary outline-none">
<option>Metrics</option>
<option>Profitability</option>
<option>Volume</option>
</select>
<select class="bg-surface border border-outline-variant rounded-lg px-4 py-2 text-body-sm font-medium focus:ring-1 focus:ring-primary outline-none">
<option>All Portfolios</option>
<option>Main Electronics</option>
<option>Accessories</option>
</select>
<select class="bg-surface border border-outline-variant rounded-lg px-4 py-2 text-body-sm font-medium focus:ring-1 focus:ring-primary outline-none">
<option>All Campaigns</option>
<option>Prime Day 2023</option>
<option>Auto Evergreen</option>
</select>
</div>
<div class="flex items-center gap-4 ml-auto">
<a class="text-secondary font-body-sm hover:underline" href="#">Clear</a>
<button class="bg-[#007185] text-white px-6 py-2 rounded-lg font-body-sm font-semibold hover:bg-opacity-90 transition-all">Apply Filters</button>
</div>
</div>
<!-- Data Table Card -->
<div class="bg-surface-container-lowest border border-outline-variant rounded-xl overflow-hidden">
<div class="overflow-x-auto custom-scrollbar">
<table class="w-full text-left border-collapse">
<thead class="bg-surface-container-low border-b border-outline-variant">
<tr>
<th class="px-4 py-3 font-label-caps text-label-caps text-secondary whitespace-nowrap">Search Term</th><th class="px-4 py-3 font-label-caps text-label-caps text-secondary whitespace-nowrap">Keyword Target</th>
<th class="px-4 py-3 font-label-caps text-label-caps text-secondary whitespace-nowrap">Match Type</th>
<th class="px-4 py-3 font-label-caps text-label-caps text-secondary whitespace-nowrap">Campaign</th>
<th class="px-4 py-3 font-label-caps text-label-caps text-secondary whitespace-nowrap">Portfolio</th>
<th class="px-4 py-3 font-label-caps text-label-caps text-secondary whitespace-nowrap text-right">Impr.</th>
<th class="px-4 py-3 font-label-caps text-label-caps text-secondary whitespace-nowrap text-right">Clicks</th>
<th class="px-4 py-3 font-label-caps text-label-caps text-secondary whitespace-nowrap text-right">CTR</th>
<th class="px-4 py-3 font-label-caps text-label-caps text-secondary whitespace-nowrap text-right">CVR</th>
<th class="px-4 py-3 font-label-caps text-label-caps text-secondary whitespace-nowrap text-right">CPC</th>
<th class="px-4 py-3 font-label-caps text-label-caps text-secondary whitespace-nowrap text-right text-primary">Spend</th>
<th class="px-4 py-3 font-label-caps text-label-caps text-secondary whitespace-nowrap text-right font-bold text-on-surface">Sales</th>
<th class="px-4 py-3 font-label-caps text-label-caps text-secondary whitespace-nowrap text-right">ACOS</th>
<th class="px-4 py-3 font-label-caps text-label-caps text-secondary whitespace-nowrap text-right">ROAS</th>
</tr>
</thead>
<tbody class="divide-y divide-outline-variant">
<!-- Row 1 -->
<tr class="zebra-stripe hover:bg-surface-container transition-colors group">
<td class="px-4 py-3 font-body-md text-body-md font-semibold text-primary cursor-pointer hover:underline">breathable running shoes</td><td class="px-4 py-3 font-body-sm text-body-sm text-secondary italic">running shoes</td>
<td class="px-4 py-3 font-body-sm text-body-sm"><span class="px-2 py-0.5 rounded bg-blue-50 text-blue-700 text-[10px] font-bold uppercase">Exact</span></td>
<td class="px-4 py-3 font-body-sm text-body-sm text-secondary">Q4_Performance_Sneakers</td>
<td class="px-4 py-3 font-body-sm text-body-sm text-secondary">Footwear_Main</td>
<td class="px-4 py-3 font-data-mono text-data-mono text-right">145,290</td>
<td class="px-4 py-3 font-data-mono text-data-mono text-right">6,842</td>
<td class="px-4 py-3 font-data-mono text-data-mono text-right">4.71%</td>
<td class="px-4 py-3 font-data-mono text-data-mono text-right">15.2%</td>
<td class="px-4 py-3 font-data-mono text-data-mono text-right">$1.42</td>
<td class="px-4 py-3 font-data-mono text-data-mono text-right text-primary font-bold">$9,715.64</td>
<td class="px-4 py-3 font-data-mono text-data-mono text-right font-bold">$42,851.20</td>
<td class="px-4 py-3 font-data-mono text-data-mono text-right text-green-700 font-bold">22.6%</td>
<td class="px-4 py-3 font-data-mono text-data-mono text-right">4.41x</td>
</tr>
<!-- Row 2 -->
<tr class="zebra-stripe hover:bg-surface-container transition-colors group">
<td class="px-4 py-3 font-body-md text-body-md font-semibold text-primary cursor-pointer hover:underline">waterproof wireless earbuds</td><td class="px-4 py-3 font-body-sm text-body-sm text-secondary italic">wireless earbuds</td>
<td class="px-4 py-3 font-body-sm text-body-sm"><span class="px-2 py-0.5 rounded bg-purple-50 text-purple-700 text-[10px] font-bold uppercase">Phrase</span></td>
<td class="px-4 py-3 font-body-sm text-body-sm text-secondary">Audio_HighCVR_Terms</td>
<td class="px-4 py-3 font-body-sm text-body-sm text-secondary">Tech_Accessories</td>
<td class="px-4 py-3 font-data-mono text-data-mono text-right">82,401</td>
<td class="px-4 py-3 font-data-mono text-data-mono text-right">3,120</td>
<td class="px-4 py-3 font-data-mono text-data-mono text-right">3.79%</td>
<td class="px-4 py-3 font-data-mono text-data-mono text-right">9.8%</td>
<td class="px-4 py-3 font-data-mono text-data-mono text-right">$0.85</td>
<td class="px-4 py-3 font-data-mono text-data-mono text-right text-primary font-bold">$2,652.00</td>
<td class="px-4 py-3 font-data-mono text-data-mono text-right font-bold">$18,450.50</td>
<td class="px-4 py-3 font-data-mono text-data-mono text-right text-green-700 font-bold">14.3%</td>
<td class="px-4 py-3 font-data-mono text-data-mono text-right">6.96x</td>
</tr>
<!-- Row 3 -->
<tr class="zebra-stripe hover:bg-surface-container transition-colors group">
<td class="px-4 py-3 font-body-md text-body-md font-semibold text-primary cursor-pointer hover:underline">luxury wrist watch</td><td class="px-4 py-3 font-body-sm text-body-sm text-secondary italic">wrist watch</td>
<td class="px-4 py-3 font-body-sm text-body-sm"><span class="px-2 py-0.5 rounded bg-blue-50 text-blue-700 text-[10px] font-bold uppercase">Exact</span></td>
<td class="px-4 py-3 font-body-sm text-body-sm text-secondary">Premium_Timepieces_ST</td>
<td class="px-4 py-3 font-body-sm text-body-sm text-secondary">Luxury_Goods</td>
<td class="px-4 py-3 font-data-mono text-data-mono text-right">24,192</td>
<td class="px-4 py-3 font-data-mono text-data-mono text-right">412</td>
<td class="px-4 py-3 font-data-mono text-data-mono text-right">1.70%</td>
<td class="px-4 py-3 font-data-mono text-data-mono text-right">5.1%</td>
<td class="px-4 py-3 font-data-mono text-data-mono text-right">$4.50</td>
<td class="px-4 py-3 font-data-mono text-data-mono text-right text-primary font-bold">$1,854.00</td>
<td class="px-4 py-3 font-data-mono text-data-mono text-right font-bold">$5,240.00</td>
<td class="px-4 py-3 font-data-mono text-data-mono text-right text-error font-bold">35.4%</td>
<td class="px-4 py-3 font-data-mono text-data-mono text-right">2.82x</td>
</tr>
<!-- Row 4 -->
<tr class="zebra-stripe hover:bg-surface-container transition-colors group">
<td class="px-4 py-3 font-body-md text-body-md font-semibold text-primary cursor-pointer hover:underline">men's athletic sneakers</td><td class="px-4 py-3 font-body-sm text-body-sm text-secondary italic">athletic sneakers</td>
<td class="px-4 py-3 font-body-sm text-body-sm"><span class="px-2 py-0.5 rounded bg-gray-100 text-gray-700 text-[10px] font-bold uppercase">Broad</span></td>
<td class="px-4 py-3 font-body-sm text-body-sm text-secondary">Discovery_Broad_Men</td>
<td class="px-4 py-3 font-body-sm text-body-sm text-secondary">Footwear_Main</td>
<td class="px-4 py-3 font-data-mono text-data-mono text-right">256,104</td>
<td class="px-4 py-3 font-data-mono text-data-mono text-right">12,410</td>
<td class="px-4 py-3 font-data-mono text-data-mono text-right">4.84%</td>
<td class="px-4 py-3 font-data-mono text-data-mono text-right">8.2%</td>
<td class="px-4 py-3 font-data-mono text-data-mono text-right">$1.15</td>
<td class="px-4 py-3 font-data-mono text-data-mono text-right text-primary font-bold">$14,271.50</td>
<td class="px-4 py-3 font-data-mono text-data-mono text-right font-bold">$54,120.00</td>
<td class="px-4 py-3 font-data-mono text-data-mono text-right text-green-700 font-bold">26.3%</td>
<td class="px-4 py-3 font-data-mono text-data-mono text-right">3.79x</td>
</tr>
<!-- Row 5 -->
<tr class="zebra-stripe hover:bg-surface-container transition-colors group">
<td class="px-4 py-3 font-body-md text-body-md font-semibold text-primary cursor-pointer hover:underline">travel duffel bag</td><td class="px-4 py-3 font-body-sm text-body-sm text-secondary italic">duffel bag</td>
<td class="px-4 py-3 font-body-sm text-body-sm"><span class="px-2 py-0.5 rounded bg-blue-50 text-blue-700 text-[10px] font-bold uppercase">Exact</span></td>
<td class="px-4 py-3 font-body-sm text-body-sm text-secondary">Travel_Essentials_Top</td>
<td class="px-4 py-3 font-body-sm text-body-sm text-secondary">Luggage_Dept</td>
<td class="px-4 py-3 font-data-mono text-data-mono text-right">61,005</td>
<td class="px-4 py-3 font-data-mono text-data-mono text-right">2,104</td>
<td class="px-4 py-3 font-data-mono text-data-mono text-right">3.45%</td>
<td class="px-4 py-3 font-data-mono text-data-mono text-right">12.1%</td>
<td class="px-4 py-3 font-data-mono text-data-mono text-right">$1.95</td>
<td class="px-4 py-3 font-data-mono text-data-mono text-right text-primary font-bold">$4,102.80</td>
<td class="px-4 py-3 font-data-mono text-data-mono text-right font-bold">$19,840.00</td>
<td class="px-4 py-3 font-data-mono text-data-mono text-right text-green-700 font-bold">20.6%</td>
<td class="px-4 py-3 font-data-mono text-data-mono text-right">4.84x</td>
</tr>
</tbody>
</table>
</div>
<!-- Pagination -->
<div class="px-6 py-4 flex items-center justify-between border-t border-outline-variant bg-surface-container-low">
<span class="font-body-sm text-body-sm text-secondary">Showing 1 to 5 of 2,451 search terms</span>
<div class="flex items-center gap-2">
<button class="p-1 rounded hover:bg-surface-container-highest transition-colors disabled:opacity-30" disabled="">
<span class="material-symbols-outlined">chevron_left</span>
</button>
<button class="px-3 py-1 rounded bg-primary text-on-primary font-data-mono text-data-mono">1</button>
<button class="px-3 py-1 rounded hover:bg-surface-container-highest font-data-mono text-data-mono">2</button>
<button class="px-3 py-1 rounded hover:bg-surface-container-highest font-data-mono text-data-mono">3</button>
<span class="text-secondary px-1">...</span>
<button class="px-3 py-1 rounded hover:bg-surface-container-highest font-data-mono text-data-mono">491</button>
<button class="p-1 rounded hover:bg-surface-container-highest transition-colors">
<span class="material-symbols-outlined">chevron_right</span>
</button>
</div>
</div>
</div>
<!-- Strategy Insights (Asymmetric Layout Extra) -->
<div class="grid grid-cols-1 lg:grid-cols-12 gap-6 pb-margin-desktop">
<div class="lg:col-span-8 bg-surface-container-lowest border border-outline-variant rounded-xl p-6 relative overflow-hidden">
<div class="relative z-10">
<h3 class="font-headline-sm text-headline-sm text-on-surface mb-2">Efficiency Analysis</h3>
<p class="font-body-md text-body-md text-secondary max-w-lg mb-6">Your 'Exact' match terms are performing with 18% higher efficiency than Broad discovery keywords. Consider moving high-performing Broad terms to Exact campaigns.</p>
<div class="flex gap-4">
<button class="px-4 py-2 bg-secondary-container text-on-secondary-container rounded-lg font-body-sm font-semibold">View Harvested Terms</button>
<button class="px-4 py-2 border border-outline-variant rounded-lg font-body-sm font-semibold hover:bg-surface-container transition-colors">Automate Rule</button>
</div>
</div>
<!-- Decorative Graphic -->
<div class="absolute right-0 top-0 w-1/3 h-full opacity-10 flex items-center justify-center">
<span class="material-symbols-outlined text-[120px] text-primary" style="font-variation-settings: 'FILL' 1;">trending_up</span>
</div>
</div>
<div class="lg:col-span-4 bg-[#001f26] rounded-xl p-6 text-white shadow-lg flex flex-col justify-between">
<div>
<div class="flex items-center gap-2 mb-4">
<span class="material-symbols-outlined text-tertiary-fixed">tips_and_updates</span>
<span class="font-label-caps text-label-caps tracking-widest text-tertiary-fixed">QUICK ACTION</span>
</div>
<h4 class="font-headline-sm text-headline-sm mb-2 leading-tight">Wasted Spend Detected</h4>
<p class="font-body-sm text-body-sm text-tertiary-fixed/80">14 Search Terms have spent &gt;$50 with 0 sales in the last 30 days.</p>
</div>
<button class="w-full mt-6 py-3 bg-tertiary-container text-on-tertiary-container rounded-lg font-bold hover:scale-[1.02] active:scale-[0.98] transition-all">Review Negatives</button>
</div>
</div>
</div>
</main>
<script>
        // Micro-interaction for KPI cards hover depth
        document.querySelectorAll('.kpi-card').forEach(card => {
            card.addEventListener('mouseenter', () => {
                card.style.borderColor = '#8a5100';
            });
            card.addEventListener('mouseleave', () => {
                card.style.borderColor = '#E0E3E3';
            });
        });

        // Simple tab visual interaction
        document.querySelectorAll('nav a').forEach(link => {
            if (!link.classList.contains('bg-secondary-container')) {
                link.addEventListener('mouseenter', () => {
                    link.style.transform = 'translateX(4px)';
                });
                link.addEventListener('mouseleave', () => {
                    link.style.transform = 'translateX(0)';
                });
            }
        });
    </script>


</body></html>

<!-- Search Terms - Performance Management -->
<!DOCTYPE html><html class="light" lang="en"><head>
<meta charset="utf-8">
<meta content="width=device-width, initial-scale=1.0" name="viewport">
<title>ASIN Targets | AdTracker Pro</title>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&amp;family=JetBrains+Mono:wght@500&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<style>
        .material-symbols-outlined {
            font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
        }
        .custom-scrollbar::-webkit-scrollbar {
            width: 4px;
            height: 4px;
        }
        .custom-scrollbar::-webkit-scrollbar-track {
            background: transparent;
        }
        .custom-scrollbar::-webkit-scrollbar-thumb {
            background: #e1e3e3;
            border-radius: 10px;
        }
        .custom-scrollbar::-webkit-scrollbar-thumb:hover {
            background: #887361;
        }
    </style>
<script id="tailwind-config">
        tailwind.config = {
            darkMode: "class",
            theme: {
                extend: {
                    "colors": {
                        "secondary": "#535f70",
                        "primary-fixed": "#ffdcbd",
                        "background": "#f8fafa",
                        "on-secondary-fixed": "#101c2b",
                        "error-container": "#ffdad6",
                        "primary-container": "#ff9900",
                        "surface-container": "#eceeee",
                        "outline-variant": "#dbc2ad",
                        "outline": "#887361",
                        "surface-container-low": "#f2f4f4",
                        "on-tertiary-fixed-variant": "#004e5d",
                        "on-background": "#191c1d",
                        "inverse-on-surface": "#eff1f1",
                        "tertiary-container": "#6abdd3",
                        "on-primary-fixed": "#2c1600",
                        "on-error": "#ffffff",
                        "inverse-primary": "#ffb86f",
                        "surface-variant": "#e1e3e3",
                        "secondary-container": "#d4e1f5",
                        "primary-fixed-dim": "#ffb86f",
                        "tertiary": "#00687a",
                        "surface-container-highest": "#e1e3e3",
                        "secondary-fixed": "#d7e3f7",
                        "on-surface-variant": "#554434",
                        "tertiary-fixed-dim": "#80d2e9",
                        "on-tertiary-container": "#004b59",
                        "surface": "#f8fafa",
                        "on-tertiary-fixed": "#001f26",
                        "on-surface": "#191c1d",
                        "on-error-container": "#93000a",
                        "on-secondary": "#ffffff",
                        "on-primary": "#ffffff",
                        "surface-bright": "#f8fafa",
                        "on-secondary-container": "#576474",
                        "on-tertiary": "#ffffff",
                        "error": "#ba1a1a",
                        "tertiary-fixed": "#adecff",
                        "primary": "#8a5100",
                        "on-primary-fixed-variant": "#693c00",
                        "inverse-surface": "#2e3131",
                        "surface-dim": "#d8dada",
                        "surface-container-lowest": "#ffffff",
                        "secondary-fixed-dim": "#bbc7db",
                        "on-primary-container": "#653a00",
                        "on-secondary-fixed-variant": "#3c4858",
                        "surface-container-high": "#e6e8e8",
                        "surface-tint": "#8a5100"
                    },
                    "borderRadius": {
                        "DEFAULT": "0.125rem",
                        "lg": "0.25rem",
                        "xl": "0.5rem",
                        "full": "0.75rem"
                    },
                    "spacing": {
                        "max-width": "1440px",
                        "margin-desktop": "32px",
                        "container-padding": "24px",
                        "gutter": "16px",
                        "margin-mobile": "16px",
                        "unit": "4px"
                    },
                    "fontFamily": {
                        "label-caps": ["Inter"],
                        "headline-sm": ["Inter"],
                        "body-sm": ["Inter"],
                        "data-mono": ["JetBrains Mono"],
                        "body-md": ["Inter"],
                        "display-md": ["Inter"],
                        "display-lg": ["Inter"],
                        "body-lg": ["Inter"]
                    },
                    "fontSize": {
                        "label-caps": ["11px", {"lineHeight": "16px", "letterSpacing": "0.05em", "fontWeight": "700"}],
                        "headline-sm": ["18px", {"lineHeight": "24px", "fontWeight": "600"}],
                        "body-sm": ["12px", {"lineHeight": "16px", "fontWeight": "400"}],
                        "data-mono": ["13px", {"lineHeight": "18px", "fontWeight": "500"}],
                        "body-md": ["14px", {"lineHeight": "20px", "fontWeight": "400"}],
                        "display-md": ["24px", {"lineHeight": "32px", "letterSpacing": "-0.01em", "fontWeight": "600"}],
                        "display-lg": ["32px", {"lineHeight": "40px", "letterSpacing": "-0.02em", "fontWeight": "700"}],
                        "body-lg": ["16px", {"lineHeight": "24px", "fontWeight": "400"}]
                    }
                }
            }
        }
    </script>
</head>
<body class="bg-background text-on-surface font-body-md overflow-hidden flex h-screen">
<!-- Sidebar Navigation -->
<aside class="flex flex-col h-full py-4 px-2 gap-1 bg-surface-container-lowest border-r border-outline-variant w-64 shrink-0 overflow-y-auto custom-scrollbar">
<div class="px-4 mb-6">
<h1 class="font-headline-sm text-headline-sm font-black text-on-surface">AdTracker Pro</h1>
<p class="text-[10px] uppercase tracking-widest text-secondary font-bold opacity-70">PPC Performance</p>
</div>
<nav class="flex flex-col gap-0.5">
<!-- Navigation Items Mapping -->
<a class="flex items-center gap-3 px-4 py-2.5 text-secondary transition-all group hover:bg-tertiary-container/20" href="#">
<span class="material-symbols-outlined text-[20px]">dashboard</span>
<span class="font-label-caps text-label-caps">Dashboard</span>
</a>
<a class="flex items-center gap-3 px-4 py-2.5 text-secondary transition-all group hover:bg-tertiary-container/20" href="#">
<span class="material-symbols-outlined text-[20px]">campaign</span>
<span class="font-label-caps text-label-caps">Campaigns</span>
</a>
<a class="flex items-center gap-3 px-4 py-2.5 text-secondary transition-all group hover:bg-tertiary-container/20" href="#">
<span class="material-symbols-outlined text-[20px]">inventory_2</span>
<span class="font-label-caps text-label-caps">Products</span>
</a>
<a class="flex items-center gap-3 px-4 py-2.5 text-secondary transition-all group hover:bg-tertiary-container/20" href="#">
<span class="material-symbols-outlined text-[20px]">analytics</span>
<span class="font-label-caps text-label-caps">Match Type</span>
</a>
<a class="flex items-center gap-3 px-4 py-2.5 text-secondary transition-all group hover:bg-tertiary-container/20" href="#">
<span class="material-symbols-outlined text-[20px]">key</span>
<span class="font-label-caps text-label-caps">Keywords</span>
</a>
<a class="flex items-center gap-3 px-4 py-2.5 text-secondary transition-all group hover:bg-tertiary-container/20" href="#">
<span class="material-symbols-outlined text-[20px]">manage_search</span>
<span class="font-label-caps text-label-caps">Search Terms</span>
</a>
<!-- Active Tab: ASIN Targets -->
<a class="flex items-center gap-3 px-4 py-2.5 font-bold rounded-lg scale-[0.98] bg-tertiary-container text-on-tertiary-container" href="#">
<span class="material-symbols-outlined text-[20px]">track_changes</span>
<span class="font-label-caps text-label-caps">ASIN Targets</span>
</a>
<a class="flex items-center gap-3 px-4 py-2.5 text-secondary transition-all group hover:bg-tertiary-container/20" href="#">
<span class="material-symbols-outlined text-[20px]">troubleshoot</span>
<span class="font-label-caps text-label-caps">ASIN from STR</span>
</a>
<a class="flex items-center gap-3 px-4 py-2.5 text-secondary transition-all group hover:bg-tertiary-container/20" href="#">
<span class="material-symbols-outlined text-[20px]">smart_toy</span>
<span class="font-label-caps text-label-caps">Auto Campaigns</span>
</a>
<a class="flex items-center gap-3 px-4 py-2.5 text-secondary transition-all group hover:bg-tertiary-container/20" href="#">
<span class="material-symbols-outlined text-[20px]">category</span>
<span class="font-label-caps text-label-caps">Category Targets</span>
</a>
<a class="flex items-center gap-3 px-4 py-2.5 text-secondary transition-all group hover:bg-tertiary-container/20" href="#">
<span class="material-symbols-outlined text-[20px]">money_off</span>
<span class="font-label-caps text-label-caps">Wasted Ad Spend</span>
</a>
</nav>
<div class="mt-auto px-4 py-4 border-t border-outline-variant">
<div class="flex items-center gap-3">
<img alt="Account settings" class="w-8 h-8 rounded-full bg-surface-container-high" src="https://lh3.googleusercontent.com/aida-public/AB6AXuBKbZlSCZIniGeo_Kr3AturHZ10YWhkstSYitPtBSr_8uGfxW5t8vNtahcxpprsQGf0cByurgXubAvQPSo4zJN7L6qQyn40kzOpAudHJ32JjXEKcVg-7JhjoBseeS15zBM6xnh7d3XnprvNbGsE9mjjR5L3Una4Sq82vnZDMY5GQUe6eGL5BVg_6nG3aBDandiX28ZtnHV5o-pM-5vCWRw2rLK1z02mRML3tpk6T0Tif36mMK9V5RH7ZNRUy8tO-5xYoTZrzgQj">
<div class="overflow-hidden">
<p class="text-body-sm font-bold truncate">Premium Seller</p>
<p class="text-[10px] text-secondary truncate">Global Marketplace</p>
</div>
</div>
</div>
</aside>
<!-- Main Content Canvas -->
<main class="flex-1 flex flex-col overflow-hidden">
<!-- Top App Bar -->
<header class="flex justify-between items-center w-full px-margin-desktop h-16 bg-surface border-b border-outline-variant shrink-0">
<div class="flex items-center gap-6">
<h2 class="font-headline-sm text-headline-sm font-bold text-primary">ASIN Targets</h2>
<div class="flex items-center gap-2 bg-surface-container-low px-3 py-1.5 rounded-lg border border-outline-variant">
<span class="material-symbols-outlined text-[18px] text-secondary">calendar_today</span>
<span class="font-label-caps text-label-caps text-on-surface">Last 30 Days</span>
</div>
</div>
<div class="flex items-center gap-4">
<div class="relative">
<span class="absolute left-3 top-1/2 -translate-y-1/2 material-symbols-outlined text-secondary text-[20px]">search</span>
<input class="bg-surface-container-low border border-outline-variant rounded-lg pl-10 pr-4 py-1.5 text-body-sm w-64 focus:ring-2 focus:ring-tertiary focus:border-transparent outline-none transition-all" placeholder="Search ASIN or Campaign..." type="text">
</div>
<button class="material-symbols-outlined p-2 text-secondary hover:bg-surface-container-low rounded-full transition-colors">notifications</button>
<button class="material-symbols-outlined p-2 text-secondary hover:bg-surface-container-low rounded-full transition-colors">settings</button>
</div>
</header>
<!-- Scrollable Body -->
<div class="flex-1 overflow-y-auto custom-scrollbar p-gutter md:p-margin-desktop space-y-6">
<!-- KPI Summary Grid (13 Core Metrics) -->
<section class="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-7 gap-3">
<!-- Row 1 -->
<div class="bg-surface-container-lowest border border-outline-variant p-3 flex flex-col justify-between hover:shadow-sm transition-shadow">
<span class="font-label-caps text-label-caps text-secondary">Impressions</span>
<div class="mt-1 flex items-baseline gap-2">
<span class="font-data-mono text-display-md text-on-surface">1.2M</span>
<span class="text-[10px] text-error font-bold flex items-center">-2.4%</span>
</div>
</div>
<div class="bg-surface-container-lowest border border-outline-variant p-3 flex flex-col justify-between">
<span class="font-label-caps text-label-caps text-secondary">Clicks</span>
<div class="mt-1 flex items-baseline gap-2">
<span class="font-data-mono text-display-md text-on-surface">42.8K</span>
<span class="text-[10px] text-tertiary font-bold flex items-center">+5.1%</span>
</div>
</div>
<div class="bg-surface-container-lowest border border-outline-variant p-3 flex flex-col justify-between">
<span class="font-label-caps text-label-caps text-secondary">CTR</span>
<div class="mt-1 flex items-baseline gap-2">
<span class="font-data-mono text-display-md text-on-surface">3.57%</span>
</div>
</div>
<div class="bg-surface-container-lowest border border-outline-variant p-3 flex flex-col justify-between">
<span class="font-label-caps text-label-caps text-secondary">CVR</span>
<div class="mt-1 flex items-baseline gap-2">
<span class="font-data-mono text-display-md text-on-surface">12.4%</span>
</div>
</div>
<div class="bg-surface-container-lowest border border-outline-variant p-3 flex flex-col justify-between">
<span class="font-label-caps text-label-caps text-secondary">CPC</span>
<div class="mt-1 flex items-baseline gap-2">
<span class="font-data-mono text-display-md text-on-surface">$0.84</span>
</div>
</div>
<div class="bg-surface-container-lowest border border-outline-variant p-3 flex flex-col justify-between">
<span class="font-label-caps text-label-caps text-secondary">Spend</span>
<div class="mt-1 flex items-baseline gap-2">
<span class="font-data-mono text-display-md text-on-surface">$35.9K</span>
<span class="text-[10px] text-error font-bold flex items-center">+$1.2K</span>
</div>
</div>
<div class="bg-surface-container-lowest border border-outline-variant p-3 flex flex-col justify-between">
<span class="font-label-caps text-label-caps text-secondary">Sales</span>
<div class="mt-1 flex items-baseline gap-2">
<span class="font-data-mono text-display-md text-on-surface">$142K</span>
<span class="text-[10px] text-tertiary font-bold flex items-center">+$8.4K</span>
</div>
</div>
<!-- Row 2 (Remaining 6) -->
<div class="bg-surface-container-lowest border border-outline-variant p-3 flex flex-col justify-between">
<span class="font-label-caps text-label-caps text-secondary">Orders</span>
<div class="mt-1 flex items-baseline gap-2">
<span class="font-data-mono text-display-md text-on-surface">5,310</span>
</div>
</div>
<div class="bg-surface-container-lowest border border-outline-variant p-3 flex flex-col justify-between">
<span class="font-label-caps text-label-caps text-secondary">Units</span>
<div class="mt-1 flex items-baseline gap-2">
<span class="font-data-mono text-display-md text-on-surface">5,842</span>
</div>
</div>
<div class="bg-surface-container-lowest border border-outline-variant p-3 flex flex-col justify-between ring-1 ring-tertiary/20">
<span class="font-label-caps text-label-caps text-tertiary">ACOS</span>
<div class="mt-1 flex items-baseline gap-2">
<span class="font-data-mono text-display-md text-on-surface">25.3%</span>
<div class="h-2 w-2 rounded-full bg-tertiary-container"></div>
</div>
</div>
<div class="bg-surface-container-lowest border border-outline-variant p-3 flex flex-col justify-between ring-1 ring-tertiary/20">
<span class="font-label-caps text-label-caps text-tertiary">ROAS</span>
<div class="mt-1 flex items-baseline gap-2">
<span class="font-data-mono text-display-md text-on-surface">3.95</span>
</div>
</div>
<div class="bg-surface-container-lowest border border-outline-variant p-3 flex flex-col justify-between">
<span class="font-label-caps text-label-caps text-secondary">Spend % Split</span>
<div class="mt-1 flex items-baseline gap-2">
<span class="font-data-mono text-display-md text-on-surface">22%</span>
</div>
</div>
<div class="bg-surface-container-lowest border border-outline-variant p-3 flex flex-col justify-between">
<span class="font-label-caps text-label-caps text-secondary">Sales % Split</span>
<div class="mt-1 flex items-baseline gap-2">
<span class="font-data-mono text-display-md text-on-surface">28%</span>
</div>
</div>
<div class="bg-primary-container p-3 flex flex-col justify-center items-center cursor-pointer hover:bg-orange-500 transition-colors">
<span class="material-symbols-outlined text-on-primary-container">add_circle</span>
<span class="font-label-caps text-label-caps text-on-primary-container mt-1">Add Target</span>
</div>
</section>
<!-- Table Filters -->
<section class="flex flex-wrap items-center justify-between gap-4">
<div class="flex items-center gap-3">
<div class="flex items-center gap-2">
<span class="text-body-sm font-bold text-secondary">Portfolio:</span>
<select class="bg-surface-container-lowest border border-outline-variant rounded px-3 py-1.5 text-body-sm outline-none focus:border-primary transition-colors">
<option>All Portfolios</option>
<option>Summer Collection</option>
<option>Kitchen Gadgets</option>
</select>
</div>
<div class="flex items-center gap-2">
<span class="text-body-sm font-bold text-secondary">Metrics:</span>
<button class="bg-surface-container-lowest border border-outline-variant rounded px-3 py-1.5 text-body-sm flex items-center gap-2">
                            Custom View <span class="material-symbols-outlined text-[16px]">tune</span>
</button>
</div>
</div>
<div class="flex items-center gap-2">
<button class="flex items-center gap-2 px-4 py-2 border border-outline-variant text-body-sm font-bold text-secondary hover:bg-surface-container-low transition-colors">
<span class="material-symbols-outlined text-[18px]">download</span> Export CSV
                    </button>
<button class="flex items-center gap-2 px-4 py-2 bg-primary text-white text-body-sm font-bold hover:opacity-90 transition-opacity">
<span class="material-symbols-outlined text-[18px]">bolt</span> Bulk Actions
                    </button>
</div>
</section>
<!-- Data Table Container -->
<section class="bg-surface-container-lowest border border-outline-variant overflow-hidden">
<div class="overflow-x-auto custom-scrollbar">
<table class="w-full text-left border-collapse min-w-[1800px]">
<thead>
<tr class="bg-surface-container-low border-b border-outline-variant">
<th class="p-3 w-10"><input class="rounded-sm border-outline" type="checkbox"></th>
<th class="p-3 font-label-caps text-label-caps text-secondary sticky left-0 bg-surface-container-low z-10">ASIN / Product Target</th>
<th class="p-3 font-label-caps text-label-caps text-secondary">Campaign / Portfolio</th>
<th class="p-3 font-label-caps text-label-caps text-secondary text-right">Imp</th>
<th class="p-3 font-label-caps text-label-caps text-secondary text-right">Clicks</th>
<th class="p-3 font-label-caps text-label-caps text-secondary text-right">CTR</th>
<th class="p-3 font-label-caps text-label-caps text-secondary text-right">CPC</th>
<th class="p-3 font-label-caps text-label-caps text-secondary text-right">Spend</th>
<th class="p-3 font-label-caps text-label-caps text-secondary text-right">Sales</th>
<th class="p-3 font-label-caps text-label-caps text-secondary text-right">Orders</th>
<th class="p-3 font-label-caps text-label-caps text-secondary text-right">ACOS</th>
<th class="p-3 font-label-caps text-label-caps text-secondary text-right">ROAS</th>
<th class="p-3 font-label-caps text-label-caps text-secondary text-right">CVR</th>
<th class="p-3 font-label-caps text-label-caps text-secondary text-right">Units</th>
<th class="p-3 font-label-caps text-label-caps text-secondary text-right">Sp%</th>
<th class="p-3 font-label-caps text-label-caps text-secondary text-right">Sa%</th>
<th class="p-3 w-12"></th>
</tr>
</thead>
<tbody class="divide-y divide-outline-variant/50">
<!-- Row 1 -->
<tr class="hover:bg-surface-container-low/50 transition-colors group">
<td class="p-3"><input class="rounded-sm border-outline" type="checkbox"></td>
<td class="p-3 sticky left-0 bg-white group-hover:bg-surface-container-low/50 z-10">
<div class="flex items-center gap-3">
<div class="w-10 h-10 bg-surface-container rounded border border-outline-variant flex-shrink-0 overflow-hidden">
<img class="w-full h-full object-cover" data-alt="A professional high-resolution product studio shot of a sleek kitchen gadget against a neutral grey background. The lighting is crisp and commercial, emphasizing metallic textures and ergonomic design. The composition is centered and balanced, fitting a high-end Amazon product listing aesthetic with clean, professional light-mode UI colors." src="https://lh3.googleusercontent.com/aida-public/AB6AXuBEiz2pIl6kq3fCenaUi9srFth9LczhbwYlzJl_4FV0P6SS5R-m5CsUHWbcuC2rot-sKhzKCVF0Q4t5m6WRhCfKaH9FBX8rGDFE2wLjrP1K8wZxwPWWDSm8TW_0S_TVLeJNQlxJlwikRuBa-g7IQjXzn6g7ngJekrdIkHt3TL1yg8USaXkvg-4Mh273MnC2kGDPcP1yy3rjmpxUcGUmqEOot-pbhtoqZtVtuYbHPDA9ZKnqGBP1AwSGySf75EguO_DmsTJQ5M72">
</div>
<div>
<p class="font-data-mono text-body-sm font-bold text-primary">B07XQZ4L9Y</p>
<p class="text-[11px] text-secondary truncate max-w-[200px]">Premium Stainless Steel Garlic Press - Ergonomic...</p>
</div>
</div>
</td>
<td class="p-3">
<p class="text-body-sm font-medium">SP_Kitchen_Pro_Targets</p>
<p class="text-[11px] text-secondary">Kitchen Portfolio</p>
</td>
<td class="p-3 text-right font-data-mono text-body-sm">45,201</td>
<td class="p-3 text-right font-data-mono text-body-sm">1,240</td>
<td class="p-3 text-right font-data-mono text-body-sm">2.74%</td>
<td class="p-3 text-right font-data-mono text-body-sm">$0.92</td>
<td class="p-3 text-right font-data-mono text-body-sm font-bold">$1,140.80</td>
<td class="p-3 text-right font-data-mono text-body-sm font-bold text-tertiary">$5,420.00</td>
<td class="p-3 text-right font-data-mono text-body-sm">184</td>
<td class="p-3 text-right font-data-mono text-body-sm">
<span class="px-2 py-0.5 bg-green-100 text-green-800 rounded-full text-[10px] font-bold">21.0%</span>
</td>
<td class="p-3 text-right font-data-mono text-body-sm">4.75</td>
<td class="p-3 text-right font-data-mono text-body-sm">14.8%</td>
<td class="p-3 text-right font-data-mono text-body-sm">210</td>
<td class="p-3 text-right font-data-mono text-body-sm">12.5%</td>
<td class="p-3 text-right font-data-mono text-body-sm">15.2%</td>
<td class="p-3 text-right">
<button class="material-symbols-outlined text-secondary opacity-0 group-hover:opacity-100 transition-opacity">more_vert</button>
</td>
</tr>
<!-- Row 2 -->
<tr class="bg-surface-container-low/20 hover:bg-surface-container-low/50 transition-colors group">
<td class="p-3"><input class="rounded-sm border-outline" type="checkbox"></td>
<td class="p-3 sticky left-0 bg-white/50 group-hover:bg-surface-container-low/50 z-10">
<div class="flex items-center gap-3">
<div class="w-10 h-10 bg-surface-container rounded border border-outline-variant flex-shrink-0 overflow-hidden">
<img class="w-full h-full object-cover" data-alt="A lifestyle product photograph of a non-stick frying pan being used on a modern induction stovetop. The scene is bright and airy with soft morning light filtering through a nearby window. The aesthetic is clean, minimalist, and upscale, following a corporate modern design system. The colors are dominated by soft whites, cool greys, and subtle metallic glints." src="https://lh3.googleusercontent.com/aida-public/AB6AXuAKImhMB7qmKnuNimSlA9cTlD1n7GbEfPPH6KerV-w0U4ItuBl-HllUIa0UyqSQy9wguSDn3QmSkXuC94Qlt2td2Peyw-lVItsfLNDVqJA-tP3Xb2XDW-nm26KRnDsizdnaR9bqN-z4gR7IGodxw7Ldq-qzfo2sGB-4LyDI5bTpzERTJ4lGK1XrBKrEYnnUONW-uRrmaW5R_QktrtGw9wZjLnumNZCxewipOp7eGfbcQa7cnlNm7180buUeQQfO70aiu66qYw8Q">
</div>
<div>
<p class="font-data-mono text-body-sm font-bold text-primary">B082Y3K4M2</p>
<p class="text-[11px] text-secondary truncate max-w-[200px]">Non-Stick Ceramic Frying Pan - 12 Inch...</p>
</div>
</div>
</td>
<td class="p-3">
<p class="text-body-sm font-medium">SP_Cookware_Exact</p>
<p class="text-[11px] text-secondary">Kitchen Portfolio</p>
</td>
<td class="p-3 text-right font-data-mono text-body-sm">12,104</td>
<td class="p-3 text-right font-data-mono text-body-sm">542</td>
<td class="p-3 text-right font-data-mono text-body-sm">4.48%</td>
<td class="p-3 text-right font-data-mono text-body-sm">$1.24</td>
<td class="p-3 text-right font-data-mono text-body-sm font-bold">$672.08</td>
<td class="p-3 text-right font-data-mono text-body-sm font-bold text-tertiary">$1,840.50</td>
<td class="p-3 text-right font-data-mono text-body-sm">42</td>
<td class="p-3 text-right font-data-mono text-body-sm">
<span class="px-2 py-0.5 bg-yellow-100 text-yellow-800 rounded-full text-[10px] font-bold">36.5%</span>
</td>
<td class="p-3 text-right font-data-mono text-body-sm">2.74</td>
<td class="p-3 text-right font-data-mono text-body-sm">7.7%</td>
<td class="p-3 text-right font-data-mono text-body-sm">45</td>
<td class="p-3 text-right font-data-mono text-body-sm">8.2%</td>
<td class="p-3 text-right font-data-mono text-body-sm">6.1%</td>
<td class="p-3 text-right">
<button class="material-symbols-outlined text-secondary opacity-0 group-hover:opacity-100 transition-opacity">more_vert</button>
</td>
</tr>
<!-- Row 3 -->
<tr class="hover:bg-surface-container-low/50 transition-colors group">
<td class="p-3"><input class="rounded-sm border-outline" type="checkbox"></td>
<td class="p-3 sticky left-0 bg-white group-hover:bg-surface-container-low/50 z-10">
<div class="flex items-center gap-3">
<div class="w-10 h-10 bg-surface-container rounded border border-outline-variant flex-shrink-0 overflow-hidden">
<img class="w-full h-full object-cover" data-alt="A cinematic close-up of a professional chef's knife resting on a dark walnut cutting board. The lighting is dramatic and precise, highlighting the Damascus steel pattern on the blade. The background is a blurred high-end modern kitchen. The image exudes authority, precision, and luxury, consistent with a high-performance advertising dashboard aesthetic." src="https://lh3.googleusercontent.com/aida-public/AB6AXuD6cHoEQVYlMGD54B0APZaH6lssJX8F12hKbUQTzc36_kVDGOFHZ7OL7iEICo6h1eGetQ-7SJl2ZEHSjSalBOQ2OlSSaes45vZyKlOykRylLr2c9GIqRG8HVtLM-26Lqt_b2XOlPKavNBkLdYVwxwGK55XpB5HXtM7ZprPI3vsAzzpCxU9xNmugdFnVeWtVzsHGMVMPveBlC5LS9PuWE0um1HUUG7GLvcALr0oraYecUt60BvMxeFaBumGqucFAMKRedNOeBEMP">
</div>
<div>
<p class="font-data-mono text-body-sm font-bold text-primary">B09F8G7H6J</p>
<p class="text-[11px] text-secondary truncate max-w-[200px]">8-Piece Professional Knife Set with Block...</p>
</div>
</div>
</td>
<td class="p-3">
<p class="text-body-sm font-medium">SP_Knives_Competitor_ASIN</p>
<p class="text-[11px] text-secondary">Kitchen Portfolio</p>
</td>
<td class="p-3 text-right font-data-mono text-body-sm">8,452</td>
<td class="p-3 text-right font-data-mono text-body-sm">122</td>
<td class="p-3 text-right font-data-mono text-body-sm">1.44%</td>
<td class="p-3 text-right font-data-mono text-body-sm">$2.10</td>
<td class="p-3 text-right font-data-mono text-body-sm font-bold">$256.20</td>
<td class="p-3 text-right font-data-mono text-body-sm font-bold text-error">$180.00</td>
<td class="p-3 text-right font-data-mono text-body-sm">1</td>
<td class="p-3 text-right font-data-mono text-body-sm">
<span class="px-2 py-0.5 bg-red-100 text-red-800 rounded-full text-[10px] font-bold">142.3%</span>
</td>
<td class="p-3 text-right font-data-mono text-body-sm">0.70</td>
<td class="p-3 text-right font-data-mono text-body-sm">0.8%</td>
<td class="p-3 text-right font-data-mono text-body-sm">1</td>
<td class="p-3 text-right font-data-mono text-body-sm">2.1%</td>
<td class="p-3 text-right font-data-mono text-body-sm">0.4%</td>
<td class="p-3 text-right">
<button class="material-symbols-outlined text-secondary opacity-0 group-hover:opacity-100 transition-opacity">more_vert</button>
</td>
</tr>
</tbody>
</table>
</div>
<!-- Table Pagination -->
<div class="flex items-center justify-between px-margin-desktop py-3 bg-surface-container-low border-t border-outline-variant">
<span class="text-body-sm text-secondary">Showing <span class="font-bold text-on-surface">1-50</span> of <span class="font-bold text-on-surface">1,248</span> targets</span>
<div class="flex items-center gap-1">
<button class="p-1 hover:bg-surface-container-highest rounded transition-colors disabled:opacity-30" disabled="">
<span class="material-symbols-outlined">chevron_left</span>
</button>
<button class="px-3 py-1 bg-primary-container text-on-primary-container font-bold text-body-sm rounded">1</button>
<button class="px-3 py-1 hover:bg-surface-container-highest text-body-sm rounded">2</button>
<button class="px-3 py-1 hover:bg-surface-container-highest text-body-sm rounded">3</button>
<span class="px-2">...</span>
<button class="px-3 py-1 hover:bg-surface-container-highest text-body-sm rounded">25</button>
<button class="p-1 hover:bg-surface-container-highest rounded transition-colors">
<span class="material-symbols-outlined">chevron_right</span>
</button>
</div>
</div>
</section>
</div>
<!-- Float Action Button (Contextual for ASIN Target creation) -->
<button class="fixed bottom-8 right-8 bg-primary-container text-on-primary-container w-14 h-14 rounded-full shadow-lg flex items-center justify-center hover:scale-105 transition-transform active:scale-95 group">
<span class="material-symbols-outlined text-[32px]">add</span>
<span class="absolute right-16 bg-on-surface text-white px-3 py-1 text-label-caps rounded whitespace-nowrap opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none">NEW ASIN TARGET</span>
</button>
</main>
<script>
        // Simple Micro-interaction for table row checkboxes
        document.querySelectorAll('input[type="checkbox"]').forEach(checkbox => {
            checkbox.addEventListener('change', function() {
                const row = this.closest('tr');
                if (row) {
                    if (this.checked) {
                        row.classList.add('bg-primary-container/10');
                    } else {
                        row.classList.remove('bg-primary-container/10');
                    }
                }
            });
        });

        // Search Bar Focus Effect
        const searchInput = document.querySelector('input[type="text"]');
        searchInput.addEventListener('focus', () => {
            searchInput.classList.add('w-80');
        });
        searchInput.addEventListener('blur', () => {
            searchInput.classList.remove('w-80');
        });
    </script>


</body></html>

<!-- ASIN Targets - Performance Management -->
<!DOCTYPE html><html class="light" lang="en"><head>
<meta charset="utf-8">
<meta content="width=device-width, initial-scale=1.0" name="viewport">
<title>ASIN from STR Performance | AdTracker Pro</title>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&amp;family=JetBrains+Mono:wght@500&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<script id="tailwind-config">
        tailwind.config = {
            darkMode: "class",
            theme: {
                extend: {
                    "colors": {
                        "surface-bright": "#f8fafa",
                        "on-tertiary-container": "#004b59",
                        "surface-container-lowest": "#ffffff",
                        "on-secondary-container": "#576474",
                        "surface-dim": "#d8dada",
                        "on-secondary-fixed": "#101c2b",
                        "on-error-container": "#93000a",
                        "on-tertiary-fixed": "#001f26",
                        "on-primary-container": "#653a00",
                        "secondary-fixed": "#d7e3f7",
                        "on-primary-fixed": "#2c1600",
                        "inverse-on-surface": "#eff1f1",
                        "secondary-fixed-dim": "#bbc7db",
                        "surface-container-highest": "#e1e3e3",
                        "secondary-container": "#d4e1f5",
                        "tertiary": "#00687a",
                        "primary": "#8a5100",
                        "on-primary": "#ffffff",
                        "primary-container": "#ff9900",
                        "on-secondary-fixed-variant": "#3c4858",
                        "on-error": "#ffffff",
                        "on-primary-fixed-variant": "#693c00",
                        "surface-container-high": "#e6e8e8",
                        "surface-container": "#eceeee",
                        "on-tertiary-fixed-variant": "#004e5d",
                        "primary-fixed-dim": "#ffb86f",
                        "on-tertiary": "#ffffff",
                        "error": "#ba1a1a",
                        "on-background": "#191c1d",
                        "tertiary-fixed": "#adecff",
                        "surface-container-low": "#f2f4f4",
                        "on-surface-variant": "#554434",
                        "inverse-surface": "#2e3131",
                        "inverse-primary": "#ffb86f",
                        "background": "#f8fafa",
                        "on-surface": "#191c1d",
                        "tertiary-fixed-dim": "#80d2e9",
                        "secondary": "#535f70",
                        "outline-variant": "#dbc2ad",
                        "on-secondary": "#ffffff",
                        "error-container": "#ffdad6",
                        "tertiary-container": "#6abdd3",
                        "outline": "#887361",
                        "surface-tint": "#8a5100",
                        "surface-variant": "#e1e3e3",
                        "surface": "#f8fafa",
                        "primary-fixed": "#ffdcbd"
                    },
                    "borderRadius": {
                        "DEFAULT": "0.125rem",
                        "lg": "0.25rem",
                        "xl": "0.5rem",
                        "full": "0.75rem"
                    },
                    "spacing": {
                        "max-width": "1440px",
                        "margin-desktop": "32px",
                        "unit": "4px",
                        "container-padding": "24px",
                        "margin-mobile": "16px",
                        "gutter": "16px"
                    },
                    "fontFamily": {
                        "data-mono": ["JetBrains Mono"],
                        "label-caps": ["Inter"],
                        "body-md": ["Inter"],
                        "headline-sm": ["Inter"],
                        "display-lg": ["Inter"],
                        "display-md": ["Inter"],
                        "body-lg": ["Inter"],
                        "body-sm": ["Inter"]
                    },
                    "fontSize": {
                        "data-mono": ["13px", {"lineHeight": "18px", "fontWeight": "500"}],
                        "label-caps": ["11px", {"lineHeight": "16px", "letterSpacing": "0.05em", "fontWeight": "700"}],
                        "body-md": ["14px", {"lineHeight": "20px", "fontWeight": "400"}],
                        "headline-sm": ["18px", {"lineHeight": "24px", "fontWeight": "600"}],
                        "display-lg": ["32px", {"lineHeight": "40px", "letterSpacing": "-0.02em", "fontWeight": "700"}],
                        "display-md": ["24px", {"lineHeight": "32px", "letterSpacing": "-0.01em", "fontWeight": "600"}],
                        "body-lg": ["16px", {"lineHeight": "24px", "fontWeight": "400"}],
                        "body-sm": ["12px", {"lineHeight": "16px", "fontWeight": "400"}]
                    }
                },
            },
        }
    </script>
<style>
        .material-symbols-outlined {
            font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
            display: inline-block;
            vertical-align: middle;
        }
        .custom-scrollbar::-webkit-scrollbar {
            width: 6px;
            height: 6px;
        }
        .custom-scrollbar::-webkit-scrollbar-track {
            background: transparent;
        }
        .custom-scrollbar::-webkit-scrollbar-thumb {
            background: #e1e3e3;
            border-radius: 10px;
        }
        .custom-scrollbar::-webkit-scrollbar-thumb:hover {
            background: #887361;
        }
        tr:nth-child(even) {
            background-color: #f8fafa;
        }
    </style>
</head>
<body class="bg-background text-on-surface font-body-md overflow-hidden">
<div class="flex h-screen overflow-hidden">
<!-- Sidebar Navigation -->
<aside class="bg-surface-container-lowest border-r border-surface-container-highest w-64 flex flex-col h-screen flex-shrink-0 z-50">
<div class="p-6 flex flex-col gap-1">
<span class="font-display-md text-display-md font-bold text-primary">AdTracker Pro</span>
<span class="font-body-sm text-body-sm text-on-secondary-container">Global PPC Manager</span>
</div>
<nav class="flex-1 px-4 py-2 space-y-1 overflow-y-auto custom-scrollbar">
<!-- Dashboard -->
<a class="flex items-center px-3 py-2 text-on-surface-variant hover:bg-surface-container-high transition-colors rounded-lg group" href="#">
<span class="material-symbols-outlined mr-3 group-hover:text-primary" data-icon="dashboard">dashboard</span>
<span class="font-body-sm text-body-sm">Dashboard</span>
</a>
<!-- Campaigns -->
<a class="flex items-center px-3 py-2 text-on-surface-variant hover:bg-surface-container-high transition-colors rounded-lg group" href="#">
<span class="material-symbols-outlined mr-3 group-hover:text-primary" data-icon="campaign">campaign</span>
<span class="font-body-sm text-body-sm">Campaigns</span>
</a>
<!-- Products -->
<a class="flex items-center px-3 py-2 text-on-surface-variant hover:bg-surface-container-high transition-colors rounded-lg group" href="#">
<span class="material-symbols-outlined mr-3 group-hover:text-primary" data-icon="inventory_2">inventory_2</span>
<span class="font-body-sm text-body-sm">Products</span>
</a>
<!-- Match Type -->
<a class="flex items-center px-3 py-2 text-on-surface-variant hover:bg-surface-container-high transition-colors rounded-lg group" href="#">
<span class="material-symbols-outlined mr-3 group-hover:text-primary" data-icon="compare_arrows">compare_arrows</span>
<span class="font-body-sm text-body-sm">Match Type</span>
</a>
<!-- Keywords -->
<a class="flex items-center px-3 py-2 text-on-surface-variant hover:bg-surface-container-high transition-colors rounded-lg group" href="#">
<span class="material-symbols-outlined mr-3 group-hover:text-primary" data-icon="key">key</span>
<span class="font-body-sm text-body-sm">Keywords</span>
</a>
<!-- Search Terms -->
<a class="flex items-center px-3 py-2 text-on-surface-variant hover:bg-surface-container-high transition-colors rounded-lg group" href="#">
<span class="material-symbols-outlined mr-3 group-hover:text-primary" data-icon="manage_search">manage_search</span>
<span class="font-body-sm text-body-sm">Search Terms</span>
</a>
<!-- ASIN Targets -->
<a class="flex items-center px-3 py-2 text-on-surface-variant hover:bg-surface-container-high transition-colors rounded-lg group" href="#">
<span class="material-symbols-outlined mr-3 group-hover:text-primary" data-icon="target">target</span>
<span class="font-body-sm text-body-sm">ASIN Targets</span>
</a>
<!-- ASIN from STR (ACTIVE) -->
<a class="flex items-center px-3 py-2 bg-tertiary-container text-on-tertiary-container font-semibold rounded-lg" href="#">
<span class="material-symbols-outlined mr-3" data-icon="query_stats">query_stats</span>
<span class="font-body-sm text-body-sm">ASIN from STR</span>
</a>
<!-- Auto Campaigns -->
<a class="flex items-center px-3 py-2 text-on-surface-variant hover:bg-surface-container-high transition-colors rounded-lg group" href="#">
<span class="material-symbols-outlined mr-3 group-hover:text-primary" data-icon="smart_toy">smart_toy</span>
<span class="font-body-sm text-body-sm">Auto Campaigns</span>
</a>
<!-- Category Targets -->
<a class="flex items-center px-3 py-2 text-on-surface-variant hover:bg-surface-container-high transition-colors rounded-lg group" href="#">
<span class="material-symbols-outlined mr-3 group-hover:text-primary" data-icon="category">category</span>
<span class="font-body-sm text-body-sm">Category Targets</span>
</a>
<!-- Wasted Ad Spend -->
<a class="flex items-center px-3 py-2 text-on-surface-variant hover:bg-surface-container-high transition-colors rounded-lg group" href="#">
<span class="material-symbols-outlined mr-3 group-hover:text-primary" data-icon="receipt_long">receipt_long</span>
<span class="font-body-sm text-body-sm">Wasted Ad Spend</span>
</a>
</nav>
<div class="p-4 border-t border-surface-container-highest">
<div class="flex items-center gap-3 p-2 rounded-lg bg-surface-container-low">
<img alt="User Profile Avatar" class="w-10 h-10 rounded-full object-cover" data-alt="A professional headshot of a mature business executive in a high-end corporate setting. The person is wearing a tailored charcoal suit and has a confident, warm expression. Background is a soft-focus modern office with glass walls and minimalist furniture, bathed in warm afternoon sunlight and cool professional blue tones." src="https://lh3.googleusercontent.com/aida-public/AB6AXuA0XxKT7WQl193ODmRHcrCOj6CV_Fezbm_502OqHpnWbfFBIVnsjuU1W0w6TDYWt5Sk3XTCQc7z0dcSxxsmAVLuG_KXDv_G1sGZAGzzS2pHZuuhVk_HZDjyNUKNpFgs3YSS6MyhNzHush1l14rNFNN3DyWGmuIs42oEzEjNMM8R174F_4bR40LeAQgsJgOz8fim4w6Nufbg0Ca8CJdnlUfe8G0uezHWcTfOp6I3p7-2QeczPi237B0UurW_5DCXQJElXiiMb84t">
<div class="flex flex-col">
<span class="font-label-caps text-label-caps text-on-surface">Alex Rivera</span>
<span class="text-[10px] uppercase text-on-secondary-container tracking-wider">Account Manager</span>
</div>
</div>
</div>
</aside>
<!-- Main Content Area -->
<main class="flex-1 flex flex-col min-w-0 bg-background overflow-hidden">
<!-- Top App Bar -->
<header class="h-16 flex justify-between items-center px-8 w-full sticky top-0 bg-surface-container-lowest border-b border-surface-container-highest z-40">
<div class="flex items-center gap-6">
<div class="flex flex-col">
<h1 class="font-display-md text-headline-sm font-bold text-primary">ASIN from STR Performance</h1>
<p class="font-body-sm text-[11px] text-on-secondary-container">Analysis of product targets harvested from customer search terms.</p>
</div>
</div>
<div class="flex items-center gap-4">
<!-- Date Picker -->
<div class="flex items-center gap-2 px-3 py-1.5 border border-surface-container-highest rounded bg-white cursor-pointer hover:bg-surface-container-low transition-colors">
<span class="material-symbols-outlined text-[18px]" data-icon="calendar_today">calendar_today</span>
<span class="font-body-sm text-body-sm">Last 30 Days</span>
<span class="material-symbols-outlined text-[16px]" data-icon="expand_more">expand_more</span>
</div>
<button class="flex items-center gap-2 px-4 py-1.5 bg-primary text-on-primary rounded font-semibold hover:opacity-90 transition-all text-body-sm shadow-sm">
<span class="material-symbols-outlined text-[18px]" data-icon="download">download</span>
                        Export
                    </button>
<div class="flex items-center gap-2 ml-4">
<button class="p-2 text-on-secondary-container hover:text-primary transition-colors"><span class="material-symbols-outlined" data-icon="notifications">notifications</span></button>
<button class="p-2 text-on-secondary-container hover:text-primary transition-colors"><span class="material-symbols-outlined" data-icon="settings">settings</span></button>
</div>
</div>
</header>
<!-- Scrollable Content -->
<div class="flex-1 overflow-y-auto custom-scrollbar p-8">
<!-- Metric Summary Grid (13 Metrics) -->
<div class="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-7 xl:grid-cols-13 gap-3 mb-8">
<!-- Metrics repeated 13 times with slight variations -->
<div class="bg-white border border-surface-container-highest p-3 rounded shadow-sm flex flex-col justify-between">
<span class="font-label-caps text-label-caps text-on-secondary-container opacity-70">Impressions</span>
<div class="flex flex-col mt-1">
<span class="font-data-mono text-data-mono text-lg">1,240,812</span>
<span class="text-[10px] text-primary flex items-center"><span class="material-symbols-outlined text-[12px]" data-icon="arrow_upward">arrow_upward</span> 12.4%</span>
</div>
</div>
<div class="bg-white border border-surface-container-highest p-3 rounded shadow-sm flex flex-col justify-between">
<span class="font-label-caps text-label-caps text-on-secondary-container opacity-70">Clicks</span>
<div class="flex flex-col mt-1">
<span class="font-data-mono text-data-mono text-lg">45,102</span>
<span class="text-[10px] text-error flex items-center"><span class="material-symbols-outlined text-[12px]" data-icon="arrow_downward">arrow_downward</span> 2.1%</span>
</div>
</div>
<div class="bg-white border border-surface-container-highest p-3 rounded shadow-sm flex flex-col justify-between">
<span class="font-label-caps text-label-caps text-on-secondary-container opacity-70">CTR</span>
<div class="flex flex-col mt-1">
<span class="font-data-mono text-data-mono text-lg">3.63%</span>
<span class="text-[10px] text-primary flex items-center"><span class="material-symbols-outlined text-[12px]" data-icon="arrow_upward">arrow_upward</span> 0.5%</span>
</div>
</div>
<div class="bg-white border border-surface-container-highest p-3 rounded shadow-sm flex flex-col justify-between">
<span class="font-label-caps text-label-caps text-on-secondary-container opacity-70">CVR</span>
<div class="flex flex-col mt-1">
<span class="font-data-mono text-data-mono text-lg">8.42%</span>
<span class="text-[10px] text-primary flex items-center"><span class="material-symbols-outlined text-[12px]" data-icon="trending_up">trending_up</span> 1.2%</span>
</div>
</div>
<div class="bg-white border border-surface-container-highest p-3 rounded shadow-sm flex flex-col justify-between">
<span class="font-label-caps text-label-caps text-on-secondary-container opacity-70">CPC</span>
<div class="flex flex-col mt-1">
<span class="font-data-mono text-data-mono text-lg">$1.45</span>
<span class="text-[10px] text-on-secondary-container opacity-50">Flat</span>
</div>
</div>
<div class="bg-white border border-surface-container-highest p-3 rounded shadow-sm flex flex-col justify-between">
<span class="font-label-caps text-label-caps text-on-secondary-container opacity-70">Spend</span>
<div class="flex flex-col mt-1">
<span class="font-data-mono text-data-mono text-lg">$65,398</span>
<span class="text-[10px] text-primary flex items-center"><span class="material-symbols-outlined text-[12px]" data-icon="arrow_upward">arrow_upward</span> 8%</span>
</div>
</div>
<div class="bg-white border border-surface-container-highest p-3 rounded shadow-sm flex flex-col justify-between">
<span class="font-label-caps text-label-caps text-on-secondary-container opacity-70">Sales</span>
<div class="flex flex-col mt-1">
<span class="font-data-mono text-data-mono text-lg">$284,510</span>
<span class="text-[10px] text-primary flex items-center"><span class="material-symbols-outlined text-[12px]" data-icon="arrow_upward">arrow_upward</span> 15%</span>
</div>
</div>
<div class="bg-white border border-surface-container-highest p-3 rounded shadow-sm flex flex-col justify-between">
<span class="font-label-caps text-label-caps text-on-secondary-container opacity-70">Orders</span>
<div class="flex flex-col mt-1">
<span class="font-data-mono text-data-mono text-lg">3,797</span>
<span class="text-[10px] text-primary flex items-center"><span class="material-symbols-outlined text-[12px]" data-icon="add">add</span> 410</span>
</div>
</div>
<div class="bg-white border border-surface-container-highest p-3 rounded shadow-sm flex flex-col justify-between">
<span class="font-label-caps text-label-caps text-on-secondary-container opacity-70">Units</span>
<div class="flex flex-col mt-1">
<span class="font-data-mono text-data-mono text-lg">4,212</span>
<span class="text-[10px] text-primary flex items-center"><span class="material-symbols-outlined text-[12px]" data-icon="add">add</span> 502</span>
</div>
</div>
<div class="bg-white border border-surface-container-highest p-3 rounded shadow-sm flex flex-col justify-between border-l-4 border-l-tertiary">
<span class="font-label-caps text-label-caps text-on-secondary-container opacity-70">ACOS</span>
<div class="flex flex-col mt-1">
<span class="font-data-mono text-data-mono text-lg text-tertiary">22.98%</span>
<span class="text-[10px] text-tertiary flex items-center">Efficient</span>
</div>
</div>
<div class="bg-white border border-surface-container-highest p-3 rounded shadow-sm flex flex-col justify-between">
<span class="font-label-caps text-label-caps text-on-secondary-container opacity-70">ROAS</span>
<div class="flex flex-col mt-1">
<span class="font-data-mono text-data-mono text-lg">4.35x</span>
<span class="text-[10px] text-primary flex items-center"><span class="material-symbols-outlined text-[12px]" data-icon="show_chart">show_chart</span> +0.4</span>
</div>
</div>
<div class="bg-white border border-surface-container-highest p-3 rounded shadow-sm flex flex-col justify-between">
<span class="font-label-caps text-label-caps text-on-secondary-container opacity-70">Spend % Split</span>
<div class="flex flex-col mt-1">
<span class="font-data-mono text-data-mono text-lg">18.4%</span>
<span class="text-[10px] text-on-secondary-container">of Total</span>
</div>
</div>
<div class="bg-white border border-surface-container-highest p-3 rounded shadow-sm flex flex-col justify-between">
<span class="font-label-caps text-label-caps text-on-secondary-container opacity-70">Sales % Split</span>
<div class="flex flex-col mt-1">
<span class="font-data-mono text-data-mono text-lg">24.1%</span>
<span class="text-[10px] text-on-secondary-container">of Total</span>
</div>
</div>
</div>
<!-- Filters Bar -->
<div class="flex flex-wrap items-center gap-4 mb-6 bg-surface-container-lowest p-4 rounded border border-surface-container-highest">
<div class="flex-1 min-w-[300px] relative">
<span class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-on-secondary-container" data-icon="search">search</span>
<input class="w-full pl-10 pr-4 py-2 border border-surface-container-highest rounded bg-white text-body-md focus:outline-none focus:ring-2 focus:ring-tertiary transition-all" placeholder="Search Source Search Term..." type="text">
</div>
<div class="flex items-center gap-3">
<div class="flex flex-col">
<label class="text-[10px] font-bold text-on-secondary-container mb-1 ml-1 uppercase tracking-tighter">Campaign Filter</label>
<select class="px-4 py-2 border border-surface-container-highest rounded bg-white text-body-sm focus:outline-none focus:border-tertiary appearance-none pr-10 relative">
<option>All Campaigns</option>
<option>SP - Electronics - US</option>
<option>SB - Home Goods - CA</option>
</select>
</div>
<div class="flex flex-col">
<label class="text-[10px] font-bold text-on-secondary-container mb-1 ml-1 uppercase tracking-tighter">View Metrics</label>
<select class="px-4 py-2 border border-surface-container-highest rounded bg-white text-body-sm focus:outline-none focus:border-tertiary appearance-none pr-10">
<option>Standard Set (13)</option>
<option>Conversion Focused</option>
<option>Traffic Analysis</option>
</select>
</div>
<button class="mt-5 p-2 bg-white border border-surface-container-highest rounded hover:bg-surface-container-low transition-colors">
<span class="material-symbols-outlined" data-icon="filter_list">filter_list</span>
</button>
</div>
</div>
<!-- Data Table -->
<div class="bg-white border border-surface-container-highest rounded shadow-sm overflow-hidden flex flex-col">
<div class="overflow-x-auto custom-scrollbar">
<table class="w-full text-left border-collapse min-w-[1600px]">
<thead>
<tr class="bg-surface-container text-on-surface-variant">
<th class="px-4 py-3 font-label-caps text-label-caps border-b border-surface-container-highest">ASIN</th>
<th class="px-4 py-3 font-label-caps text-label-caps border-b border-surface-container-highest">Discovery Source</th>
<th class="px-4 py-3 font-label-caps text-label-caps border-b border-surface-container-highest">Parent Campaign</th>
<th class="px-4 py-3 font-label-caps text-label-caps border-b border-surface-container-highest">Match</th>
<th class="px-4 py-3 font-label-caps text-label-caps border-b border-surface-container-highest text-right">Impr.</th>
<th class="px-4 py-3 font-label-caps text-label-caps border-b border-surface-container-highest text-right">Clicks</th>
<th class="px-4 py-3 font-label-caps text-label-caps border-b border-surface-container-highest text-right">CTR</th>
<th class="px-4 py-3 font-label-caps text-label-caps border-b border-surface-container-highest text-right">CVR</th>
<th class="px-4 py-3 font-label-caps text-label-caps border-b border-surface-container-highest text-right">CPC</th>
<th class="px-4 py-3 font-label-caps text-label-caps border-b border-surface-container-highest text-right">Spend</th>
<th class="px-4 py-3 font-label-caps text-label-caps border-b border-surface-container-highest text-right">Sales</th>
<th class="px-4 py-3 font-label-caps text-label-caps border-b border-surface-container-highest text-right">ACOS</th>
<th class="px-4 py-3 font-label-caps text-label-caps border-b border-surface-container-highest text-right">ROAS</th>
<th class="px-4 py-3 font-label-caps text-label-caps border-b border-surface-container-highest text-center">Action</th>
</tr>
</thead>
<tbody class="divide-y divide-surface-container-highest">
<!-- Row 1 -->
<tr class="hover:bg-surface-container-low transition-colors group">
<td class="px-4 py-3">
<div class="flex items-center gap-3">
<div class="w-10 h-10 bg-surface-container flex-shrink-0 rounded overflow-hidden border border-surface-container-highest">
<img alt="Product thumbnail" class="w-full h-full object-cover" data-alt="A macro studio shot of a high-performance red sneaker. The lighting is crisp, using a dual-light setup that highlights the texture of the fabric and the sleek design of the sole. The background is a clean, neutral gray that emphasizes the product's vibrant color and professional finish." src="https://lh3.googleusercontent.com/aida-public/AB6AXuBwNHWSLK-NdM5Pt4ADV4GIyTmn9vA34j8JKwihlB3tSsetKnTawYQt3ff-3fAYNLlCsdC1yzrfnvziY5JCtN592Zv8lCNa06ggYZmIXQpC5-UKqgNGT5UErjnH8mz1rPZxjQ1Y1Nag-FA18v8C0wmbdPbYbJ3N0gnCt0TxhibH-JduDmxCbJ1pkRDyQc6fL97FOeekv7DbBGXdBphpcqFamHBVbOeCGMBBHrxFN1UvauYTbwtkxgDSuTJR2t_7W0FORSo_CZFB">
</div>
<div class="flex flex-col">
<span class="font-data-mono text-body-sm font-bold text-primary">B08XY25J9L</span>
<span class="text-[10px] text-on-secondary-container truncate w-32">Running Shoes X2</span>
</div>
</div>
</td>
<td class="px-4 py-3"><span class="text-body-sm font-medium">Auto Targeting Discovery</span></td>
<td class="px-4 py-3 font-body-sm text-on-secondary-container">SP_Category_Growth</td>
<td class="px-4 py-3"><span class="text-[10px] font-bold px-2 py-0.5 bg-surface-container-high rounded text-on-surface-variant">AUTO</span></td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">42,901</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">1,102</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">2.57%</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">12.4%</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">$1.12</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">$1,234</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">$8,921</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono text-tertiary font-bold">13.8%</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">7.2x</td>
<td class="px-4 py-3 text-center">
<button class="p-1 hover:text-primary transition-colors"><span class="material-symbols-outlined text-[20px]" data-icon="add_circle">add_circle</span></button>
</td>
</tr>
<!-- Row 2 -->
<tr class="hover:bg-surface-container-low transition-colors group">
<td class="px-4 py-3">
<div class="flex items-center gap-3">
<div class="w-10 h-10 bg-surface-container flex-shrink-0 rounded overflow-hidden border border-surface-container-highest">
<img alt="Product thumbnail" class="w-full h-full object-cover" data-alt="A minimalist high-angle shot of a sleek white smartwatch on a clean wooden desk. The composition is balanced, featuring soft natural morning light coming from a side window. The overall aesthetic is clean, modern, and high-tech, with a focus on product craftsmanship and simplicity." src="https://lh3.googleusercontent.com/aida-public/AB6AXuBNH2OevnHHtC4KdyKrIZfc7q6jogrCK8DkmFkMwbQ0RtEDjy6hOBVVQAQDDFWsP9KeaaSIZJUbiKKyLW8TcE2JJtbNmQyAVmLl-CZarCumVPX72wYq5YYr0RYCeh6U1CN1Fe6hBcGdfluMiQ0cp7t8jC5H4cMtpHzmfVFotk8MVM6KBHjtdihau2XH7EvNbzMyFkuSKD9ME1C4MEMZsXFjrF_-zqwjYnQoKP6DbAiB7dOT-eXDa7zZxZUqG_5VqQVLkz2CM4W_">
</div>
<div class="flex flex-col">
<span class="font-data-mono text-body-sm font-bold text-primary">B091V6K8M2</span>
<span class="text-[10px] text-on-secondary-container truncate w-32">SmartWatch Series 5</span>
</div>
</div>
</td>
<td class="px-4 py-3"><span class="text-body-sm font-medium">Auto Targeting Discovery</span></td>
<td class="px-4 py-3 font-body-sm text-on-secondary-container">SP_Generic_Electronics</td>
<td class="px-4 py-3"><span class="text-[10px] font-bold px-2 py-0.5 bg-surface-container-high rounded text-on-surface-variant">AUTO</span></td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">18,502</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">654</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">3.53%</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">5.2%</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">$2.45</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">$1,602</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">$4,821</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono text-error font-bold">33.2%</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">3.0x</td>
<td class="px-4 py-3 text-center">
<button class="p-1 hover:text-primary transition-colors"><span class="material-symbols-outlined text-[20px]" data-icon="add_circle">add_circle</span></button>
</td>
</tr>
<!-- Row 3 -->
<tr class="hover:bg-surface-container-low transition-colors group">
<td class="px-4 py-3">
<div class="flex items-center gap-3">
<div class="w-10 h-10 bg-surface-container flex-shrink-0 rounded overflow-hidden border border-surface-container-highest">
<img alt="Product thumbnail" class="w-full h-full object-cover" data-alt="A stylish, cinematic shot of premium over-ear headphones resting on a marble surface. The lighting is low-key, creating elegant highlights along the metallic curves of the product. Deep shadows add depth, while the overall palette is dominated by dark tones and brushed metal accents, suggesting professional audio quality." src="https://lh3.googleusercontent.com/aida-public/AB6AXuCHoqLq8CJ9Qu-shijXAW1L_IuVd9jpnUsSmXO1m7CnYmvKTIm5eAkTMgOHjZrddvZAPDlF8MJza0YjQ6FAVVn2-KhuWjw_lsCpU_nwHfwrUrxnX-WWt4EgtaVASlXMtmMFxwKesW165peuQf2sflpu4ZlOUUVM8U-Q8dqnOMGmH_5oTdNTCmDVM8NC3wLBCl0ch2xKbmshgq5fXvBuGXlw97KKwrtIOHUdmepkGwF6284JDua8Axm-zhZ4so4rGOIXD5IAM1ax">
</div>
<div class="flex flex-col">
<span class="font-data-mono text-body-sm font-bold text-primary">B07G4MT978</span>
<span class="text-[10px] text-on-secondary-container truncate w-32">AudioMax Pro ANC</span>
</div>
</div>
</td>
<td class="px-4 py-3"><span class="text-body-sm font-medium">Auto Targeting Discovery</span></td>
<td class="px-4 py-3 font-body-sm text-on-secondary-container">SP_Competitor_Harvesting</td>
<td class="px-4 py-3"><span class="text-[10px] font-bold px-2 py-0.5 bg-surface-container-high rounded text-on-surface-variant">AUTO</span></td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">31,008</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">892</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">2.87%</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">15.1%</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">$3.10</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">$2,765</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">$22,450</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono text-tertiary font-bold">12.3%</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">8.1x</td>
<td class="px-4 py-3 text-center">
<button class="p-1 hover:text-primary transition-colors"><span class="material-symbols-outlined text-[20px]" data-icon="add_circle">add_circle</span></button>
</td>
</tr>
<!-- Row 4 -->
<tr class="hover:bg-surface-container-low transition-colors group">
<td class="px-4 py-3">
<div class="flex items-center gap-3">
<div class="w-10 h-10 bg-surface-container flex-shrink-0 rounded overflow-hidden border border-surface-container-highest">
<img alt="Product thumbnail" class="w-full h-full object-cover" data-alt="A professional flat-lay photograph of high-end office stationery and a sleek black fountain pen on premium cream-colored paper. The light is soft and diffused, creating a serene, scholarly atmosphere. Minimalist and sophisticated, the image uses deep blacks and rich ivory tones to communicate luxury and precision." src="https://lh3.googleusercontent.com/aida-public/AB6AXuBAYNvrjIRHvkdTDlTqMEIAX1b_xVhnAwD7mtyupUk1RkKyWq0j9RR4H92WmkPl_bdtfU9gb_KlHp8oX_poL5Fhcmpr4Bi5yAZVMiqZa9wo6yUTN54GML3ljhEU983H1AG72xcOkN6Lxz8I8W6O99bg-PjWBgSximAdXHx-mjQoD1ub0VIL-9WJn9ibN3unRljqhINJKu8bJBMkdTIR67R3x-fofCdYIZN1N_MwW2MBw1gk9F0wGZIHn9NSaIhVthK4tlKu0tVj">
</div>
<div class="flex flex-col">
<span class="font-data-mono text-body-sm font-bold text-primary">B03D165X2Z</span>
<span class="text-[10px] text-on-secondary-container truncate w-32">Executive Pen Set</span>
</div>
</div>
</td>
<td class="px-4 py-3"><span class="text-body-sm font-medium">Auto Targeting Discovery</span></td>
<td class="px-4 py-3 font-body-sm text-on-secondary-container">SP_Office_Premium</td>
<td class="px-4 py-3"><span class="text-[10px] font-bold px-2 py-0.5 bg-surface-container-high rounded text-on-surface-variant">AUTO</span></td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">5,420</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">112</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">2.06%</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">3.2%</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">$0.85</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">$95</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">$450</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono text-on-surface-variant font-bold">21.1%</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">4.7x</td>
<td class="px-4 py-3 text-center">
<button class="p-1 hover:text-primary transition-colors"><span class="material-symbols-outlined text-[20px]" data-icon="add_circle">add_circle</span></button>
</td>
</tr>
<!-- Row 5 -->
<tr class="hover:bg-surface-container-low transition-colors group">
<td class="px-4 py-3">
<div class="flex items-center gap-3">
<div class="w-10 h-10 bg-surface-container flex-shrink-0 rounded overflow-hidden border border-surface-container-highest">
<img alt="Product thumbnail" class="w-full h-full object-cover" data-alt="A clean, isolated product shot of a vintage-style instant camera in pastel blue. The camera is centered against a soft, monochromatic blue background. Soft, even lighting eliminates harsh shadows, creating a playful yet high-quality commercial aesthetic that feels modern and nostalgic simultaneously." src="https://lh3.googleusercontent.com/aida-public/AB6AXuBaWekKmbAjKr0xsCqgsTWr1EWWDn-Ws16xrYgUG3G1p9D_YoQx3GjTGQpKU52pryf6haQ6wiUYoTqHSwoiMxxbESHoUXrFhF0bme2PPnv6XkX7Ffqe2pp9JTrtm3hamEchq5q0Bizw4NG7sfHlYwfuwwOTBveftufy0FVi2_x9BbCbPhV-BtcSJoig-N-oNs-IuBQwoprLkzCmPCwcSnb_8NkGmQYWzuWDWRt8Be9GzlhlpYPjIIEeKALmSzoEs3mZlA-RsGjY">
</div>
<div class="flex flex-col">
<span class="font-data-mono text-body-sm font-bold text-primary">B05K9M2L4P</span>
<span class="text-[10px] text-on-secondary-container truncate w-32">Instant Cam Retro</span>
</div>
</div>
</td>
<td class="px-4 py-3"><span class="text-body-sm font-medium">Auto Targeting Discovery</span></td>
<td class="px-4 py-3 font-body-sm text-on-secondary-container">SP_Lifestyle_Auto</td>
<td class="px-4 py-3"><span class="text-[10px] font-bold px-2 py-0.5 bg-surface-container-high rounded text-on-surface-variant">AUTO</span></td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">124,500</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">3,890</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">3.12%</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">6.8%</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">$1.05</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">$4,084</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">$15,402</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono text-error font-bold">26.5%</td>
<td class="px-4 py-3 text-right font-data-mono text-data-mono">3.7x</td>
<td class="px-4 py-3 text-center">
<button class="p-1 hover:text-primary transition-colors"><span class="material-symbols-outlined text-[20px]" data-icon="add_circle">add_circle</span></button>
</td>
</tr>
</tbody>
</table>
</div>
<div class="p-4 bg-surface-container-low flex justify-between items-center border-t border-surface-container-highest">
<span class="font-body-sm text-on-secondary-container">Showing 1-5 of 124 harvested ASINs</span>
<div class="flex gap-2">
<button class="px-3 py-1 border border-surface-container-highest rounded bg-white hover:bg-surface-container-high disabled:opacity-50" disabled="">Previous</button>
<button class="px-3 py-1 border border-surface-container-highest rounded bg-white hover:bg-surface-container-high">Next</button>
</div>
</div>
</div>
<!-- Helper Content -->
<div class="mt-8 grid grid-cols-1 md:grid-cols-2 gap-6">
<div class="p-6 rounded-xl bg-secondary-container text-on-secondary-container">
<div class="flex items-center gap-3 mb-3">
<span class="material-symbols-outlined" data-icon="lightbulb">lightbulb</span>
<h3 class="font-headline-sm text-headline-sm">Smart Harvesting Tip</h3>
</div>
<p class="font-body-sm text-body-sm leading-relaxed opacity-90">This view exclusively displays product targets (ASINs) discovered by Amazon's algorithm through your Auto campaigns. Reviewing these high-performance ASIN targets allows you to "harvest" them into Manual Product Targeting campaigns for better bid control and higher ROI.</p>
</div>
<div class="p-6 rounded-xl border border-outline-variant bg-surface-container-lowest">
<div class="flex items-center gap-3 mb-3 text-primary">
<span class="material-symbols-outlined" data-icon="insights">insights</span>
<h3 class="font-headline-sm text-headline-sm">Performance Benchmark</h3>
</div>
<p class="font-body-sm text-body-sm leading-relaxed text-on-surface-variant">
                            Current aggregate ACOS for harvested ASINs is 18.4% lower than generic keyword targets. Moving these to a dedicated "Manual Harvesting" campaign is recommended to scale volume while maintaining efficiency.
                        </p>
</div>
</div>
</div>
</main>
</div>
<!-- Micro-interaction JS -->
<script>
        // Simple hover effect and row selection simulation
        document.querySelectorAll('tbody tr').forEach(row => {
            row.addEventListener('click', () => {
                // Remove active classes from others
                document.querySelectorAll('tbody tr').forEach(r => r.classList.remove('bg-secondary-container/20'));
                // Add to current
                row.classList.add('bg-secondary-container/20');
            });
        });

        // Dropdown interactions (visual only)
        const selects = document.querySelectorAll('select');
        selects.forEach(s => {
            s.addEventListener('focus', () => {
                s.parentElement.classList.add('ring-2', 'ring-tertiary/20');
            });
            s.addEventListener('blur', () => {
                s.parentElement.classList.remove('ring-2', 'ring-tertiary/20');
            });
        });
    </script>


</body></html>

<!-- ASIN from STR - Performance Management -->
<!DOCTYPE html>

<html lang="en"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Auto Campaigns Performance | AmzAds Performance</title>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&amp;family=JetBrains+Mono:wght@500&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<script id="tailwind-config">
        tailwind.config = {
            darkMode: "class",
            theme: {
                extend: {
                    "colors": {
                        "surface-container-low": "#f2f4f4",
                        "surface-variant": "#e1e3e3",
                        "on-secondary-container": "#576474",
                        "on-primary": "#ffffff",
                        "on-primary-container": "#653a00",
                        "on-tertiary-fixed-variant": "#004e5d",
                        "error": "#ba1a1a",
                        "secondary": "#535f70",
                        "primary-container": "#ff9900",
                        "on-error-container": "#93000a",
                        "secondary-fixed": "#d7e3f7",
                        "outline-variant": "#dbc2ad",
                        "on-background": "#191c1d",
                        "surface-tint": "#8a5100",
                        "on-secondary": "#ffffff",
                        "tertiary-fixed": "#adecff",
                        "error-container": "#ffdad6",
                        "on-surface": "#191c1d",
                        "on-tertiary": "#ffffff",
                        "inverse-surface": "#2e3131",
                        "background": "#f8fafa",
                        "on-error": "#ffffff",
                        "surface-bright": "#f8fafa",
                        "tertiary": "#00687a",
                        "secondary-container": "#d4e1f5",
                        "surface-dim": "#d8dada",
                        "surface-container": "#eceeee",
                        "inverse-on-surface": "#eff1f1",
                        "primary-fixed": "#ffdcbd",
                        "on-secondary-fixed": "#101c2b",
                        "on-surface-variant": "#554434",
                        "on-tertiary-fixed": "#001f26",
                        "secondary-fixed-dim": "#bbc7db",
                        "tertiary-fixed-dim": "#80d2e9",
                        "surface-container-lowest": "#ffffff",
                        "on-tertiary-container": "#004b59",
                        "surface-container-high": "#e6e8e8",
                        "surface-container-highest": "#e1e3e3",
                        "primary": "#8a5100",
                        "on-primary-fixed-variant": "#693c00",
                        "inverse-primary": "#ffb86f",
                        "surface": "#f8fafa",
                        "tertiary-container": "#6abdd3",
                        "primary-fixed-dim": "#ffb86f",
                        "outline": "#887361",
                        "on-secondary-fixed-variant": "#3c4858",
                        "on-primary-fixed": "#2c1600"
                    },
                    "borderRadius": {
                        "DEFAULT": "0.125rem",
                        "lg": "0.25rem",
                        "xl": "0.5rem",
                        "full": "0.75rem"
                    },
                    "spacing": {
                        "margin-mobile": "16px",
                        "unit": "4px",
                        "margin-desktop": "32px",
                        "gutter": "16px",
                        "container-padding": "24px",
                        "max-width": "1440px"
                    },
                    "fontFamily": {
                        "label-caps": ["Inter"],
                        "headline-sm": ["Inter"],
                        "data-mono": ["JetBrains Mono"],
                        "body-md": ["Inter"],
                        "display-lg": ["Inter"],
                        "body-lg": ["Inter"],
                        "display-md": ["Inter"],
                        "body-sm": ["Inter"]
                    },
                    "fontSize": {
                        "label-caps": ["11px", {"lineHeight": "16px", "letterSpacing": "0.05em", "fontWeight": "700"}],
                        "headline-sm": ["18px", {"lineHeight": "24px", "fontWeight": "600"}],
                        "data-mono": ["13px", {"lineHeight": "18px", "fontWeight": "500"}],
                        "body-md": ["14px", {"lineHeight": "20px", "fontWeight": "400"}],
                        "display-lg": ["32px", {"lineHeight": "40px", "letterSpacing": "-0.02em", "fontWeight": "700"}],
                        "body-lg": ["16px", {"lineHeight": "24px", "fontWeight": "400"}],
                        "display-md": ["24px", {"lineHeight": "32px", "letterSpacing": "-0.01em", "fontWeight": "600"}],
                        "body-sm": ["12px", {"lineHeight": "16px", "fontWeight": "400"}]
                    }
                },
            },
        }
    </script>
<style>
        .material-symbols-outlined {
            font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
            vertical-align: middle;
        }
        .custom-scrollbar::-webkit-scrollbar {
            width: 4px;
            height: 4px;
        }
        .custom-scrollbar::-webkit-scrollbar-track {
            background: transparent;
        }
        .custom-scrollbar::-webkit-scrollbar-thumb {
            background: #e1e3e3;
            border-radius: 10px;
        }
        .table-sticky-column {
            position: sticky;
            left: 0;
            background: white;
            z-index: 10;
        }
        tr:nth-child(even) {
            background-color: #F8FAFA;
        }
    </style>
</head>
<body class="bg-background text-on-surface font-body-md overflow-hidden">
<!-- Shell Container -->
<div class="flex h-screen w-full">
<!-- SideNavBar -->
<aside class="flex flex-col h-screen overflow-y-auto p-4 gap-2 fixed left-0 top-0 h-full w-64 z-50 bg-surface-container-low border-r border-surface-variant">
<div class="flex items-center gap-3 mb-6 px-2">
<div class="w-10 h-10 bg-primary-container rounded flex items-center justify-center">
<span class="material-symbols-outlined text-on-primary-container" style="font-variation-settings: 'FILL' 1;">analytics</span>
</div>
<div>
<h1 class="text-headline-sm font-headline-sm font-bold text-on-surface">Brand Analytics</h1>
<p class="text-body-sm font-body-sm text-on-secondary-container">Amazon PPC</p>
</div>
</div>
<nav class="flex flex-col gap-1">
<!-- Dashboard -->
<a class="hover:bg-surface-container-highest transition-all text-on-secondary-container py-2 px-4 flex items-center gap-3" href="#">
<span class="material-symbols-outlined text-[20px]">dashboard</span>
<span class="text-label-caps font-label-caps">Dashboard</span>
</a>
<!-- Campaigns -->
<a class="hover:bg-surface-container-highest transition-all text-on-secondary-container py-2 px-4 flex items-center gap-3" href="#">
<span class="material-symbols-outlined text-[20px]">ads_click</span>
<span class="text-label-caps font-label-caps">Campaigns</span>
</a>
<!-- Products -->
<a class="hover:bg-surface-container-highest transition-all text-on-secondary-container py-2 px-4 flex items-center gap-3" href="#">
<span class="material-symbols-outlined text-[20px]">inventory_2</span>
<span class="text-label-caps font-label-caps">Products</span>
</a>
<!-- Match Type -->
<a class="hover:bg-surface-container-highest transition-all text-on-secondary-container py-2 px-4 flex items-center gap-3" href="#">
<span class="material-symbols-outlined text-[20px]">reorder</span>
<span class="text-label-caps font-label-caps">Match Type</span>
</a>
<!-- Keywords -->
<a class="hover:bg-surface-container-highest transition-all text-on-secondary-container py-2 px-4 flex items-center gap-3" href="#">
<span class="material-symbols-outlined text-[20px]">key</span>
<span class="text-label-caps font-label-caps">Keywords</span>
</a>
<!-- Search Terms -->
<a class="hover:bg-surface-container-highest transition-all text-on-secondary-container py-2 px-4 flex items-center gap-3" href="#">
<span class="material-symbols-outlined text-[20px]">search_insights</span>
<span class="text-label-caps font-label-caps">Search Terms</span>
</a>
<!-- ASIN Targets -->
<a class="hover:bg-surface-container-highest transition-all text-on-secondary-container py-2 px-4 flex items-center gap-3" href="#">
<span class="material-symbols-outlined text-[20px]">target</span>
<span class="text-label-caps font-label-caps">ASIN Targets</span>
</a>
<!-- ASIN from STR -->
<a class="hover:bg-surface-container-highest transition-all text-on-secondary-container py-2 px-4 flex items-center gap-3" href="#">
<span class="material-symbols-outlined text-[20px]">analytics</span>
<span class="text-label-caps font-label-caps">ASIN from STR</span>
</a>
<!-- Auto Campaigns (ACTIVE) -->
<a class="bg-tertiary-container text-on-tertiary-container rounded-lg font-bold py-2 px-4 flex items-center gap-3 scale-95 duration-150 shadow-sm" href="#">
<span class="material-symbols-outlined text-[20px]" style="font-variation-settings: 'FILL' 1;">smart_button</span>
<span class="text-label-caps font-label-caps">Auto Campaigns</span>
</a>
<!-- Category Targets -->
<a class="hover:bg-surface-container-highest transition-all text-on-secondary-container py-2 px-4 flex items-center gap-3" href="#">
<span class="material-symbols-outlined text-[20px]">category</span>
<span class="text-label-caps font-label-caps">Category Targets</span>
</a>
<!-- Wasted Ad Spend -->
<a class="hover:bg-surface-container-highest transition-all text-on-secondary-container py-2 px-4 flex items-center gap-3" href="#">
<span class="material-symbols-outlined text-[20px]">trending_down</span>
<span class="text-label-caps font-label-caps">Wasted Ad Spend</span>
</a>
</nav>
<div class="mt-auto pt-6 px-2">
<button class="w-full bg-primary-container text-on-primary-container py-3 rounded font-bold text-label-caps font-label-caps flex items-center justify-center gap-2 hover:opacity-90 transition-all">
<span class="material-symbols-outlined">add</span>
                    New Campaign
                </button>
</div>
</aside>
<!-- Main Content Canvas -->
<main class="flex-1 ml-64 overflow-y-auto bg-background">
<!-- TopNavBar -->
<header class="flex justify-between items-center w-full px-margin-desktop h-16 sticky top-0 z-40 bg-surface-container-lowest border-b border-surface-variant">
<div class="flex items-center gap-4">
<h2 class="text-display-md font-display-md font-black text-primary">AmzAds Performance</h2>
<div class="h-6 w-[1px] bg-surface-variant"></div>
<nav class="flex items-center gap-6">
<span class="text-headline-sm font-headline-sm text-primary border-b-2 border-primary pb-1">Auto Campaigns Performance</span>
</nav>
</div>
<div class="flex items-center gap-4">
<div class="flex items-center bg-surface-container gap-2 px-3 py-1.5 rounded-lg border border-surface-variant cursor-pointer hover:bg-surface-container-high transition-colors">
<span class="material-symbols-outlined text-on-secondary-container text-[18px]">calendar_month</span>
<span class="text-body-sm font-bold text-on-secondary-container">Last 30 Days</span>
<span class="material-symbols-outlined text-on-secondary-container text-[18px]">expand_more</span>
</div>
<button class="flex items-center gap-2 px-4 py-2 bg-primary-container text-on-primary-container rounded font-bold text-label-caps font-label-caps hover:opacity-80 transition-all">
<span class="material-symbols-outlined text-[18px]">file_download</span>
                        Export Report
                    </button>
<button class="p-2 hover:bg-surface-container-high rounded-full transition-colors">
<span class="material-symbols-outlined text-on-secondary-container">settings</span>
</button>
<div class="w-8 h-8 rounded-full bg-surface-variant overflow-hidden">
<img alt="Account Manager Avatar" class="w-full h-full object-cover" data-alt="A professional headshot of a young, confident account manager in a modern business-casual outfit. He has a warm, approachable smile and is set against a clean, soft-focus office background with high-key lighting. The overall style is corporate, clean, and optimistic, matching the professional analytic theme of the dashboard." src="https://lh3.googleusercontent.com/aida-public/AB6AXuBKTtwhfO4V8g4Wdi1r_U0Gy-reaCQbEo-qhRBwpxMevgQRUeezT6xyzgOBuhVQgq_eSTSNypDA-z0OdijEePRkl1oZL0DOgImCU_bicZ2CVdT86Ew-EAYSB7xLPrEY6fG1xMezkTi0yZ2m06-oyZFNLudIm_n4kN2-G5lzWUv4a5suRLHB1QEnWMnmJQjlsAIC0tIQAEF6lgaaD5DWLCtg9yYsKCOpOcEAKxOzyKHccayKuaneJckFqGrcx-DB7MojjJfZ5SSS"/>
</div>
</div>
</header>
<div class="p-margin-desktop space-y-8 max-w-[1440px] mx-auto">
<!-- Metrics Grid (13 summary cards) -->
<section class="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-7 gap-4">
<!-- Metric Card 1 -->
<div class="bg-surface-container-lowest border border-surface-variant p-4 rounded-lg flex flex-col gap-1">
<span class="text-label-caps font-label-caps text-on-secondary-container">Impressions</span>
<div class="flex items-end justify-between">
<span class="text-display-md font-display-md font-data-mono">1.2M</span>
<span class="text-body-sm font-bold text-error flex items-center">-4.2%</span>
</div>
</div>
<!-- Metric Card 2 -->
<div class="bg-surface-container-lowest border border-surface-variant p-4 rounded-lg flex flex-col gap-1">
<span class="text-label-caps font-label-caps text-on-secondary-container">Clicks</span>
<div class="flex items-end justify-between">
<span class="text-display-md font-display-md font-data-mono">24.5k</span>
<span class="text-body-sm font-bold text-on-tertiary-fixed-variant flex items-center">+12.1%</span>
</div>
</div>
<!-- Metric Card 3 -->
<div class="bg-surface-container-lowest border border-surface-variant p-4 rounded-lg flex flex-col gap-1">
<span class="text-label-caps font-label-caps text-on-secondary-container">CTR</span>
<div class="flex items-end justify-between">
<span class="text-display-md font-display-md font-data-mono">2.04%</span>
<span class="text-body-sm font-bold text-on-tertiary-fixed-variant flex items-center">+0.5%</span>
</div>
</div>
<!-- Metric Card 4 -->
<div class="bg-surface-container-lowest border border-surface-variant p-4 rounded-lg flex flex-col gap-1">
<span class="text-label-caps font-label-caps text-on-secondary-container">CVR</span>
<div class="flex items-end justify-between">
<span class="text-display-md font-display-md font-data-mono">8.2%</span>
<span class="text-body-sm font-bold text-error flex items-center">-1.8%</span>
</div>
</div>
<!-- Metric Card 5 -->
<div class="bg-surface-container-lowest border border-surface-variant p-4 rounded-lg flex flex-col gap-1">
<span class="text-label-caps font-label-caps text-on-secondary-container">CPC</span>
<div class="flex items-end justify-between">
<span class="text-display-md font-display-md font-data-mono">$0.82</span>
<span class="text-body-sm font-bold text-on-secondary-container flex items-center">0.0%</span>
</div>
</div>
<!-- Metric Card 6 -->
<div class="bg-surface-container-lowest border border-surface-variant p-4 rounded-lg flex flex-col gap-1">
<span class="text-label-caps font-label-caps text-on-secondary-container">Spend</span>
<div class="flex items-end justify-between">
<span class="text-display-md font-display-md font-data-mono">$20,1k</span>
<span class="text-body-sm font-bold text-on-tertiary-fixed-variant flex items-center">+8.4%</span>
</div>
</div>
<!-- Metric Card 7 -->
<div class="bg-surface-container-lowest border border-surface-variant p-4 rounded-lg flex flex-col gap-1">
<span class="text-label-caps font-label-caps text-on-secondary-container">Sales</span>
<div class="flex items-end justify-between">
<span class="text-display-md font-display-md font-data-mono">$84.2k</span>
<span class="text-body-sm font-bold text-on-tertiary-fixed-variant flex items-center">+15.2%</span>
</div>
</div>
<!-- Row 2 -->
<div class="bg-surface-container-lowest border border-surface-variant p-4 rounded-lg flex flex-col gap-1">
<span class="text-label-caps font-label-caps text-on-secondary-container">Orders</span>
<div class="flex items-end justify-between">
<span class="text-display-md font-display-md font-data-mono">2,010</span>
<span class="text-body-sm font-bold text-on-tertiary-fixed-variant">+10%</span>
</div>
</div>
<div class="bg-surface-container-lowest border border-surface-variant p-4 rounded-lg flex flex-col gap-1">
<span class="text-label-caps font-label-caps text-on-secondary-container">Units</span>
<div class="flex items-end justify-between">
<span class="text-display-md font-display-md font-data-mono">2,450</span>
<span class="text-body-sm font-bold text-on-tertiary-fixed-variant">+9.2%</span>
</div>
</div>
<div class="bg-surface-container-lowest border border-surface-variant p-4 rounded-lg flex flex-col gap-1">
<span class="text-label-caps font-label-caps text-on-secondary-container">ACOS</span>
<div class="flex items-end justify-between">
<span class="text-display-md font-display-md font-data-mono text-tertiary">23.8%</span>
<span class="text-body-sm font-bold text-on-tertiary-fixed-variant flex items-center">
<span class="material-symbols-outlined text-[14px]">arrow_downward</span>
                                2.4%
                            </span>
</div>
</div>
<div class="bg-surface-container-lowest border border-surface-variant p-4 rounded-lg flex flex-col gap-1">
<span class="text-label-caps font-label-caps text-on-secondary-container">ROAS</span>
<div class="flex items-end justify-between">
<span class="text-display-md font-display-md font-data-mono">4.2x</span>
<span class="text-body-sm font-bold text-on-tertiary-fixed-variant">+0.4</span>
</div>
</div>
<div class="bg-surface-container-lowest border border-surface-variant p-4 rounded-lg flex flex-col gap-1">
<span class="text-label-caps font-label-caps text-on-secondary-container">Spend % Split</span>
<div class="flex items-end justify-between">
<span class="text-display-md font-display-md font-data-mono">100%</span>
<div class="w-12 bg-surface-variant h-1 rounded overflow-hidden mb-2">
<div class="bg-primary w-full h-full"></div>
</div>
</div>
</div>
<div class="bg-surface-container-lowest border border-surface-variant p-4 rounded-lg flex flex-col gap-1">
<span class="text-label-caps font-label-caps text-on-secondary-container">Sales % Split</span>
<div class="flex items-end justify-between">
<span class="text-display-md font-display-md font-data-mono">100%</span>
<div class="w-12 bg-surface-variant h-1 rounded overflow-hidden mb-2">
<div class="bg-tertiary w-full h-full"></div>
</div>
</div>
</div>
<div class="bg-surface-container-lowest border border-primary border-dashed p-4 rounded-lg flex flex-col justify-center items-center gap-1 cursor-pointer hover:bg-surface-container-low transition-colors">
<span class="material-symbols-outlined text-primary">add_circle</span>
<span class="text-label-caps font-label-caps text-primary">Add Metric</span>
</div>
</section>
<!-- Targeting Group Management Section -->
<section class="bg-surface-container-lowest border border-surface-variant rounded-lg overflow-hidden shadow-sm">
<!-- Table Header Actions -->
<div class="p-4 border-b border-surface-variant flex flex-wrap justify-between items-center gap-4 bg-surface-bright">
<div class="flex items-center gap-4">
<div class="relative">
<span class="absolute left-3 top-1/2 -translate-y-1/2 material-symbols-outlined text-on-secondary-container text-[20px]">filter_list</span>
<select class="appearance-none bg-surface-container-low border border-surface-variant rounded-lg pl-10 pr-8 py-2 text-body-sm font-bold text-on-surface focus:outline-none focus:ring-2 focus:ring-tertiary cursor-pointer">
<option>Campaign Filter: All Active</option>
<option>Sponsor Products: Best Sellers</option>
<option>Seasonality: Prime Day</option>
</select>
</div>
<div class="relative">
<span class="absolute left-3 top-1/2 -translate-y-1/2 material-symbols-outlined text-on-secondary-container text-[20px]">visibility</span>
<select class="appearance-none bg-surface-container-low border border-surface-variant rounded-lg pl-10 pr-8 py-2 text-body-sm font-bold text-on-surface focus:outline-none focus:ring-2 focus:ring-tertiary cursor-pointer">
<option>Metrics View: Performance All</option>
<option>View: Conversion Focus</option>
<option>View: Cost Control</option>
</select>
</div>
</div>
<div class="flex items-center gap-2">
<div class="flex bg-surface-container-low p-1 rounded-lg border border-surface-variant">
<button class="px-3 py-1 bg-white shadow-sm rounded text-body-sm font-bold text-primary">Table</button>
<button class="px-3 py-1 text-body-sm text-on-secondary-container hover:text-on-surface transition-colors">Chart</button>
</div>
</div>
</div>
<!-- High-Density Data Table -->
<div class="overflow-x-auto custom-scrollbar">
<table class="w-full text-left border-collapse min-w-[1600px]">
<thead class="bg-surface-container text-on-secondary-container text-label-caps font-label-caps">
<tr>
<th class="py-3 px-4 border-b border-surface-variant table-sticky-column w-12">
<input class="rounded border-surface-variant text-primary focus:ring-primary h-4 w-4" type="checkbox"/>
</th>
<th class="py-3 px-4 border-b border-surface-variant table-sticky-column left-12">Targeting Group</th>
<th class="py-3 px-4 border-b border-surface-variant">Status</th>
<th class="py-3 px-4 border-b border-surface-variant text-right">Impressions</th>
<th class="py-3 px-4 border-b border-surface-variant text-right">Clicks</th>
<th class="py-3 px-4 border-b border-surface-variant text-right">CTR</th>
<th class="py-3 px-4 border-b border-surface-variant text-right">CPC</th>
<th class="py-3 px-4 border-b border-surface-variant text-right">Spend</th>
<th class="py-3 px-4 border-b border-surface-variant text-right">Sales</th>
<th class="py-3 px-4 border-b border-surface-variant text-right">Orders</th>
<th class="py-3 px-4 border-b border-surface-variant text-right">CVR</th>
<th class="py-3 px-4 border-b border-surface-variant text-right">ACOS</th>
<th class="py-3 px-4 border-b border-surface-variant text-right">ROAS</th>
<th class="py-3 px-4 border-b border-surface-variant text-right">Units</th>
<th class="py-3 px-4 border-b border-surface-variant text-right">Spend %</th>
<th class="py-3 px-4 border-b border-surface-variant text-right">Sales %</th>
</tr>
</thead>
<tbody class="text-body-sm">
<!-- Group 1: Close Match -->
<tr class="hover:bg-surface-container-high transition-colors">
<td class="py-3 px-4 border-b border-surface-variant table-sticky-column">
<input checked="" class="rounded border-surface-variant text-primary focus:ring-primary h-4 w-4" type="checkbox"/>
</td>
<td class="py-3 px-4 border-b border-surface-variant table-sticky-column font-bold left-12">
<div class="flex items-center gap-2">
<span class="material-symbols-outlined text-primary text-[20px]">center_focus_strong</span>
                                            Close Match
                                        </div>
</td>
<td class="py-3 px-4 border-b border-surface-variant">
<label class="relative inline-flex items-center cursor-pointer">
<input checked="" class="sr-only peer" type="checkbox"/>
<div class="w-9 h-5 bg-surface-variant peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-4 after:w-4 after:transition-all peer-checked:bg-on-tertiary-fixed-variant"></div>
</label>
</td>
<td class="py-3 px-4 border-b border-surface-variant text-right font-data-mono">542,120</td>
<td class="py-3 px-4 border-b border-surface-variant text-right font-data-mono">12,450</td>
<td class="py-3 px-4 border-b border-surface-variant text-right font-data-mono">2.29%</td>
<td class="py-3 px-4 border-b border-surface-variant text-right font-data-mono">$0.95</td>
<td class="py-3 px-4 border-b border-surface-variant text-right font-data-mono">$11,827.50</td>
<td class="py-3 px-4 border-b border-surface-variant text-right font-data-mono font-bold">$58,240.10</td>
<td class="py-3 px-4 border-b border-surface-variant text-right font-data-mono">1,120</td>
<td class="py-3 px-4 border-b border-surface-variant text-right font-data-mono">8.99%</td>
<td class="py-3 px-4 border-b border-surface-variant text-right font-data-mono text-tertiary font-bold">20.3%</td>
<td class="py-3 px-4 border-b border-surface-variant text-right font-data-mono">4.9x</td>
<td class="py-3 px-4 border-b border-surface-variant text-right font-data-mono">1,245</td>
<td class="py-3 px-4 border-b border-surface-variant text-right font-data-mono">58.8%</td>
<td class="py-3 px-4 border-b border-surface-variant text-right font-data-mono">69.1%</td>
</tr>
<!-- Group 2: Loose Match -->
<tr class="hover:bg-surface-container-high transition-colors">
<td class="py-3 px-4 border-b border-surface-variant table-sticky-column">
<input checked="" class="rounded border-surface-variant text-primary focus:ring-primary h-4 w-4" type="checkbox"/>
</td>
<td class="py-3 px-4 border-b border-surface-variant table-sticky-column font-bold left-12">
<div class="flex items-center gap-2">
<span class="material-symbols-outlined text-on-secondary-container text-[20px]">filter_tilt_shift</span>
                                            Loose Match
                                        </div>
</td>
<td class="py-3 px-4 border-b border-surface-variant">
<label class="relative inline-flex items-center cursor-pointer">
<input checked="" class="sr-only peer" type="checkbox"/>
<div class="w-9 h-5 bg-surface-variant peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-4 after:w-4 after:transition-all peer-checked:bg-on-tertiary-fixed-variant"></div>
</label>
</td>
<td class="py-3 px-4 border-b border-surface-variant text-right font-data-mono">410,230</td>
<td class="py-3 px-4 border-b border-surface-variant text-right font-data-mono">8,120</td>
<td class="py-3 px-4 border-b border-surface-variant text-right font-data-mono">1.97%</td>
<td class="py-3 px-4 border-b border-surface-variant text-right font-data-mono">$0.72</td>
<td class="py-3 px-4 border-b border-surface-variant text-right font-data-mono">$5,846.40</td>
<td class="py-3 px-4 border-b border-surface-variant text-right font-data-mono font-bold">$18,450.00</td>
<td class="py-3 px-4 border-b border-surface-variant text-right font-data-mono">450</td>
<td class="py-3 px-4 border-b border-surface-variant text-right font-data-mono">5.54%</td>
<td class="py-3 px-4 border-b border-surface-variant text-right font-data-mono text-error font-bold">31.6%</td>
<td class="py-3 px-4 border-b border-surface-variant text-right font-data-mono">3.1x</td>
<td class="py-3 px-4 border-b border-surface-variant text-right font-data-mono">510</td>
<td class="py-3 px-4 border-b border-surface-variant text-right font-data-mono">29.1%</td>
<td class="py-3 px-4 border-b border-surface-variant text-right font-data-mono">21.9%</td>
</tr>
<!-- Group 3: Substitutes -->
<tr class="hover:bg-surface-container-high transition-colors">
<td class="py-3 px-4 border-b border-surface-variant table-sticky-column">
<input checked="" class="rounded border-surface-variant text-primary focus:ring-primary h-4 w-4" type="checkbox"/>
</td>
<td class="py-3 px-4 border-b border-surface-variant table-sticky-column font-bold left-12">
<div class="flex items-center gap-2">
<span class="material-symbols-outlined text-on-secondary-container text-[20px]">swap_horiz</span>
                                            Substitutes
                                        </div>
</td>
<td class="py-3 px-4 border-b border-surface-variant">
<label class="relative inline-flex items-center cursor-pointer">
<input checked="" class="sr-only peer" type="checkbox"/>
<div class="w-9 h-5 bg-surface-variant peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-4 after:w-4 after:transition-all peer-checked:bg-on-tertiary-fixed-variant"></div>
</label>
</td>
<td class="py-3 px-4 border-b border-surface-variant text-right font-data-mono">185,450</td>
<td class="py-3 px-4 border-b border-surface-variant text-right font-data-mono">2,840</td>
<td class="py-3 px-4 border-b border-surface-variant text-right font-data-mono">1.53%</td>
<td class="py-3 px-4 border-b border-surface-variant text-right font-data-mono">$0.65</td>
<td class="py-3 px-4 border-b border-surface-variant text-right font-data-mono">$1,846.00</td>
<td class="py-3 px-4 border-b border-surface-variant text-right font-data-mono font-bold">$5,240.40</td>
<td class="py-3 px-4 border-b border-surface-variant text-right font-data-mono">320</td>
<td class="py-3 px-4 border-b border-surface-variant text-right font-data-mono">11.2%</td>
<td class="py-3 px-4 border-b border-surface-variant text-right font-data-mono text-tertiary font-bold">35.2%</td>
<td class="py-3 px-4 border-b border-surface-variant text-right font-data-mono">2.8x</td>
<td class="py-3 px-4 border-b border-surface-variant text-right font-data-mono">380</td>
<td class="py-3 px-4 border-b border-surface-variant text-right font-data-mono">9.2%</td>
<td class="py-3 px-4 border-b border-surface-variant text-right font-data-mono">6.2%</td>
</tr>
<!-- Group 4: Complements -->
<tr class="hover:bg-surface-container-high transition-colors">
<td class="py-3 px-4 border-b border-surface-variant table-sticky-column">
<input checked="" class="rounded border-surface-variant text-primary focus:ring-primary h-4 w-4" type="checkbox"/>
</td>
<td class="py-3 px-4 border-b border-surface-variant table-sticky-column font-bold left-12">
<div class="flex items-center gap-2">
<span class="material-symbols-outlined text-on-secondary-container text-[20px]">add_task</span>
                                            Complements
                                        </div>
</td>
<td class="py-3 px-4 border-b border-surface-variant">
<label class="relative inline-flex items-center cursor-pointer">
<input checked="" class="sr-only peer" type="checkbox"/>
<div class="w-9 h-5 bg-surface-variant peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-4 after:w-4 after:transition-all peer-checked:bg-on-tertiary-fixed-variant"></div>
</label>
</td>
<td class="py-3 px-4 border-b border-surface-variant text-right font-data-mono">62,190</td>
<td class="py-3 px-4 border-b border-surface-variant text-right font-data-mono">1,090</td>
<td class="py-3 px-4 border-b border-surface-variant text-right font-data-mono">1.75%</td>
<td class="py-3 px-4 border-b border-surface-variant text-right font-data-mono">$0.54</td>
<td class="py-3 px-4 border-b border-surface-variant text-right font-data-mono">$588.60</td>
<td class="py-3 px-4 border-b border-surface-variant text-right font-data-mono font-bold">$2,269.50</td>
<td class="py-3 px-4 border-b border-surface-variant text-right font-data-mono">120</td>
<td class="py-3 px-4 border-b border-surface-variant text-right font-data-mono">11.0%</td>
<td class="py-3 px-4 border-b border-surface-variant text-right font-data-mono text-tertiary font-bold">25.9%</td>
<td class="py-3 px-4 border-b border-surface-variant text-right font-data-mono">3.8x</td>
<td class="py-3 px-4 border-b border-surface-variant text-right font-data-mono">315</td>
<td class="py-3 px-4 border-b border-surface-variant text-right font-data-mono">2.9%</td>
<td class="py-3 px-4 border-b border-surface-variant text-right font-data-mono">2.8%</td>
</tr>
</tbody>
<tfoot class="bg-surface-container-high text-on-surface font-bold text-body-sm">
<tr>
<td class="py-3 px-4 table-sticky-column"></td>
<td class="py-3 px-4 table-sticky-column left-12">Grand Total</td>
<td class="py-3 px-4"></td>
<td class="py-3 px-4 text-right font-data-mono">1,199,990</td>
<td class="py-3 px-4 text-right font-data-mono">24,500</td>
<td class="py-3 px-4 text-right font-data-mono">2.04%</td>
<td class="py-3 px-4 text-right font-data-mono">$0.82</td>
<td class="py-3 px-4 text-right font-data-mono">$20,108.50</td>
<td class="py-3 px-4 text-right font-data-mono">$84,200.00</td>
<td class="py-3 px-4 text-right font-data-mono">2,010</td>
<td class="py-3 px-4 text-right font-data-mono">8.2%</td>
<td class="py-3 px-4 text-right font-data-mono text-tertiary">23.8%</td>
<td class="py-3 px-4 text-right font-data-mono">4.2x</td>
<td class="py-3 px-4 text-right font-data-mono">2,450</td>
<td class="py-3 px-4 text-right font-data-mono">100%</td>
<td class="py-3 px-4 text-right font-data-mono">100%</td>
</tr>
</tfoot>
</table>
</div>
</section>
<!-- Data Visualization Preview Section -->
<section class="grid grid-cols-1 lg:grid-cols-2 gap-margin-desktop pb-8">
<div class="bg-surface-container-lowest border border-surface-variant rounded-lg p-6">
<div class="flex justify-between items-center mb-6">
<h3 class="text-headline-sm font-headline-sm text-on-surface">Targeting Split (Spend vs Sales)</h3>
<span class="material-symbols-outlined text-on-secondary-container">more_vert</span>
</div>
<div class="flex flex-col gap-6">
<div class="space-y-2">
<div class="flex justify-between text-label-caps font-label-caps text-on-secondary-container">
<span>Close Match</span>
<span>$11.8k Spend / $58.2k Sales</span>
</div>
<div class="h-8 w-full bg-surface-container flex rounded-lg overflow-hidden">
<div class="bg-primary h-full" style="width: 58%"></div>
<div class="bg-tertiary h-full opacity-50" style="width: 69%"></div>
</div>
</div>
<div class="space-y-2">
<div class="flex justify-between text-label-caps font-label-caps text-on-secondary-container">
<span>Loose Match</span>
<span>$5.8k Spend / $18.4k Sales</span>
</div>
<div class="h-8 w-full bg-surface-container flex rounded-lg overflow-hidden">
<div class="bg-primary h-full" style="width: 29%"></div>
<div class="bg-tertiary h-full opacity-50" style="width: 21%"></div>
</div>
</div>
</div>
</div>
<div class="bg-surface-container-lowest border border-surface-variant rounded-lg p-6 flex flex-col items-center justify-center text-center">
<div class="w-full flex justify-between items-center mb-6 text-left">
<h3 class="text-headline-sm font-headline-sm text-on-surface">Performance Trend (30D)</h3>
<div class="flex gap-2">
<span class="flex items-center gap-1 text-body-sm text-primary font-bold"><div class="w-3 h-3 bg-primary rounded-full"></div> Spend</span>
<span class="flex items-center gap-1 text-body-sm text-tertiary font-bold"><div class="w-3 h-3 bg-tertiary rounded-full"></div> Sales</span>
</div>
</div>
<div class="w-full h-48 flex items-end gap-1 px-4">
<!-- Mock chart bars -->
<div class="flex-1 bg-surface-container h-1/2 rounded-t-sm relative group">
<div class="absolute bottom-0 w-full bg-primary h-1/2 rounded-t-sm group-hover:opacity-80 transition-opacity"></div>
<div class="absolute bottom-1/2 w-full bg-tertiary h-1/3 rounded-t-sm opacity-60"></div>
</div>
<div class="flex-1 bg-surface-container h-2/3 rounded-t-sm relative group">
<div class="absolute bottom-0 w-full bg-primary h-2/3 rounded-t-sm group-hover:opacity-80 transition-opacity"></div>
<div class="absolute bottom-1/2 w-full bg-tertiary h-1/4 rounded-t-sm opacity-60"></div>
</div>
<div class="flex-1 bg-surface-container h-1/3 rounded-t-sm relative group">
<div class="absolute bottom-0 w-full bg-primary h-1/3 rounded-t-sm group-hover:opacity-80 transition-opacity"></div>
<div class="absolute bottom-1/2 w-full bg-tertiary h-1/5 rounded-t-sm opacity-60"></div>
</div>
<div class="flex-1 bg-surface-container h-3/4 rounded-t-sm relative group">
<div class="absolute bottom-0 w-full bg-primary h-3/4 rounded-t-sm group-hover:opacity-80 transition-opacity"></div>
<div class="absolute bottom-1/2 w-full bg-tertiary h-1/2 rounded-t-sm opacity-60"></div>
</div>
<div class="flex-1 bg-surface-container h-1/2 rounded-t-sm relative group">
<div class="absolute bottom-0 w-full bg-primary h-1/2 rounded-t-sm group-hover:opacity-80 transition-opacity"></div>
<div class="absolute bottom-1/2 w-full bg-tertiary h-1/3 rounded-t-sm opacity-60"></div>
</div>
<div class="flex-1 bg-surface-container h-5/6 rounded-t-sm relative group">
<div class="absolute bottom-0 w-full bg-primary h-5/6 rounded-t-sm group-hover:opacity-80 transition-opacity"></div>
<div class="absolute bottom-1/2 w-full bg-tertiary h-2/3 rounded-t-sm opacity-60"></div>
</div>
<div class="flex-1 bg-surface-container h-2/3 rounded-t-sm relative group">
<div class="absolute bottom-0 w-full bg-primary h-2/3 rounded-t-sm group-hover:opacity-80 transition-opacity"></div>
<div class="absolute bottom-1/2 w-full bg-tertiary h-1/4 rounded-t-sm opacity-60"></div>
</div>
</div>
<p class="text-body-sm text-on-secondary-container mt-4">Last 7 days show a significant 15% increase in ROAS efficiency for Close Match targets.</p>
</div>
</section>
</div>
</main>
</div>
<!-- Micro-interaction Script -->
<script>
        // Subtle hover effects for cards
        document.querySelectorAll('.bg-surface-container-lowest').forEach(card => {
            card.addEventListener('mouseenter', () => {
                card.classList.add('shadow-md');
            });
            card.addEventListener('mouseleave', () => {
                card.classList.remove('shadow-md');
            });
        });
    </script>
</body></html>

<!-- Auto Campaigns - Performance Management -->
<!DOCTYPE html>

<html lang="en"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>AdTracker Pro - Category Targets</title>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&amp;family=JetBrains+Mono:wght@500&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<script id="tailwind-config">
        tailwind.config = {
            darkMode: "class",
            theme: {
                extend: {
                    "colors": {
                        "surface-container-highest": "#e1e3e3",
                        "on-tertiary-fixed": "#001f26",
                        "on-primary-fixed-variant": "#693c00",
                        "on-surface": "#191c1d",
                        "on-secondary": "#ffffff",
                        "primary-container": "#ff9900",
                        "on-error-container": "#93000a",
                        "on-background": "#191c1d",
                        "outline-variant": "#dbc2ad",
                        "surface-container-high": "#e6e8e8",
                        "outline": "#887361",
                        "on-secondary-fixed-variant": "#3c4858",
                        "surface-tint": "#8a5100",
                        "secondary": "#535f70",
                        "surface-bright": "#f8fafa",
                        "primary": "#8a5100",
                        "surface-variant": "#e1e3e3",
                        "tertiary-fixed": "#adecff",
                        "tertiary-container": "#6abdd3",
                        "on-tertiary-fixed-variant": "#004e5d",
                        "on-tertiary": "#ffffff",
                        "error-container": "#ffdad6",
                        "primary-fixed": "#ffdcbd",
                        "on-primary-container": "#653a00",
                        "error": "#ba1a1a",
                        "on-primary": "#ffffff",
                        "on-surface-variant": "#554434",
                        "tertiary-fixed-dim": "#80d2e9",
                        "tertiary": "#00687a",
                        "surface-container-lowest": "#ffffff",
                        "secondary-fixed-dim": "#bbc7db",
                        "secondary-fixed": "#d7e3f7",
                        "secondary-container": "#d4e1f5",
                        "inverse-on-surface": "#eff1f1",
                        "surface-container-low": "#f2f4f4",
                        "on-tertiary-container": "#004b59",
                        "inverse-primary": "#ffb86f",
                        "surface-container": "#eceeee",
                        "on-secondary-fixed": "#101c2b",
                        "background": "#f8fafa",
                        "surface-dim": "#d8dada",
                        "primary-fixed-dim": "#ffb86f",
                        "surface": "#f8fafa",
                        "on-error": "#ffffff",
                        "on-primary-fixed": "#2c1600",
                        "inverse-surface": "#2e3131"
                    },
                    "borderRadius": {
                        "DEFAULT": "0.125rem",
                        "lg": "0.25rem",
                        "xl": "0.5rem",
                        "full": "0.75rem"
                    },
                    "spacing": {
                        "unit": "4px",
                        "gutter": "16px",
                        "margin-mobile": "16px",
                        "container-padding": "24px",
                        "max-width": "1440px",
                        "margin-desktop": "32px"
                    },
                    "fontFamily": {
                        "body-sm": ["Inter"],
                        "data-mono": ["JetBrains Mono"],
                        "body-lg": ["Inter"],
                        "label-caps": ["Inter"],
                        "headline-sm": ["Inter"],
                        "display-md": ["Inter"],
                        "body-md": ["Inter"],
                        "display-lg": ["Inter"]
                    },
                    "fontSize": {
                        "body-sm": ["12px", {"lineHeight": "16px", "fontWeight": "400"}],
                        "data-mono": ["13px", {"lineHeight": "18px", "fontWeight": "500"}],
                        "body-lg": ["16px", {"lineHeight": "24px", "fontWeight": "400"}],
                        "label-caps": ["11px", {"lineHeight": "16px", "letterSpacing": "0.05em", "fontWeight": "700"}],
                        "headline-sm": ["18px", {"lineHeight": "24px", "fontWeight": "600"}],
                        "display-md": ["24px", {"lineHeight": "32px", "letterSpacing": "-0.01em", "fontWeight": "600"}],
                        "body-md": ["14px", {"lineHeight": "20px", "fontWeight": "400"}],
                        "display-lg": ["32px", {"lineHeight": "40px", "letterSpacing": "-0.02em", "fontWeight": "700"}]
                    }
                }
            }
        }
    </script>
<style>
        .material-symbols-outlined {
            font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
            vertical-align: middle;
        }
        ::-webkit-scrollbar { width: 6px; height: 6px; }
        ::-webkit-scrollbar-track { background: transparent; }
        ::-webkit-scrollbar-thumb { background: #e1e3e3; border-radius: 10px; }
        ::-webkit-scrollbar-thumb:hover { background: #887361; }
        .zebra-table tr:nth-child(even) { background-color: #f8fafa; }
    </style>
</head>
<body class="bg-surface text-on-surface font-body-md overflow-hidden">
<!-- Side Navigation Shell -->
<aside class="fixed left-0 top-0 h-full flex flex-col py-margin-desktop z-40 bg-surface dark:bg-surface-dim border-r border-outline-variant dark:border-outline w-64">
<div class="px-6 mb-8">
<h1 class="font-headline-sm text-primary flex items-center gap-2">
<span class="material-symbols-outlined" data-icon="analytics">analytics</span>
                AdTracker Pro
            </h1>
<p class="text-body-sm text-on-surface-variant opacity-70 mt-1">Seller Central ID: 4829</p>
</div>
<nav class="flex-1 overflow-y-auto px-3 space-y-1">
<!-- Nav Item: Dashboard -->
<a class="flex items-center gap-3 px-3 py-2 text-secondary dark:text-secondary-fixed-dim hover:bg-surface-container transition-all font-label-caps text-label-caps rounded-lg" href="#">
<span class="material-symbols-outlined" data-icon="dashboard">dashboard</span>
                Dashboard
            </a>
<!-- Nav Item: Campaigns -->
<a class="flex items-center gap-3 px-3 py-2 text-secondary dark:text-secondary-fixed-dim hover:bg-surface-container transition-all font-label-caps text-label-caps rounded-lg" href="#">
<span class="material-symbols-outlined" data-icon="campaign">campaign</span>
                Campaigns
            </a>
<!-- Nav Item: Products -->
<a class="flex items-center gap-3 px-3 py-2 text-secondary dark:text-secondary-fixed-dim hover:bg-surface-container transition-all font-label-caps text-label-caps rounded-lg" href="#">
<span class="material-symbols-outlined" data-icon="inventory_2">inventory_2</span>
                Products
            </a>
<!-- Nav Item: Match Type -->
<a class="flex items-center gap-3 px-3 py-2 text-secondary dark:text-secondary-fixed-dim hover:bg-surface-container transition-all font-label-caps text-label-caps rounded-lg" href="#">
<span class="material-symbols-outlined" data-icon="analytics">analytics</span>
                Match Type
            </a>
<!-- Nav Item: Keywords -->
<a class="flex items-center gap-3 px-3 py-2 text-secondary dark:text-secondary-fixed-dim hover:bg-surface-container transition-all font-label-caps text-label-caps rounded-lg" href="#">
<span class="material-symbols-outlined" data-icon="key">key</span>
                Keywords
            </a>
<!-- Nav Item: Search Terms -->
<a class="flex items-center gap-3 px-3 py-2 text-secondary dark:text-secondary-fixed-dim hover:bg-surface-container transition-all font-label-caps text-label-caps rounded-lg" href="#">
<span class="material-symbols-outlined" data-icon="search">search</span>
                Search Terms
            </a>
<!-- Nav Item: ASIN Targets -->
<a class="flex items-center gap-3 px-3 py-2 text-secondary dark:text-secondary-fixed-dim hover:bg-surface-container transition-all font-label-caps text-label-caps rounded-lg" href="#">
<span class="material-symbols-outlined" data-icon="target">target</span>
                ASIN Targets
            </a>
<!-- Nav Item: ASIN from STR -->
<a class="flex items-center gap-3 px-3 py-2 text-secondary dark:text-secondary-fixed-dim hover:bg-surface-container transition-all font-label-caps text-label-caps rounded-lg" href="#">
<span class="material-symbols-outlined" data-icon="query_stats">query_stats</span>
                ASIN from STR
            </a>
<!-- Nav Item: Auto Campaigns -->
<a class="flex items-center gap-3 px-3 py-2 text-secondary dark:text-secondary-fixed-dim hover:bg-surface-container transition-all font-label-caps text-label-caps rounded-lg" href="#">
<span class="material-symbols-outlined" data-icon="smart_toy">smart_toy</span>
                Auto Campaigns
            </a>
<!-- Nav Item: Category Targets (ACTIVE) -->
<a class="flex items-center gap-3 px-3 py-2 bg-tertiary-container dark:bg-tertiary text-on-tertiary-container dark:text-on-tertiary font-bold font-label-caps text-label-caps rounded-lg transition-all" href="#">
<span class="material-symbols-outlined" data-icon="category" style="font-variation-settings: 'FILL' 1;">category</span>
                Category Targets
            </a>
<!-- Nav Item: Wasted Ad Spend -->
<a class="flex items-center gap-3 px-3 py-2 text-secondary dark:text-secondary-fixed-dim hover:bg-surface-container transition-all font-label-caps text-label-caps rounded-lg" href="#">
<span class="material-symbols-outlined" data-icon="receipt_long">receipt_long</span>
                Wasted Ad Spend
            </a>
</nav>
<div class="mt-auto px-4 pt-6 border-t border-outline-variant">
<button class="w-full py-3 bg-primary-container text-on-primary-container font-bold rounded shadow-sm hover:opacity-90 transition-opacity flex items-center justify-center gap-2">
<span class="material-symbols-outlined" data-icon="add">add</span>
                Create Campaign
            </button>
<div class="mt-6 flex items-center gap-3">
<img alt="Account Manager" class="w-8 h-8 rounded-full border border-outline-variant" data-alt="A professional headshot of a smiling male account manager in business casual attire. The image has a clean, high-key studio lighting set against a soft, neutral-gray background, matching the professional and corporate aesthetic of a high-end data dashboard system." src="https://lh3.googleusercontent.com/aida-public/AB6AXuBi4JiMB-m3FEPyywc3P2lqoB0ytxASxZyFDPWg06OMTyAJFJAZKxnJ1-8Ns2i7FY3Y1Nr-j-DHqJEtj50OSfQH_EINnNZ6Kpau-zPqj9btoB_vZv4oML-yu4MfoYBXleDBDxMHRhouWEHhI9ZXFw9huFnQXbjVW_ChFvPRFUqIT33dR1UVd3_M8G-ZabqMLwr31kOueli-2tWTMGtXWSmQbucsCgzRCCy87AYWJ0o6RCXJLhYVxgkkMshD0M8h2bA21SHY8wr6"/>
<div class="overflow-hidden">
<p class="text-body-sm font-bold truncate">Alex Rivera</p>
<p class="text-label-caps text-on-surface-variant text-[9px] opacity-60">SENIOR ANALYST</p>
</div>
<span class="material-symbols-outlined ml-auto text-on-surface-variant cursor-pointer" data-icon="logout">logout</span>
</div>
</div>
</aside>
<!-- Main Content Area -->
<main class="ml-64 h-screen flex flex-col overflow-hidden relative">
<!-- Top Bar Shell -->
<header class="flex justify-between items-center w-full px-margin-desktop h-14 z-50 bg-surface-container-lowest dark:bg-surface-dim border-b border-outline-variant dark:border-outline">
<div class="flex items-center gap-4">
<h2 class="text-headline-sm font-bold text-on-surface">Category Targets</h2>
<div class="h-6 w-px bg-outline-variant"></div>
<div class="flex items-center gap-2 bg-surface-container px-3 py-1.5 rounded text-body-sm cursor-pointer hover:bg-surface-container-high transition-colors">
<span class="material-symbols-outlined text-[18px]" data-icon="calendar_today">calendar_today</span>
<span class="font-medium">Last 30 Days</span>
<span class="material-symbols-outlined text-[16px]" data-icon="expand_more">expand_more</span>
</div>
</div>
<div class="flex items-center gap-3">
<button class="px-4 py-1.5 text-secondary border border-outline-variant rounded font-medium text-body-sm hover:bg-surface-container transition-colors flex items-center gap-2">
<span class="material-symbols-outlined text-[18px]" data-icon="download">download</span>
                    Export
                </button>
<div class="flex items-center gap-2">
<span class="material-symbols-outlined p-2 text-on-surface-variant hover:bg-surface-container rounded-full cursor-pointer transition-colors" data-icon="notifications">notifications</span>
<span class="material-symbols-outlined p-2 text-on-surface-variant hover:bg-surface-container rounded-full cursor-pointer transition-colors" data-icon="settings">settings</span>
</div>
</div>
</header>
<!-- Scrollable Body -->
<div class="flex-1 overflow-y-auto p-margin-desktop space-y-gutter">
<!-- Performance Summary Grid -->
<section class="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-7 gap-4">
<!-- KPI Card Template (Iterated for 13 metrics) -->
<!-- 1 Impressions -->
<div class="bg-surface-container-lowest border border-outline-variant p-4 rounded-lg flex flex-col justify-between h-28">
<div class="flex justify-between items-start">
<span class="font-label-caps text-label-caps text-on-surface-variant opacity-70 uppercase">Impressions</span>
<span class="text-error font-body-sm flex items-center">-2.4% <span class="material-symbols-outlined text-[14px]" data-icon="trending_down">trending_down</span></span>
</div>
<div class="mt-auto">
<span class="font-display-md text-display-md text-on-surface font-data-mono">1.2M</span>
</div>
</div>
<!-- 2 Clicks -->
<div class="bg-surface-container-lowest border border-outline-variant p-4 rounded-lg flex flex-col justify-between h-28">
<div class="flex justify-between items-start">
<span class="font-label-caps text-label-caps text-on-surface-variant opacity-70 uppercase">Clicks</span>
<span class="text-primary font-body-sm flex items-center">+5.1% <span class="material-symbols-outlined text-[14px]" data-icon="trending_up">trending_up</span></span>
</div>
<div class="mt-auto">
<span class="font-display-md text-display-md text-on-surface font-data-mono">48.2K</span>
</div>
</div>
<!-- 3 CTR -->
<div class="bg-surface-container-lowest border border-outline-variant p-4 rounded-lg flex flex-col justify-between h-28">
<div class="flex justify-between items-start">
<span class="font-label-caps text-label-caps text-on-surface-variant opacity-70 uppercase">CTR</span>
<span class="text-primary font-body-sm flex items-center">+0.08% <span class="material-symbols-outlined text-[14px]" data-icon="trending_up">trending_up</span></span>
</div>
<div class="mt-auto">
<span class="font-display-md text-display-md text-on-surface font-data-mono">4.01%</span>
</div>
</div>
<!-- 4 CVR -->
<div class="bg-surface-container-lowest border border-outline-variant p-4 rounded-lg flex flex-col justify-between h-28">
<div class="flex justify-between items-start">
<span class="font-label-caps text-label-caps text-on-surface-variant opacity-70 uppercase">CVR</span>
<span class="text-error font-body-sm flex items-center">-1.2% <span class="material-symbols-outlined text-[14px]" data-icon="trending_down">trending_down</span></span>
</div>
<div class="mt-auto">
<span class="font-display-md text-display-md text-on-surface font-data-mono">12.5%</span>
</div>
</div>
<!-- 5 CPC -->
<div class="bg-surface-container-lowest border border-outline-variant p-4 rounded-lg flex flex-col justify-between h-28">
<div class="flex justify-between items-start">
<span class="font-label-caps text-label-caps text-on-surface-variant opacity-70 uppercase">CPC</span>
<span class="text-on-surface-variant font-body-sm">Flat</span>
</div>
<div class="mt-auto">
<span class="font-display-md text-display-md text-on-surface font-data-mono">$1.12</span>
</div>
</div>
<!-- 6 Spend -->
<div class="bg-surface-container-lowest border border-outline-variant p-4 rounded-lg flex flex-col justify-between h-28">
<div class="flex justify-between items-start">
<span class="font-label-caps text-label-caps text-on-surface-variant opacity-70 uppercase">Spend</span>
<span class="text-primary font-body-sm flex items-center">+12% <span class="material-symbols-outlined text-[14px]" data-icon="trending_up">trending_up</span></span>
</div>
<div class="mt-auto">
<span class="font-display-md text-display-md text-on-surface font-data-mono">$54,012</span>
</div>
</div>
<!-- 7 Sales -->
<div class="bg-surface-container-lowest border border-outline-variant p-4 rounded-lg flex flex-col justify-between h-28">
<div class="flex justify-between items-start">
<span class="font-label-caps text-label-caps text-on-surface-variant opacity-70 uppercase">Sales</span>
<span class="text-primary font-body-sm flex items-center">+18% <span class="material-symbols-outlined text-[14px]" data-icon="trending_up">trending_up</span></span>
</div>
<div class="mt-auto">
<span class="font-display-md text-display-md text-on-surface font-data-mono">$210,480</span>
</div>
</div>
<!-- 8 Orders -->
<div class="bg-surface-container-lowest border border-outline-variant p-4 rounded-lg flex flex-col justify-between h-28">
<div class="flex justify-between items-start">
<span class="font-label-caps text-label-caps text-on-surface-variant opacity-70 uppercase">Orders</span>
<span class="text-primary font-body-sm flex items-center">+6% <span class="material-symbols-outlined text-[14px]" data-icon="trending_up">trending_up</span></span>
</div>
<div class="mt-auto">
<span class="font-display-md text-display-md text-on-surface font-data-mono">6,025</span>
</div>
</div>
<!-- 9 Units -->
<div class="bg-surface-container-lowest border border-outline-variant p-4 rounded-lg flex flex-col justify-between h-28">
<div class="flex justify-between items-start">
<span class="font-label-caps text-label-caps text-on-surface-variant opacity-70 uppercase">Units</span>
<span class="text-primary font-body-sm flex items-center">+4% <span class="material-symbols-outlined text-[14px]" data-icon="trending_up">trending_up</span></span>
</div>
<div class="mt-auto">
<span class="font-display-md text-display-md text-on-surface font-data-mono">8,110</span>
</div>
</div>
<!-- 10 ACOS -->
<div class="bg-surface-container-lowest border border-outline-variant p-4 rounded-lg flex flex-col justify-between h-28 bg-surface-container-low">
<div class="flex justify-between items-start">
<span class="font-label-caps text-label-caps text-primary font-bold uppercase">ACOS</span>
<span class="text-primary font-body-sm flex items-center">-4.1% <span class="material-symbols-outlined text-[14px]" data-icon="trending_down">trending_down</span></span>
</div>
<div class="mt-auto">
<span class="font-display-md text-display-md text-primary font-data-mono">25.6%</span>
</div>
</div>
<!-- 11 ROAS -->
<div class="bg-surface-container-lowest border border-outline-variant p-4 rounded-lg flex flex-col justify-between h-28">
<div class="flex justify-between items-start">
<span class="font-label-caps text-label-caps text-on-surface-variant opacity-70 uppercase">ROAS</span>
<span class="text-primary font-body-sm flex items-center">+0.4x <span class="material-symbols-outlined text-[14px]" data-icon="trending_up">trending_up</span></span>
</div>
<div class="mt-auto">
<span class="font-display-md text-display-md text-on-surface font-data-mono">3.9x</span>
</div>
</div>
<!-- 12 Spend % Split -->
<div class="bg-surface-container-lowest border border-outline-variant p-4 rounded-lg flex flex-col justify-between h-28">
<div class="flex justify-between items-start">
<span class="font-label-caps text-label-caps text-on-surface-variant opacity-70 uppercase">Spend % Split</span>
</div>
<div class="mt-auto">
<span class="font-display-md text-display-md text-on-surface font-data-mono">14.2%</span>
</div>
</div>
<!-- 13 Sales % Split -->
<div class="bg-surface-container-lowest border border-outline-variant p-4 rounded-lg flex flex-col justify-between h-28">
<div class="flex justify-between items-start">
<span class="font-label-caps text-label-caps text-on-surface-variant opacity-70 uppercase">Sales % Split</span>
</div>
<div class="mt-auto">
<span class="font-display-md text-display-md text-on-surface font-data-mono">22.8%</span>
</div>
</div>
</section>
<!-- Table Controls/Filters -->
<section class="bg-surface-container-lowest border border-outline-variant p-4 rounded-lg flex flex-wrap items-center gap-4">
<div class="flex-1 min-w-[200px] relative">
<span class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-on-surface-variant" data-icon="search">search</span>
<input class="w-full bg-surface-container-low border-outline-variant rounded py-2 pl-10 pr-4 text-body-sm focus:ring-1 focus:ring-primary focus:border-primary outline-none" placeholder="Filter categories or campaigns..." type="text"/>
</div>
<div class="flex items-center gap-2">
<span class="text-body-sm font-bold text-on-surface-variant">Metric Filter:</span>
<select class="bg-surface-container-low border-outline-variant rounded py-1.5 px-3 text-body-sm outline-none focus:ring-1 focus:ring-primary">
<option>ACOS &gt; 30%</option>
<option>ROAS &lt; 2.0x</option>
<option>Spend &gt; $500</option>
</select>
</div>
<div class="flex items-center gap-2">
<span class="text-body-sm font-bold text-on-surface-variant">Campaign Filter:</span>
<select class="bg-surface-container-low border-outline-variant rounded py-1.5 px-3 text-body-sm outline-none focus:ring-1 focus:ring-primary">
<option>All Active Campaigns</option>
<option>SB_Video_Core</option>
<option>SP_Category_Growth</option>
</select>
</div>
<button class="ml-auto text-secondary text-body-sm font-medium hover:underline">Clear all filters</button>
</section>
<!-- Data Table Container -->
<section class="bg-surface-container-lowest border border-outline-variant rounded-lg overflow-hidden flex-1 flex flex-col min-h-0">
<div class="overflow-x-auto flex-1">
<table class="w-full zebra-table border-collapse text-left">
<thead class="sticky top-0 bg-surface-container-low z-10">
<tr class="font-label-caps text-label-caps text-on-surface-variant border-b border-outline-variant">
<th class="py-3 px-4 w-12 text-center">Status</th>
<th class="py-3 px-4 min-w-[240px]">Category Target</th>
<th class="py-3 px-4 min-w-[180px]">Parent Campaign</th>
<th class="py-3 px-4 text-right">Impr.</th>
<th class="py-3 px-4 text-right">Clicks</th>
<th class="py-3 px-4 text-right">CTR</th>
<th class="py-3 px-4 text-right">CVR</th>
<th class="py-3 px-4 text-right">CPC</th>
<th class="py-3 px-4 text-right">Spend</th>
<th class="py-3 px-4 text-right">Sales</th>
<th class="py-3 px-4 text-right">Orders</th>
<th class="py-3 px-4 text-right">Units</th>
<th class="py-3 px-4 text-right text-primary">ACOS</th>
<th class="py-3 px-4 text-right">ROAS</th>
<th class="py-3 px-4 text-right">Spend %</th>
<th class="py-3 px-4 text-right">Sales %</th>
</tr>
</thead>
<tbody class="divide-y divide-outline-variant text-body-sm">
<!-- Row 1 -->
<tr class="hover:bg-surface-container-high transition-colors">
<td class="py-2 px-4 text-center">
<div class="w-8 h-4 bg-primary-container rounded-full relative cursor-pointer mx-auto">
<div class="absolute right-1 top-1 w-2 h-2 bg-white rounded-full"></div>
</div>
</td>
<td class="py-2 px-4">
<div class="flex items-center gap-2">
<span class="material-symbols-outlined text-on-surface-variant text-[18px]" data-icon="coffee_maker">coffee_maker</span>
<span class="font-medium">Home &amp; Kitchen &gt; Small Appliances</span>
</div>
</td>
<td class="py-2 px-4 text-on-surface-variant">SP_Category_Growth_Q3</td>
<td class="py-2 px-4 text-right font-data-mono">412,050</td>
<td class="py-2 px-4 text-right font-data-mono">15,420</td>
<td class="py-2 px-4 text-right font-data-mono">3.74%</td>
<td class="py-2 px-4 text-right font-data-mono">14.2%</td>
<td class="py-2 px-4 text-right font-data-mono">$1.05</td>
<td class="py-2 px-4 text-right font-data-mono">$16,191</td>
<td class="py-2 px-4 text-right font-data-mono">$65,240</td>
<td class="py-2 px-4 text-right font-data-mono">2,190</td>
<td class="py-2 px-4 text-right font-data-mono">2,850</td>
<td class="py-2 px-4 text-right font-data-mono font-bold text-primary">24.8%</td>
<td class="py-2 px-4 text-right font-data-mono">4.03x</td>
<td class="py-2 px-4 text-right font-data-mono">30.0%</td>
<td class="py-2 px-4 text-right font-data-mono">31.0%</td>
</tr>
<!-- Row 2 -->
<tr class="hover:bg-surface-container-high transition-colors">
<td class="py-2 px-4 text-center">
<div class="w-8 h-4 bg-primary-container rounded-full relative cursor-pointer mx-auto">
<div class="absolute right-1 top-1 w-2 h-2 bg-white rounded-full"></div>
</div>
</td>
<td class="py-2 px-4">
<div class="flex items-center gap-2">
<span class="material-symbols-outlined text-on-surface-variant text-[18px]" data-icon="blender">blender</span>
<span class="font-medium">Kitchen &amp; Dining &gt; Blenders</span>
</div>
</td>
<td class="py-2 px-4 text-on-surface-variant">SP_Category_Growth_Q3</td>
<td class="py-2 px-4 text-right font-data-mono">285,120</td>
<td class="py-2 px-4 text-right font-data-mono">9,240</td>
<td class="py-2 px-4 text-right font-data-mono">3.24%</td>
<td class="py-2 px-4 text-right font-data-mono">11.1%</td>
<td class="py-2 px-4 text-right font-data-mono">$1.18</td>
<td class="py-2 px-4 text-right font-data-mono">$10,903</td>
<td class="py-2 px-4 text-right font-data-mono">$38,250</td>
<td class="py-2 px-4 text-right font-data-mono">1,025</td>
<td class="py-2 px-4 text-right font-data-mono">1,410</td>
<td class="py-2 px-4 text-right font-data-mono font-bold text-primary">28.5%</td>
<td class="py-2 px-4 text-right font-data-mono">3.51x</td>
<td class="py-2 px-4 text-right font-data-mono">20.2%</td>
<td class="py-2 px-4 text-right font-data-mono">18.2%</td>
</tr>
<!-- Row 3 -->
<tr class="hover:bg-surface-container-high transition-colors">
<td class="py-2 px-4 text-center">
<div class="w-8 h-4 bg-surface-container-highest rounded-full relative cursor-pointer mx-auto">
<div class="absolute left-1 top-1 w-2 h-2 bg-white rounded-full"></div>
</div>
</td>
<td class="py-2 px-4">
<div class="flex items-center gap-2">
<span class="material-symbols-outlined text-on-surface-variant text-[18px]" data-icon="restaurant">restaurant</span>
<span class="font-medium">Dining &gt; Cutlery &amp; Utensils</span>
</div>
</td>
<td class="py-2 px-4 text-on-surface-variant">SB_Brand_Offensive</td>
<td class="py-2 px-4 text-right font-data-mono">112,400</td>
<td class="py-2 px-4 text-right font-data-mono">4,110</td>
<td class="py-2 px-4 text-right font-data-mono">3.65%</td>
<td class="py-2 px-4 text-right font-data-mono">8.5%</td>
<td class="py-2 px-4 text-right font-data-mono">$0.85</td>
<td class="py-2 px-4 text-right font-data-mono">$3,493</td>
<td class="py-2 px-4 text-right font-data-mono">$12,400</td>
<td class="py-2 px-4 text-right font-data-mono">349</td>
<td class="py-2 px-4 text-right font-data-mono">512</td>
<td class="py-2 px-4 text-right font-data-mono font-bold text-primary">28.2%</td>
<td class="py-2 px-4 text-right font-data-mono">3.55x</td>
<td class="py-2 px-4 text-right font-data-mono">6.5%</td>
<td class="py-2 px-4 text-right font-data-mono">5.9%</td>
</tr>
<!-- Row 4 -->
<tr class="hover:bg-surface-container-high transition-colors">
<td class="py-2 px-4 text-center">
<div class="w-8 h-4 bg-primary-container rounded-full relative cursor-pointer mx-auto">
<div class="absolute right-1 top-1 w-2 h-2 bg-white rounded-full"></div>
</div>
</td>
<td class="py-2 px-4">
<div class="flex items-center gap-2">
<span class="material-symbols-outlined text-on-surface-variant text-[18px]" data-icon="skillet">skillet</span>
<span class="font-medium">Kitchen &gt; Cookware &gt; Pans</span>
</div>
</td>
<td class="py-2 px-4 text-on-surface-variant">SP_Category_Growth_Q3</td>
<td class="py-2 px-4 text-right font-data-mono">350,900</td>
<td class="py-2 px-4 text-right font-data-mono">12,100</td>
<td class="py-2 px-4 text-right font-data-mono">3.45%</td>
<td class="py-2 px-4 text-right font-data-mono">13.8%</td>
<td class="py-2 px-4 text-right font-data-mono">$1.10</td>
<td class="py-2 px-4 text-right font-data-mono">$13,310</td>
<td class="py-2 px-4 text-right font-data-mono">$58,420</td>
<td class="py-2 px-4 text-right font-data-mono">1,670</td>
<td class="py-2 px-4 text-right font-data-mono">1,920</td>
<td class="py-2 px-4 text-right font-data-mono font-bold text-primary">22.8%</td>
<td class="py-2 px-4 text-right font-data-mono">4.39x</td>
<td class="py-2 px-4 text-right font-data-mono">24.6%</td>
<td class="py-2 px-4 text-right font-data-mono">27.7%</td>
</tr>
<!-- Row 5 (Inefficient row example) -->
<tr class="hover:bg-surface-container-high transition-colors">
<td class="py-2 px-4 text-center">
<div class="w-8 h-4 bg-primary-container rounded-full relative cursor-pointer mx-auto">
<div class="absolute right-1 top-1 w-2 h-2 bg-white rounded-full"></div>
</div>
</td>
<td class="py-2 px-4">
<div class="flex items-center gap-2">
<span class="material-symbols-outlined text-on-surface-variant text-[18px]" data-icon="lunch_dining">lunch_dining</span>
<span class="font-medium">Kitchen &gt; Food Storage</span>
</div>
</td>
<td class="py-2 px-4 text-on-surface-variant">SB_Brand_Offensive</td>
<td class="py-2 px-4 text-right font-data-mono">92,400</td>
<td class="py-2 px-4 text-right font-data-mono">2,840</td>
<td class="py-2 px-4 text-right font-data-mono">3.07%</td>
<td class="py-2 px-4 text-right font-data-mono">4.2%</td>
<td class="py-2 px-4 text-right font-data-mono">$1.25</td>
<td class="py-2 px-4 text-right font-data-mono">$3,550</td>
<td class="py-2 px-4 text-right font-data-mono">$8,210</td>
<td class="py-2 px-4 text-right font-data-mono">119</td>
<td class="py-2 px-4 text-right font-data-mono">240</td>
<td class="py-2 px-4 text-right font-data-mono font-bold text-error">43.2%</td>
<td class="py-2 px-4 text-right font-data-mono">2.31x</td>
<td class="py-2 px-4 text-right font-data-mono">6.6%</td>
<td class="py-2 px-4 text-right font-data-mono">3.9%</td>
</tr>
</tbody>
</table>
</div>
<!-- Table Pagination/Footer -->
<div class="p-3 border-t border-outline-variant bg-surface-container-low flex justify-between items-center text-body-sm text-on-surface-variant">
<div>Showing 1 - 5 of 48 Category Targets</div>
<div class="flex gap-2">
<button class="px-3 py-1 border border-outline-variant rounded hover:bg-surface-container transition-colors disabled:opacity-30" disabled="">Previous</button>
<button class="px-3 py-1 border border-outline-variant rounded bg-primary-container text-on-primary-container font-bold">1</button>
<button class="px-3 py-1 border border-outline-variant rounded hover:bg-surface-container transition-colors">2</button>
<button class="px-3 py-1 border border-outline-variant rounded hover:bg-surface-container transition-colors">3</button>
<button class="px-3 py-1 border border-outline-variant rounded hover:bg-surface-container transition-colors">Next</button>
</div>
</div>
</section>
</div>
<!-- Atmospheric Micro-interaction Layer -->
<div class="fixed bottom-gutter right-gutter z-[100] flex flex-col gap-2" id="toast-container"></div>
</main>
<script>
        // Micro-interaction: Status Toggle Simulation
        document.querySelectorAll('.zebra-table tr td:first-child div').forEach(toggle => {
            toggle.addEventListener('click', function() {
                const dot = this.querySelector('div');
                if (this.classList.contains('bg-primary-container')) {
                    this.classList.remove('bg-primary-container');
                    this.classList.add('bg-surface-container-highest');
                    dot.classList.remove('right-1');
                    dot.classList.add('left-1');
                    showToast('Target paused successfully');
                } else {
                    this.classList.add('bg-primary-container');
                    this.classList.remove('bg-surface-container-highest');
                    dot.classList.add('right-1');
                    dot.classList.remove('left-1');
                    showToast('Target resumed successfully');
                }
            });
        });

        function showToast(message) {
            const container = document.getElementById('toast-container');
            const toast = document.createElement('div');
            toast.className = 'bg-inverse-surface text-inverse-on-surface px-4 py-3 rounded-lg shadow-xl flex items-center gap-3 animate-bounce-short';
            toast.innerHTML = `
                <span class="material-symbols-outlined text-primary-fixed" style="font-variation-settings: 'FILL' 1;">check_circle</span>
                <span class="text-body-md">${message}</span>
            `;
            container.appendChild(toast);
            setTimeout(() => {
                toast.classList.add('opacity-0', 'transition-opacity', 'duration-500');
                setTimeout(() => toast.remove(), 500);
            }, 3000);
        }

        // Custom style for short bounce
        const style = document.createElement('style');
        style.innerHTML = `
            @keyframes bounce-short {
                0%, 20%, 50%, 80%, 100% {transform: translateY(0);}
                40% {transform: translateY(-5px);}
                60% {transform: translateY(-3px);}
            }
            .animate-bounce-short {
                animation: bounce-short 0.5s ease-in-out;
            }
        `;
        document.head.appendChild(style);
    </script>
</body></html>

<!-- Category Targets - Performance Management -->
<!DOCTYPE html><html class="light" lang="en"><head>
<meta charset="utf-8">
<meta content="width=device-width, initial-scale=1.0" name="viewport">
<title>Wasted Ad Spend - AdTracker Pro</title>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;900&amp;family=JetBrains+Mono:wght@500&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet">
<script id="tailwind-config">
        tailwind.config = {
            darkMode: "class",
            theme: {
                extend: {
                    "colors": {
                        "surface": "#f8fafa",
                        "surface-variant": "#e1e3e3",
                        "tertiary-fixed-dim": "#80d2e9",
                        "inverse-primary": "#ffb86f",
                        "on-tertiary-fixed": "#001f26",
                        "surface-container-highest": "#e1e3e3",
                        "primary": "#8a5100",
                        "secondary-fixed": "#d7e3f7",
                        "background": "#f8fafa",
                        "inverse-on-surface": "#eff1f1",
                        "on-secondary-container": "#576474",
                        "error-container": "#ffdad6",
                        "tertiary": "#00687a",
                        "secondary": "#535f70",
                        "on-primary-fixed": "#2c1600",
                        "on-primary-fixed-variant": "#693c00",
                        "error": "#ba1a1a",
                        "primary-fixed-dim": "#ffb86f",
                        "outline": "#887361",
                        "surface-dim": "#d8dada",
                        "on-tertiary": "#ffffff",
                        "secondary-container": "#d4e1f5",
                        "on-secondary": "#ffffff",
                        "tertiary-fixed": "#adecff",
                        "primary-fixed": "#ffdcbd",
                        "surface-tint": "#8a5100",
                        "surface-container": "#eceeee",
                        "surface-bright": "#f8fafa",
                        "surface-container-lowest": "#ffffff",
                        "surface-container-low": "#f2f4f4",
                        "on-primary-container": "#653a00",
                        "on-error-container": "#93000a",
                        "outline-variant": "#dbc2ad",
                        "on-secondary-fixed-variant": "#3c4858",
                        "surface-container-high": "#e6e8e8",
                        "secondary-fixed-dim": "#bbc7db",
                        "on-background": "#191c1d",
                        "on-tertiary-container": "#004b59",
                        "on-surface": "#191c1d",
                        "on-error": "#ffffff",
                        "on-secondary-fixed": "#101c2b",
                        "on-primary": "#ffffff",
                        "tertiary-container": "#6abdd3",
                        "primary-container": "#ff9900",
                        "on-surface-variant": "#554434",
                        "inverse-surface": "#2e3131",
                        "on-tertiary-fixed-variant": "#004e5d"
                    },
                    "borderRadius": {
                        "DEFAULT": "0.125rem",
                        "lg": "0.25rem",
                        "xl": "0.5rem",
                        "full": "0.75rem"
                    },
                    "spacing": {
                        "max-width": "1440px",
                        "container-padding": "24px",
                        "margin-desktop": "32px",
                        "margin-mobile": "16px",
                        "gutter": "16px",
                        "unit": "4px"
                    },
                    "fontFamily": {
                        "label-caps": ["Inter"],
                        "data-mono": ["JetBrains Mono"],
                        "headline-sm": ["Inter"],
                        "display-lg": ["Inter"],
                        "body-lg": ["Inter"],
                        "display-md": ["Inter"],
                        "body-md": ["Inter"],
                        "body-sm": ["Inter"]
                    },
                    "fontSize": {
                        "label-caps": ["11px", {"lineHeight": "16px", "letterSpacing": "0.05em", "fontWeight": "700"}],
                        "data-mono": ["13px", {"lineHeight": "18px", "fontWeight": "500"}],
                        "headline-sm": ["18px", {"lineHeight": "24px", "fontWeight": "600"}],
                        "display-lg": ["32px", {"lineHeight": "40px", "letterSpacing": "-0.02em", "fontWeight": "700"}],
                        "body-lg": ["16px", {"lineHeight": "24px", "fontWeight": "400"}],
                        "display-md": ["24px", {"lineHeight": "32px", "letterSpacing": "-0.01em", "fontWeight": "600"}],
                        "body-md": ["14px", {"lineHeight": "20px", "fontWeight": "400"}],
                        "body-sm": ["12px", {"lineHeight": "16px", "fontWeight": "400"}]
                    }
                }
            }
        }
    </script>
<style>
        .material-symbols-outlined {
            font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
            vertical-align: middle;
        }
        .custom-scrollbar::-webkit-scrollbar { width: 4px; }
        .custom-scrollbar::-webkit-scrollbar-track { background: transparent; }
        .custom-scrollbar::-webkit-scrollbar-thumb { background: #e1e3e3; border-radius: 10px; }
        .zebra-table tr:nth-child(even) { background-color: #f2f4f4; }
    </style>
</head>
<body class="bg-surface font-body-md text-on-surface">
<!-- TopNavBar -->
<header class="flex justify-between items-center w-full px-margin-desktop h-16 sticky top-0 z-40 bg-surface border-b border-surface-variant">
<div class="flex items-center gap-8">
<span class="text-display-md font-display-md font-bold text-primary">AdTracker Pro</span>
<div class="relative hidden md:block">
<span class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-on-surface-variant">search</span>
<input class="pl-10 pr-4 py-2 bg-surface-container-low border border-outline-variant rounded-lg w-64 focus:ring-2 focus:ring-tertiary outline-none transition-all font-body-sm" placeholder="Search keywords..." type="text">
</div>
</div>
<div class="flex items-center gap-4">
<button class="material-symbols-outlined text-on-surface-variant hover:bg-surface-container-high p-2 rounded-full transition-colors cursor-pointer active:opacity-80">notifications</button>
<button class="material-symbols-outlined text-on-surface-variant hover:bg-surface-container-high p-2 rounded-full transition-colors cursor-pointer active:opacity-80">settings</button>
<div class="h-8 w-8 rounded-full bg-secondary-container flex items-center justify-center overflow-hidden border border-outline-variant">
<img alt="User profile" data-alt="A professional headshot of a smiling agency manager in their thirties, set against a blurred office background with warm afternoon sunlight. The image is clean and corporate, featuring natural skin tones and professional attire, reflecting a high-trust analytical environment." src="https://lh3.googleusercontent.com/aida-public/AB6AXuCYvxQNuVYi6wMBbXN78CQcykkYhG4YCu4__hsQT3DwYz_qoANfteEQmkFNx5k5wVLzKeKEIEQlEFdTmKe5ABifw5wVkfBuHai0SnLd_Q7HccjjHMBiz-aXTGe_tjhx1LS0jNjZeszUHW8apvVfV-wOY2GoJ33GGeo-uwSe4lpMMIASlXkHNvA_TvHCItMApF5l0sNiZ9dlxZM24kpIfGnOCYDWg1JlPxwdJ8Zr_WXfUooGNTY5H5wQLdJLJ2N4FLiL_hygWoXu">
</div>
</div>
</header>
<div class="flex min-h-screen">
<!-- SideNavBar -->
<nav class="flex flex-col fixed left-0 top-16 h-[calc(100vh-64px)] w-64 py-6 px-4 bg-surface-container-low border-r border-surface-variant overflow-y-auto custom-scrollbar">
<div class="mb-8 px-2">
<h2 class="font-display-md text-headline-sm text-primary font-black">Performance</h2>
<p class="text-on-surface-variant text-body-sm opacity-70">PPC Control Center</p>
</div>
<div class="space-y-1 flex-1">
<!-- Navigation Items -->
<a class="flex items-center gap-3 px-3 py-2 text-on-surface-variant hover:bg-surface-container-high rounded-lg transition-all scale-95 duration-150" href="#">
<span class="material-symbols-outlined">dashboard</span>
<span class="font-label-caps text-label-caps">Dashboard</span>
</a>
<a class="flex items-center gap-3 px-3 py-2 text-on-surface-variant hover:bg-surface-container-high rounded-lg transition-all scale-95 duration-150" href="#">
<span class="material-symbols-outlined">campaign</span>
<span class="font-label-caps text-label-caps">Campaigns</span>
</a>
<a class="flex items-center gap-3 px-3 py-2 text-on-surface-variant hover:bg-surface-container-high rounded-lg transition-all scale-95 duration-150" href="#">
<span class="material-symbols-outlined">inventory_2</span>
<span class="font-label-caps text-label-caps">Products</span>
</a>
<a class="flex items-center gap-3 px-3 py-2 text-on-surface-variant hover:bg-surface-container-high rounded-lg transition-all scale-95 duration-150" href="#">
<span class="material-symbols-outlined">format_list_bulleted</span>
<span class="font-label-caps text-label-caps">Match Type</span>
</a>
<a class="flex items-center gap-3 px-3 py-2 text-on-surface-variant hover:bg-surface-container-high rounded-lg transition-all scale-95 duration-150" href="#">
<span class="material-symbols-outlined">key</span>
<span class="font-label-caps text-label-caps">Keywords</span>
</a>
<a class="flex items-center gap-3 px-3 py-2 text-on-surface-variant hover:bg-surface-container-high rounded-lg transition-all scale-95 duration-150" href="#">
<span class="material-symbols-outlined">search</span>
<span class="font-label-caps text-label-caps">Search Terms</span>
</a>
<a class="flex items-center gap-3 px-3 py-2 text-on-surface-variant hover:bg-surface-container-high rounded-lg transition-all scale-95 duration-150" href="#">
<span class="material-symbols-outlined">target</span>
<span class="font-label-caps text-label-caps">ASIN Targets</span>
</a>
<a class="flex items-center gap-3 px-3 py-2 text-on-surface-variant hover:bg-surface-container-high rounded-lg transition-all scale-95 duration-150" href="#">
<span class="material-symbols-outlined">track_changes</span>
<span class="font-label-caps text-label-caps">ASIN from STR</span>
</a>
<a class="flex items-center gap-3 px-3 py-2 text-on-surface-variant hover:bg-surface-container-high rounded-lg transition-all scale-95 duration-150" href="#">
<span class="material-symbols-outlined">smart_toy</span>
<span class="font-label-caps text-label-caps">Auto Campaigns</span>
</a>
<a class="flex items-center gap-3 px-3 py-2 text-on-surface-variant hover:bg-surface-container-high rounded-lg transition-all scale-95 duration-150" href="#">
<span class="material-symbols-outlined">category</span>
<span class="font-label-caps text-label-caps">Category Targets</span>
</a>
<a class="flex items-center gap-3 px-3 py-2 bg-tertiary-container text-on-tertiary-container font-bold rounded-lg transition-all scale-95 duration-150" href="#">
<span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">delete_forever</span>
<span class="font-label-caps text-label-caps">Wasted Ad Spend</span>
</a>
</div>
<div class="mt-auto pt-4 space-y-1">
<a class="flex items-center gap-3 px-3 py-2 text-on-surface-variant hover:bg-surface-container-high rounded-lg transition-all" href="#">
<span class="material-symbols-outlined">help</span>
<span class="font-label-caps text-label-caps">Support</span>
</a>
<a class="flex items-center gap-3 px-3 py-2 text-on-surface-variant hover:bg-surface-container-high rounded-lg transition-all" href="#">
<span class="material-symbols-outlined">logout</span>
<span class="font-label-caps text-label-caps">Sign Out</span>
</a>
</div>
</nav>
<!-- Main Content -->
<main class="ml-64 w-full p-margin-desktop overflow-x-hidden">
<!-- Header Section -->
<div class="mb-8">
<div class="flex justify-between items-start mb-6">
<div>
<h1 class="font-display-lg text-display-lg text-on-surface tracking-tight">Wasted Ad Spend</h1>
<p class="font-body-md text-secondary mt-1">Search terms with spend but no sales (Orders = 0)</p>
</div>
<button class="bg-[#ff9900] text-white px-6 py-2 rounded-lg font-headline-sm hover:opacity-90 transition-opacity flex items-center gap-2">
<span class="material-symbols-outlined text-[20px]">download</span>
                        Export Report
                    </button>
</div>
<!-- Global Filters -->
<div class="grid grid-cols-12 gap-gutter bg-surface-container-lowest p-6 border border-surface-variant rounded-xl shadow-sm">
<div class="col-span-12 md:col-span-3">
<label class="block font-body-sm font-bold mb-2">Spend Threshold ($)</label>
<input class="w-full h-1 bg-surface-variant rounded-lg appearance-none cursor-pointer accent-primary" max="1000" min="1" type="range" value="50">
<div class="flex justify-between mt-1 text-[10px] font-data-mono text-on-surface-variant">
<span class="">$1</span>
<span class="">$1000</span>
</div>
</div>
<div class="col-span-12 md:col-span-3">
<label class="block font-body-sm font-bold mb-2">Match Type</label>
<div class="flex gap-2">
<select class="w-full bg-surface border border-outline-variant rounded p-2 text-body-sm focus:ring-1 focus:ring-tertiary">
<option>All Match Types</option>
<option>Broad</option>
<option>Phrase</option>
<option>Exact</option>
</select>
</div>
</div>
<div class="col-span-12 md:col-span-3">
<label class="block font-body-sm font-bold mb-2">Targeting Type</label>
<select class="w-full bg-surface border border-outline-variant rounded p-2 text-body-sm">
<option>All Types</option>
<option>Manual</option>
<option>Auto</option>
</select>
</div>
<div class="col-span-12 md:col-span-3">
<label class="block font-body-sm font-bold mb-2">Auto-Targeting Groups</label>
<select class="w-full bg-surface border border-outline-variant rounded p-2 text-body-sm">
<option>All Groups</option>
<option>Close Match</option>
<option>Loose Match</option>
<option>Substitutes</option>
<option>Complements</option>
</select>
</div>
</div>
</div>
<!-- Metrics Summary -->
<div class="grid grid-cols-12 gap-gutter mb-8">
<!-- KPI Card: Total Wasted Spend -->
<div class="col-span-12 md:col-span-4 bg-surface-container-lowest p-5 border border-surface-variant rounded-xl">
<div class="flex justify-between items-start mb-2">
<span class="font-label-caps text-label-caps text-secondary opacity-70">TOTAL WASTED SPEND</span>
<span class="bg-error-container text-on-error-container px-2 py-0.5 rounded-full text-[10px] font-bold">+12.4%</span>
</div>
<div class="font-display-md text-display-md text-error tracking-tighter">$14,290.45</div>
<div class="mt-4 h-1 bg-surface-variant rounded-full overflow-hidden">
<div class="bg-error h-full w-3/4"></div>
</div>
</div>
<!-- KPI Card: Impressions/Clicks Group -->
<div class="col-span-12 md:col-span-4 bg-surface-container-lowest p-5 border border-surface-variant rounded-xl grid grid-cols-2 gap-4">
<div>
<span class="font-label-caps text-label-caps text-secondary opacity-70">IMPRESSIONS</span>
<div class="font-display-md text-headline-sm font-bold text-on-surface mt-1">2.4M</div>
<span class="text-[10px] text-error font-bold flex items-center gap-1">
<span class="material-symbols-outlined text-[12px]">trending_up</span> 4% vs LW
                        </span>
</div>
<div>
<span class="font-label-caps text-label-caps text-secondary opacity-70">CLICKS</span>
<div class="font-display-md text-headline-sm font-bold text-on-surface mt-1">12,840</div>
<span class="text-[10px] text-error font-bold flex items-center gap-1">
<span class="material-symbols-outlined text-[12px]">trending_up</span> 8% vs LW
                        </span>
</div>
</div>
<!-- KPI Card: CTR/CVR/CPC -->
<div class="col-span-12 md:col-span-4 bg-surface-container-lowest p-5 border border-surface-variant rounded-xl flex flex-col justify-between">
<div class="grid grid-cols-3 gap-2 text-center">
<div>
<span class="font-label-caps text-label-caps text-secondary opacity-70">CTR</span>
<div class="font-data-mono text-body-lg font-bold mt-1">0.53%</div>
</div>
<div>
<span class="font-label-caps text-label-caps text-secondary opacity-70">CVR</span>
<div class="font-data-mono text-body-lg font-bold mt-1 text-on-surface-variant">0.00%</div>
</div>
<div>
<span class="font-label-caps text-label-caps text-secondary opacity-70">CPC</span>
<div class="font-data-mono text-body-lg font-bold mt-1">$1.11</div>
</div>
</div>
<div class="mt-4 text-[11px] text-on-surface-variant italic border-t border-surface-variant pt-2">
                        Inefficiency identified across 4,201 unique search terms.
                    </div>
</div>
</div>
<!-- Data Table -->
<div class="bg-surface-container-lowest border border-surface-variant rounded-xl overflow-hidden shadow-sm">
<div class="p-4 border-b border-surface-variant flex justify-between items-center bg-surface-container-low">
<h3 class="font-headline-sm text-on-surface">Inefficient Search Terms</h3>
<div class="flex gap-2">
<button class="material-symbols-outlined p-2 hover:bg-surface-container-high rounded text-on-surface-variant">filter_list</button>
<button class="material-symbols-outlined p-2 hover:bg-surface-container-high rounded text-on-surface-variant">view_column</button>
</div>
</div>
<div class="overflow-x-auto">
<table class="w-full text-left border-collapse zebra-table">
<thead>
<tr class="bg-surface-container-low border-b border-surface-variant">
<th class="p-3 font-label-caps text-label-caps text-secondary">Search Term</th>
<th class="p-3 font-label-caps text-label-caps text-secondary">Match</th>
<th class="p-3 font-label-caps text-label-caps text-secondary">Target Type</th>
<th class="p-3 font-label-caps text-label-caps text-secondary">Target Group</th>
<th class="p-3 font-label-caps text-label-caps text-secondary text-right">Impr.</th>
<th class="p-3 font-label-caps text-label-caps text-secondary text-right">Clicks</th>
<th class="p-3 font-label-caps text-label-caps text-secondary text-right">CTR</th>
<th class="p-3 font-label-caps text-label-caps text-secondary text-right">CPC</th>
<th class="p-3 font-label-caps text-label-caps text-secondary text-right">Spend</th>
<th class="p-3 font-label-caps text-label-caps text-secondary text-right">Split %</th>
<th class="p-3 font-label-caps text-label-caps text-secondary text-center">Action</th>
</tr>
</thead>
<tbody class="text-body-sm font-data-mono">
<!-- Row 1 -->
<tr class="border-b border-surface-variant hover:bg-surface-container-high transition-colors">
<td class="p-3 font-body-sm font-bold text-on-surface">ergonomic desk chair extra cushion</td>
<td class="p-3"><span class="px-2 py-0.5 bg-secondary-container text-on-secondary-container rounded text-[10px]">Broad</span></td>
<td class="p-3 text-on-surface-variant">Manual</td>
<td class="p-3 text-on-surface-variant text-center">—</td>
<td class="p-3 text-right">45,200</td>
<td class="p-3 text-right">182</td>
<td class="p-3 text-right">0.40%</td>
<td class="p-3 text-right">$2.14</td>
<td class="p-3 text-right font-bold text-error">$389.48</td>
<td class="p-3 text-right">2.7%</td>
<td class="p-3 text-center">
<button class="text-primary hover:underline font-label-caps text-[10px] flex items-center justify-center gap-1 mx-auto">
<span class="material-symbols-outlined text-[14px]">block</span> NEGATIVE
                                    </button>
</td>
</tr>
<!-- Row 2 -->
<tr class="border-b border-surface-variant hover:bg-surface-container-high transition-colors">
<td class="p-3 font-body-sm font-bold text-on-surface">office supply bundle bulk</td>
<td class="p-3"><span class="px-2 py-0.5 bg-surface-variant text-on-surface-variant rounded text-[10px]">Auto</span></td>
<td class="p-3 text-on-surface-variant">Auto</td>
<td class="p-3 text-on-surface-variant">Loose Match</td>
<td class="p-3 text-right">12,401</td>
<td class="p-3 text-right">94</td>
<td class="p-3 text-right">0.75%</td>
<td class="p-3 text-right">$1.85</td>
<td class="p-3 text-right font-bold text-error">$173.90</td>
<td class="p-3 text-right">1.2%</td>
<td class="p-3 text-center">
<button class="text-primary hover:underline font-label-caps text-[10px] flex items-center justify-center gap-1 mx-auto">
<span class="material-symbols-outlined text-[14px]">block</span> NEGATIVE
                                    </button>
</td>
</tr>
<!-- Row 3 -->
<tr class="border-b border-surface-variant hover:bg-surface-container-high transition-colors">
<td class="p-3 font-body-sm font-bold text-on-surface">best gaming headset 2024</td>
<td class="p-3"><span class="px-2 py-0.5 bg-secondary-container text-on-secondary-container rounded text-[10px]">Phrase</span></td>
<td class="p-3 text-on-surface-variant">Manual</td>
<td class="p-3 text-on-surface-variant text-center">—</td>
<td class="p-3 text-right">8,220</td>
<td class="p-3 text-right">45</td>
<td class="p-3 text-right">0.54%</td>
<td class="p-3 text-right">$3.40</td>
<td class="p-3 text-right font-bold text-error">$153.00</td>
<td class="p-3 text-right">1.1%</td>
<td class="p-3 text-center">
<button class="text-primary hover:underline font-label-caps text-[10px] flex items-center justify-center gap-1 mx-auto">
<span class="material-symbols-outlined text-[14px]">block</span> NEGATIVE
                                    </button>
</td>
</tr>
<!-- Row 4 -->
<tr class="border-b border-surface-variant hover:bg-surface-container-high transition-colors">
<td class="p-3 font-body-sm font-bold text-on-surface">waterproof laptop bag</td>
<td class="p-3"><span class="px-2 py-0.5 bg-secondary-container text-on-secondary-container rounded text-[10px]">Exact</span></td>
<td class="p-3 text-on-surface-variant">Manual</td>
<td class="p-3 text-on-surface-variant text-center">—</td>
<td class="p-3 text-right">4,100</td>
<td class="p-3 text-right">62</td>
<td class="p-3 text-right">1.51%</td>
<td class="p-3 text-right">$1.98</td>
<td class="p-3 text-right font-bold text-error">$122.76</td>
<td class="p-3 text-right">0.8%</td>
<td class="p-3 text-center">
<button class="text-primary hover:underline font-label-caps text-[10px] flex items-center justify-center gap-1 mx-auto">
<span class="material-symbols-outlined text-[14px]">block</span> NEGATIVE
                                    </button>
</td>
</tr>
<!-- Row 5 -->
<tr class="border-b border-surface-variant hover:bg-surface-container-high transition-colors">
<td class="p-3 font-body-sm font-bold text-on-surface">discount electronics store</td>
<td class="p-3"><span class="px-2 py-0.5 bg-surface-variant text-on-surface-variant rounded text-[10px]">Auto</span></td>
<td class="p-3 text-on-surface-variant">Auto</td>
<td class="p-3 text-on-surface-variant">Complements</td>
<td class="p-3 text-right">19,430</td>
<td class="p-3 text-right">88</td>
<td class="p-3 text-right">0.45%</td>
<td class="p-3 text-right">$1.12</td>
<td class="p-3 text-right font-bold text-error">$98.56</td>
<td class="p-3 text-right">0.7%</td>
<td class="p-3 text-center">
<button class="text-primary hover:underline font-label-caps text-[10px] flex items-center justify-center gap-1 mx-auto">
<span class="material-symbols-outlined text-[14px]">block</span> NEGATIVE
                                    </button>
</td>
</tr>
</tbody>
</table>
</div>
<!-- Pagination -->
<div class="p-4 border-t border-surface-variant flex justify-between items-center bg-surface-container-low">
<span class="text-body-sm text-on-surface-variant font-data-mono">Showing 1-25 of 4,201 terms</span>
<div class="flex gap-1">
<button class="w-8 h-8 flex items-center justify-center border border-outline-variant rounded hover:bg-surface-container-high"><span class="material-symbols-outlined text-sm">chevron_left</span></button>
<button class="w-8 h-8 flex items-center justify-center bg-primary text-white rounded font-data-mono text-sm">1</button>
<button class="w-8 h-8 flex items-center justify-center border border-outline-variant rounded hover:bg-surface-container-high font-data-mono text-sm">2</button>
<button class="w-8 h-8 flex items-center justify-center border border-outline-variant rounded hover:bg-surface-container-high font-data-mono text-sm">3</button>
<button class="w-8 h-8 flex items-center justify-center border border-outline-variant rounded hover:bg-surface-container-high"><span class="material-symbols-outlined text-sm">chevron_right</span></button>
</div>
</div>
</div>
</main>
</div>
<!-- Micro-interactions Script -->
<script>
        document.querySelectorAll('button').forEach(button => {
            button.addEventListener('mousedown', function() {
                this.style.transform = 'scale(0.96)';
            });
            button.addEventListener('mouseup', function() {
                this.style.transform = 'scale(1)';
            });
            button.addEventListener('mouseleave', function() {
                this.style.transform = 'scale(1)';
            });
        });

        // Simple range value update visual (optional enrichment)
        const range = document.querySelector('input[type="range"]');
        if(range) {
            range.addEventListener('input', (e) => {
                // Logic could go here to update UI dynamically
            });
        }
    </script>


</body></html>
main
main
