# Job Scheduling Program

## Overview
This program is designed to schedule jobs optimally while adhering to given constraints of release time, processing time, and deadlines. The program uses a priority-based scheduling algorithm to minimize unscheduled jobs (`-1` start times) and ensures efficient use of time.

## Features
- Reads job data from input files.
- Schedules jobs to minimize the number of unscheduled tasks.
- Writes the schedule (start times) to output files.
- Handles multiple instances automatically.
- Implements a greedy algorithm with deadline prioritization and dynamic replacement of less efficient schedules.

---

## Input and Output Format

### Input File Format
Each input file contains:
1. **First Line**: The number of jobs (`n`).
2. **Subsequent Lines**: Three integers for each job:
   - **Release Time (`r`)**: The earliest time a job can start.
   - **Deadline (`d`)**: The latest time by which the job must be completed.
   - **Processing Time (`p`)**: The time required to complete the job.

**Example Input File:**
```
5
1 9 3
1 2 1
4 8 2
2 7 2
5 9 6
```

### Output File Format
Each output file contains one integer per line, representing the start time of each job. If a job cannot be scheduled, its start time is `-1`.

**Example Output File:**
```
1
1
4
2
5
```

---

## How to Run

### Prerequisites
- Python 3.x installed on your system.
- Input files (e.g., `instance00.txt`, `instance01.txt`) placed in the current directory.

### Steps
1. Save the script (`busy_time_scheduler.py`) in the same directory as the input files.
2. Run the script:
   ```
   python busy_time_scheduler.py
   ```
3. Output files (e.g., `solution00.txt`, `solution01.txt`) will be generated in the same directory.

---

## Program Structure

### Functions

#### `read_jobs(file_path)`
- Reads job details from an input file.
- Returns a list of jobs as namedtuples.

#### `write_solution(file_path, start_times)`
- Writes the computed start times to an output file.

#### `busy_time_scheduler(jobs)`
- Schedules jobs to minimize unscheduled tasks.
- Implements a greedy algorithm with deadline prioritization.
- Returns a list of start times.

#### `main()`
- Iterates through input files (`instance00.txt` to `instance99.txt`).
- Reads job data, schedules tasks, and writes solutions.

---

## Example Execution
Given the input file `instance00.txt`:
```
5
1 9 3
1 2 1
4 8 2
2 7 2
5 9 6
```
The program will generate the output file `solution00.txt`:
```
1
1
4
2
5
```

---

## Key Scheduling Rules
1. Jobs with tighter deadlines are prioritized.
2. Jobs are scheduled starting from their release time if possible.
3. If a job cannot be scheduled within its constraints, it is marked as `-1`.
4. Less efficient jobs may be unscheduled to accommodate better fits.

---

## File Structure
- `busy_time_scheduler.py`: The main script.
- `instanceXX.txt`: Input files containing job data.
- `solutionXX.txt`: Output files containing the scheduled start times.

---

## Customization
- **Input Directory**: Modify the `input_directory` variable in the `main()` function to change where input files are read from.
- **Output Directory**: Modify the `output_directory` variable in the `main()` function to change where output files are written.

---

## Troubleshooting
1. **No Output Files Generated**:
   - Ensure the input files are named correctly (e.g., `instance00.txt`).
   - Verify that the script is running in the correct directory.

2. **Incorrect Scheduling**:
   - Ensure the input file format matches the expected format.
   - Debug using smaller input instances.

---

## License
This program is open-source and can be modified for academic or personal use.

## Author
Name: Amos Nyamai.
Github: https://github.com/amosmn4


