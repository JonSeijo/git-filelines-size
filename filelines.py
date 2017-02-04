import subprocess
filename = "README.md"

subprocess.call(["git", "log", "--stat", "--graph", "--pretty=format:", filename])