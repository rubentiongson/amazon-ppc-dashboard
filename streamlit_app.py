import pandas as pd
import streamlit as st

st.set_page_config(page_title="PPC Insights Dashboard", layout="wide")

codex/create-amazon-ppc-dashboard-web-app-0hrlu9

codex/create-amazon-ppc-dashboard-web-app-hurcrc
 main
CUSTOM_CSS = '''
<style>
@import url("https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@500&display=swap");

:root {
 codex/create-amazon-ppc-dashboard-web-app-0hrlu9
  --bg:#f8fafa; --text:#191c1d; --muted:#554434; --line:#dbc2ad;
  --side:#f2f4f4; --primary:#8a5100; --tertiary:#00687a;

  --bg:#f8fafa; --text:#191c1d; --muted:#554434; --line:#dbc2ad; --panel:#ffffff;
  --side:#f2f4f4; --primary:#8a5100;
 main
}
html, body, [class*="css"] { font-family: Inter, sans-serif; }
.stApp { background: var(--bg); color: var(--text); }
header[data-testid="stHeader"] { background: transparent; }
codex/create-amazon-ppc-dashboard-web-app-0hrlu9
section.main > div { padding-top: 0.25rem; max-width: 1440px; }

[data-testid="stSidebar"] { background: var(--side); border-right: 1px solid var(--line); }
[data-testid="stSidebar"] .stRadio label { padding: 4px 0; }
.brand { font-size: 1.75rem; font-weight:700; color:var(--primary); margin:12px 0 0 0; }
.subbrand { font-size:11px; text-transform:uppercase; letter-spacing:.12em; color:#887361; margin:0 0 10px 0; }

.topbar { height:62px; background:#fff; border-top:1px solid var(--line); border-bottom:1px solid var(--line);
  margin:0 -1rem 14px -1rem; display:flex; align-items:center; justify-content:space-between; padding:0 2rem; }
.top-title { font-size:2.1rem; color:#1f2a44; font-weight:700; }
.chip { border:1px solid var(--line); background:#f2f4f4; padding:7px 14px; border-radius:999px; font-size:11px; font-weight:700; }

.metric-card { border:1px solid var(--line); background:#fff; border-radius:8px; padding:14px; min-height:88px; }
.metric-label { font-size:10px; font-weight:700; letter-spacing:.09em; color:var(--muted); }
.metric-value { font-size:2.5rem; font-weight:700; color:var(--primary); line-height:1.1; }
.badge-red,.badge-green { font-size:10px; font-weight:700; padding:2px 8px; border-radius:6px; }
.badge-red { background:#ffdad6; color:#ba1a1a; }
.badge-green { background:#e8f5e9; color:#2e7d32; }

.section-title { font-size:1.9rem; font-weight:700; margin:0 0 8px 0; }
.alert { border-radius:8px; padding:12px 14px; margin-bottom:10px; font-size:0.95rem; }

section.main > div { padding-top: 0.5rem; max-width: 1440px; }

[data-testid="stSidebar"] { background: var(--side); border-right: 1px solid var(--line); }
.brand { font-size: 28px; font-weight:700; color:var(--primary); margin:18px 0 0 0; }
.subbrand { font-size:11px; text-transform:uppercase; letter-spacing:.08em; color:#887361; margin:0 0 14px 0; }

.topbar {
  height:64px; background:#fff; border:1px solid var(--line); border-left:none; border-right:none;
  margin-bottom:14px; display:flex; align-items:center; justify-content:space-between; padding:0 18px;
}
.top-title { font-size:48px; line-height:1; color:var(--primary); font-weight:700; }
.chip { border:1px solid var(--line); background:#f2f4f4; padding:7px 14px; border-radius:99px; font-size:11px; font-weight:700; display:inline-block; }

.metric-card { border:1px solid var(--line); background:#fff; border-radius:8px; padding:12px; }
.metric-label { font-size:11px; font-weight:700; letter-spacing:.05em; color:var(--muted); }
.metric-value { font-size:38px; font-weight:700; color:var(--primary); line-height:1.1; }
.badge-red,.badge-green { font-size:11px; font-weight:700; padding:2px 8px; border-radius:6px; }
.badge-red { background:#ffdad6; color:#ba1a1a; }
.badge-green { background:#e8f5e9; color:#2e7d32; }

.title { font-size:30px; font-weight:700; margin:0 0 10px 0; }
.alert { border-radius:8px; padding:12px 14px; margin-bottom:10px; }
 main
.a1 { background:#d4e1f566; border-left:4px solid #535f70; }
.a2 { background:#ffdcbd44; border-left:4px solid #8a5100; }
.a3 { background:#adecff44; }

codex/create-amazon-ppc-dashboard-web-app-0hrlu9
.table-wrap { border:1px solid var(--line); border-radius:8px; overflow:hidden; background:#fff; margin-top:10px; }
.table-head { display:flex; justify-content:space-between; align-items:center; padding:14px 18px; border-bottom:1px solid var(--line); }
.small-btn { font-size:11px; font-weight:700; color:var(--primary); }
[data-testid="stDataFrame"] { border:1px solid var(--line); border-radius:0 0 8px 8px; overflow:hidden; }
[data-testid="stDataFrame"] table tbody tr:nth-child(even){background:#f8fafa}

.table-wrap { border:1px solid var(--line); border-radius:8px; overflow:hidden; background:#fff; }
.table-head { display:flex; justify-content:space-between; align-items:center; padding:14px 18px; border-bottom:1px solid var(--line); }
.small-btn { font-size:11px; font-weight:700; color:var(--primary); }
 main
</style>
'''

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

with st.sidebar:
    st.markdown("<div class='brand'>Ads Console</div><div class='subbrand'>Seller Central API</div>", unsafe_allow_html=True)
    st.radio("", ["Dashboard", "Campaigns", "Products", "Match Type", "Keywords", "Search Terms", "ASIN Targets", "ASIN from STR", "Auto Campaigns", "Category Targets", "Wasted Ad Spend"], index=0)
    st.button("⚡ Sync Data", use_container_width=True)
    st.divider()
    st.button("Help Center", use_container_width=True)
    st.button("Log Out", use_container_width=True)

codex/create-amazon-ppc-dashboard-web-app-0hrlu9
st.markdown("<div class='topbar'><div class='top-title'>PPC Insights</div><div class='chip'>🏦 ACCOUNT SELECTION ▾</div></div>", unsafe_allow_html=True)

a, b, c = st.columns([6, 1, 2])
a.markdown("<div class='chip'>📅 Date Range: Last 30 Days</div>", unsafe_allow_html=True)
b.markdown("<div style='padding-top:9px'>🔔</div>", unsafe_allow_html=True)
c.markdown("<div style='padding-top:9px'>❔ &nbsp;&nbsp; 👤</div>", unsafe_allow_html=True)

kcols = st.columns(4)
for col, (label, value, delta, is_good) in zip(kcols, [
    ("TOTAL SPEND", "$12,450.00", "+5%", False),
    ("TOTAL SALES", "$84,200.00", "+12%", True),
    ("ACoS", "14.78%", "-2%", True),
    ("ROAS", "6.76x", "+8%", True),
]):
    badge = "badge-green" if is_good else "badge-red"
    col.markdown(f"<div class='metric-card'><div class='metric-label'>{label}</div><div style='display:flex;justify-content:space-between;align-items:end;'><div class='metric-value'>{value}</div><div class='{badge}'>{delta}</div></div></div>", unsafe_allow_html=True)

main, side = st.columns([3, 1])
with main:
    st.markdown("<div class='section-title'>Performance Trends</div>", unsafe_allow_html=True)
    chart_df = pd.DataFrame({
        "Spend": [40,42,45,49,51,54,56,60,63,64,64,62,59,56,54,53,55,59,65,72,77,80,79,75,68,63,61,62,66,72],
        "Sales": [50,54,58,64,71,78,86,94,102,108,112,113,111,106,100,96,95,98,105,116,128,138,143,142,135,126,120,118,121,131],
    })
    st.line_chart(chart_df, height=360, color=["#8a5100", "#00687a"])

with side:
    st.markdown("<div class='section-title'>Insights & Alerts</div>", unsafe_allow_html=True)

st.markdown("<div class='topbar'><div class='top-title'>PPC Insights</div><div class='chip'>ACCOUNT SELECTION ▾</div></div>", unsafe_allow_html=True)

a, b, c = st.columns([6, 1, 2])
a.markdown("<div class='chip'>📅 Date Range: Last 30 Days</div>", unsafe_allow_html=True)
b.markdown("<div style='padding-top:8px'>🔔</div>", unsafe_allow_html=True)
c.markdown("<div style='padding-top:8px'>❔ &nbsp; 👤</div>", unsafe_allow_html=True)

kcols = st.columns(4)
for col, (label, value, delta, is_good) in zip(
    kcols,
    [
        ("TOTAL SPEND", "$12,450.00", "+5%", False),
        ("TOTAL SALES", "$84,200.00", "+12%", True),
        ("ACoS", "14.78%", "-2%", True),
        ("ROAS", "6.76x", "+8%", True),
    ],
):
    badge = "badge-green" if is_good else "badge-red"
    col.markdown(
        f"<div class='metric-card'><div class='metric-label'>{label}</div><div style='display:flex;justify-content:space-between;align-items:end;'><div class='metric-value'>{value}</div><div class='{badge}'>{delta}</div></div></div>",
        unsafe_allow_html=True,
    )

main, side = st.columns([3, 1])
with main:
    st.markdown("<div class='title'>Performance Trends</div>", unsafe_allow_html=True)
    st.line_chart({"Spend": [40,42,45,49,51,54,56,60,63,64,64,62,59,56,54,53,55,59,65,72,77,80,79,75,68,63,61,62,66,72], "Sales": [50,54,58,64,71,78,86,94,102,108,112,113,111,106,100,96,95,98,105,116,128,138,143,142,135,126,120,118,121,131]}, height=350)
with side:
    st.markdown("<div class='title'>Insights & Alerts</div>", unsafe_allow_html=True)
 main
    st.markdown("<div class='alert a1'><b>Budget Alert</b><br><br>3 campaigns are nearing daily budget limit.</div>", unsafe_allow_html=True)
    st.markdown("<div class='alert a2'><b>Optimization Tip</b><br><br>Lowering bids on \"keyword_x\" could save $45/day.</div>", unsafe_allow_html=True)
    st.markdown("<div class='alert a3'><b>Unlock AI Insights</b><br><br>Get predictive keyword scaling advice.</div>", unsafe_allow_html=True)
    st.button("UPGRADE PRO", use_container_width=True)

codex/create-amazon-ppc-dashboard-web-app-0hrlu9
st.markdown("<div class='table-wrap'><div class='table-head'><div class='section-title' style='font-size:1.25rem;margin:0;'>Top Performing Campaigns</div><div class='small-btn'>VIEW ALL REPORTS</div></div></div>", unsafe_allow_html=True)

st.markdown("<div class='table-wrap'><div class='table-head'><div class='title' style='font-size:20px'>Top Performing Campaigns</div><div class='small-btn'>VIEW ALL REPORTS</div></div></div>", unsafe_allow_html=True)
main

df = pd.DataFrame([
    ["Summer_Collection_Manual_2023", "ACTIVE", "$1,420.50", "$12,500.00", "11.36%", "⋯"],
    ["Prime_Day_Headphones_Auto", "ACTIVE", "$2,105.00", "$18,450.00", "11.41%", "⋯"],
    ["Competitor_Targeting_Bags", "PAUSED", "$850.40", "$6,120.00", "13.89%", "⋯"],
    ["Brand_Defense_Keywords", "ACTIVE", "$3,200.00", "$24,800.00", "12.90%", "⋯"],
    ["Home_Office_Desk_Lamp_Manual", "OUT OF BUDGET", "$680.00", "$3,450.00", "19.71%", "⋯"],
], columns=["CAMPAIGN NAME", "STATUS", "SPEND", "SALES", "ACoS", "ACTION"])

st.dataframe(df, use_container_width=True, hide_index=True)
codex/create-amazon-ppc-dashboard-web-app-0hrlu9


st.markdown(
    """
    <style>
    .stApp { background:#f8fafa; color:#191c1d; font-family: Inter, sans-serif; }
    [data-testid="stSidebar"] { background:#f2f4f4; border-right:1px solid #dbc2ad; }
    .block-container { max-width: 1440px; padding-top: 4.5rem; padding-bottom: 2rem; }

    .shell { background:#fff; border:1px solid #dbc2ad; border-radius:12px; }
    .topbar { padding:14px 20px; display:flex; align-items:center; justify-content:space-between; }
    .title { color:#8a5100; font-size:28px; font-weight:700; margin:0; }
    .caps { color:#554434; font-size:11px; letter-spacing:.06em; text-transform:uppercase; font-weight:700; }
    .chip { background:#f2f4f4; border:1px solid #dbc2ad; border-radius:999px; padding:8px 12px; }

    .panel { background:#fff; border:1px solid #dbc2ad; border-radius:12px; padding:14px; }
    .panel h4 { margin:0; font-size:18px; }

    div[data-testid="stMetric"] { background:#fff; border:1px solid #dbc2ad; border-radius:10px; padding:12px; }
    div[data-testid="stMetricLabel"] { text-transform:uppercase; letter-spacing:.06em; font-weight:700; }

    .alert { border-left:4px solid #535f70; background:#d4e1f5; color:#101c2b; border-radius:8px; padding:10px 12px; font-size:13px; }
    .tip { border-left:4px solid #8a5100; background:#ffdcbd; color:#653a00; border-radius:8px; padding:10px 12px; font-size:13px; }
    .upgrade { background:#adecff; border:1px solid #6abdd3; border-radius:10px; padding:12px; text-align:center; font-size:12px; }

    div[data-testid="stDataFrame"] [role="row"]:nth-child(even){ background:#f8fafa; }
    </style>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    st.markdown("### Ads Console")
    st.caption("Seller Central API")
    st.markdown("**Dashboard**")
    for item in ["Campaigns", "Products", "Match Type", "Keywords", "Search Terms", "ASIN Targets", "ASIN from STR", "Auto Campaigns", "Category Targets", "Wasted Ad Spend"]:
        st.markdown(item)
    st.button("Sync Data", use_container_width=True)

st.markdown(
    """
    <div class='shell topbar'>
      <div>
        <p class='title'>PPC Insights</p>
        <div class='caps'>Seller Central API Dashboard</div>
      </div>
      <div class='chip caps'>Date Range: Last 30 Days</div>
    </div>
    """,
    unsafe_allow_html=True,
)

COLUMN_MAPPING = {
    "impressions": ["Impressions"],
    "clicks": ["Clicks"],
    "spend": ["Spend", "Cost"],
    "sales": ["Sales", "7-Day Total Sales", "14-Day Total Sales"],
    "orders": ["Orders", "7-Day Total Orders", "Total Orders"],
    "units": ["Units", "7-Day Total Units", "Total Units"],
}


def load_file(uploaded_file) -> pd.DataFrame:
    if uploaded_file.name.lower().endswith(".csv"):
        return pd.read_csv(uploaded_file)
    return pd.read_excel(uploaded_file)


def standardize_columns(df: pd.DataFrame) -> pd.DataFrame:
    rename_map = {}
    for standard_name, candidates in COLUMN_MAPPING.items():
        for candidate in candidates:
            if candidate in df.columns:
                rename_map[candidate] = standard_name
                break
    standardized = df.rename(columns=rename_map).copy()
    for required in COLUMN_MAPPING:
        if required not in standardized.columns:
            standardized[required] = 0
    return standardized


def to_numeric(series: pd.Series) -> pd.Series:
    if pd.api.types.is_numeric_dtype(series):
        return series.fillna(0)
    cleaned = (
        series.astype(str)
        .str.replace("$", "", regex=False)
        .str.replace(",", "", regex=False)
        .str.replace("%", "", regex=False)
        .str.strip()
    )
    return pd.to_numeric(cleaned, errors="coerce").fillna(0)


def safe_divide(numerator: float, denominator: float) -> float:
    return numerator / denominator if denominator else 0.0

st.markdown("<div class='panel'>", unsafe_allow_html=True)
uploaded_files = st.file_uploader(
    "Upload Amazon PPC report files (.csv or .xlsx)",
    type=["csv", "xlsx"],
    accept_multiple_files=True,
)
st.markdown("</div>", unsafe_allow_html=True)

all_data = []
if uploaded_files:
    for file in uploaded_files:
        try:
            all_data.append(standardize_columns(load_file(file)))
        except Exception as exc:
            st.error(f"Could not process {file.name}: {exc}")

if all_data:
    combined = pd.concat(all_data, ignore_index=True)
    for col in ["impressions", "clicks", "spend", "sales", "orders", "units"]:
        combined[col] = to_numeric(combined[col])
else:
    st.info("Upload files to populate dashboard data.")
    combined = pd.DataFrame(columns=["Campaign Name", "impressions", "clicks", "spend", "sales", "orders", "units"])

totals = {k: float(combined[k].sum()) if k in combined.columns else 0.0 for k in ["impressions", "clicks", "spend", "sales", "orders", "units"]}
ctr = safe_divide(totals["clicks"], totals["impressions"])
cvr = safe_divide(totals["orders"], totals["clicks"])
acos = safe_divide(totals["spend"], totals["sales"])

kpi = [
    ("Impressions", f"{totals['impressions']:,.0f}"),
    ("Clicks", f"{totals['clicks']:,.0f}"),
    ("Spend", f"${totals['spend']:,.2f}"),
    ("Sales", f"${totals['sales']:,.2f}"),
    ("Orders", f"{totals['orders']:,.0f}"),
    ("Units", f"{totals['units']:,.0f}"),
    ("CTR", f"{ctr:.2%}"),
    ("CVR", f"{cvr:.2%}"),
    ("ACoS", f"{acos:.2%}"),
]
for i in range(0, 9, 3):
    cols = st.columns(3)
    for col, (label, value) in zip(cols, kpi[i:i+3]):
        col.metric(label, value)

left, right = st.columns([3, 1])
with left:
    st.markdown("<div class='panel'><h4>Performance Trends</h4><div style='height:220px;margin-top:12px;background-image:linear-gradient(to right,#f0f2f2 1px,transparent 1px),linear-gradient(to bottom,#f0f2f2 1px,transparent 1px);background-size:40px 40px;border-left:1px solid #dbc2ad;border-bottom:1px solid #dbc2ad;'></div></div>", unsafe_allow_html=True)
with right:
    st.markdown("<div class='panel'><h4>Insights & Alerts</h4><div class='alert' style='margin-top:10px;'>Budget alert: 3 campaigns nearing daily budget limit.</div><div class='tip' style='margin-top:10px;'>Optimization tip: Lowering bids on keyword_x could save $45/day.</div><div class='upgrade' style='margin-top:10px;'>Unlock AI insights for predictive keyword scaling.</div></div>", unsafe_allow_html=True)

st.markdown("<div class='panel' style='margin-top:16px;'><h4>Top Performing Campaigns</h4></div>", unsafe_allow_html=True)
if all_data and "Campaign Name" in combined.columns:
    campaign_summary = (
        combined.groupby("Campaign Name", dropna=False)[["impressions", "clicks", "spend", "sales", "orders", "units"]]
        .sum()
        .reset_index()
        .sort_values("sales", ascending=False)
    )
    campaign_summary["ACoS"] = campaign_summary.apply(lambda r: safe_divide(r["spend"], r["sales"]), axis=1)
    st.dataframe(campaign_summary, use_container_width=True, hide_index=True)
elif uploaded_files:
    st.warning("'Campaign Name' column not found in uploaded files.")
else:
    st.dataframe(combined, use_container_width=True, hide_index=True)
 main
 main
