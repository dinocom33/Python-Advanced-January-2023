from collections import deque

food_portions = deque(int(x) for x in input().split(", "))
stamina = deque(int(x) for x in input().split(", "))

peaks = {
    80: "Vihren",
    90: "Kutelo",
    100: "Banski Suhodol",
    60: "Polezhan",
    70: "Kamenitza"
}

conquered_peaks = []
idx = 0

for level, peak in peaks.items():
    while food_portions and stamina:
        curr_food = food_portions.pop()
        curr_stamina = stamina.popleft()
        if curr_food + curr_stamina >= level:
            conquered_peaks.append(peak)
            break

if len(conquered_peaks) == len(peaks):
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered_peaks:
    print("Conquered peaks:")
    print(*conquered_peaks, sep="\n")
