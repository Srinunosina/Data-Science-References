import os

# Define the directory path
path = 'D:\Repos\Predictive Analytics\Database\PrismDatabase\SQLServer\Procedures'
# path = 'D:\Repos\Predictive Analytics\Database\PrismDatabase\SQLServer'
# Iterate through the files in the directory
for file in os.listdir(path):
    if file.endswith('.sql'):
        # Open the file in read mode
        with open(os.path.join(path, file), 'r') as f:
            # Read the contents of the file
            contents = f.read()
            # Replace the desired value
            contents = contents.replace('AlarmAssignments', 'Alert.AlarmAssignments')
            # Open the file in write mode
            with open(os.path.join(path, file), 'w') as f:
                # Write the modified contents back to the file
                f.write(contents)