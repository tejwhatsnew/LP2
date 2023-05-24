def job_scheduling():
    num_jobs = int(input("Enter the number of jobs: "))

    # Initialize the jobs list
    jobs = []

    # Get the job details from the user
    for i in range(num_jobs):
        job_name = input(f"Enter the name of job {i+1}: ")
        start_time = int(input(f"Enter the start time of job {i+1}: "))
        end_time = int(input(f"Enter the end time of job {i+1}: "))
        profit = int(input(f"Enter the profit of job {i+1}: "))
        jobs.append((job_name, start_time, end_time, profit))

    # Sort the jobs in descending order of their profits
    jobs.sort(key=lambda x: x[3], reverse=True)

    # Display the sorted jobs
    print("Sorted Jobs:")
    for i, job in enumerate(jobs):
        print(f"Job {i+1}: {job[0]}, Start Time: {job[1]}, End Time: {job[2]}, Profit: {job[3]}")
    
    # Initialize the schedule and profit variables
    schedule = []
    total_profit = 0

    # Iterate over the sorted jobs
    for job in jobs:
        # Check if the job can be scheduled without overlapping with existing jobs
        if all(job[1] >= scheduled_job[2] for scheduled_job in schedule):
            schedule.append(job)
            total_profit += job[3]  

    return schedule, total_profit
    
# Example usage
schedule, total_profit = job_scheduling()
print("Scheduled Jobs:")
for i, job in enumerate(schedule):
    print(f"Job {i+1}: {job[0]}, Start Time: {job[1]}, End Time: {job[2]}, Profit: {job[3]}")
print("Total Profit:", total_profit)
