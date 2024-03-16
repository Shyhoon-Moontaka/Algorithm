import subprocess
command=["bash","-c","cd myFolder && ls"]
result=subprocess.run(command)
print(result.stdout)