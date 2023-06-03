import pytest
import GUIController
import pandas as pd
import os

# Tests the export graph as PNG feature
def test_export_png(controller: GUIController):
    # Create a sample graph data
    graph_data = pd.DataFrame({'x': [1, 2, 3, 4, 5], 'y': [10, 20, 30, 40, 50]})

    # Set the graph data in the controller
    controller.set_graph_data(graph_data)

    # Export the graph as PNG
    exported_file_path = controller.export_graph_png('graph.png')

    # Assert that the exported file path is not empty
    assert exported_file_path != ''

    # Assert that the exported file path is valid and the file exists
    assert os.path.isfile(exported_file_path)

    # Assert that the exported file has the correct extension
    assert exported_file_path.endswith('.png')

