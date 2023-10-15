# Abaqus Input File Generation

This repository contains a Python script for automating the generation of Abaqus input files based on data from a CSV file. The script reads material properties (E1 and E2) from a CSV file (`data.csv`) and inserts them into an Abaqus input file (`master_file.inp`). Multiple input files are generated with varying material properties.

## Prerequisites

Before using the script, ensure you have the following prerequisites:

- Python environment with the necessary libraries (e.g., Pandas).
- Abaqus installed and properly configured for running simulations.

## Usage

Follow these steps to use the script:

1. Place the `data.csv` file containing material properties in the same directory as the script.

2. Make sure the Abaqus input file `master_file.inp` is also in the same directory.

3. Run the script using a Python environment that meets the prerequisites mentioned earlier.

Here's a breakdown of what the script does:

- It reads the `data.csv` file using Pandas to obtain material properties.

- It loops through a range of indices (in this case, `i_values` ranging from 0 to 5) and assigns values to `E1` and `E2` based on the CSV data.

- It opens the `master_file.inp` and searches for the string "Material-1" and the following line containing "*Elastic" (case-sensitive).

- After locating the correct line, it replaces the line after "*Elastic" with the new material property values.

- It constructs output filenames based on the `i_values` variable and writes modified data to new input files (e.g., `model_0.inp`, `model_1.inp`, ...).

## CSV Data Format

The `data.csv` file should follow a specific format, where each line represents material properties:


