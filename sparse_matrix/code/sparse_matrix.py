import os
import sys

class SparseMatrix:
    """
    SparseMatrix represents a sparse matrix and provides methods for
    addition, subtraction, multiplication, and file I/O operations.
    """

    def __init__(self, file_path=None, num_rows=None, num_cols=None):
        """
        Initializes a SparseMatrix object.
        
        Either file_path or both num_rows and num_cols must be provided.
        
        Args:
            file_path (str): Path to the file containing matrix data.
            num_rows (int): Number of rows in the matrix.
            num_cols (int): Number of columns in the matrix.
        """
        self.elements = {}
        if file_path:
            self._load_from_file(file_path)
        elif num_rows is not None and num_cols is not None:
            self.rows = num_rows
            self.cols = num_cols
        else:
            raise ValueError("Either file_path or num_rows and num_cols must be provided")
    
    def _load_from_file(self, file_path):
        """
        Loads matrix data from a file.
        
        Args:
            file_path (str): Path to the file containing matrix data.
        
        Raises:
            FileNotFoundError: If the file does not exist.
            ValueError: If the file format is incorrect.
        """
        print(f"Loading file: {file_path}")
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        with open(file_path, 'r') as f:
            lines = [line.strip() for line in f if line.strip()]
            self.rows = int(lines[0].split('=')[1])
            self.cols = int(lines[1].split('=')[1])
            for line in lines[2:]:
                self._parse_and_set_element(line)
    
    def _parse_and_set_element(self, line):
        """
        Parses a line from the file and sets the matrix element.
        
        Args:
            line (str): A line from the matrix file.
        
        Raises:
            ValueError: If the line format is incorrect.
        """
        if line[0] != '(' or line[-1] != ')':
            raise ValueError("Input file has wrong format")
        try:
            row, col, value = map(int, line[1:-1].split(','))
            self.set_element(row, col, value)
        except Exception as e:
            raise ValueError("Input file has wrong format") from e
    
    def get_element(self, row, col):
        """
        Returns the value of the element at the specified position.
        
        Args:
            row (int): Row index.
            col (int): Column index.
        
        Returns:
            int: Value at the specified position, or 0 if not set.
        """
        return self.elements.get((row, col), 0)
    
    def set_element(self, row, col, value):
        """
        Sets the value of the element at the specified position.
        
        Args:
            row (int): Row index.
            col (int): Column index.
            value (int): Value to set.
        """
        if value != 0:
            self.elements[(row, col)] = value
        elif (row, col) in self.elements:
            del self.elements[(row, col)]
    
    def __add__(self, other):
        """
        Adds two sparse matrices.
        
        Args:
            other (SparseMatrix): The matrix to add.
        
        Returns:
            SparseMatrix: The result of the addition.
        
        Raises:
            ValueError: If the matrices have different dimensions.
        """
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices dimensions do not match for addition")
        result = SparseMatrix(num_rows=self.rows, num_cols=self.cols)
        for (row, col), value in self.elements.items():
            result.set_element(row, col, value + other.get_element(row, col))
        for (row, col), value in other.elements.items():
            if (row, col) not in self.elements:
                result.set_element(row, col, value)
        return result

    def __sub__(self, other):
        """
        Subtracts another sparse matrix from this matrix.
        
        Args:
            other (SparseMatrix): The matrix to subtract.
        
        Returns:
            SparseMatrix: The result of the subtraction.
        
        Raises:
            ValueError: If the matrices have different dimensions.
        """
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices dimensions do not match for subtraction")
        result = SparseMatrix(num_rows=self.rows, num_cols=self.cols)
        for (row, col), value in self.elements.items():
            result.set_element(row, col, value - other.get_element(row, col))
        for (row, col), value in other.elements.items():
            if (row, col) not in self.elements:
                result.set_element(row, col, -value)
        return result

    def __mul__(self, other):
        """
        Multiplies two sparse matrices.
        
        Args:
            other (SparseMatrix): The matrix to multiply with.
        
        Returns:
            SparseMatrix: The result of the multiplication.
        
        Raises:
            ValueError: If the matrices cannot be multiplied (dimension mismatch).
        """
        if self.cols != other.rows:
            raise ValueError("Matrices dimensions do not match for multiplication")
        result = SparseMatrix(num_rows=self.rows, num_cols=other.cols)
        for (row, col), value in self.elements.items():
            for k in range(other.cols):
                result.set_element(row, k, result.get_element(row, k) + value * other.get_element(col, k))
        return result
    
    def to_file(self, file_path):
        """
        Writes the matrix to a file.
        
        Args:
            file_path (str): Path to the output file.
        """
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as f:
            f.write(f"rows={self.rows}\n")
            f.write(f"cols={self.cols}\n")
            for (row, col), value in self.elements.items():
                f.write(f"({row}, {col}, {value})\n")

    def __str__(self):
        """
        Returns a string representation of the matrix.
        
        Returns:
            str: The string representation of the matrix.
        """
        elements_str = '\n'.join([f"({row}, {col}, {value})" for (row, col), value in self.elements.items()])
        return f"rows={self.rows}\ncols={self.cols}\n{elements_str}"

def process_files(input_file_paths, output_file_path, operation):
    """
    Processes two input files, performs the specified matrix operation,
    and writes the result to an output file.
    
    Args:
        input_file_paths (list of str): Paths to the two input files.
        output_file_path (str): Path to the output file.
        operation (str): The operation to perform ('1' for addition, '2' for subtraction, '3' for multiplication).
    
    Raises:
        ValueError: If the number of input files is not exactly two.
        ValueError: If the operation is invalid.
    """
    if len(input_file_paths) != 2:
        raise ValueError("There must be exactly two input files for the operation.")
    
    print(f"Processing files: {input_file_paths}")
    matrix1 = SparseMatrix(file_path=input_file_paths[0])
    matrix2 = SparseMatrix(file_path=input_file_paths[1])
    
    if operation == '1':
        result = matrix1 + matrix2
    elif operation == '2':
        result = matrix1 - matrix2
    elif operation == '3':
        result = matrix1 * matrix2
    else:
        raise ValueError("Invalid operation")

    result.to_file(output_file_path)
    print(f"Result written to {output_file_path}")

if __name__ == "__main__":
    # Organize paths according to instructions
    input_file_paths = [
        ("../sample_inputs/easy_sample_01_1.txt", "../sample_inputs/easy_sample_01_2.txt"),
        ("../sample_inputs/easy_sample_02_1.txt", "../sample_inputs/easy_sample_02_2.txt"),
        ("../sample_inputs/easy_sample_03_1.txt", "../sample_inputs/easy_sample_03_2.txt"),
        ("../sample_inputs/easy_sample_04_1.txt", "../sample_inputs/easy_sample_04_2.txt")
    ]

    output_file_paths = [
        "../sample_results/easy_sample_results_01.txt",
        "../sample_results/easy_sample_results_02.txt",
        "../sample_results/easy_sample_results_03.txt",
        "../sample_results/easy_sample_results_04.txt"
    ]

    if len(sys.argv) != 2:
        print("Usage: python script.py <operation>")
        print("Select operation: 1 for addition, 2 for subtraction, 3 for multiplication")
        sys.exit(1)

    operation = sys.argv[1]

    for input_pair, output_path in zip(input_file_paths, output_file_paths):
        process_files(input_pair, output_path, operation)
