
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Coffee Shop Analytics",
    page_icon="☕",
    layout="wide",
)

DATA_PATH = Path(__file__).parent / "data" / "Coffee Shop Sales.xlsx"


@st.cache_data
def load_data():
    df = pd.read_excel(DATA_PATH)

    df["transaction_date"] = pd.to_datetime(df["transaction_date"])
    df["transaction_time"] = pd.to_datetime(
        df["transaction_time"].astype(str),
        format="%H:%M:%S",
        errors="coerce",
    ).dt.time

    df["revenue"] = df["transaction_qty"] * df["unit_price"]
    df["month"] = df["transaction_date"].dt.to_period("M").astype(str)

    return df


df = load_data()

st.title("☕ Coffee Shop Analytics")
st.caption("Sales performance dashboard | January–June 2023")

# Sidebar filters
st.sidebar.header("Filters")

min_date = df["transaction_date"].min().date()
max_date = df["transaction_date"].max().date()

date_range = st.sidebar.date_input(
    "Date range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date,
)

selected_stores = st.sidebar.multiselect(
    "Store",
    options=sorted(df["store_location"].unique()),
    default=sorted(df["store_location"].unique()),
)

selected_categories = st.sidebar.multiselect(
    "Product category",
    options=sorted(df["product_category"].unique()),
    default=sorted(df["product_category"].unique()),
)

# Apply filters
if isinstance(date_range, (tuple, list)) and len(date_range) == 2:
    start_date, end_date = date_range
else:
    start_date, end_date = min_date, max_date

filtered = df[
    (df["transaction_date"].dt.date >= start_date)
    & (df["transaction_date"].dt.date <= end_date)
    & (df["store_location"].isin(selected_stores))
    & (df["product_category"].isin(selected_categories))
].copy()

st.subheader("Key performance indicators")

revenue = filtered["revenue"].sum()
transactions = filtered["transaction_id"].nunique()
units = filtered["transaction_qty"].sum()
ticket = revenue / transactions if transactions else 0

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total revenue", f"${revenue:,.2f}")
col2.metric("Transactions", f"{transactions:,}")
col3.metric("Units sold", f"{units:,}")
col4.metric("Average ticket", f"${ticket:,.2f}")

if filtered.empty:
    st.warning("No data matches the selected filters.")
else:
    left, right = st.columns(2)

    with left:
        monthly = (
            filtered.groupby("month", as_index=False)["revenue"]
            .sum()
            .sort_values("month")
        )

        fig_month = px.line(
            monthly,
            x="month",
            y="revenue",
            markers=True,
            title="Revenue by month",
            labels={"month": "Month", "revenue": "Revenue ($)"},
        )
        st.plotly_chart(fig_month, use_container_width=True)

    with right:
        categories = (
            filtered.groupby("product_category", as_index=False)["revenue"]
            .sum()
            .sort_values("revenue", ascending=False)
        )

        fig_category = px.bar(
            categories,
            x="product_category",
            y="revenue",
            title="Revenue by category",
            labels={
                "product_category": "Category",
                "revenue": "Revenue ($)",
            },
        )
        st.plotly_chart(fig_category, use_container_width=True)

    products = (
        filtered.groupby("product_detail", as_index=False)
        .agg(
            revenue=("revenue", "sum"),
            units=("transaction_qty", "sum"),
        )
        .sort_values("revenue", ascending=False)
        .head(10)
    )

    fig_products = px.bar(
        products.sort_values("revenue"),
        x="revenue",
        y="product_detail",
        orientation="h",
        title="Top 10 products by revenue",
        labels={
            "product_detail": "Product",
            "revenue": "Revenue ($)",
        },
    )

    st.plotly_chart(fig_products, use_container_width=True)

    with st.expander("View filtered data"):
        st.dataframe(filtered, use_container_width=True)

st.caption("Source: Maven Analytics Coffee Shop Sales dataset.")


# Natural language questions
st.divider()
st.header("Ask your coffee data ☕")
st.write("Ask a question about sales. This assistant uses the complete dataset.")

question = st.text_input(
    "Your question",
    placeholder="e.g. Which category generated the most revenue in June?",
    key="business_question",
)

if st.button("Ask", key="ask_question"):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        q = question.lower().strip()

        # Always use the complete dataset, ignoring dashboard filters.
        analysis_data = df.copy()

        # Optional month filter
        months = {
            "january": 1, "jan": 1, "enero": 1,
            "february": 2, "feb": 2, "febrero": 2,
            "march": 3, "marzo": 3,
            "april": 4, "abril": 4,
            "may": 5, "mayo": 5,
            "june": 6, "jun": 6, "junio": 6,
        }

        selected_month = next(
            (number for name, number in months.items() if name in q),
            None,
        )

        if selected_month:
            analysis_data = analysis_data[
                analysis_data["transaction_date"].dt.month == selected_month
            ]

        if analysis_data.empty:
            st.warning("No data found for that period.")

        elif any(word in q for word in ["category", "categoría", "categoria"]):
            result = (
                analysis_data.groupby("product_category")["revenue"]
                .sum()
                .sort_values(ascending=False)
            )
            st.success(
                f"Top category: {result.index[0]} "
                f"(${result.iloc[0]:,.2f})"
            )

        elif any(word in q for word in ["store", "tienda", "sucursal"]):
            result = (
                analysis_data.groupby("store_location")["revenue"]
                .sum()
                .sort_values(ascending=False)
            )
            st.success(
                f"Top store: {result.index[0]} "
                f"(${result.iloc[0]:,.2f})"
            )

        elif any(word in q for word in ["product", "producto"]):
            result = (
                analysis_data.groupby("product_detail")
                .agg(
                    revenue=("revenue", "sum"),
                    units=("transaction_qty", "sum"),
                )
                .sort_values("revenue", ascending=False)
                .head(5)
                .reset_index()
            )
            st.write("Top 5 products by revenue")
            st.dataframe(result, use_container_width=True)

        elif any(word in q for word in [
            "revenue", "sales", "vendimos", "ingresos", "ventas"
        ]):
            total_revenue = analysis_data["revenue"].sum()
            st.metric("Total revenue", f"${total_revenue:,.2f}")

        else:
            st.info(
                "I couldn't recognize that question yet. "
                "Try asking about total revenue, categories, stores, "
                "or products."
            )

        if selected_month and not analysis_data.empty:
            st.caption(f"Period: month {selected_month}, 2023.")


