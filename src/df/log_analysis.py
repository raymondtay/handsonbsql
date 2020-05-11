from blazingsql import BlazingContext
bc = BlazingContext()

# BlazingSQL has an internal log that records events from every node from all
# queries run. The events include runtime query step execution information,
# performance timings, errors and warnings.
# 
def main():
    """Summary of main()
       parameters:
       -----------
      
       description:
       ------------  
       The logs table is called bsql_logs. You can query the logs as if it were any
       other table, except you use the .log() function, instead of the .sql()
       function.

    """
    global bc
    print('#> Most recent logs: {}'.format(bc.log('select * from bsql_logs').head()))
    print('#> Execution times of MRU-completed queries: {}'.format(bc.log("select log_time, query_id, duration from bsql_logs where info = 'Query Execution Done' order by log_time DESC")))
    discover_totaltime_query_execution()
    compute_execution_times_frequent_queries()


def compute_execution_times_frequent_queries():
    global bc
    query = '''
    select
        max(end_time) as end_time,
        sum(query_duration)/count(query_duration) as avg_time,
        min(query_duration) as min_time,
        max(query_duration) as max_time,
        count(query_duration) as num_times,
        relational_algebra
    from (
        select
            times.end_time as end_time,
            times.query_id, times.avg_time,
            times.max_time as query_duration,
            times.min_time,
            ral.relational_algebra as relational_algebra
        from (
            select query_id,
                max(log_time) as end_time,
                sum(duration)/count(duration) as avg_time,
                min(duration) as min_time,
                max(duration) as max_time
            from bsql_logs where info = 'Query Execution Done' group by query_id
        ) as times
        inner join (
            select query_id, substring(info, 13, 2000) as relational_algebra
            from bsql_logs where info like 'Query Start%' group by query_id,info
        ) as ral on times.query_id = ral.query_id order by times.end_time desc
    ) as temp group by relational_algebra
    '''
    print('#> Data execution times for frequent queries {}'.format(bc.log(query)))


def discover_totaltime_query_execution():
    """Summary

        This query determines the data load time and total time for all queries,
        showing the latest ones first.
        
        Load time and total time being the maximum load time and total time for any
        node.
    """
    global bc
    log_query = '''
    select max(end_time) as end_time, query_id,
           max(load_time) as load_time, max(total_time) as total_time
    from (
          select query_id, node_id, sum(case when info = 'evaluate_split_query load_data' then duration else 0 end) as load_time,
                                    sum(case when info = 'Query Execution Done' then duration else 0 end) as total_time,
                                    max(log_time) as end_time
          from bsql_logs where info = 'evaluate_split_query_load_data' or info = 'Query Execution Done'
                         group by node_id, query_id
    ) group by query_id order by end_time desc
    '''
    print('#> Data load times (DESC order): {}'.format(bc.log(log_query)))

 
if __name__ == "__main__":
    main()


