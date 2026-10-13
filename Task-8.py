
# Take user input
data = input("Enter some text: ")

# Write data to the file
with open("output.txt", "w") as file:
    file.write(data + "\n")

print("Data written successfully!")

# Append additional data
additional_data = input("Enter additional text: ")

with open("output.txt", "a") as file:
    file.write(additional_data + "\n")

print("Additional data appended successfully!")

# Read and display the final content
with open("output.txt", "r") as file:
    print("\nFinal content of output.txt:")
    print(file.read())
