import subprocess
filename = "README.md"

outfile_git_name = "tmp_git.txt"
outfile_format_name = "tmp_formatted.txt"
git_log_constant = "1 file changed, "

with open(outfile_git_name, "w") as outfile:
    subprocess.call(["git", "log", "--stat",  "--pretty=format:", filename], stdout = outfile)

with open(outfile_format_name, "w") as outfile:
    subprocess.call(["grep", git_log_constant, outfile_git_name], stdout = outfile)

subprocess.call(["gedit", outfile_format_name])
