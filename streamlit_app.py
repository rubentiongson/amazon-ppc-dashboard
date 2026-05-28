import pandas as pd
import streamlit as st

st.set_page_config(page_title="PPC Insights Dashboard", layout="wide")

# --------- Theme/UI ---------
st.markdown(
    """
    <style>
    .stApp {background: #f8fafa;}
    .main-title {font-size: 2rem; font-weight: 800; color: #8a5100; margin: 0;}
    .subtitle {font-size: 0.75rem; letter-spacing: .08em; text-transform: uppercase; color:#554434;}
    .shell-card {background:#ffffff; border:1px solid #dbc2ad; border-radius:12px; padding:12px 16px;}
    .section-title {font-size:1.1rem; font-weight:700; color:#191c1d; margin-bottom:8px;}
    div[data-testid="stMetric"] {
        background:#ffffff;
        border:1px solid #dbc2ad;
        border-radius:12px;
        padding:10px 14px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    st.markdown("## Ads Console")
    st.caption("Seller Central API")
    st.markdown("- 📊 Dashboard\n- 🎯 Campaigns\n- 📦 Products\n- 🔑 Keywords")

header_left, header_right = st.columns([3, 1])
with header_left:
    st.markdown("<p class='main-title'>PPC Insights</p>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Seller Central API Dashboard</p>", unsafe_allow_html=True)
with header_right:
    st.markdown("<div class='shell-card subtitle' style='text-align:center;'>Date Range: Last 30 Days</div>", unsafe_allow_html=True)

# --------- Data logic ---------
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


st.markdown("<div class='shell-card'>", unsafe_allow_html=True)
uploaded_files = st.file_uploader(
    "Upload Amazon PPC report files (.csv or .xlsx)",
    type=["csv", "xlsx"],
    accept_multiple_files=True,
)
st.markdown("</div>", unsafe_allow_html=True)

if not uploaded_files:
    st.info("Upload one or more files to populate KPIs and campaign table.")
    st.stop()

all_data = []
for file in uploaded_files:
    try:
        all_data.append(standardize_columns(load_file(file)))
    except Exception as exc:
        st.error(f"Could not process {file.name}: {exc}")

if not all_data:
    st.warning("No valid files were processed.")
    st.stop()

combined = pd.concat(all_data, ignore_index=True)
for col in ["impressions", "clicks", "spend", "sales", "orders", "units"]:
    combined[col] = to_numeric(combined[col])

totals = {k: float(combined[k].sum()) for k in ["impressions", "clicks", "spend", "sales", "orders", "units"]}
ctr = safe_divide(totals["clicks"], totals["impressions"])
cvr = safe_divide(totals["orders"], totals["clicks"])
acos = safe_divide(totals["spend"], totals["sales"])

metric_rows = [
    [("Impressions", f"{totals['impressions']:,.0f}"), ("Clicks", f"{totals['clicks']:,.0f}"), ("Spend", f"${totals['spend']:,.2f}")],
    [("Sales", f"${totals['sales']:,.2f}"), ("Orders", f"{totals['orders']:,.0f}"), ("Units", f"{totals['units']:,.0f}")],
    [("CTR", f"{ctr:.2%}"), ("CVR", f"{cvr:.2%}"), ("ACoS", f"{acos:.2%}")],
]

for row in metric_rows:
    cols = st.columns(3)
    for col, (label, value) in zip(cols, row):
        col.metric(label, value)

st.markdown("<p class='section-title'>Performance by Campaign Name</p>", unsafe_allow_html=True)
if "Campaign Name" in combined.columns:
    campaign_summary = (
        combined.groupby("Campaign Name", dropna=False)[["impressions", "clicks", "spend", "sales", "orders", "units"]]
        .sum()
        .reset_index()
        .sort_values("sales", ascending=False)
    )
    campaign_summary["ACoS"] = campaign_summary.apply(lambda r: safe_divide(r["spend"], r["sales"]), axis=1)

    st.dataframe(campaign_summary, use_container_width=True, hide_index=True)
else:
    st.warning("'Campaign Name' column not found in uploaded files.")
