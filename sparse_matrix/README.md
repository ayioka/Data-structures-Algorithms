Sparse Matrix Operations Overview This project provides an implementation of sparse matrix operations, including addition, subtraction, and multiplication, using a custom data structure for efficient storage and computation. The matrices are loaded from input files in a specific format, and the operations are performed based on user input.

Directory Structure / Data-structures-Algorithms/sparse_matrix/ ├── code/ │ └── src/ │ └── sparse_matrix.py └── sample_inputs/ ├── matrix1.txt └── matrix2.txt

python

Input File Format Each sparse matrix is stored in a text file with the following format:

rows=NUMBER_OF_ROWS cols=NUMBER_OF_COLUMNS (ROW_INDEX, COLUMN_INDEX, VALUE) ...

mathematica

For example:

rows=8433 cols=3180 (0, 381, -694) (0, 128, -838) (0, 639, 857) (0, 165, -933) (0, 1350, -89)

Usage Place Input Files: Place your input files in the sample_inputs directory.

Run the Code: Execute the script sparse_matrix.py located in the code/src directory.

Follow Prompts: The program will prompt you to enter the paths to two matrix files and the desired operation (add, subtract, multiply).

Example $ cd /dsa/sparse_matrix/code/src/ $ python3 sparse_matrix.py Enter path to the first matrix file: ../../sample_inputs/matrix1.txt Enter path to the second matrix file: ../../sample_inputs/matrix2.txt Enter operation (add/subtract/multiply): add Result: ... # Matrix result printed here

Code Explanation SparseMatrix Class Initialization: Initialize with given number of rows and columns.

Set Element: set_element(row, col, value) sets the value at the specified position.

Get Element: get_element(row, col) retrieves the value at the specified position.

Addition: add(other) adds two sparse matrices.

Subtraction: subtract(other) subtracts the second sparse matrix from the first.

Multiplication: multiply(other) multiplies two sparse matrices.

read_sparse_matrix Function

Reads a sparse matrix from a file and returns a SparseMatrix object.

Main Function Prompts the user for file paths and desired operation. Loads the matrices from the files. Performs the requested operation and prints the result.

Error Handling Handles invalid file formats with appropriate error messages. Ensures matrix dimensions are compatible for the requested operations.

Dependencies This implementation uses only standard Python libraries.

Notes The implementation does not use built-in libraries for matrix operations to ensure custom handling of sparse matrices. Ensure that input files are correctly formatted to avoid errors.

License This project is licensed under the MIT License.

This README.md provides a comprehensive guide to the project, covering the directory structure, input file format, usage instructions, code explanation, error handling, dependencies, and licensing information.
