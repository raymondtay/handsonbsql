from blazingsql import BlazingContext

bc = BlazingContext()

def main():
    """
    main():
        parameters:
        -----------
        None
    
        description:
        ------------
        Creates a connection to the GPU underneath and holds it in "bc".
        Next, we access the "colab" environment S3 bucket (which holds a parquet
        file) and creates a table named "taxi" with it.
        Finally, a query is triggered
    
        result:
        -------
           passenger_count  trip_distance
        0              1.0            1.1
        1              1.0            0.7
    
        notes:
        ------
        You can run a general table scan like this:
        >>> bc.sql("select * from taxi limit 1000")
             VendorID tpep_pickup_datetime tpep_dropoff_datetime  passenger_count  trip_distance     pickup_x  ...  fare_amount  extra mta_tax  tip_amount  tolls_amount  total_amount
        0         2.0  2015-03-05 07:38:36   2015-03-05 07:44:06              1.0           1.10 -8235279.565  ...          6.0    0.0     0.5        2.00           0.0          8.80
        1         1.0  2015-02-03 05:41:55   2015-02-03 05:46:54              1.0           0.70 -8235656.655  ...          5.5    0.5     0.5        1.36           0.0          8.16
        2         2.0  2015-02-08 16:17:51   2015-02-08 16:37:45              1.0           3.65 -8238228.336  ...         16.0    0.0     0.5        0.00           0.0         16.80
        3         2.0  2015-03-07 02:17:05   2015-03-07 02:22:18              3.0           0.77 -8232200.852  ...          5.5    0.5     0.5        0.00           0.0          6.80
        4         2.0  2015-02-05 21:05:35   2015-02-05 21:10:33              2.0           0.74 -8236124.619  ...          5.5    0.5     0.5        1.00           0.0          7.80
        ..        ...                  ...                   ...              ...            ...          ...  ...          ...    ...     ...         ...           ...           ...
        995       2.0  2015-01-24 20:27:32   2015-01-24 20:45:25              1.0           1.73 -8238088.201  ...         12.0    0.5     0.5        3.32           0.0          0.30
        996       1.0  2015-01-23 07:13:47   2015-01-23 07:31:52              1.0           4.50 -8238835.586  ...         16.0    0.0     0.5        3.00           0.0          0.30
        997       2.0  2015-01-04 11:01:15   2015-01-04 11:03:16              1.0           0.71 -8235919.938  ...          4.0    0.0     0.5        0.00           0.0          0.30
        998       2.0  2015-03-29 00:46:34   2015-03-29 01:00:10              1.0           2.97 -8236252.014  ...         12.5    0.5     0.5        2.76           0.0         16.56
        999       1.0  2015-02-06 17:34:14   2015-02-06 17:53:36              1.0           1.90 -8239127.745  ...         13.5    1.0     0.5        3.05           0.0         18.35
    
        [1000 rows x 18 columns]
    
    """
    global bc
    bc.s3('blazingsql-colab', bucket_name='blazingsql-colab')
    
    bc.create_table('taxi', 's3://blazingsql-colab/yellow_taxi/taxi_data.parquet')
    
    bc.sql('SELECT passenger_count, trip_distance FROM taxi LIMIT 2')

if __name__ == "__main__":
    main()
