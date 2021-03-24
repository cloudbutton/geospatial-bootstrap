def choose_town():
    options = [(town["NOMMUNI"], town["CODIMUNI"]) for index, town in gdf_tgn.iterrows()]

    widgets.Dropdown(
        options=options,
        value="431482",
        description='Choose a town:',
    )