import pandas as pd
import streamlit as st

st.set_page_config(page_title="Amazon PPC Dashboard", layout="wide")

st.title("Amazon PPC Performance Dashboard")

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


uploaded_files = st.file_uploader(
    "Upload Amazon PPC report files (.csv or .xlsx)",
    type=["csv", "xlsx"],
    accept_multiple_files=True,
)

if not uploaded_files:
    st.info("Upload one or more report files to view dashboard metrics.")
    st.stop()

all_data = []
for file in uploaded_files:
    try:
        df = load_file(file)
        standardized = standardize_columns(df)
        all_data.append(standardized)
    except Exception as exc:
        st.error(f"Could not process {file.name}: {exc}")

if not all_data:
    st.warning("No valid files were processed.")
    st.stop()

combined = pd.concat(all_data, ignore_index=True)

for col in ["impressions", "clicks", "spend", "sales", "orders", "units"]:
    combined[col] = to_numeric(combined[col])

totals = {
    "impressions": float(combined["impressions"].sum()),
    "clicks": float(combined["clicks"].sum()),
    "spend": float(combined["spend"].sum()),
    "sales": float(combined["sales"].sum()),
    "orders": float(combined["orders"].sum()),
    "units": float(combined["units"].sum()),
}

metrics = {
    "CTR": safe_divide(totals["clicks"], totals["impressions"]),
    "CVR": safe_divide(totals["orders"], totals["clicks"]),
    "ACoS": safe_divide(totals["spend"], totals["sales"]),
}

cards = st.columns(3)
cards[0].metric("Impressions", f"{totals['impressions']:,.0f}")
cards[1].metric("Clicks", f"{totals['clicks']:,.0f}")
cards[2].metric("Orders", f"{totals['orders']:,.0f}")

cards = st.columns(3)
cards[0].metric("Spend", f"${totals['spend']:,.2f}")
cards[1].metric("Sales", f"${totals['sales']:,.2f}")
cards[2].metric("Units", f"{totals['units']:,.0f}")

cards = st.columns(3)
cards[0].metric("CTR", f"{metrics['CTR']:.2%}")
cards[1].metric("CVR", f"{metrics['CVR']:.2%}")
cards[2].metric("ACoS", f"{metrics['ACoS']:.2%}")

st.subheader("Performance by Campaign Name")
if "Campaign Name" in combined.columns:
    campaign_summary = (
        combined.groupby("Campaign Name", dropna=False)[
            ["impressions", "clicks", "spend", "sales", "orders", "units"]
        ]
        .sum()
        .reset_index()
        .sort_values("sales", ascending=False)
    )

    for col in ["spend", "sales"]:
        campaign_summary[col] = campaign_summary[col].map(lambda x: f"${x:,.2f}")

    st.dataframe(campaign_summary, use_container_width=True)
else:
    st.warning("'Campaign Name' column not found in uploaded files.")
