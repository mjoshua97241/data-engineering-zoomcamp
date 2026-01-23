import marimo

__generated_with = "0.19.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    import pandas as pd
    return (pd,)


@app.cell
def _():
    trips_data = 'data/green_tripdata_2025-11.parquet'
    zone_data = 'data/taxi_zone_lookup.csv'
    return trips_data, zone_data


@app.cell
def _(pd, trips_data):
    trips_data_df = pd.read_parquet(trips_data)
    trips_data_df.head()
    return (trips_data_df,)


@app.cell
def _(mo):
    mo.md(r"""
    ## Question 3. Counting short trips

    For the trips in November 2025 (lpep_pickup_datetime between '2025-11-01' and '2025-12-01', exclusive of the upper bound), how many trips had a `trip_distance` of less than or equal to 1 mile?
    """)
    return


@app.cell
def _(trips_data_df):
    short_trips = trips_data_df[
        trips_data_df["lpep_pickup_datetime"].between('2025-11-01', '2025-12-01') &
         (trips_data_df["trip_distance"] <= 1.0)
         ]
    short_trips.count()
    return


@app.cell
def _():
    return


@app.cell
def _(mo):
    mo.md(r"""
    The answer is 8,007.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Question 4. Longest trip for each day

    Which was the pick up day with the longest trip distance? Only consider trips with trip_distance less than 100 miles.
    """)
    return


@app.cell
def _():
    return


@app.cell
def _(pd, zone_data):
    zone_df = pd.read_csv(zone_data)
    # zone_df.head()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
