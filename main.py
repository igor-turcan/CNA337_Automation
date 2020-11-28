# This is the template code for the CNA337 Final Project
# Zachary Rubin, zrubin@rtc.edu
# CNA 337 Fall 2020
# Igor Turcan
# Tutoring help: Daniel Turcan, dan.tur000@gmail.com
def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.1 by Igor")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    # TODO - Create a Server object
    import os
    ip = "18.224.151.54"
    response = os.system("ping -n 4 " + ip)
    # TODO - Call Ping method and print the results
    if response == 0:
        print(ip, 'is up!')
    else:
        print(ip, 'is down!')