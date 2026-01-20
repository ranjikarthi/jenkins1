from app import group_data
import os

def test_group_data_basic():
    categories = ["A", "B", "A"]
    values = [10, 20, 5]

    result = group_data(categories, values)

    assert result["A"] == 15
    assert result["B"] == 20

def test_group_data_empty():
    result = group_data([], [])
    assert result == {}

def test_output_file_creation():
    # Simulate plotting result
    from app import plot_grouped_data
    data = {"A": 10, "B": 20}

    plot_grouped_data(data)

    assert os.path.exists("output.png")
