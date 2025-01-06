import os

def read_jobs(file_path):
    """Reads jobs from the file and returns a list of (release, deadline, processing time) tuples."""
    with open(file_path, 'r') as f:
        n = int(f.readline().strip())
        jobs = []
        for _ in range(n):
            r_i, d_i, p_i = map(int, f.readline().strip().split())
            jobs.append((r_i, d_i, p_i))
    return jobs

def schedule_jobs(jobs):
    """
    Schedules jobs to minimize busy time.
    Each job's start time is determined within the constraints.
    """
    # Sort jobs by earliest deadline to prioritize jobs that need to complete sooner
    jobs.sort(key=lambda job: job[1])
    
    schedule = []  # List to store start times
    current_time = 0  # Track the machine's current time

    for r_i, d_i, p_i in jobs:
        # Ensure the start time respects release and current time
        s_i = max(r_i, current_time)  
        
        # Check if this start time allows the job to complete before its deadline
        if s_i + p_i <= d_i:
            schedule.append(s_i)
            current_time = s_i + p_i  # Update current time for the next job
        else:
            # If scheduling within constraints is impossible, output -1 (or handle differently as needed)
            schedule.append(-1)
            
    return schedule

def write_schedule(output_path, schedule):
    """Writes the schedule to the output file."""
    with open(output_path, 'w') as f:
        for start_time in schedule:
            f.write(f"{start_time}\n")

def main():
    """Processes multiple instances from input files and writes schedules to output files."""
    for i in range(1, 100):
        input_file = f"instance{i:02}.txt"
        output_file = f"solution{i:02}.txt"

        if os.path.exists(input_file):
            jobs = read_jobs(input_file)
            schedule = schedule_jobs(jobs)
            write_schedule(output_file, schedule)
            print(f"Processed {input_file} -> {output_file}")
        else:
            print(f"{input_file} does not exist. Skipping.")

if __name__ == "__main__":
    main()
