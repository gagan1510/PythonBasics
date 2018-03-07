import sys

sys.stderr.write("Stderr text\n")
sys.stderr.flush()
sys.stdout.write("Stdout Text\n")

# print(sys.argv)

if len(sys.argv) > 1:
    print(sys.argv[1])

# we can pass anything through the command line or while executing the python file
# like cmd>> python3 SysModule.py 1