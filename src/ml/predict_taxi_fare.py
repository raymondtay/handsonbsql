# See the README.md if you wish to play with the CUDA Machine Learning library

from blazingsql import BlazingContext
bc = BlazingContext()

def initialize():
    """Summary of initialize
       basically create a table on the GPU by using the dataset(in parquet
       format)
    """
    global bc
    bc.s3('blazingsql-colab', bucket_name='blazingsql-colab')
    bc.create_table('taxi','s3://blazingsql-colab/yellow_taxi/1_0_0.parquet')

def prepare_n_score():
    from cuml import LinearRegression
    from cuml.preprocessing.model_selection import train_test_split
    from sklearn.metrics import r2_score

    X = bc.sql('SELECT trip_distance, tolls_amount FROM taxi')
    y = bc.sql('SELECT fare_amount FROM taxi')['fare_amount']
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8)

    # Call linear regression model
    lr = LinearRegression()

    # Train the model
    lr.fit(X_train, y_train)
    
    # Make predictions for the X_test dataset
    y_pred = lr.predict(X_test)

    # Print the predicted values
    print('#> Predicted values: {}'.format(y_pred.to_pandas()))

    print('#> Scoring the model: {}'.format(r2_score(y_true=y_test.to_pandas(), y_pred=y_pred.to_pandas())))

def main():
    """Summary of main:
        This ML program is a "getting started" approach and you need the
        scikit-learn and scipy packages before you can run it.

        Its a pretty standard ML LR (linear regression) to predict the taxi
        fares based on the dataset.

        results:
        ----------
        
        (bsql) ubuntu@ip-10-0-0-33$ python ./predict_taxi_fare.py
        listening: tcp://*:30585
        BlazingContext ready
        #> Predicted values:
        0           6.898416
        1          22.000317
        2          27.852303
        3           8.516476
        4           5.981514
                     ...
        3765362    11.698662
        3765363     7.437769
        3765364    37.803375
        3765365    17.955164
        3765366     7.087189
        Length: 3765367, dtype: float32
        #> Scoring the model: 0.0026912197331891985
    """
    initialize()
    prepare_n_score()
    
if __name__ == "__main__":
    main()


