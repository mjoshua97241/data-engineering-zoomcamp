import marimo

__generated_with = "0.19.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return


@app.cell
def _():
    import numpy as np
    import pandas as pd
    from sqlalchemy import create_engine
    return create_engine, pd


@app.cell
def _(pd):
    df_zones = pd.read_csv('data/taxi_zone_lookup.csv')
    df_zones.head()
    return (df_zones,)


@app.cell
def _(create_engine):
    engine = create_engine(f'postgresql://root:root@localhost:5432/ny_taxi')
    return (engine,)


@app.cell
def _(df_zones, engine):
    df_zones.to_sql(name='zones', con=engine, if_exists='replace')
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
