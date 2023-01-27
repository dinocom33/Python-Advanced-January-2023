def math_operations(*numbers, **kwargs):
    for idx in range(len(numbers)):
        key = list(kwargs.keys())[idx % 4]

        if key == "a":
            kwargs[key] += numbers[idx]
        elif key == "s":
            kwargs[key] -= numbers[idx]
        elif key == "d":
            if numbers[idx] != 0:
                kwargs[key] /= numbers[idx]
        elif key == "m":
            kwargs[key] *= numbers[idx]
    sorted_result = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))
    return "\n".join(f"{k}: {v:.1f}" for k, v in sorted_result)


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))