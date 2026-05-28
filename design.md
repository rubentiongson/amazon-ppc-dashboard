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
