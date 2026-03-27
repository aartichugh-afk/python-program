# Step 1: Write data to a file
f = open("sample.txt", "w")
f.write("First line\n")
f.write("Second line\n")
f.write("File handling is easy\n")
f.close()

# Step 2: Append new data
f = open("sample.txt", "a")
f.write("Fourth line added later\n")
f.close()

# Step 3: Read the file
f = open("sample.txt", "r")
content = f.read()
print("File Content:")
print(content)
f.close()

# Step 4: Count number of lines
f = open("sample.txt", "r")
lines = f.readlines()
print("Total number of lines:", len(lines))
f.close()