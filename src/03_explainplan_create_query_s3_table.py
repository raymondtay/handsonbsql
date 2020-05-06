from blazingsql import BlazingContext

bc = BlazingContext()

def main() :
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
        Finally, this example ends off by saying that we wish to understand how
        BSQL is planning to extract the data rather than actually extracting it.
    
        result:
        -------
        'LogicalSort(fetch=[2])
             BindableTableScan(table=[[main, taxi]], projects=[[3, 4]], aliases=[[passenger_count, trip_distance]])
        '
    """
    global bc
    bc.s3('blazingsql-colab', bucket_name='blazingsql-colab')
    
    bc.create_table('taxi', 's3://blazingsql-colab/yellow_taxi/taxi_data.parquet')
    
    query = 'SELECT passenger_count, trip_distance FROM taxi LIMIT 2'
    
    bc.explain(query)


if __name__ == "__main__":
    main()
