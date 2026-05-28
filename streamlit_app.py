import pandas as pd
import streamlit as st

st.set_page_config(page_title="PPC Insights Dashboard", layout="wide")

st.markdown(
    """
    <style>
    .stApp { background:#f8fafa; color:#191c1d; }
    [data-testid="stSidebar"] { background:#f2f4f4; border-right:1px solid #dbc2ad; }
    .block-container { max-width: 1440px; padding-top: 5.5rem; padding-bottom: 1.5rem; }
    .top-shell { background:#fff; border:1px solid #dbc2ad; border-radius:12px; padding:14px 18px; margin-bottom:16px; }
    .app-title { font-size:30px; line-height:1.1; font-weight:800; color:#8a5100; margin:0; }
    .app-subtitle { font-size:11px; letter-spacing:.08em; text-transform:uppercase; color:#554434; margin:0; }
    .pill { background:#f2f4f4; border:1px solid #dbc2ad; border-radius:999px; padding:8px 12px; font-size:11px; font-weight:700; color:#554434; }
    .panel { background:#fff; border:1px solid #dbc2ad; border-radius:12px; padding:14px; }
    div[data-testid="stMetric"] { background:#fff; border:1px solid #dbc2ad; border-radius:12px; padding:12px; }
    div[data-testid="stMetricLabel"] { text-transform:uppercase; letter-spacing:.06em; }
    .section-head { font-size:18px; font-weight:700; margin:0 0 8px 0; }
    div[data-testid="stDataFrame"] [role="row"]:nth-child(even) { background:#f8fafa; }
    </style>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    st.markdown("### Ads Console")
    st.caption("Seller Central API")
    st.markdown("**Dashboard**")
    st.markdown("Campaigns")
    st.markdown("Products")
    st.markdown("Match Type")
    st.markdown("Keywords")
    st.markdown("Search Terms")
    st.markdown("ASIN Targets")
    st.markdown("Auto Campaigns")

left, right = st.columns([3, 1])
with left:
    st.markdown("<div class='top-shell'><p class='app-title'>PPC Insights</p><p class='app-subtitle'>Seller Central API Dashboard</p></div>", unsafe_allow_html=True)
with right:
    st.markdown("<div class='top-shell' style='display:flex;align-items:center;justify-content:center;min-height:72px;'><span class='pill'>Date Range: Last 30 Days</span></div>", unsafe_allow_html=True)

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
if not uploaded_files:
    st.info("Upload files to replace placeholder zeros with live metrics.")
else:
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
    combined = pd.DataFrame(columns=["Campaign Name", "impressions", "clicks", "spend", "sales", "orders", "units"])

totals = {k: float(combined[k].sum()) if k in combined.columns else 0.0 for k in ["impressions", "clicks", "spend", "sales", "orders", "units"]}
ctr = safe_divide(totals["clicks"], totals["impressions"])
cvr = safe_divide(totals["orders"], totals["clicks"])
acos = safe_divide(totals["spend"], totals["sales"])

rows = [
    [("Impressions", f"{totals['impressions']:,.0f}"), ("Clicks", f"{totals['clicks']:,.0f}"), ("Spend", f"${totals['spend']:,.2f}")],
    [("Sales", f"${totals['sales']:,.2f}"), ("Orders", f"{totals['orders']:,.0f}"), ("Units", f"{totals['units']:,.0f}")],
    [("CTR", f"{ctr:.2%}"), ("CVR", f"{cvr:.2%}"), ("ACoS", f"{acos:.2%}")],
]

for row in rows:
    cols = st.columns(3)
    for col, (label, value) in zip(cols, row):
        col.metric(label, value)

st.markdown("<div class='panel' style='margin-top:16px;'><p class='section-head'>Performance by Campaign Name</p></div>", unsafe_allow_html=True)
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
