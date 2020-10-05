import os

prefix = 'name-segments'
print(f"\nChecking {prefix} directory for duplicate names...")
for filename in (f for f in os.listdir(prefix) if f.endswith('.txt')):
    print(f" Checking {filename}")

    unique_names = set()
    duplicate_names = {}

    with open(prefix + '/' + filename, 'r') as f:
        names = (l.strip() for l in f.readlines())
        
        for name in names:
            if name in unique_names:
                duplicate_names[name] = duplicate_names.get(name, 0) + 1
            unique_names.add(name)

        for name, count in duplicate_names.items():
            print(f"  {name} - {count} duplicate(s)")

    with open(prefix + '/' + filename, 'w') as f:
        f.writelines('\n'.join(sorted(unique_names)))
