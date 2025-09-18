import backdoor_generate
import flag_handler
import ipaddress
import script_generate


def is_valid_ip(ip: str) -> bool:
    """判断输入的IP地址是否合法（支持IPv4和IPv6）"""
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False


def check_input(input_content):
    if int(input_content) in (1, 2, 3, 4):
        return True
    else:
        return False


def check_port_input(input_content):
    if int(input_content) in range(1, 65536):
        return True
    else:
        return False


print(
    """
Welcome to AWD_toolkits.
Made by VioLina
"""
)

while 1:
    print(
        """
Enter the corresponding number to use the function:
1. Activate port handler
2. Generate Backdoor program
3. Generate Backdoor script
4. Exit
"""
    )
    input_content = input()
    if not check_input(input_content):
        print("Invalid input")
        continue
    if input_content == "1":
        port = input("Please input port number:")
        if not check_port_input(port):
            print("Invalid port number")
            continue
        flag_handler.start_server(host="0.0.0.0", port=int(port))
    if input_content == "2":
        port = input("Please input port number:(press Q to exit)")
        if port.upper() == "Q":
            print("exiting...")
            continue
        if not check_port_input(port):
            print("Invalid port number")
            continue
        ip_addr = input("Please input ip address(xxx.xxx.xxx.xxx):")
        if not is_valid_ip(ip_addr):
            print("Invalid ip address")
            continue
        backdoor_generate.main(ip_addr, str(port))
    if input_content == "3":
        script_generate.generate_single_cat_command("polkit-1", "polkit-1")
    if input_content == "4":
        print("exiting...")
        break
