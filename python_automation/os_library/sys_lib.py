import sys

print("Python version: ",sys.version)
sys.stdout.write("Pandit\n")

n=len(sys.argv)
print(n)
print("\nName of the python script:",sys.argv[0])

sys.exit(0)

def print_to_stderr(*a):
    # Here a is the array holding the objects
    # passed as the argument of the function
    print(*a, file=sys.stderr)


print_to_stderr("Hello World")

for line in sys.stdin:
    if 'q'==line.strip():
        break
    elif not 'q':
        pass

    else:
        print(f'input:{line}')