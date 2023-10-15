# Abaqus Automation
Part of this work has been utilized for the publication:

[_**Dsouza, Royson Donate, et al. "Mutual dependence of experimental and data analysis features in characterization of fiber‐matrix interface via microdroplets." Polymer Composites (2023).**_](https://4spepublications.onlinelibrary.wiley.com/doi/full/10.1002/pc.27649 "DOI")

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#Usage)

## Features

This GitLab repository contains Python scripts for automating various tasks related to Abaqus simulations. The provided scripts include:

1. [Input File Generation](https://gitlab.com/royson316/abaqus-automation-inp-and-odb/-/tree/main/1.%20Input%20file%20generation?ref_type=heads): Automatically generate Abaqus input files based on data from a CSV file.
2. [Batch Running of Input Files](https://gitlab.com/royson316/abaqus-automation-inp-and-odb/-/tree/main/2.%20Batch%20running%20of%20inp%20files?ref_type=heads): Automate the execution of Abaqus input files in parallel.
3. [Automation for Reading ODB Files](https://gitlab.com/royson316/abaqus-automation-inp-and-odb/-/tree/main/3.%20Automation%20for%20reading%20odb%20files?ref_type=heads): Automate the extraction of data from Abaqus ODB files for multiple models.
4. [Automation for Reading ODB Files](https://gitlab.com/royson316/abaqus-automation-inp-and-odb/-/tree/main/Example): An example file with the above three processes.

## Prerequisites

Before using the scripts, ensure you have the following prerequisites:

- Python environment (Python 3.x) with the following libraries installed:
  - Pandas
  - Abaqus libraries (Abaqus CAE, Abaqus Python scripting, etc.)
- Abaqus installed and properly configured for running simulations.

## Installation

1. Clone this GitLab repository to your local machine using the following command:

```bash
https://gitlab.com/royson316/abaqus-automation-inp-and-odb.git
```
2. Navigate to the repository directory:

```bash
cd abaqus-automation
```

3. Ensure that the Abaqus executable (`abaqus.bat`) is available and properly configured in your system's PATH.


## Usage
After completing the installation steps, you can use the Abaqus automation scripts as described in the individual sections of the README:

1. Input File Generation: Instructions for generating Abaqus input files.
2. Batch Running of Input Files: Guidance on running Abaqus jobs in batch mode.
3. Automation for Reading ODB Files: Instructions for automating data extraction from ODB files.
4. Example file.