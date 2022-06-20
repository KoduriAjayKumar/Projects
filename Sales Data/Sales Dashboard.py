import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(page_title = "D:\\Internshala\\Data Science - SideKick\\Sales Dashboard.xlsx",
                   page_icon = ":bar_chart:",
                   layout = "wide")


df = pd.read_excel("Sales Data.xlsx", "Sales Dataset")


st.sidebar.header("Please Filter here: ")

DEALSIZE = st.sidebar.multiselect("Select the Deal Size",
                               options = df["DEALSIZE"].unique(),
                               default = df["DEALSIZE"].unique())

CITY = st.sidebar.multiselect("Select the city",
                               options = df["CITY"].unique(),
                               default = df["CITY"].unique())


df_selection = df.query("CITY == @CITY & DEALSIZE == @DEALSIZE")


st.title(":bar_chart: Sales Dashboard")
st.markdown("##")

Sales_Amount = int(df_selection["SALESAMOUNT"].sum())

Avg_sale_per_customer = round(df_selection["SALESAMOUNT"].mean(), 2)

left_column, right_column = st.columns(2)

with left_column:
    st.subheader("Total Sales")
    st.subheader(f"US $ {Sales_Amount:,}")

with right_column:
    st.subheader("Average sale per customer") 
    st.subheader(f"US $ {Avg_sale_per_customer:,}")

st.markdown("----")

sales_by_product_line = df.groupby(by = ["PRODUCTLINE"]).sum()[["SALESAMOUNT"]].sort_values(by="SALESAMOUNT")



fig1 = px.bar(sales_by_product_line, x = "SALESAMOUNT",
              y = sales_by_product_line.index,
              orientation = "h",
              title = "<b>Sales by product line.</b>",
              color_discrete_sequence = ["#0083B8"]*len(sales_by_product_line),
              template = "plotly_white")

fig1.update_layout(
    plot_bgcolor = "rgba(0,0,0,0)",
                   xaxis = (dict(showgrid = False)))

Sales_by_year = df.groupby(by = ["YEAR"]).sum()[["SALESAMOUNT"]].sort_values(by="SALESAMOUNT")

fig2 = px.bar(Sales_by_year,x = Sales_by_year.index, y = ["SALESAMOUNT"] ,
              title = "<b>Sales by Year</b>",
              color_discrete_sequence = ["#0083B8"]*len(Sales_by_year),
              template = "plotly_white")
fig2.update_layout(
    plot_bgcolor = "rgba(0,0,0,0)",
                   yaxis = (dict(showgrid = False)))


left_column, right_column = st.columns(2)

left_column.plotly_chart(fig1, use_container_width = True)
right_column.plotly_chart(fig2, use_container_width = True)



hide_st_style = """
               <style>
               #MainMenu{visibility: hidden;}
               footer {visibility: hidden;}
               header {visibility: hidden;}
               </style>
               """

st.markdown(hide_st_style, unsafe_allow_html= True )






    














