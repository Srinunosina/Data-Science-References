
import re
import os

# Define the root directory path
root = 'D:\Repos\Predictive Analytics\Database\PrismDatabase\SQLServer'

# Iterate through the directory tree
for dirpath, dirnames, filenames in os.walk(root):
    for file in filenames:
        if file.endswith('.sql'):
            # Open the file in read mode
            with open(os.path.join(dirpath, file), 'r') as f:
                # Read the contents of the file
                contents = f.read()
                # Replace the desired value
                #contents = contents.replace('Asset', 'AssetService.Asset')
                contents = re.sub(r"\balert\b", "pa_alert", contents)
                # Open the file in write mode
                with open(os.path.join(dirpath, file), 'w') as f:
                    # Write the modified contents back to the file
                    f.write(contents)