"""A dummy file to test the CI/CD template."""

import numpy.typing as npt
from scipy.sparse import csr_matrix, spmatrix


def dense_to_sparse(matrix: npt.NDArray) -> spmatrix:
    """Convert a dense matrix to a sparse matrix.

    Parameters
    ----------
    matrix : npt.NDArray
        A dense matrix.

    Returns
    -------
    spmatrix
        A sparse matrix.
    """
    return csr_matrix(matrix)
