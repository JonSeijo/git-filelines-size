import subprocess
filename = "README.md"

subprocess.call(["git", "log", "--stat",  "--pretty=format:", filename])