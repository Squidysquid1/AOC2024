import time

def time_it(task_name, fn):
    total_duration = 0
    runs = 10
    
    for _ in range(runs):
        start = time.time()
        fn()  # Run the function
        duration = time.time() - start
        total_duration += duration
    
    average_duration = total_duration / runs
    
    # Output the result
    print(f"{task_name} took {average_duration:.6f} seconds\n")