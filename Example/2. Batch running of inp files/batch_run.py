import os
import subprocess
import concurrent.futures
os.chdir('D:/Git_projects/Abaqus_automation/Batch running of inp files/')

# Specify the path to the Abaqus executable
abaqus_path = 'C:/Apps/SIMULIA/Commands/abaqus.bat'

# Specify the number of CPUs to use
cpus = 2

# Define the range of job names to run
start_job = 0
end_job = 5
job_name_base = "Model_"
job_names = [job_name_base + str(i) for i in range(start_job, end_job+1)]

# Define a function to run a single Abaqus job
def run_job(job_name):
    print(f"Starting job {job_name}...")
    # Construct the command to run the Abaqus analysis in interactive mode
    command = f'call abaqus job={job_name} interactive cpus={cpus}'

    try:
        result = subprocess.run(command, shell=True, capture_output=True, check=True)
        print(result.stdout.decode('utf-8'))
        print(f"Job {job_name} completed successfully.")
    except subprocess.CalledProcessError as e:
        print(e.stderr.decode('utf-8'))
        print(f"Job {job_name} failed.")

# Define a function to check for the presence of .lck files in the current directory
def check_lck_files():
    while True:
        lck_files = [f for f in os.listdir() if f.endswith('.lck')]
        if len(lck_files) > 0:
            print(f"Waiting for {len(lck_files)} .lck files to be released...")
            time.sleep(60)
        else:
            break
    print("All .lck files released, starting next job.")

# Create a list of jobs to run concurrently
concurrent_jobs = []
for job_name in job_names:
    concurrent_jobs.append((job_name,))

# Create a thread pool with a maximum of 3 threads
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    # Submit the jobs to the thread pool
    for job_args in concurrent_jobs:
        executor.submit(check_lck_files)
        executor.submit(run_job, *job_args)

print("All jobs completed.")  

# Remove files with certain extensions
extensions_to_remove = ['.dat', '.com', '.msg', '.prt', '.sim', '.sta']
for extension in extensions_to_remove:
    for filename in os.listdir():
        if filename.endswith(extension):
            os.remove(filename)

print('Program complete!')