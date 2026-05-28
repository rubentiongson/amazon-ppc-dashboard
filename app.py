codex/create-amazon-ppc-dashboard-web-app-0hrlu9
"""Streamlit entrypoint shim.

Some environments default to running `app.py`. This module ensures the
main dashboard in `streamlit_app.py` is loaded regardless of entrypoint.
"""

from streamlit_app import *  # noqa: F401,F403

codex/create-amazon-ppc-dashboard-web-app-hurcrc
"""Streamlit entrypoint shim.

Some environments default to running `app.py`. This module ensures the
main dashboard in `streamlit_app.py` is loaded regardless of entrypoint.
"""

from streamlit_app import *  # noqa: F401,F403

codex/create-streamlit-app-for-amazon-ppc-reports
"""Streamlit entrypoint shim.

Some environments default to running `app.py`. This module ensures the
main dashboard in `streamlit_app.py` is loaded regardless of entrypoint.
"""

from streamlit_app import *  # noqa: F401,F403

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(page_title="PPC Insights Dashboard", layout="wide")

st.markdown(
    """
codex/create-amazon-ppc-dashboard-web-app-kjuziu
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@500&display=swap');

:root {
  --bg:#f8fafa; --text:#191c1d; --muted:#554434; --line:#dbc2ad; --panel:#ffffff;
  --side:#f2f4f4; --primary:#8a5100; --secondaryContainer:#d4e1f5; --tertiary:#00687a;
}
html, body, [class*="css"] { font-family: Inter, sans-serif; }
.stApp { background: var(--bg); color: var(--text); }
header[data-testid="stHeader"] { background: transparent; }
section.main > div { padding-top: 0.5rem; max-width: 1440px; }

[data-testid="stSidebar"] { background: var(--side); border-right:1px solid var(--line); }
[data-testid="stSidebar"] .stRadio label p { font-size: 30px; }

.brand { font-size: 32px; font-weight:700; color:var(--primary); margin:18px 0 0 0; }
.subbrand { font-size:11px; text-transform:uppercase; letter-spacing:.08em; color:#887361; margin:0 0 14px 0; }

.topbar {height:64px; background:#fff; border:1px solid var(--line); border-left:none; border-right:none; margin-bottom:14px;
 display:flex; align-items:center; justify-content:space-between; padding:0 18px;}
.top-title {font-size:48px; line-height:1; color:var(--primary); font-weight:700;}

.chip {border:1px solid var(--line); background:#f2f4f4; padding:7px 14px; border-radius:99px; font-size:11px; font-weight:700; display:inline-block;}
.metric-card { border:1px solid var(--line); background:#fff; border-radius:8px; padding:12px; }
.metric-label{font-size:11px;font-weight:700;letter-spacing:.05em;color:var(--muted);}
.metric-value{font-size:38px;font-weight:700;color:var(--primary);line-height:1.1;}
.badge-red,.badge-green{font-size:11px;font-weight:700;padding:2px 8px;border-radius:6px;}
.badge-red{background:#ffdad6;color:#ba1a1a}.badge-green{background:#e8f5e9;color:#2e7d32}

.panel{border:1px solid var(--line);background:#fff;border-radius:8px;padding:16px;}
.title{font-size:30px;font-weight:700;margin:0 0 10px 0;}
.legend{font-size:12px;font-weight:600;text-transform:uppercase;}

.alert{border-radius:8px;padding:12px 14px;margin-bottom:10px;}
.a1{background:#d4e1f566;border-left:4px solid #535f70;}.a2{background:#ffdcbd44;border-left:4px solid #8a5100;}.a3{background:#adecff44;}

.table-wrap{border:1px solid var(--line);border-radius:8px;overflow:hidden;background:#fff;}
.table-head{display:flex;justify-content:space-between;align-items:center;padding:14px 18px;border-bottom:1px solid var(--line);}
.small-btn{font-size:11px;font-weight:700;color:var(--primary)}

[data-testid="stDataFrame"] table tbody tr:nth-child(even){background:#f8fafa}
</style>
""",

    <style>
    .stApp {
        background-color: #f8fafa;
        color: #191c1d;
    }
    [data-testid="stSidebar"] {
        background-color: #f2f4f4;
        border-right: 1px solid #dbc2ad;
    }
    [data-testid="stSidebar"] * {
        color: #554434;
    }
    .brand-title {
        color: #8a5100;
        font-weight: 700;
        font-size: 1.1rem;
        margin-bottom: 0;
    }
    .brand-subtitle {
        text-transform: uppercase;
        font-size: 0.66rem;
        letter-spacing: 0.08em;
        color: #887361;
        margin-top: -6px;
        margin-bottom: 1rem;
    }
    .kpi-card {
        border: 1px solid #dbc2ad;
        border-radius: 10px;
        padding: 14px;
        background: #ffffff;
    }
    .kpi-label {
        font-size: 0.66rem;
        letter-spacing: 0.08em;
        font-weight: 700;
        color: #554434;
    }
    .kpi-value {
        color: #8a5100;
        font-size: 1.8rem;
        font-weight: 700;
        margin: 2px 0 0 0;
    }
    .kpi-delta-up {
        color: #2e7d32;
        background: #e8f5e9;
        padding: 2px 8px;
        border-radius: 6px;
        font-size: 0.7rem;
        font-weight: 700;
    }
    .kpi-delta-down {
        color: #ba1a1a;
        background: #ffdad6;
        padding: 2px 8px;
        border-radius: 6px;
        font-size: 0.7rem;
        font-weight: 700;
    }
    .panel {
        border: 1px solid #dbc2ad;
        border-radius: 10px;
        padding: 16px;
        background: #ffffff;
        height: 100%;
    }
    .section-title {
        font-size: 1.05rem;
        font-weight: 700;
        margin-bottom: 0.75rem;
    }
    </style>
    """,
main
    unsafe_allow_html=True,
)

with st.sidebar:
codex/create-amazon-ppc-dashboard-web-app-kjuziu
    st.markdown("<div class='brand'>Ads Console</div><div class='subbrand'>Seller Central API</div>", unsafe_allow_html=True)
    st.radio("", ["Dashboard","Campaigns","Products","Match Type","Keywords","Search Terms","ASIN Targets","ASIN from STR","Auto Campaigns","Category Targets","Wasted Ad Spend"], index=0)
    st.button("⚡  Sync Data", use_container_width=True)

    st.markdown("<p class='brand-title'>Ads Console</p>", unsafe_allow_html=True)
    st.markdown("<p class='brand-subtitle'>Seller Central API</p>", unsafe_allow_html=True)

    pages = [
        "Dashboard",
        "Campaigns",
        "Products",
        "Match Type",
        "Keywords",
        "Search Terms",
        "ASIN Targets",
        "ASIN from STR",
        "Auto Campaigns",
        "Category Targets",
        "Wasted Ad Spend",
    ]
    st.radio("Navigation", pages, index=0, label_visibility="collapsed")
    st.button("⚡ Sync Data", use_container_width=True)
main
    st.divider()
    st.button("Help Center", use_container_width=True)
    st.button("Log Out", use_container_width=True)

codex/create-amazon-ppc-dashboard-web-app-kjuziu
st.markdown("<div class='topbar'><div class='top-title'>PPC Insights</div><div class='chip'>ACCOUNT SELECTION ▾</div></div>", unsafe_allow_html=True)

r1c1, r1c2, r1c3 = st.columns([6,1,2])
r1c1.markdown("<div class='chip'>📅 Date Range: Last 30 Days</div>", unsafe_allow_html=True)
r1c2.markdown("<div style='padding-top:8px'>🔔</div>", unsafe_allow_html=True)
r1c3.markdown("<div style='padding-top:8px'>❔&nbsp;&nbsp;👤</div>", unsafe_allow_html=True)

kcols = st.columns(4)
cards = [("TOTAL SPEND","$12,450.00","+5%",0),("TOTAL SALES","$84,200.00","+12%",1),("ACoS","14.78%","-2%",1),("ROAS","6.76x","+8%",1)]
for c,(l,v,d,g) in zip(kcols,cards):
    badge = "badge-green" if g else "badge-red"
    c.markdown(f"<div class='metric-card'><div class='metric-label'>{l}</div><div style='display:flex;justify-content:space-between;align-items:end;'><div class='metric-value'>{v}</div><div class='{badge}'>{d}</div></div></div>", unsafe_allow_html=True)

main, side = st.columns([3,1])
with main:
    st.markdown("<div class='panel'><div class='title'>Performance Trends</div></div>", unsafe_allow_html=True)
    st.line_chart({"Spend":[40,42,45,49,51,54,56,60,63,64,64,62,59,56,54,53,55,59,65,72,77,80,79,75,68,63,61,62,66,72],"Sales":[50,54,58,64,71,78,86,94,102,108,112,113,111,106,100,96,95,98,105,116,128,138,143,142,135,126,120,118,121,131]}, height=350)
with side:
    st.markdown("<div class='title'>Insights & Alerts</div>", unsafe_allow_html=True)
    st.markdown("<div class='alert a1'><b>Budget Alert</b><br><br>3 campaigns are nearing daily budget limit.</div>", unsafe_allow_html=True)
    st.markdown("<div class='alert a2'><b>Optimization Tip</b><br><br>Lowering bids on \"keyword_x\" could save $45/day.</div>", unsafe_allow_html=True)
    st.markdown("<div class='alert a3'><b>Unlock AI Insights</b><br><br>Get predictive keyword scaling advice.</div>", unsafe_allow_html=True)
    st.button("UPGRADE PRO", use_container_width=True)

st.markdown("<div class='table-wrap'><div class='table-head'><div class='title' style='font-size:20px'>Top Performing Campaigns</div><div class='small-btn'>VIEW ALL REPORTS</div></div></div>", unsafe_allow_html=True)

import pandas as pd

df = pd.DataFrame([
["Summer_Collection_Manual_2023","ACTIVE","$1,420.50","$12,500.00","11.36%","⋯"],
["Prime_Day_Headphones_Auto","ACTIVE","$2,105.00","$18,450.00","11.41%","⋯"],
["Competitor_Targeting_Bags","PAUSED","$850.40","$6,120.00","13.89%","⋯"],
["Brand_Defense_Keywords","ACTIVE","$3,200.00","$24,800.00","12.90%","⋯"],
["Home_Office_Desk_Lamp_Manual","OUT OF BUDGET","$680.00","$3,450.00","19.71%","⋯"]
], columns=["CAMPAIGN NAME","STATUS","SPEND","SALES","ACoS","ACTION"])
st.dataframe(df, use_container_width=True, hide_index=True)

header_left, header_right = st.columns([3, 2])
with header_left:
    st.markdown("## PPC Insights")
with header_right:
    st.selectbox("Account Selection", ["Account Selection"], label_visibility="collapsed")

filter1, filter2, filter3 = st.columns([2, 1, 1])
with filter1:
    st.caption("Date Range: Last 30 Days")
with filter2:
    st.caption("🔔")
with filter3:
    st.caption("❔")

kpi_cols = st.columns(4)
kpis = [
    ("TOTAL SPEND", "$12,450.00", "+5%", "down"),
    ("TOTAL SALES", "$84,200.00", "+12%", "up"),
    ("ACoS", "14.78%", "-2%", "up"),
    ("ROAS", "6.76x", "+8%", "up"),
]

for col, (label, value, delta, trend) in zip(kpi_cols, kpis):
    badge_class = "kpi-delta-up" if trend == "up" else "kpi-delta-down"
    with col:
        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-label">{label}</div>
                <div style="display:flex;justify-content:space-between;align-items:end;gap:8px;">
                    <div class="kpi-value">{value}</div>
                    <div class="{badge_class}">{delta}</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

main_col, side_col = st.columns([3, 1])

with main_col:
    st.markdown("<div class='panel'>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Performance Trends</div>", unsafe_allow_html=True)

    x = pd.date_range("2026-10-01", periods=30, freq="D")
    spend = [40, 42, 45, 48, 50, 53, 56, 60, 63, 64, 64, 62, 59, 56, 54, 53, 55, 59, 65, 72, 77, 80, 79, 75, 68, 63, 61, 62, 66, 72]
    sales = [50, 54, 58, 64, 71, 78, 86, 94, 102, 108, 112, 113, 111, 106, 100, 96, 95, 98, 105, 116, 128, 138, 143, 142, 135, 126, 120, 118, 121, 131]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=spend, mode="lines", name="Spend", line=dict(color="#8a5100", width=2)))
    fig.add_trace(go.Scatter(x=x, y=sales, mode="lines", name="Sales", line=dict(color="#00687a", width=2)))
    fig.update_layout(
        margin=dict(l=8, r=8, t=0, b=8),
        paper_bgcolor="#ffffff",
        plot_bgcolor="#ffffff",
        xaxis=dict(showgrid=True, gridcolor="#f0f2f2", tickfont=dict(size=10)),
        yaxis=dict(showgrid=True, gridcolor="#f0f2f2", tickfont=dict(size=10)),
        legend=dict(orientation="h", y=1.12, x=0.76),
        height=300,
    )
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

with side_col:
    st.markdown("<div class='panel'>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Insights & Alerts</div>", unsafe_allow_html=True)
    st.info("**Budget Alert**\n\n3 campaigns are nearing daily budget limit.")
    st.warning('**Optimization Tip**\n\nLowering bids on "keyword_x" could save $45/day.')
    st.success("**Unlock AI Insights**\n\nGet predictive keyword scaling advice.")
    st.button("UPGRADE PRO", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("### Top Performing Campaigns")

campaigns_df = pd.DataFrame(
    [
        ["Summer_Collection_Manual_2023", "ACTIVE", 1420.50, 12500.00, "11.36%", "⋯"],
        ["Prime_Day_Headphones_Auto", "ACTIVE", 2105.00, 18450.00, "11.41%", "⋯"],
        ["Competitor_Targeting_Bags", "PAUSED", 850.40, 6120.00, "13.89%", "⋯"],
        ["Brand_Defense_Keywords", "ACTIVE", 3200.00, 24800.00, "12.90%", "⋯"],
        ["Home_Office_Desk_Lamp_Manual", "OUT OF BUDGET", 680.00, 3450.00, "19.71%", "⋯"],
    ],
    columns=["Campaign Name", "Status", "Spend", "Sales", "ACoS", "Action"],
)

st.dataframe(
    campaigns_df,
    use_container_width=True,
    hide_index=True,
    column_config={
        "Spend": st.column_config.NumberColumn(format="$%.2f"),
        "Sales": st.column_config.NumberColumn(format="$%.2f"),
    },
)
codex/create-amazon-ppc-dashboard-web-app-kjuziu
main

 main
main
main
main
