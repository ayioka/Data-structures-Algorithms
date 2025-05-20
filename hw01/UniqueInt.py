import time
import tracemalloc

class UniqueInt:
    def __init__(self):
        """
       adds a boolean array to the UniqueInt object's initialization in order to monitor seen integers.
        """
        self.seen = [False] * 2047  # Tracking integers from -1023 to 1023 using an array

    def readNextItemFromFile(self, inputFileStream):
        """
      skips over invalid lines and reads the subsequent integer item from the input file stream.

        Args: inputFileStream (file object): The stream of input files.

        Returns: int or None: If the file's end is reached, return None. Otherwise, return the next valid integer from the file..
        """
        while True:
            line = inputFileStream.readline()
            if not line:
                return None
            line = line.strip()
            if line:  # Ignore blank lines
                try:
                    integer = int(line)
                    return integer
                except ValueError:
                    continue  # Skip lines that don't have a legitimate integer on them.

class UniqueInt:
    def processFile(self, input_file_path, output_file_path):
        with open(input_file_path, 'r') as input_file:
            # Process the contents of the file here.
            pass
        # Put the result in output_file_path.

    def processFiles(self, input_file_paths, output_file_paths):
        for input_file_path, output_file_path in zip(input_file_paths, output_file_paths):
            self.processFile(input_file_path, output_file_path)

    def processFiles(self, inputFilePaths, outputFilePaths):
       
        unique_integers = []

        # Begin tracking your time and memory usage.
        start_time = time.time()
        tracemalloc.start()

       # Use a custom bubble sort to sort unique integers.
        sorted_unique_integers = self.bubble_sort(unique_integers)

        # Write the output file with the sorted unique integers.
        '''with open(outputFilePaths,'w') as output_file:
            for integer in sorted_unique_integers:
                output_file.write(f"{integer}\n")'''


    def processFiles(self, input_file_paths, output_file_paths):
        for input_file_path, output_file_path in zip(input_file_paths, output_file_paths):
            self.processFile(input_file_path, output_file_path)

            # Open the output file for writing
            with open(output_file_path, 'w') as output_file:
                # Write output to the output file
                pass  # You need to implement this part

        # Stop measuring time and memory usage
        end_time = time.time()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        start_time = time.time()

        # Print the runtime and peak memory usage
        print(f"Runtime: {end_time - start_time:.6f} seconds")
        print(f"Memory usage: {peak / 10**6:.6f} MB")

    def bubble_sort(self, arr):
        """
       uses the bubble sort method to arrange an array of numbers in ascending order.

        Args: arr (list of int): The list of integers to be sorted in the input.

        Returns: list of int: The integer list that has been sorted.
        """
        r = len(arr)
        for a in range(r):
            for w in range(0, r - a - 1):
                if arr[a] > arr[a + 1]:
                    arr[a], arr[a + 1] = arr[a + 1], arr[a]
        return arr

# Example usage
if __name__ == "__main__":
    unique_int_processor = UniqueInt()
    input_file_paths = [
    "sample_inputs/small_sample_input_01.txt",
    "sample_inputs/small_sample_input_02.txt",
    "sample_inputs/small_sample_input_03.txt",
    "sample_inputs/small_sample_input_04.txt"
    # Add more file paths as needed
]

    output_file_paths= [
            "sample_results/small_sample_results_01.txt",
            "sample_results/small_sample_results_02.txt",
            "sample_results/small_sample_results_03.txt",
            "sample_results/small_sample_results_04.txt",                                                                   
            ]
    unique_int_processor.processFiles(input_file_paths, output_file_paths)

