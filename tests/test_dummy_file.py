"""Test for the dummy file."""

import unittest

import numpy as np
from scipy.sparse import issparse

from package_src.dummy_file import dense_to_sparse


class TestDummyFile(unittest.TestCase):
    """Tester for the dummy file."""

    def test_dense_to_sparse(self):
        """Test the dense_to_sparse function."""

        matrix = np.array([[1, 0, 0], [0, 0, 1]])
        sparse_matrix = dense_to_sparse(matrix)
        self.assertTrue(issparse(sparse_matrix))
        self.assertTrue((sparse_matrix.toarray() == matrix).all())
