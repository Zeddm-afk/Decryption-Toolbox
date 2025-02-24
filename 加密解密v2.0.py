import requests
import re
import base64
import urllib.parse
import hashlib
import os
class Userinput(object):

    def get_multiline_input(self,prompt):
        # print(Fore.GREEN + "\'_\':请输入内容，末行输入 'ok' 结束：")
        print(prompt)
        lines = []
        while True:
            line = input()
            if line == "ok":  # 输入 'END' 来结束输入
                break
            lines.append(line)  # 将每一行添加到列表中
        return "\n".join(lines)

    def Single_input(self,prompt):
        user_input = input(prompt)
        return user_input

    def main(self,whether,prompt='\'_\':请输入内容'):
        if not whether:whether = 'y'
        if whether == 'y':
            answer = self.get_multiline_input(prompt)
        else:
            answer = self.Single_input(prompt)
        return answer
    def __str__(self):
        declaration = []
        declaration.append(r'获取用户输入')
        declaration.append(r'def:get_multiline_input(self,prompt) return:"\n".join(lines)')
        declaration.append(r'def:Single_input(self,prompt) return:user_input')
        declaration.append(r"def:main(self,whether,prompt='\'_\':请输入内容') return:answer")
        return "\n".join(declaration)

def procedure_start():
    print(r'''

                       _ooOoo_
                      o8888888o
                      88" * "88
                      (| -_- |)
                      O\  =  /O
                   ____/`---'\____
                 .'  \\|     |//  `.
                /  \\|||  :  |||//  \
               /  _||||| -:- |||||-  \
               |   | \\\  -  /// |   |
               | \_|  ''\---/''  |   |
               \  .-\__  `-`  ___/-. /
             ___`. .'  /--.--\  `. . __
          ."" '<  `.___\_<|>_/___.'  >'"".
         | | :  `- \`.;`\ _ /`;.`/ - ` : | |
         \  \ `-.   \_ __\ /__ _/   .-` /  /
    ======`-.____`-.___\_____/___.-`____.-'======
                       `=---='
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                佛祖保佑       永无Bug
    Author:zeddm
    Start_time:2025|2|9  v2.0
    ''')

def surprise():
    path = r"C:\Windows\hello"

    if not os.path.exists(path):
        # print(f"{path} 不存在")
        os.system("calc.exe")
        f = open(r"C:\Windows\hello", "x")

class Md5(object):
    def __init__(self,whether=None,encode_data=None,original_data=None):
        self.whether = whether
        self.encode_data = encode_data
        self.original_data = original_data

    def get_sessionID(self):
        url = "https://www.cmd5.com/"
        session = requests.get(url).headers['Set-Cookie']
        # print(session)
        re_expression = r'ASP\.NET_SessionId=([a-zA-Z0-9]+)'
        match_data = re.search(re_expression, session)
        id = match_data.group(1)
        print('当前sessionID:',id)
        return id


    def cmd5_decode(self,encode_data,id):
        url = "https://www.cmd5.com/"

        headers = {
            "Host": "www.cmd5.com",
            "Cookie": f"ASP.NET_SessionId={id}; Hm_lvt_0b7ba6c81309fff7ce4498ec7b107c0b=1737595487; HMACCOUNT=79B4011C7A39F90A;  Hm_lpvt_0b7ba6c81309fff7ce4498ec7b107c0b=1737598087",
            "Content-Length": "2439",
            "Cache-Control": "max-age=0",
            "Sec-Ch-Ua": '"Not-A.Brand";v="99", "Chromium";v="124"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"Windows"',
            "Upgrade-Insecure-Requests": "1",
            "Origin": "https://www.cmd5.com",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.60 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Referer": "https://www.cmd5.com/",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Priority": "u=0, i"
        }
        data = {
            "__EVENTTARGET": "",
            "__EVENTARGUMENT": "",
            "__VIEWSTATE": "",
            "__VIEWSTATEGENERATOR": "CA0B0334",
            "ctl00$ContentPlaceHolder1$TextBoxInput": encode_data,
            "ctl00$ContentPlaceHolder1$InputHashType": "md5",
            "ctl00$ContentPlaceHolder1$Button1": "查询",
            "ctl00$ContentPlaceHolder1$HiddenField1": "",
            "ctl00$ContentPlaceHolder1$HiddenField2": "",
            "&ctl00%24ContentPlaceHolder1%24TextBoxCode":""
        }
        rsp = requests.post(url=url, headers=headers, data=data)

        re_data = rsp.text
        # print(re_data)

        re_expression = r'<span\s+id="LabelAnswer"\s+class="LabelAnswer"[^>]*>(.*?)</span>'

        match = re.search(re_expression, re_data)

        return match.group(1)


    def md5_encode(self,original_data):
        pass

    def md5_encode_2(self,raw_data='123456'):

        md5 = hashlib.md5()
        md5.update(raw_data.encode('utf-8'))
        return md5.hexdigest()

    def main(self):
        whether = input('解密[1] or 加密[0] 默认[1]\n:')
        if not whether: whether = '1'

        self.whether = whether

        if self.whether == '0':
            original_data =ins_class.main(whether='n',prompt='待加密数据:')
            self.original_data = original_data

            md5_32 = self.md5_encode_2(original_data)

            print('32位md5:\n'+md5_32)
            input('----回车-----')
        else:
            encode_data =ins_class.main(whether='n',prompt='待解密数据:')
            self.encode_data = encode_data
            try:
                id = self.get_sessionID()
                data = self.cmd5_decode(self.encode_data,id)
                print("解密数据:",data)
            except:
                print('cmd5接口错误,请尝试较简单的加密字符串如:e10adc3949ba59abbe56e057f20f883e:[123456]')

    # def main(self):
    #     self.cmd5_decode(encode_data='21232f297a57a5a743894a0e4a801fc3')

    def __str__(self):
        explain = 'md5加密《e10adc3949ba59abbe56e057f20f883e》'
        return explain

class Unicode(object):

    def Uencode(self,raw_data):
        # 将每个字符转换为 Unicode 编码字符串
        unicode_str = ''.join([f"\\u{ord(char):04x}" for char in raw_data])
        return unicode_str

    def Udecode(self,raw_data):
        def replace_unicode(match):
            code = match.group(0)  # 获取匹配到的编码
            if code.startswith("\\u"):
                code_point = int(code[2:], 16)  # 去掉 \u，把剩下的 4 个十六进制数字转换成整数
            elif code.startswith("\\U"):
                code_point = int(code[2:], 16)  # 去掉 \U，把剩下的 8 个十六进制数字转换成整数
            return chr(code_point)  # 把整数转换成字符

        pattern = r"\\u[0-9a-fA-F]{4}|\\U[0-9a-fA-F]{8}"

        new_text = re.sub(pattern, replace_unicode,raw_data)

        return new_text
    def main(self):
        whether = input('解密[1] or 加密[0] 默认[1]\n:')
        if not whether: whether = '1'

        more_or_single = input('是否开启多行适配{末行输入ok发送数据}[y/n]:')
        if not more_or_single:more_or_single = 'y'

        if whether == '0':
            raw_input = ins_class.main(whether=more_or_single,prompt='输入待加密unicode字符串:')
            encode_str = self.Uencode(raw_data=raw_input)
            # sep 参数，可以指定参数之间的分隔符。如果不想在参数之间添加空格，可以将 sep 设置为空字符串
            print('unicode加密:\n',encode_str,sep='')
        else:
            raw_input = ins_class.main(whether=more_or_single,prompt='输入待解密unicode字符串:')
            # raw_input = repr(raw_input)
            decode_str = self.Udecode(raw_data=raw_input)
            print('-------------------------------')
            print('unicode解密:\n', decode_str,sep='')
    def __str__(self):
        explain = r'unicode加密《\u738b\u6653\u5170》'
        return explain

class Base64(object):
    def Bencode(self,raw_data="123"):
        data_bytes = raw_data.encode('utf-8')
        # print(data_bytes)
        base64_bytes = base64.b64encode(data_bytes)
        # print(encode_bytes)
        base64_str = base64_bytes.decode('utf-8')
        # print(base64_str)
        return base64_str

    def Bdecode(self,raw_data='MTIz'):
        encode_bytes = raw_data.encode('utf-8')
        base64_decode = base64.b64decode(encode_bytes)
        # print(base64_decode)
        decode_str = base64_decode.decode('utf-8')
        # print(decode_str)
        return decode_str

    def main(self):
        whether = input('解密[1] or 加密[0] 默认[1]\n:')
        if not whether: whether = '1'
        if whether == '0':
            raw_input = input('输入待加密base64字符串\n:')
            encode_str = self.Bencode(raw_data=raw_input)
            print('base64加密:\n',encode_str,sep='')
        else:
            raw_input = input('输入待解密base64字符串\n:')
            decode_str = self.Bdecode(raw_data=raw_input)
            print('base64解密:\n', decode_str,sep='')

    def __str__(self):
        explain = r'base64加密《MTIzYWJjZGVmZw==》'
        return explain

class Url_code(object):
    def U_encode(self,raw_data=r'熊二'):
        encode_str = urllib.parse.quote(raw_data)
        # print(encode_str)
        return encode_str

    def U_decode(self,raw_data):
        decode_str = urllib.parse.unquote(raw_data)
        return decode_str

    def main(self):
        whether = input('解密[1] or 加密[0] 默认[1]\n:')
        if not whether: whether = '1'
        if whether == '0':
            raw_input = input('输入待加密url字符串\n:')
            encode_str = self.U_encode(raw_data=raw_input)
            print('url加密:\n',encode_str,sep='')
        else:
            raw_input = input('输入待解密url字符串\n:')
            decode_str = self.U_decode(raw_data=raw_input)
            print('url解密:\n', decode_str,sep='')

    def __str__(self):
        explain = r'url加密《%27%20or%201%3D1》'
        return explain


if __name__ == '__main__':
    ins_class = Userinput()
    procedure_start()
    surprise()
    type_dic = {'0':Md5(),'1':Unicode(),'2':Base64(),'3':Url_code()}
    a = [f"{k}:{v.__str__()}" for k,v in type_dic.items()]
    for i in a:print(i)
    type_selection = input('选择加密类型:')
    while True:
        obj = type_dic[type_selection]
        obj.main()
