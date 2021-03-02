t = (19, 42, 21)

t_str = ""
for i in range(len(t)-1):
    t_str += str(t[i])+", "
t_str += str(t[-1])

print(f"The {len(t)} numbers are: {t_str}")
