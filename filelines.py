import subprocess
import re

filename = "README.md"

outfile_git_name = "tmp_git.txt"
outfile_format_name = "tmp_formatted.txt"

git_log_constant = "1 file changed, "  # Used for grep, do not modify

diff_list = []

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
    print(diff_list)


with open(outfile_git_name, "w") as outfile:
    subprocess.call(["git", "log", "--stat",  "--pretty=format:", filename], stdout = outfile)

with open(outfile_format_name, "w") as outfile:
    subprocess.call(["grep", git_log_constant, outfile_git_name], stdout = outfile)

subprocess.call(["rm", outfile_git_name])

# subprocess.call(["gedit", outfile_format_name])


with open(outfile_format_name) as f:
    for line in f:
        get_stats(line)


