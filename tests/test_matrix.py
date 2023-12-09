import sys
import unittest

sys.path.append("../matrices")

from matrices import Matrix

class TestMatrix(unittest.TestCase):
    def test_invalid_matrix_definition(self):
        with self.assertRaises(Exception) as exception:
            Matrix([[10, 2], [2]])
            
        self.assertEqual(str(exception.exception), "Matrices rows should always be the same length (1 != 2)")
    
    # Operations
    # - Addition
    def test_matrices_addition(self):
        a = Matrix([[21, 10], [96, 100]])
        b = Matrix([[34, 92], [47, 26]])
        
        matrix = a + b
        self.assertListEqual(matrix.matrix, [[55, 102], [143, 126]], "Should be [[55, 102], [143, 126]]")
        
    def test_invalid_matrices_addition(self):
        a = Matrix([[21], [100]])
        b = Matrix([[34, 92], [47, 26]])
        
        with self.assertRaises(Exception) as exception:
            a + b
            
        self.assertEqual(str(exception.exception), "Matrices should be the same size ((2x1) != (2x2))")
    
    # - Subtraction
    def test_matrices_subtraction(self):
        a = Matrix([[38, 57], [84, 82]])
        b = Matrix([[74, 51], [57, 4]])
        
        matrix = a - b
        self.assertListEqual(matrix.matrix, [[-36, 6], [27, 78]], "Should be [[-36, 6], [27, 78]]")
    
    def test_invalid_matrices_subtraction(self):
        a = Matrix([[38], [82]])
        b = Matrix([[74, 51], [57, 4]])
        
        with self.assertRaises(Exception) as exception:
            a - b
            
        self.assertEqual(str(exception.exception), "Matrices should be the same size ((2x1) != (2x2))")
    
    # - Multiplication
    # --> Scalar
    def test_matrix_scalar_multiplication(self):
        matrix = Matrix([[80, 89], [49, 32]])
        matrix *= 2
        
        self.assertListEqual(matrix.matrix, [[160, 178], [98, 64]], "Should be [[160, 178], [98, 64]]")
        
    # --> Matrices
    def test_matrices_multiplication(self):
        a = Matrix([[24, 98, 18]])
        b = Matrix([[80, 42, 23], [64, 25, 61], [73, 65, 61]])
        
        matrix = a @ b
        self.assertListEqual(matrix.matrix, [[9506, 4628, 7628]], "Should be [[9506, 4628, 7628]]")
        
    def test_invalid_matrices_multiplication(self):
        a = Matrix([[24, 98, 18]])
        b = Matrix([[80, 42, 23], [64, 25, 61], [73, 65, 61]])
        
        with self.assertRaises(Exception) as exception:
            b @ a
            
        self.assertEqual(str(exception.exception), "Matrix a should have a columns number equals to the matrix b rows number (3 != 1)")
    
    # - Transpose
    def test_transpose_matrix(self):
        matrix = Matrix([[60, 86], [2, 20], [80, 60]]).transpose()
        self.assertListEqual(matrix.matrix, [[60, 2, 80], [86, 20, 60]], "Should be [[60, 2, 80], [86, 20, 60]]")
        
    def test_transpose_row_vector(self):
        matrix = Matrix([[7, 90, 56]]).transpose()
        self.assertListEqual(matrix.matrix, [[7], [90], [56]], "Should be [[10], [12], [13]]")
        
    def test_transpose_column_vector(self):
        matrix = Matrix([[1], [59], [69]]).transpose()
        self.assertListEqual(matrix.matrix, [[1, 59, 69]], "Should be [[1, 59, 69]]")
        
    def test_transpose_square_matrix(self):
        matrix = Matrix([[2, 67, 77], [29, 33, 50], [43, 58, 69]]).transpose()
        self.assertListEqual(matrix.matrix, [[2, 29, 43], [67, 33, 58], [77, 50, 69]], "Should be [[2, 28, 43], [67, 33, 58], [77, 50, 69]]")
