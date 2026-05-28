import pandas as pd
import streamlit as st

st.set_page_config(page_title="PPC Insights Dashboard", layout="wide")

st.markdown(
    """
    <style>
    .stApp {background:#f8fafa; color:#191c1d; font-family:'Inter',sans-serif;}
    .block-container {padding-top:1rem; padding-bottom:1.5rem; max-width: 1400px;}
    .topbar {
        background:#ffffff; border:1px solid #dbc2ad; border-radius:12px;
        padding:14px 18px; margin-bottom:16px; display:flex; justify-content:space-between; align-items:center;
    }
    .title {font-size:28px; font-weight:700; color:#8a5100; margin:0;}
    .subtle {font-size:12px; color:#554434; text-transform:uppercase; letter-spacing:0.06em;}
    .upload-card {background:#fff; border:1px solid #dbc2ad; border-radius:12px; padding:14px; margin-bottom:16px;}
    .kpi {
        background:#fff; border:1px solid #dbc2ad; border-radius:10px; padding:14px 16px;
        min-height:100px; display:flex; flex-direction:column; justify-content:space-between;
    }
    .kpi-label {font-size:11px; text-transform:uppercase; letter-spacing:0.06em; color:#554434; font-weight:700;}
    .kpi-value {font-size:28px; line-height:1.2; color:#8a5100; font-weight:700;}
    .section-card {background:#fff; border:1px solid #dbc2ad; border-radius:10px; padding:14px; margin-top:16px;}
    .section-title {font-size:18px; font-weight:600; margin:0 0 10px 0;}
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class='topbar'>
        <div>
            <p class='title'>PPC Insights</p>
            <p class='subtle'>Seller Central API Dashboard</p>
        </div>
        <div class='subtle'>Date Range: Last 30 Days</div>
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


st.markdown("<div class='upload-card'>", unsafe_allow_html=True)
uploaded_files = st.file_uploader(
    "Upload Amazon PPC report files (.csv or .xlsx)",
    type=["csv", "xlsx"],
    accept_multiple_files=True,
)
st.markdown("</div>", unsafe_allow_html=True)

if not uploaded_files:
    st.info("Upload one or more report files to view styled KPI dashboard and campaign table.")
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
metrics = {
    "ctr": safe_divide(totals["clicks"], totals["impressions"]),
    "cvr": safe_divide(totals["orders"], totals["clicks"]),
    "acos": safe_divide(totals["spend"], totals["sales"]),
}

cards = [
    ("Total Impressions", f"{totals['impressions']:,.0f}"),
    ("Total Clicks", f"{totals['clicks']:,.0f}"),
    ("Total Spend", f"${totals['spend']:,.2f}"),
    ("Total Sales", f"${totals['sales']:,.2f}"),
    ("Total Orders", f"{totals['orders']:,.0f}"),
    ("Total Units", f"{totals['units']:,.0f}"),
    ("CTR", f"{metrics['ctr']:.2%}"),
    ("CVR", f"{metrics['cvr']:.2%}"),
    ("ACoS", f"{metrics['acos']:.2%}"),
]

for row_start in range(0, 9, 3):
    cols = st.columns(3, gap="medium")
    for idx, col in enumerate(cols):
        label, value = cards[row_start + idx]
        col.markdown(
            f"<div class='kpi'><div class='kpi-label'>{label}</div><div class='kpi-value'>{value}</div></div>",
            unsafe_allow_html=True,
        )

st.markdown("<div class='section-card'><h3 class='section-title'>Performance by Campaign Name</h3></div>", unsafe_allow_html=True)

if "Campaign Name" in combined.columns:
    campaign_summary = (
        combined.groupby("Campaign Name", dropna=False)[["impressions", "clicks", "spend", "sales", "orders", "units"]]
        .sum()
        .reset_index()
    )
    campaign_summary["ACoS"] = campaign_summary.apply(
        lambda r: safe_divide(r["spend"], r["sales"]), axis=1
    )
    campaign_summary = campaign_summary.sort_values("sales", ascending=False)

    display = campaign_summary.rename(
        columns={
            "impressions": "Impressions",
            "clicks": "Clicks",
            "spend": "Spend",
            "sales": "Sales",
            "orders": "Orders",
            "units": "Units",
        }
    )
    display["Spend"] = display["Spend"].map(lambda x: f"${x:,.2f}")
    display["Sales"] = display["Sales"].map(lambda x: f"${x:,.2f}")
    display["ACoS"] = display["ACoS"].map(lambda x: f"{x:.2%}")

    st.dataframe(display, use_container_width=True, hide_index=True)
else:
    st.warning("'Campaign Name' column not found in uploaded files.")
