import re
from functools import cached_property
from itertools import chain


class Directory:
    def __init__(self, parent):
        self.parent = parent
        self.subdirectories = {}
        self.files = {}

    def get_relative_directory(self, path):
        if path == '/':
            return base_directory
        if path == '..':
            return self.parent
        return self.subdirectories[path]

    def add_subdirectory(self, name):
        self.subdirectories[name] = self.subdirectories.get(
            name, Directory(self))

    def add_file(self, name, size):
        self.files[name] = size

    @cached_property
    def size(self):
        total_file_size = sum(self.files.values())
        total_subdirectory_size = sum(dir.size
                                      for dir in self.subdirectories.values())
        return total_file_size + total_subdirectory_size

    def get_directories(self):
        return chain([self], *[dir.get_directories() for dir in self.subdirectories.values()])


cd_pattern = re.compile(r"\$ cd (.+)")
ls_pattern = re.compile(r"\$ ls")
dir_pattern = re.compile(r"dir (.+)")
file_pattern = re.compile(r"(\d+) (.+)")

base_directory = Directory(None)

lines = (line.strip() for line in open("2022_7_filesystem_input.txt"))

current_directory = base_directory
for line in lines:
    match = cd_pattern.match(line)
    if match:
        current_directory = current_directory.get_relative_directory(
            match.group(1))
        continue
    match = ls_pattern.match(line)
    if match:
        continue
    match = dir_pattern.match(line)
    if match:
        current_directory.add_subdirectory(match.group(1))
        continue
    match = file_pattern.match(line)
    if match:
        current_directory.add_file(match.group(2), int(match.group(1)))
        continue
    raise Exception("Unexpected line type")

print(sum(dir.size for dir in base_directory.get_directories() if dir.size <= 100000))

total_space = 70000000
needed_space = 30000000
space_used = base_directory.size
free_space = total_space - space_used
extra_space_needed = needed_space - free_space
print(min(dir.size for dir in base_directory.get_directories()
      if dir.size >= extra_space_needed))
