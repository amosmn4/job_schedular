import os

def read_instance(file_path):
    with open(file_path, 'r') as file:
        n = int(file.readline().strip())
        jobs = []
        for _ in range(n):
            r, d, p = map(int, file.readline().strip().split())
            jobs.append((r, d, p))
    return jobs

def write_solution(file_path, start_times):
    with open(file_path, 'w') as file:
        for start_time in start_times:
            file.write(f"{start_time}\n")

def schedule_jobs(jobs):
    # Sort jobs by deadline for efficient processing
    jobs = sorted(jobs, key=lambda x: x[1])
    n = len(jobs)
    start_times = [0] * n

    # Implement the DP approach or greedy interval management
    # (simplified pseudo code here, you'll need to translate theorem details)

    # Initialize intervals and busy time tracking
    intervals = []
    busy_time = 0

    for i, (r, d, p) in enumerate(jobs):
        # Determine the optimal start time for the job
        # Start time is typically the latest between release and current time available
        s_i = max(r, busy_time)
        start_times[i] = s_i

        # Update the busy time and manage intervals
        busy_time = max(busy_time, s_i + p)
        intervals.append((s_i, s_i + p))
    
    # Minimize the busy time from overlapping intervals
    # Combine intervals and calculate total time on

    return start_times

def main():
    for i in range(1, 100):
        file_num = str(i).zfill(2)
        instance_file = f"instance{file_num}.txt"
        solution_file = f"solution{file_num}.txt"
        
        if not os.path.exists(instance_file):
            continue
        
        jobs = read_instance(instance_file)
        start_times = schedule_jobs(jobs)
        write_solution(solution_file, start_times)

if __name__ == "__main__":
    main()
