import subprocess
import re

filename = "README.md"

outfile_git_name = "tmp_git.txt"
outfile_format_name = "tmp_formatted.txt"

git_log_constant = "1 file changed, "  # Used for grep, do not modify


def getStats(line):
    words = re.findall("\w+", line)
    print(words)


with open(outfile_git_name, "w") as outfile:
    subprocess.call(["git", "log", "--stat",  "--pretty=format:", filename], stdout = outfile)

with open(outfile_format_name, "w") as outfile:
    subprocess.call(["grep", git_log_constant, outfile_git_name], stdout = outfile)

subprocess.call(["rm", outfile_git_name])

# subprocess.call(["gedit", outfile_format_name])


with open(outfile_format_name) as f:
    for line in f:
        getStats(line)


