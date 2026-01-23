#!/usr/bin/env python
# coding: utf-8

import os
import click
import pandas as pd
import pyarrow.parquet as pq
import pyarrow.dataset as ds
import urllib.request
from sqlalchemy import create_engine
from tqdm.auto import tqdm


# -----------------------------
# Dtype and parse_dates
# -----------------------------
dtype = {
    "VendorID": "Int64",
    "passenger_count": "Int64",
    "trip_distance": "float64",
    "RatecodeID": "Int64",
    "store_and_fwd_flag": "string",
    "PULocationID": "Int64",
    "DOLocationID": "Int64",
    "payment_type": "Int64",
    "fare_amount": "float64",
    "extra": "float64",
    "mta_tax": "float64",
    "tip_amount": "float64",
    "tolls_amount": "float64",
    "improvement_surcharge": "float64",
    "total_amount": "float64",
    "congestion_surcharge": "float64"
}

parse_dates = [
    "tpep_pickup_datetime",
    "tpep_dropoff_datetime"
]

# -----------------------------
# Click command
# -----------------------------
@click.command()
@click.option(
    "--user",
    default=lambda: os.getenv("POSTGRES_USER", "postgres"),
    help="PostgreSQL user"
)
@click.option(
    "--password",
    default=lambda: os.getenv("POSTGRES_PASSWORD", "postgres"),
    help="PostgreSQL password"
)
@click.option(
    "--host",
    default=lambda: os.getenv("POSTGRES_HOST", "db"),
    help="PostgreSQL host"
)
@click.option(
    "--port",
    default=lambda: int(os.getenv("POSTGRES_PORT", 5432)),
    type=int,
    help="PostgreSQL port"
)
@click.option(
    "--db",
    default=lambda: os.getenv("POSTGRES_DB", "ny_taxi"),
    help="PostgreSQL database name"
)
@click.option(
    "--table",
    default=lambda: os.getenv("TRIP_TABLE", "green_taxi_data"),
    help="Target table name"
)
@click.option(
    "--chunksize",
    default=lambda: int(os.getenv("CHUNKSIZE", 100_000)),
    type=int,
    help="Number of rows per chunk"
)
def run(user, password, host, port, db, table, chunksize):
    data_dir = "./data"
    os.makedirs(data_dir, exist_ok=True)
    
    # -----------------------------
    # URLs
    # -----------------------------
    trip_data = f"{data_dir}/green_tripdata_2025-11.parquet"
    zone_data = f"{data_dir}/taxi_zone_lookup.csv"
    
    # -----------------------------
    # Download data if not exists
    # -----------------------------
    trip_url = "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2025-11.parquet"
    if not os.path.exists(trip_data):
        print(f"Downloading trip data from {trip_url}...")
        urllib.request.urlretrieve(trip_url, trip_data)
    else:
        print(f"Trip data file already exists at {trip_data}")
        
    zone_url = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv"
    if not os.path.exists(zone_data):
        print(f"Downloading taxi zone lookup from {zone_url}...")
        urllib.request.urlretrieve(zone_url, zone_data)
    else:
        print(f"Taxi zone lookup file already exists at {zone_data}")
    

    # -----------------------------
    # Database engine
    # -----------------------------
    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}")

    # -----------------------------
    # Load trip data in chunks
    # -----------------------------
    print(f"Loading trip data from {trip_data} in chunks of {chunksize} rows ...")

    # Use pyarrow.dataset to stream parquet in row groups
    dataset = ds.dataset(trip_data, format="parquet")
    first = True
    row_group_counter = 0

    for batch in tqdm(dataset.to_batches(batch_size=chunksize), desc="Processing batches"):
        df_chunk = batch.to_pandas()
        if first:
            # Create table schema
            df_chunk.head(0).to_sql(name=table, con=engine, if_exists="replace", index=False)
            first = False
            print(f"Table '{table}' created")

        # Insert chunk
        df_chunk.to_sql(name=table, con=engine, if_exists="append", index=False)
        row_group_counter += len(df_chunk)
        print(f"Inserted {len(df_chunk)} rows, total so far: {row_group_counter}")

    print(f"Trip data ingestion completed: {row_group_counter} rows total")

    # -----------------------------
    # Load taxi zone lookup
    # -----------------------------
    print(f"Loading taxi zone lookup from {zone_data} ...")
    df_zones = pd.read_csv(zone_data)
    df_zones.to_sql(name="taxi_zone_lookup", con=engine, if_exists="replace", index=False)
    print(f"Taxi zone lookup loaded ({len(df_zones)} rows)")

    print("✅ All ingestion complete")


# -----------------------------
# Entry point
# -----------------------------
if __name__ == "__main__":
    run()
