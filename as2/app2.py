import pandas as pd

import plotly.express as px
import streamlit as st
dfs=[]
participants = ['p01','p02',
    'p03',
    'p04',
    'p05',
    'p06',
    'p07',
    ]
for participant in participants:
    df = pd.read_csv(f'as2/pmdata/{participant}/fitbit/calories.csv',
                 skiprows=0)
    
    df['participants']=participant
    print(df.head())
    dfs.append(df)
df=pd.concat(dfs)


st.set_page_config(page_title="Fitbit Dashboard (All Participant Analysis) 2",
                   page_icon=':bar_chart:',
                   layout='wide')

date=pd.to_datetime(df['dateTime'], utc=False).dt.date
df["date"]=date

st.sidebar.header('please Filter Data Here')

Date= st.sidebar.multiselect(
'Select The Date',
options=date.unique(),
default=date.unique()   
)
time=pd.to_datetime(df['dateTime'], utc=False).dt.time
df["time"]=time

st.sidebar.header('please Filter Data Here')

Time= st.sidebar.multiselect(
'Select The Time',
options=time.unique(),
default=time.unique()   
)
hour=pd.to_datetime(df['dateTime'], utc=False).dt.hour
df["hour"]= hour


Hour= st.sidebar.multiselect(
'Select The Hour',
options=hour.unique(),
default=hour.unique()   
)

df_selection= df.query(

    "hour== @Hour & time==@Time & date==@Date"
)
st.dataframe(df_selection)


st.title(":bar_chart: Fitbit Dashboard")
st.markdown('##')

sum_value= df_selection['value'].sum()
avg_value= df_selection['value'].mean()

min_value= df_selection['value'].min()
max_value= df_selection['value'].max()
star_avg = ":star:" * int(round(avg_value, 0))

left_column, middle_column, right_column=st.columns(3)
with left_column:
    st.subheader(" Total Value")
    st.subheader(f'{sum_value}')
with middle_column:
    st.subheader(" Min and Max")
    st.subheader(f'{min_value}  & {max_value}')
with right_column:
    st.subheader(" Avg Value")
    st.subheader(f'{avg_value}')

st.markdown('---')

# SALES BY PRODUCT LINE [BAR CHART]
hourly_values = df_selection.groupby(by=["hour"])[["value"]].sum().sort_values(by="value")
fig_hourly_values = px.bar(
    hourly_values,
    x="value",
    y=hourly_values.index,
    orientation="h",
    title="<b>Hourly Values</b>",
    color_discrete_sequence=["#0083B8"] * len(hourly_values),
    template="plotly_white",
)
fig_hourly_values.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)



values_by_date = df_selection.groupby(by=["date"])[["value"]].sum()
fig_dates_values = px.bar(
    values_by_date,
    x=values_by_date.index,
    y="value",
    title="<b>values by date</b>",
    color_discrete_sequence=["#0083B8"] * len(values_by_date),
    template="plotly_white",
)
fig_dates_values.update_layout(
    xaxis=dict(tickmode="linear"),
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)




values_by_participant = df_selection.groupby(by=["participants"])[["value"]].sum()
fig_participants_values = px.bar(
    values_by_participant,
    x=values_by_participant.index,
    y="value",
    title="<b>values by date</b>",
    color_discrete_sequence=["#0083B8"] * len(values_by_participant),
    template="plotly_white",
)
fig_participants_values.update_layout(
    xaxis=dict(tickmode="linear"),
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)


first_column, second_column, third_column = st.columns(3)
first_column.plotly_chart(fig_hourly_values, use_container_width=True)
second_column.plotly_chart(fig_dates_values, use_container_width=True)
third_column.plotly_chart(fig_participants_values, use_container_width=True)
