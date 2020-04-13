import streamlit as st
from data_processing import data_io
from data_processing import constants as ct
from data_processing import plotting

st.title("NBA Player Stats")
st.write(f"Collected career data of {len(data_io.list_players_with_ids(str()))} players.")

search_text = st.sidebar.text_input("Enter player's last name:", value="Nowitzki")
player_list = data_io.list_players_with_ids(search_text)
player_choice = st.sidebar.selectbox('Select player:', player_list)
data_set_choice = st.sidebar.selectbox('Select regular season or playoffs:', ["Regular Season", "Playoffs"])
selected_data_set = {"Regular Season": "SeasonTotalsRegularSeason",
                     "Playoffs": "SeasonTotalsPostSeason"}[data_set_choice]
selected_player = str(player_choice["player_id"])
selected_columns = st.sidebar.multiselect("Select which statistics you want to plot:", 
                                          ct.plot_cols_values, 
                                          default=["MIN","PTS","AST","FG3M","FGM"])

st.write(plotting.plot_career_stats(selected_player, selected_data_set, selected_columns))
st.write(data_io.get_player_stats(str(selected_player))[selected_data_set][ct.table_cols_values])
st.write("")
st.write("apis provided by https://github.com/swar/nba_api")
