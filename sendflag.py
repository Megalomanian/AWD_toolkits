import requests
import os

raw_headers = """\
Host: example.com
User-Agent: CustomClient/1.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp
Accept-Language: en-US,en;q=0.5
Connection: keep-alive
"""
url = "https://example.com"


def post_method(flag: str):
    def raw_headers_to_dict(raw_headers: str) -> dict:
        """
        将原始 HTTP 头字符串转换为 requests 库可用的 headers 字典。
        """
        headers = {}
        for line in raw_headers.strip().split("\n"):
            if ": " in line:
                key, value = line.split(": ", 1)
                headers[key.strip()] = value.strip()
        return headers

    # 示例原始 HTTP 头
    # 解析原始 HTTP 头
    headers_dict = raw_headers_to_dict(raw_headers)
    data = {"flag": flag}
    # 使用 requests 发送 POST 请求
    response = requests.post(url, headers=headers_dict, data=data)

    # 输出返回内容
    print(response.status_code)
    print(response.text)


def get_method(flag: str):
    def raw_headers_to_dict(raw_headers: str) -> dict:
        """
        将原始 HTTP 头字符串转换为 requests 库可用的 headers 字典。
        """
        headers = {}
        for line in raw_headers.strip().split("\n"):
            if ": " in line:
                key, value = line.split(": ", 1)
                headers[key.strip()] = value.strip()
        return headers

    # 解析原始 HTTP 头
    headers_dict = raw_headers_to_dict(raw_headers)
    data = {"flag": flag}
    # 使用 requests 发送 GET 请求
    response = requests.get(url, headers=headers_dict, params=data)

    # 输出返回内容
    print(response.status_code)
    print(response.text)


def os_command(flag: str):
    command = f'curl -X POST {url} -H "Content-Type: application/x-www-form-urlencoded" -d "flag={flag}"'
    os.system(command)


# noqa: E501  # 用于忽略行长度限制的警告
