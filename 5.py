n, m = map(int, input().split())

ani_colors = set(int(input()) for _ in range(n))
boris_colors = set(int(input()) for _ in range(m))

common_colors = ani_colors.intersection(boris_colors)
unique_ani_colors = ani_colors - common_colors
unique_boris_colors = boris_colors - common_colors

print(len(common_colors))
print(*sorted(common_colors))

print(len(unique_ani_colors))
print(*sorted(unique_ani_colors))

print(len(unique_boris_colors))
print(*sorted(unique_boris_colors))
