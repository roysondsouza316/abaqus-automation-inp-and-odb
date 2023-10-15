# Abaqus Batch Running
This repository contains a Python script for automating the batch execution of Abaqus input files. The script allows you to specify the number of CPUs to use and a range of job names to run concurrently. It also checks for the presence of .lck files to ensure that jobs are executed safely.

## Prerequisites
Before using the script, ensure you have the following prerequisites:

1. Abaqus installed and properly configured for running simulations.
2. A working knowledge of Abaqus and its job execution process.
## Usage
### Follow these steps to use the script:

Open your terminal or command prompt.

Navigate to the directory where the script is located using the cd command. For example:

```bash
cd /path/to/Abaqus_automation/Batch_running_of_inp_files/
```
In the script, set the following parameters as needed:

* abaqus_path: Specify the path to the Abaqus executable (e.g., C:/Apps/SIMULIA/Commands/abaqus.bat).
* cpus: Specify the number of CPUs to use for the job execution.
* start_job and end_job: Define the range of job names to run.
* job_name_base: Set the base name for your job names.
* extensions_to_remove: Specify file extensions to remove after job completion.
* Run the script using a Python environment that has access to Abaqus. You can execute it with the following command:

```bash
python batch_run.py
```

### Here's what the script does:

* It iterates through a range of job names and runs each job concurrently.

* Each job is executed using the specified number of CPUs in interactive mode.

* The script monitors the presence of .lck files in the current directory, waiting for them to be released before starting the next job.

* After all jobs are completed, it removes files with specific extensions (e.g., .dat, .com, .msg, etc.) to clean up the directory.

### Note
Please ensure that Abaqus is properly installed and configured on your system.

Review the script and adjust the parameters to match your specific Abaqus setup and requirements.

Be cautious when removing files with specific extensions, as this may delete important Abaqus output files.

This script is intended for batch running of Abaqus jobs. Ensure that your Abaqus input files are correctly prepared and named based on the job names specified in the script.

Always have backups of your data and use version control to track changes in your input files and scripts.

If you encounter any issues or errors, refer to the Abaqus documentation or seek assistance from Abaqus support resources.
