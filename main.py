# CNA337 Final Project
# Zachary Rubin, zrubin@rtc.edu
# Group participans:  Dorin,  Saeid, Vlado, Mohammad and Abdy.
# Tutoring help: Liviu Patrisco, liviu_patrisco@hotmail.com

from Server import Server

def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.1 by Igor")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    ec2_ip_address = "18.224.151.54"
    server = Server(ec2_ip_address)
    result = server.ping()
    print(result)
    if result == 0:
        print("Server with ip [%s] is up." % ec2_ip_address)
    else:
        print("Server with ip [%s] is down." % ec2_ip_address)
