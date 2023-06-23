
def falling_distance(time):
    # distance = (1 / 2) * (9.8 * time ** 2)
    return (1 / 2) * (9.8 * time ** 2)


# times_list = [1, 3, 5, 7, 9]
total_distance = 0
num_values = 0

for i in range(1, 10, 2):
    total_distance += falling_distance(i)
    num_values += 1

avg_distance = total_distance / num_values

print(f"Average distance covered = {avg_distance}m")
