import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# --- Step 1: Load and Preprocess the Data ---
df = pd.read_csv("chase_2025.csv", parse_dates=["Post Date"])
df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")

# Filter for expenses
df_expenses = df[df["Amount"] < 0].copy()

# Create a readable month label (e.g., "Jan 2024")
df_expenses["MonthLabel"] = df_expenses["Post Date"].dt.strftime("%b %Y")  # e.g., "Jan 2024"

# Also store datetime for correct sorting later
df_expenses["MonthSort"] = df_expenses["Post Date"].dt.to_period("M").dt.to_timestamp()

# --- Step 2: Summarize by Month and Category ---
summary = (
    df_expenses
    .groupby(["MonthSort", "MonthLabel", "Category"])["Amount"]
    .sum()
    .unstack(fill_value=0)
    .reset_index()
    .sort_values("MonthSort")
    .set_index("MonthLabel")
)

summary_positive = summary.drop(columns="MonthSort").abs()
summary_positive["Total Spendings"] = summary_positive.sum(axis=1)

# --- Step 3: Plotly Visualizations ---

# Stacked Bar Chart with Month Labels
fig_bar = go.Figure()
for category in summary_positive.columns[:-1]:  # skip Total Spendings
    fig_bar.add_trace(go.Bar(
        x=summary_positive.index,  # now readable month names
        y=summary_positive[category],
        name=category
    ))

fig_bar.update_layout(
    barmode='stack',
    title="Monthly Spending by Category",
    xaxis_title="Month",
    yaxis_title="Amount ($)",
    legend_title="Category",
    hovermode="x unified"
)

# Line Chart with Month Labels
fig_line = px.line(
    summary_positive,
    x=summary_positive.index,
    y="Total Spendings",
    title="Total Monthly Spendings",
    markers=True
)
fig_line.update_layout(
    xaxis_title="Month",
    yaxis_title="Amount ($)",
    hovermode="x"
)

# Show plots
fig_bar.show()
fig_line.show()
