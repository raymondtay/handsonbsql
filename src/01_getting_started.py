# CuDF is the CUDA binding to Apache Arrow for efficient Data Transportation
import cudf
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
        The main function defines a few things:
            (a) "bc" refers to the object that links to the CUDA installation
            (b) "df" refers to the DataFrame object where we will use to house the
            (k,v) pairs
    
        result:
        -------
          key  val
        0   a  7.6
        1   c  7.1
    
        notes:
        ------
           Note: BSQL runs on GPU Architectures that are Pascal or later (compute
           capability >= 6) ; this demo is run off the EC2 Tesla V100 GPUs (compute
           capability >= 7.5)
    """
    global bc
    df = cudf.DataFrame()
    df['key'] = ['a', 'b', 'c', 'd', 'e']
    df['val'] = [7.6, 2.9, 7.1, 1.6, 2.2]
    
    
    bc.create_table('game_1', df)
    
    bc.sql('SELECT * FROM game_1 WHERE val > 4')


if __name__ == "__main__":
    main()

