import pandas as pd
def test_dataframe_creation():
    data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    df = pd.DataFrame(data)
    assert df.shape == (3, 2)
    assert list(df.columns) == ['A', 'B']
    assert df['A'].tolist() == [1, 2, 3]
    assert df['B'].tolist() == [4, 5, 6]
    print("DataFrame creation test passed.")

def add_numbers(a, b):
    return a + b

def test_add_numbers():
    """Test for the add_numbers function."""
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0
    print("Addition test passed.")

if __name__ == "__main__":
    test_dataframe_creation()
    test_add_numbers()
    print("All tests passed.")