from blazingsql import BlazingContext
import cudf, os

bc = BlazingContext()

def all_trips_lt_10():
"""Summary
   Assumes that the sample_data.csv data is loaded into "bc",
   a query is being asked of the GPU by selecting every trip that is
   less than 10
"""
    global bc
    df = bc.sql('select * from taxi where trip_distance < 10')
    df.describe()


def main():
    """main():
        parameters:
        -----------
        None
    
        description:
        ------------
        As usual, the `BlazingContext` is created and its successful creation implies that the CUDA binding is intact and
        you have a gateway to the GPU. NExt, we read in the sample CSV file and creates a table from it.
        After that, we run a SQL query against the data we have just loaded to the associated table.
    
        result:
        -------
        TBA
    
        notes:
        ------
        (a) create_table is a zero-copy operation on the GPU i.e. its very fast and doesn't take up space on the GPU    
    
    """
    global bc
    df = cudf.read_csv('../data/sample_taxi.csv')
    bc.create_table('taxi', df)
    query = '''
select cast(substring(tpep_pickup_datetime,0,10) || ' 00:00:00' as timestamp) as pickup_date,
       count(*) as all_trips,
       avg(trip_distance) as avg_trip_distance,
       avg(fare_amount) as avg_fare_amount
from taxi
    group by cast(substring(tpep_pickup_datetime,0,10) || ' 00:00:00' as timestamp)
    order by cast(substring(tpep_pickup_datetime,0,10) || ' 00:00:00' as timestamp) limit 10
'''
    bc.sql(query)
    

if __name__ == "__main__":
  main()

