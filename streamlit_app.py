import pandas as pd
import streamlit as st

st.set_page_config(page_title="PPC Insights Dashboard", layout="wide")

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
