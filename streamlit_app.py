import pandas as pd
import streamlit as st

st.set_page_config(page_title="PPC Insights Dashboard", layout="wide")

CUSTOM_CSS = """
<style>
@import url("https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@500&display=swap");

:root {
  --bg:#f8fafa; --text:#191c1d; --muted:#554434; --line:#dbc2ad;
  --side:#f2f4f4; --primary:#8a5100; --tertiary:#00687a;
}
html, body, [class*="css"] { font-family: Inter, sans-serif; }
.stApp { background: var(--bg); color: var(--text); }
header[data-testid="stHeader"] { background: transparent; }
section.main > div { padding-top: 0.25rem; max-width: 1440px; }

[data-testid="stSidebar"] { background: var(--side); border-right: 1px solid var(--line); }
[data-testid="stSidebar"] .stRadio label { padding: 4px 0; }
.brand { font-size: 1.75rem; font-weight:700; color:var(--primary); margin:12px 0 0 0; }
.subbrand { font-size:11px; text-transform:uppercase; letter-spacing:.12em; color:#887361; margin:0 0 10px 0; }

.topbar {
  height:62px; background:#fff; border-top:1px solid var(--line); border-bottom:1px solid var(--line);
  margin:0 -1rem 14px -1rem; display:flex; align-items:center; justify-content:space-between; padding:0 2rem;
}
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
.a1 { background:#d4e1f566; border-left:4px solid #535f70; }
.a2 { background:#ffdcbd44; border-left:4px solid #8a5100; }
.a3 { background:#adecff44; }

.table-wrap { border:1px solid var(--line); border-radius:8px; overflow:hidden; background:#fff; margin-top:10px; }
.table-head { display:flex; justify-content:space-between; align-items:center; padding:14px 18px; border-bottom:1px solid var(--line); }
.small-btn { font-size:11px; font-weight:700; color:var(--primary); }
[data-testid="stDataFrame"] { border:1px solid var(--line); border-radius:0 0 8px 8px; overflow:hidden; }
[data-testid="stDataFrame"] table tbody tr:nth-child(even){background:#f8fafa}
</style>
"""

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

with st.sidebar:
    st.markdown("<div class='brand'>Ads Console</div><div class='subbrand'>Seller Central API</div>", unsafe_allow_html=True)
    st.radio(
        "",
        [
            "Dashboard", "Campaigns", "Products", "Match Type", "Keywords",
            "Search Terms", "ASIN Targets", "ASIN from STR", "Auto Campaigns",
            "Category Targets", "Wasted Ad Spend"
        ],
        index=0,
    )
    st.button("⚡ Sync Data", use_container_width=True)
    st.divider()
    st.button("Help Center", use_container_width=True)
    st.button("Log Out", use_container_width=True)

st.markdown(
    "<div class='topbar'><div class='top-title'>PPC Insights</div><div class='chip'>🏦 ACCOUNT SELECTION ▾</div></div>",
    unsafe_allow_html=True,
)

a, b, c = st.columns([6, 1, 2])
a.markdown("<div class='chip'>📅 Date Range: Last 30 Days</div>", unsafe_allow_html=True)
b.markdown("<div style='padding-top:9px'>🔔</div>", unsafe_allow_html=True)
c.markdown("<div style='padding-top:9px'>❔ &nbsp;&nbsp; 👤</div>", unsafe_allow_html=True)

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
        f"<div class='metric-card'><div class='metric-label'>{label}</div>"
        f"<div style='display:flex;justify-content:space-between;align-items:end;'>"
        f"<div class='metric-value'>{value}</div><div class='{badge}'>{delta}</div></div></div>",
        unsafe_allow_html=True,
    )

main, side = st.columns([3, 1])

with main:
    st.markdown("<div class='section-title'>Performance Trends</div>", unsafe_allow_html=True)
    chart_df = pd.DataFrame(
        {
            "Spend": [40,42,45,49,51,54,56,60,63,64,64,62,59,56,54,53,55,59,65,72,77,80,79,75,68,63,61,62,66,72],
            "Sales": [50,54,58,64,71,78,86,94,102,108,112,113,111,106,100,96,95,98,105,116,128,138,143,142,135,126,120,118,121,131],
        }
    )
    st.line_chart(chart_df, height=360, color=["#8a5100", "#00687a"])

with side:
    st.markdown("<div class='section-title'>Insights & Alerts</div>", unsafe_allow_html=True)
    st.markdown("<div class='alert a1'><b>Budget Alert</b><br><br>3 campaigns are nearing daily budget limit.</div>", unsafe_allow_html=True)
    st.markdown("<div class='alert a2'><b>Optimization Tip</b><br><br>Lowering bids on \"keyword_x\" could save $45/day.</div>", unsafe_allow_html=True)
    st.markdown("<div class='alert a3'><b>Unlock AI Insights</b><br><br>Get predictive keyword scaling advice.</div>", unsafe_allow_html=True)
    st.button("UPGRADE PRO", use_container_width=True)

st.markdown(
    "<div class='table-wrap'><div class='table-head'>"
    "<div class='section-title' style='font-size:1.25rem;margin:0;'>Top Performing Campaigns</div>"
    "<div class='small-btn'>VIEW ALL REPORTS</div></div></div>",
    unsafe_allow_html=True,
)

df = pd.DataFrame(
    [
        ["Summer_Collection_Manual_2023", "ACTIVE", "$1,420.50", "$12,500.00", "11.36%", "⋯"],
        ["Prime_Day_Headphones_Auto", "ACTIVE", "$2,105.00", "$18,450.00", "11.41%", "⋯"],
        ["Competitor_Targeting_Bags", "PAUSED", "$850.40", "$6,120.00", "13.89%", "⋯"],
        ["Brand_Defense_Keywords", "ACTIVE", "$3,200.00", "$24,800.00", "12.90%", "⋯"],
        ["Home_Office_Desk_Lamp_Manual", "OUT OF BUDGET", "$680.00", "$3,450.00", "19.71%", "⋯"],
    ],
    columns=["CAMPAIGN NAME", "STATUS", "SPEND", "SALES", "ACoS", "ACTION"],
)

st.dataframe(df, use_container_width=True, hide_index=True)
