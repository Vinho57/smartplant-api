PLOT_CONFIGS = {
    "temperature": {
        "endpoint": "latest-today",
        "config": lambda df: {
            "y_column": "temperature",
            "y_title": "Temperatur (°C)",
            "y_range": [df["temperature"].min() - 1, df["temperature"].max() + 1],
            "color": "red",
            "fillcolor": "rgba(255, 0, 0, 0.15)",
            "name": "Temperatur"
        }
    },
    "soil": {
        "endpoint": "latest-today",
        "config": lambda df: {
            "y_column": "soil_moisture",
            "y_title": "Bodenfeuchtigkeit (%)",
            "y_range": [0, 100],
            "color": "darkgreen",
            "fillcolor": "rgba(0,128,0,0.2)"
        }
    },
    "luftfeuchtigkeit": {
        "endpoint": "latest-today",
        "config": lambda df: {
            "y_column": "luftfeuchtigkeit",
            "y_title": "Luftfeuchtigkeit (%)",
            "y_range": [20, 100],
            "color": "blue",
            "fillcolor": "rgba(0, 0, 255, 0.2)"
        }
    },
    "sunlight": {
        "endpoint": "sunlight-30days",
        "config": lambda df: {
            "y_column": "sunlight",
            "y_title": "Sonnenstunden",
            "y_range": [0, df["sunlight"].max() + 1],
            "color": "orange",
            "fillcolor": "rgba(255, 165, 0, 0.2)"
        }
    }
}