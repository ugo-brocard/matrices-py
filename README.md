## Matrices.py
matrices-py is a python module to:
- [x] Add matrices
- [x] Subtract matrices
- [x] Multiply matrices either by a scalar or another matrix
- [x] Transpose a matrix

and other things will come soon...

It works with python 3.12 or later

***

## 🔧 Installation

It should work on any python3 version after the 1.10 but it's always good to have the latest version since it will be the one I'm sure it works on :)

### ⚙ Using PyPi

``` bash
$ pip install matrices-py
```

## 📚 Usage

### 📄 Matrix definition
```py
from matrices import Matrix

# Create a basic Matrix object
matrix = Matrix([
    [1, 5, 3],
    [5, 3, 1],
    [3, 1, 5],
])

# How to get the matrix back ?
print(matrix.matrix)     # Output: [[1, 5, 3], [5, 3, 1], [3, 1, 5]]

# How many columns ?
print(matrix.columns)    # Output: 3

# How many rows ?
print(matrix.rows)       # Output: 3

# How to get the size as a string ?
print(matrix.size)       # Output: (3x3)
```

### 🧮 Matrix operations

#### Addition
```py
from matrices import Matrix

a = Matrix([
    [1, 5, 3],
    [5, 9, 1],
    [7, 1, 5],
])

b = Matrix([
    [2, 8, 1],
    [3, 9, 0],
    [1, 8, 7],
])

c = Matrix([
    [1, 5, 3]
])

# How to add two matrices
matrix = a + b
print(matrix.matrix)     # Output: [[3, 13, 4], [8, 18, 1], [8, 9, 12]]

# What append if the second matrix isn't valid ?
matrix = a + c           # Exception: Matrices should be the same size ((3x3) != (1x3))
```

#### Subtraction
```py
from matrices import Matrix

a = Matrix([
    [1, 5, 3],
    [5, 9, 1],
    [7, 1, 5],
])

b = Matrix([
    [2, 8, 1],
    [3, 9, 0],
    [1, 8, 7],
])

c = Matrix([
    [1, 5, 3]
])

# How to add two matrices
matrix = a - b
print(matrix.matrix)     # Output: [[-1, -3, 2], [2, 0, 1], [6, -7, -2]]

# What append if the second matrix isn't valid ?
matrix = a + c           # Exception: Matrices should be the same size ((3x3) != (1x3))
```

#### Multiplication (scalar)
```py
from matrices import Matrix

matrix = Matrix([
    [1, 5, 3],
    [5, 3, 1],
    [3, 1, 5],
])

scalar = 2

# How to multiply a matrix by a scalar ?
matrix *= scalar
print(matrix.matrix)     # Output: [[2, 10, 6], [10, 6, 2], [6, 2, 10]]
```

#### Multiplication (matrices)
```py
from matrices import Matrix

a = Matrix([
    [1, 5, 3],
    [5, 9, 1],
    [7, 1, 5],
])

b = Matrix([
    [2],
    [3],
    [1],
])

c = Matrix([
    [2, 3, 1]
])

# How to multiply two matrices ?
matrix = a @ b
print(matrix.matrix)     # Output: [[20], [38], [22]]

# What append if the second matrix isn't valid ?
matrix = a @ c           # Exception: Matrix a should have a columns number equals to the matrix b rows number (3 != 1)
```

#### Transpose
```py
from matrices import Matrix

matrix = Matrix([
    [1, 5, 3],
    [5, 9, 1],
    [7, 1, 5],
])

transposed = matrix.transpose()
print(transposed.matrix) # Output: [[1, 5, 7], [5, 9, 1], [3, 1, 5]]
```

## 🍕 Contributing
All contribution are welcomed so consider looking at the source code on [GitHub](https://github.com/ugo-brocard/matrices-py)

## 🛡 License

This project is licensed under the [MIT License](https://github.com/ugo-brocard/matrices-py/blob/main/LICENSE)
