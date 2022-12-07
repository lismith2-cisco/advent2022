splitlines = ([elf.split('-') for elf in line.strip().split(',')]
              for line in open("2022_4_cleanup_input.txt"))
total_overlaps = 0
overlaps = 0
for elf_a, elf_b in splitlines:
    set_a = set(range(int(elf_a[0]), int(elf_a[1])+1))
    set_b = set(range(int(elf_b[0]), int(elf_b[1])+1))
    #print(set_a, set_b)
    if set_a <= set_b or set_b <= set_a:
        total_overlaps += 1
    if set_a & set_b:
        overlaps += 1
print(total_overlaps)
print(overlaps)
