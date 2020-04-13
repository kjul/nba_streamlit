table_cols_values = ["SEASON_ID", "TEAM_ABBREVIATION", "PLAYER_AGE", "GP", "GS", "MIN", "FGM", 
                     "FGA", "FG_PCT", "FG3M", "FG3A", "FG3_PCT", "FTM", "FTA", "FT_PCT", 
                     "OREB", "DREB", "REB", "AST", "STL", "BLK", "TOV", "PF", "PTS"]

plot_cols_values = ["GP", "GS", "MIN", "FGM", "FGA", "FG_PCT", "FG3M", "FG3A", "FG3_PCT", 
                    "FTM", "FTA", "FT_PCT", "OREB", "DREB", "REB", "AST", "STL", "BLK", 
                    "TOV", "PF", "PTS"]

aggregations = {"sum":[i for i in plot_cols_values if "PCT" not in i],
                "calculate":[i for i in plot_cols_values if "PCT" in i]}
