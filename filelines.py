import subprocess
import re
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("filename", help = "Relative or absolute path to the file you want to measure")

args = parser.parse_args()

filename = args.filename


outfile_git_name = "tmp_git.txt"
outfile_format_name = "tmp_formatted.txt"

git_log_constant = "1 file changed, "  # Used for grep, do not modify

diff_list = []
total_list = []

def is_insertion(str):
    return str == "insertion" or str == "insertions"


def get_stats(line):
    words = re.findall("\w+", line)

    current_diff = 0

    # Magic number 4 to avoid "1 file changed" string
    # Removing it add unnecesary extra operations when I can simply skip them 
    # (Will only read them once)
    for i in range(4, len(words), 2):
        if is_insertion(words[i]):
            current_diff += int(words[i-1])
        else:
            current_diff -= int(words[i-1])

    diff_list.append(current_diff)


with open(outfile_git_name, "w") as outfile:
    subprocess.call(["git", "log", "--stat",  "--pretty=format:", filename], stdout = outfile)

with open(outfile_format_name, "w") as outfile:
    subprocess.call(["grep", git_log_constant, outfile_git_name], stdout = outfile)


# Delete tmp file
subprocess.call(["rm", outfile_git_name])

with open(outfile_format_name) as f:
    for line in f:
        get_stats(line)


# Delete tmp file
subprocess.call(["rm", outfile_format_name])

# Reverse diffs to be in incremental time
diff_list.reverse()
total_list.append(diff_list[0]) # Need at least one element

for i in range(1, len(diff_list)):
    total_list.append(total_list[i-1] + diff_list[i])

# plot
plt.plot(total_list)
plt.title(filename)
plt.ylabel('File lines')
plt.ylabel('Commits')
plt.show()
