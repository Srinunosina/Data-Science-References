
print('hi')
with open('C:\\Users\\srinu.nosina\\Desktop\DB Design\\Files\MigrateUserLogins.sql', 'r') as file:
    contents = file.read()
    contents = contents.replace('UserPref', 'dbo.UserPref')

with open('C:\\Users\\srinu.nosina\\Desktop\DB Design\\Files\MigrateUserLogins1.sql', 'w') as file:
    # Write the modified contents back to the file
    file.write(contents)
    