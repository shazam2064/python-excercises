import sys
import subprocess


# Checking IP reachability
def ip_reach(list):
    for ip in list:
        ip = ip.rstrip("\n")

        ping_reply = subprocess.call('ping %s /n 2' % (ip), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        if ping_reply == 0:
            print("\n* {} is reachable :)\n".format(ip))
            continue

        else:
            print('\n* {} not reachable :( Check connectivity and try again.'.format(ip))
            sys.exit()

# Checking username/password file
# Prompting user for input - USERNAME/PASSWORD FILE
user_file = input("\n# Enter user file path and name (e.g. D:\\MyApps\\myfile.txt): ")

# Verifying the validity of the USERNAME/PASSWORD file
if os.path.isfile(user_file) == True:
    print("\n* Username/password file is valid :)\n")

else:
    print("\n* File {} does not exist :( Please check and try again.\n".format(user_file))
    sys.exit()
