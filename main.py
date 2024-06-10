import streamlit as st
import plotly.express as px
import functions
import glob

st.set_page_config(
        page_title="Diary mood tracker",
        layout="wide"
)

# Get path list of all diaries, sort by order
diary_paths = sorted(glob.glob('diary/*.txt'))
# Get sentiment score map of each diary entry
diary_scores_map = functions.get_sentiment(diary_paths)

# Build streamlit webpage (title, sub-header and line graphs)
st.title('Sentiment analysis of Diary 🍀')

st.write("We all have our ups and downs. How have you been recently? Let's keep track and grow.")
new_diary = st.file_uploader("Upload a new data entry here:", key="new_diary")

if new_diary is not None:
    functions.write_new_entry(new_diary)
    diary_paths = sorted(glob.glob('diary/*.txt'))
    diary_scores_map = functions.get_sentiment(diary_paths)
    st.write(":green[New diary entry added!]")

# Render graphs

col1, col2 = st.columns(2)

with col1:
    st.subheader('Positivity')
    line_chart1 = px.line(x=diary_scores_map.keys(), y=[dict['pos'] for dict in diary_scores_map.values()],
                          labels={"x": 'Date', "y": 'Positivity'})
    st.plotly_chart(line_chart1)

with col2:
    st.subheader('Negativity')
    line_chart2 = px.line(x=diary_scores_map.keys(), y=[score['neg'] for score in diary_scores_map.values()],
                          labels={"x": 'Date', "y": 'Negativity'})
    st.plotly_chart(line_chart2)
