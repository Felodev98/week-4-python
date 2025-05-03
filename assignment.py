def modify_and_write_file(input_filename, output_filename):
    """
    Reads an input file, modifies each line, and writes the modified content to a new file.

    Args:
        input_filename (str): The name of the file to read from.
        output_filename (str): The name of the file to write to.
    """
    try:
        with open(input_filename, 'r') as infile:
            with open(output_filename, 'w') as outfile:
                for line in infile:
                    # Simple modification: Add " [MODIFIED]" to each line
                    modified_line = line.strip() + " [MODIFIED]\n"
                    outfile.write(modified_line)
        print(f"Successfully read '{input_filename}', modified it, and wrote to '{output_filename}'. 🎉")

    except FileNotFoundError:
        print(f"Error: The input file '{input_filename}' was not found. 🧪")
    except IOError:
        print(f"Error: Could not read from '{input_filename}' or write to '{output_filename}'. Please check file permissions. 🧪")

if __name__ == "__main__":
    while True:
        input_file = input("Enter the name of the file you want to process: ")
        output_file = input("Enter the name for the new output file: ")

        modify_and_write_file(input_file, output_file)

        another_operation = input("Do you want to process another file? (yes/no): ").lower()
        if another_operation != 'yes':
            break

    print("\nFile processing complete! You're becoming a file handling pro! 🎉")