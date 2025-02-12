import sys

def generate_single_cat_command(input_file, output_file):
    with open(input_file, "rb") as f:
        binary_data = f.read()

    # 将二进制数据转换为十六进制
    hex_data = binary_data.hex()

    # 生成单个 Shell 命令（不使用脚本）
    shell_command = f'echo -n -e "$(echo {hex_data} | xxd -r -p)" > {output_file} && chmod +x {output_file}'

    # 输出 Shell 命令
    print(shell_command)
    with open("output.txt", "w") as file:
        file.write(shell_command)
