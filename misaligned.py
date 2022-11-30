colorMapping ={}
def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            print(f'{i * 5 + j} | {major} | {minor}')
            colorMapping[f'{major} | {minor}'] = i * 5 + j
    return len(major_colors) * len(minor_colors)


result = print_color_map()

assert(result == 25)
assert(colorMapping['White | Blue'] == 1)
assert(colorMapping['Violet | Blue'] == 20)
assert(colorMapping['Violet | Slate'] == 25)
print("All is well (maybe!)\n")
