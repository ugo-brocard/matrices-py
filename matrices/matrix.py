from typing      import Self
from dataclasses import dataclass

@dataclass(frozen=True)
class Matrix:
    matrix: list
    
    @property
    def rows(self) -> int:
        return len(self.matrix)
    
    @property
    def columns(self) -> int:
        return len(self.matrix[0])
    
    @property
    def size(self) -> str:
        return f"({self.rows}x{self.columns})"
    
    def transpose(self) -> Self:
        matrix = [[self.matrix[j][i] for j in range(self.rows)] for i in range(self.columns)]
        return Matrix(matrix)
    
    # MAGIC METHODS
    def __post_init__(self) -> None:
        for row in self.matrix:
            if len(row) == self.columns:
                continue
            
            raise Exception(f"Matrices rows should always be the same length ({len(row)} != {self.columns})")
        
    # - OPERATIONS
    def __add__(self, other: Self) -> Self:
        if self.size != other.size:
            raise Exception(f"Matrices should be the same size ({self.size} != {other.size})")
        
        matrix = [[self.matrix[i][j] + other.matrix[i][j] for j in range(self.columns)] for i in range(self.rows)]
        return Matrix(matrix)

    def __sub__(self, other: Self) -> Self:
        return self + (other * -1)
    
    def __mul__(self, scalar: int) -> Self:
        matrix = [[self.matrix[i][j] * scalar for j in range(self.columns)] for i in range(self.rows)]
        return Matrix(matrix)
    
    def __matmul__(self, other: Self) -> Self:
        if self.columns != other.rows:
            raise Exception(f"Matrix a should have a columns number equals to the matrix b rows number ({self.columns} != {other.rows})")

        matrix = matrix = self.rows*[self.columns*[0]]
        for i in range(self.rows):
            for j in range(other.columns):
                cell = 0
                
                for k in range(self.columns):
                    cell += self.matrix[i][k] * other.matrix[k][j]
                
                matrix[i][j] = cell
        
        return Matrix(matrix)