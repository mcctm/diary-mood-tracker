import streamlit as st
import plotly.express as px
import functions
import glob

# Get path list of all diaries, sort by order
diary_paths = sorted(glob.glob('diary/*.txt'))
# Get sentiment score map of each diary entry
diary_scores_map = functions.getSentiment(diary_paths)

# Build streamlit webpage (title, sub-header and line graphs)
st.title('Sentiment analysis of Diary')

st.subheader('Positivity')
line_chart1 = px.line(x=diary_scores_map.keys(), y=[dict['pos'] for dict in diary_scores_map.values()],
                      labels={"x": 'Date', "y": 'Positivity'})
st.plotly_chart(line_chart1)

st.subheader('Negativity')
line_chart2 = px.line(x=diary_scores_map.keys(), y=[score['neg'] for score in diary_scores_map.values()],
                      labels={"x": 'Date', "y": 'Negativity'}, title="Negativity")
st.plotly_chart(line_chart2)
