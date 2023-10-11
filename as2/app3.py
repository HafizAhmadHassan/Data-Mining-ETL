import pandas as pd

import plotly.express as px
import streamlit as st

st.title("Fitbit Dashboard")
dfs=[]
participants = ['p01','p02',
    'p03',
    'p04',
    'p05',
    'p06',
    'p07',
    ]
for participant in participants:
    df = pd.read_json(f'as2/pmdata/{participant}/fitbit/sleep.json')
    df['participants']=participant
    #print(df.head())
    dfs.append(df)
df=pd.concat(dfs)

df.iloc[0].levels['summary']

def get_minutes(levels, sleep_phase):
    if not levels.get('summary'):
        return None
    if not levels.get('summary').get(sleep_phase):
        return None
    if not levels.get('summary').get(sleep_phase).get('minutes'):
        return None
    return levels['summary'][sleep_phase]['minutes']


df['deepSleep'] = df.levels.apply(get_minutes, args=('deep',))
df['wakeMins'] = df.levels.apply(get_minutes, args=('wake',))
df['lightSleep'] = df.levels.apply(get_minutes, args=('light',))
df['remSleep'] = df.levels.apply(get_minutes, args=('rem',))
df.dateOfSleep = pd.to_datetime(df.dateOfSleep)
df.set_index("dateOfSleep", drop=True, inplace=True)
df.sort_index(inplace=True)
df.drop(columns=([
    "logId", 
    "startTime", 
    "endTime", 
    "duration", 
    "minutesToFallAsleep", 
    "minutesAwake", 
    "minutesAfterWakeup", 
    "efficiency",
    "type",
    "infoCode",
    "levels",
    "mainSleep"
]), inplace=True)
df.dropna(inplace=True)


#st.set_page_config(page_title= "Fitbit Dashboard (All Participant Analysis) 2",page_icon=':bar_chart:',layout='wide')

#date=pd.to_datetime(df['dateOfSleep'], utc=False).dt.date
#df["date"]=date

st.sidebar.header('please Filter Participants Type Here')

participants_= st.sidebar.multiselect(
'Select The columns',
options=list(participants),
default=list(participants)  
)
df_selection=df_selection= df.query(

    "participants== @participants_"
)
st.dataframe(df_selection)




values_by_participant = df_selection.groupby(by=["participants"])[["deepSleep"]].sum()
fig_participants_values = px.bar(
    values_by_participant,
    x=values_by_participant.index,
    y="deepSleep",
    title="<b>deepSleep by Each Participent</b>",
    color_discrete_sequence=["#0083B8"] * len(values_by_participant),
    template="plotly_white",
)
fig_participants_values.update_layout(
    xaxis=dict(tickmode="linear"),
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)




valuesavg_by_participant = df_selection.groupby(by=["participants"])[["deepSleep"]].mean()
fig_participants_valuesavg = px.bar(
    valuesavg_by_participant,
    x=valuesavg_by_participant.index,
    y="deepSleep",
    title="<b>deepSleep by Each Participent Average</b>",
    color_discrete_sequence=["#0083B8"] * len(valuesavg_by_participant),
    template="plotly_white",
)
fig_participants_valuesavg.update_layout(
    xaxis=dict(tickmode="linear"),
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)

first_column, second_column, third_column = st.columns(3)
first_column.plotly_chart(fig_participants_values, use_container_width=True)

second_column.plotly_chart(fig_participants_valuesavg, use_container_width=True)








values_by_participant = df_selection.groupby(by=["participants"])[["remSleep"]].sum()
fig_participants_values = px.bar(
    values_by_participant,
    x=values_by_participant.index,
    y="remSleep",
    title="<b>remSleep by Each Participent</b>",
    color_discrete_sequence=["#0083B8"] * len(values_by_participant),
    template="plotly_white",
)
fig_participants_values.update_layout(
    xaxis=dict(tickmode="linear"),
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)




valuesavg_by_participant = df_selection.groupby(by=["participants"])[["remSleep"]].mean()
fig_participants_valuesavg = px.bar(
    valuesavg_by_participant,
    x=valuesavg_by_participant.index,
    y="remSleep",
    title="<b>remSleep by Each Participent Average</b>",
    color_discrete_sequence=["#0083B8"] * len(valuesavg_by_participant),
    template="plotly_white",
)
fig_participants_valuesavg.update_layout(
    xaxis=dict(tickmode="linear"),
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)

first_column, second_column, third_column = st.columns(3)
first_column.plotly_chart(fig_participants_values, use_container_width=True)

second_column.plotly_chart(fig_participants_valuesavg, use_container_width=True)







values_by_participant = df_selection.groupby(by=["participants"])[["lightSleep"]].sum()
fig_participants_values = px.bar(
    values_by_participant,
    x=values_by_participant.index,
    y="lightSleep",
    title="<b>lightSleep by Each Participent</b>",
    color_discrete_sequence=["#0083B8"] * len(values_by_participant),
    template="plotly_white",
)
fig_participants_values.update_layout(
    xaxis=dict(tickmode="linear"),
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)




valuesavg_by_participant = df_selection.groupby(by=["participants"])[["lightSleep"]].mean()
fig_participants_valuesavg = px.bar(
    valuesavg_by_participant,
    x=valuesavg_by_participant.index,
    y="lightSleep",
    title="<b>lightSleep by Each Participent Average</b>",
    color_discrete_sequence=["#0083B8"] * len(valuesavg_by_participant),
    template="plotly_white",
)
fig_participants_valuesavg.update_layout(
    xaxis=dict(tickmode="linear"),
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)

first_column, second_column, third_column = st.columns(3)
first_column.plotly_chart(fig_participants_values, use_container_width=True)

second_column.plotly_chart(fig_participants_valuesavg, use_container_width=True)
