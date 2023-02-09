jobs = [int(x) for x in input().split(", ")]
index_of_job = int(input())
clock_cycles = 0

for num in sorted(jobs):
    current_index = jobs.index(num)
    clock_cycles += jobs[current_index]
    jobs[current_index] = "0"
    if current_index == index_of_job:
        break

print(clock_cycles)