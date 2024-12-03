import os
import sys

# Directory where the SCSS files are located
directory = "../"

# Output file
output_file = "compiler_scss2css.sh"

print('\nYou are will compile the next scss to css')
print(f'Directory Path:\n {os.listdir(directory)}')

# Open the output file in write mode
with open(output_file, "w") as f:
    # Write the header to the output file
    f.write("#!/bin/bash\n")
    f.write("# Receive Directory data SCSS to CSS\n")

    # Iterate through all files in the directory
    for file in os.listdir(directory):
        # Check if the file has a .scss extension
        if file.endswith(".scss"):
            # Create the corresponding command line
            # Remove the leading dot and construct the command in the new format
            scss_file = f"{directory}{file}"  # Format the path to match 'scss/main.scss'
            output_name = file.replace(".scss", ".css")
            # Write the command to the output file in the desired format
            a = f'sass "{scss_file}" "{directory}{directory}{output_name}"'
            f.write(f"echo 'Compilando {a}'\n")
            f.write(f'{a}\n')

print(f"\nFile '{output_file}' generated successfully.")
print('Wait 4 seconds ...\n')
sys.exit()