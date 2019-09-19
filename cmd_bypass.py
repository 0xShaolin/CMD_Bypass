import subprocess

print """
Welcome to the Windows CommandLine Block Bypass!
I understand that it is a simple task, but this is intended
to bring an easy to use alternative for those who lack
concrete programming knowledge or experience.

Disclaimer: This will not escalate your privileges!!

---------------------------------------------------------------
"""

while True:
    cmd = raw_input("cmd_bypass> ")
    if cmd == "exit":
        exit("Exiting the program. Thanks for using!")
    else:
        out = subprocess.Popen(["cmd.exe", "/c", cmd], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        stdout, stderr = out.communicate()
        print stdout
