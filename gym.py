# 代码开光·河洛版 (Github Copilot 推演)
# 
#             ䷀ ䷁ ䷂      太极生两仪
#            ☯ 乾坎艮震   ☯  两仪生四象
#          ䷃ 巽离坤兑 ䷄    四象生八卦
#         ↗️🖥️↖️ 焚香启禀：
#         先天八卦护法   后天九宫镇码
# 
# ▎卦象加持体系 ▎
# 乾䷀：自强不息 → CPU满载而不崩
# 坤䷁：厚德载物 → 内存包容无泄漏  
# 既济䷾：水火相交 → 循环必有终止
# 未济䷿：事未成时 → 异常皆可捕获
# 泰䷊：天地交泰 → 网络请求必达
# 大有䷍：自天佑之 → 测试覆盖周全
# 同人䷌：同心同德 → 团队协作无碍
# 谦䷎：谦尊而光 → 代码评审顺畅
#
# ▎爻辞咒语 ▎
# for _ in 六爻:   → 初九：潜龙勿用（勿写死循环）
# try-except      → 九二：见龙在田（捕获在明处）
# git commit      → 九三：终日乾乾（勤提交）
# debug()         → 六四：或跃在渊（进退无咎）
# deploy()        → 九五：飞龙在天（发布大吉）
#                 → 上九：亢龙有悔（勿过度设计）
#
# 开光偈曰：
# 先天八卦定架构 后天五行调变量
# 阴阳git护版本  太极docker容万物
# 
# 特别卦辞：
# 产品经理得中孚卦：口吐真言，需求不变
# 项目经理得益卦：十朋之龟，工期不延
# 
# 卜卦仪式说明：
# 1. 子时(23:00)运行代码可得坤卦加持
# 2. 遇BUG时默念"元亨利贞"三遍
# 3. 紧急情况掐指算动爻（Alt+Tab切换窗口）
# 
# 注：本注释已通过《开元占经》验证，运行前建议：
# echo "大衍之数五十，其用四十有九" > /dev/code


import requests
import json
import re
from datetime import datetime
import os
import msvcrt
import ctypes
import sys
from login import login_main

import time
from datetime import datetime, timedelta
from log import log_message, setup_logger, clear_log
import configparser
from bs4 import BeautifulSoup

LOGIN_URL = "https://pass.替换大学.edu.cn/cas/login?service=http%3A%2F%2Fgym.替换大学.edu.cn%2Findex.php%2Findex%2Findex%2Flogin%3Ftype%3D1"



def write_callback(response):
    return response.text

def get_date():
    return datetime.now().strftime("%Y-%m-%d")

def to_two_digits(num):
    return f"{num:02d}"

def gogogo(gym):
    while True:
        gym.s=requests.Session()
        username = gym.username
        password = gym.password
        cas_cookie = None
        while cas_cookie is None:
            try:
                cas_cookie = login_main(username, password)["CASTGC"]
            except Exception as e:
                cas_cookie = None
                log_message(f"登录失败: {e}")
                print("登录失败，请重试")
                            # 给用户一个机会选择是否返回主菜单
        if cas_cookie is not None:
            gym.set_cookie(cas_cookie)
            gym.login()
                    #fuckcas
        try:
            if gym.fuck_cas() =="登录成功":

                try:
                    return gym.Order()
                except Exception as e:
                    log_message(f"order失败,error{e}")

                

            else:
                print("retrying……")
                time.sleep(1)
                continue
        except:
            log_message("fuckcas超时，请重试")
            continue
            



class Gym:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini', encoding='utf-8')
        self.areaid = config.get('DEFAULT', 'areaid', fallback="未设置")
        self.dateid = config.get('DEFAULT', 'dateid', fallback="未设置")
        #self.areaid2 = config.get('DEFAULT', 'areaid2', fallback="未设置")
        #self.dateid2 = config.get('DEFAULT', 'dateid2', fallback="未设置")
        self.cookie = ""
        self.username = config.get('DEFAULT', 'username', fallback="未设置")
        self.password = config.get('DEFAULT', 'password', fallback="未设置")
        self.token = "未登录，请先登录"  # ST开头
        self.iPlanetDirectoryPro = "未登录，请先登录"
        self.order_num = ""
        self.locoal_time = None
        self.time_diff = timedelta(0)
        self.is_time_calibrated = False
        self.is_fucked_cas = False
        self.s = requests.Session()
        self.locoaltion = ""
        self.jsessionid = ""
        #self.isOrder2 = False
        self.headers_pay = {
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh-Hans;q=0.9",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_3_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.57(0x1800392b) NetType/WIFI Language/zh_CN",
            }
        
        self.headers = {
            "authority": "pass.替换大学.edu.cn",
            "method": "GET",
            "path": "/cas/login",
            "scheme": "https",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-encoding": "gzip, deflate, br, zstd",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "cache-control": "max-age=0",
            "cookie": "", 
            "sec-ch-ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Microsoft Edge\";v=\"128\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0",
        }
        
        self.headers_appointment = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "Connection": "keep-alive",
            "cookie": "",
            "Host": "gym.替换大学.edu.cn",
            "Referer": "http://gym.替换大学.edu.cn/index.php/index/user/index.html",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0",
            "X-Requested-With": "XMLHttpRequest"
        }

        self.headers_getinfo = {
            "accept": "application/json, text/javascript, */*; q=0.01",
            "accept-encoding": "gzip, deflate",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "connection": "keep-alive",
            "content-length": "41",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "cookie":"",
            "host": "gym.替换大学.edu.cn",
            "origin": "http://gym.替换大学.edu.cn",
            "referer": "http://gym.替换大学.edu.cn/index.php/index/yuyue/list.html?item_id=3",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0",
            "x-requested-with": "XMLHttpRequest"
        }


        self.headers_check = {
            "Host": "gym.替换大学.edu.cn",
            "Content-Length": "55",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Origin": "http://gym.替换大学.edu.cn",
            "Referer": "http://gym.替换大学.edu.cn/index.php/index/yuyue/list.html?item_id=3",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            
        }

    def set_cookie(self, cookie):
        self.cookie = cookie

    def extract_ticket(self,html_content):
        """
        正则表达式匹配ticket的值
        """
        pattern = r'ST-[^\s"<>]+cas'
        match = re.search(pattern, html_content)
        
        if match:
            return match.group(0)
        else:
            return None


    def calibrate_time(self):
        """
        校准时间，计算本地时间与服务器时间的差值
        """
        url = "http://gym.替换大学.edu.cn/"
        try:
            response = requests.get(url, timeout=5)
            server_time_str = response.headers.get("Date")
            if not server_time_str:
                raise ValueError("服务器未返回时间")
            
            server_time = datetime.strptime(server_time_str, '%a, %d %b %Y %H:%M:%S GMT')
            server_time += timedelta(hours=8)  # 转换为北京时间
            local_time = datetime.now()
            self.time_diff = server_time - local_time
            self.is_time_calibrated = True
            log_message(f"服务器时间(北京时间): {server_time}, 本地时间: {local_time}")
            log_message(f"时间差: {self.time_diff}")
            return server_time
        except Exception as e:
            log_message(f"获取服务器时间失败: {e}")
            return None

    def get_current_time(self):
        """
        获取当前校准后的时间
        """

        return datetime.now() 

    # ... (保留其他方法)

    def wait_until_noon(self):
        """
        等待直到本地时间到达 exptime，然后执行抢场地操作
        """
        current_time = self.get_current_time()
        adjusted_time = current_time + self.time_diff
        server_noon = adjusted_time.replace(hour=12, minute=0, second=0, microsecond=0)
        exptime = server_noon - self.time_diff  # 计算本地 12:00 的真实时间

        print("等待本地时间到达 exptime 开始抢场地...")
        while self.get_current_time() < exptime:
            time_left = exptime - self.get_current_time()
            hours, remainder = divmod(time_left.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            print(f"\r距离开抢还有: {hours:02d}:{minutes:02d}:{seconds:02d}", end="", flush=True)
            time.sleep(1)  # 每秒更新一次倒计时
        
        print("\n现在是中午12点，开始抢场地！")

        gogogo(self)#gogogo出发喽



    

    def extract_area(self, input_str):
        """
        拆分场地信息并保存为 JSON 文件
        """
        pattern = r'area-id="(\d+)">(.*?)<'
        matches = re.findall(pattern, input_str)
        results = []
        for area_id, content in matches:
            area_id = to_two_digits(int(area_id))
            status = self.get_timesolt(area_id)
            result = {
                "area_id": area_id,
                "name": content,
                "available_times": self.find_available_times(status)
            }
            results.append(result)

        # 保存为 JSON 文件
        directory = "timeslot"
        if not os.path.exists(directory):
            os.makedirs(directory)
        filename = os.path.join(directory, f"{get_date()}.json")
        with open(filename, 'w', encoding='utf-8') as json_file:
            json.dump(results, json_file, ensure_ascii=False, indent=4)

        print(f"场地信息已保存到 {filename}")
        return results

    def login(self):
        """
        获取ST开头的ticket和iPlanetDirectoryPro
        
        """
        log_message("正在尝试登录.... ")
        
        self.headers["cookie"] = f"CASTGC={self.cookie}"
        response = self.s.get(LOGIN_URL, headers=self.headers, allow_redirects=False)
        self.token = self.extract_ticket(response.text)
        cookies = response.cookies
        self.iPlanetDirectoryPro = cookies.get('iPlanetDirectoryPro')

        response = self.s.get(LOGIN_URL, headers=self.headers)

        log_message(f"登录成功，token={self.token}, iPlanetDirectoryPro={self.iPlanetDirectoryPro}")
        self.headers_getinfo["cookie"]=f"iPlanetDirectoryPro={self.iPlanetDirectoryPro}; PHPSESSID={self.token}"
        self.headers_appointment["cookie"]=f"iPlanetDirectoryPro={self.iPlanetDirectoryPro}; PHPSESSID={self.token}"
        #log_message(self.fuck_cas())

        
        

    def get_timesolt(self, areaid):
        """
        获取羽毛球场地的所有时间表
        
        """
        url = "http://gym.替换大学.edu.cn/index.php/index/item/timeslot.html?"
        url=url+f"item_id=3&area_id={areaid}&date_time={get_date()}"
        print(f"请求：{url}")
        time.sleep(0.5)
        response = requests.post(url,self.headers_getinfo).text
        print(f"响应: {response}")
        return response

    def get_order_id(self):
        """
        获取请求里面的order_id
        """
        url = "http://gym.替换大学.edu.cn/index.php/index/item/timeslot.html"
        date = get_date()
        response = requests.post(url, f"item_id=3&area_id={self.areaid}&date_time={date}", self.headers_getinfo).text
        data = json.loads(response)
        return data.get("order_num", "")

    def find_available_times(self, json_string):

        """
        找到可用时间
        """
        data = json.loads(json_string)
        if data.get("code") == 1:
            available_times = [f"{entry['time']}({entry['id']})" for entry in data.get("data", []) if entry.get("check") != "disable"]
            if not available_times:
                return "无可用时间\n"
            else:
                return f"{len(available_times)}个可用时间：{'   '.join(available_times)}"
        else:
            return "无可用时间\n"

    def set_area_id(self, areaid):
        self.areaid = areaid

    def set_date_id(self, dateid):
        self.dateid = dateid

    def print_area_id(self):
        """
        优先检查本地是否存在 timeslot/yyyy-mm-dd.json 文件，存在则直接读取
        """
        filename = f"timeslot/{get_date()}.json"
        if os.path.exists(filename):
            print(f"从本地文件 {filename} 读取场地信息...")
            with open(filename, 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)
                for entry in data:
                    log_message(f"area-id={entry['area_id']}: {entry['name']} {entry['available_times']}")
            return

        log_message("本地文件不存在，正在请求场地信息...")
        response = """<div class="office-time-con" style="width: 1000px">
                                        <div class="fenhang">
                                          <div class="office-time-item area_  checked" area-id="4">一楼塑胶1</div>
                                          <div class="office-time-item area_" area-id="5">一楼塑胶2</div>
                                          <div class="office-time-item area_" area-id="6">一楼塑胶3</div>
                                          </div>
                                          <div class="fenhang">
                                          <div class="office-time-item area_" area-id="7">一楼木质4</div>
                                          <div class="office-time-item area_" area-id="8">一楼塑胶5</div>
                                          <div class="office-time-item area_" area-id="9">一楼塑胶6</div>
                                          </div>
                                          <div class="fenhang">
                                          <div class="office-time-item area_" area-id="10">一楼塑胶7</div>
                                          <div class="office-time-item area_" area-id="11">一楼木质8</div>
                                          <div class="office-time-item area_" area-id="12">二楼塑胶1</div>
                                          </div>
                                          <div class="fenhang">
                                          <div class="office-time-item area_" area-id="13">二楼塑胶2</div>
                                          <div class="office-time-item area_" area-id="14">二楼塑胶3</div>
                                          <div class="office-time-item area_" area-id="15">二楼塑胶4</div>
                                          </div>
                                          <div class="fenhang">
                                          <div class="office-time-item area_" area-id="16">二楼塑胶5</div>
                                          <div class="office-time-item area_" area-id="17">二楼塑胶6</div>
                                          <div class="office-time-item area_" area-id="18">二楼塑胶7</div>
                                          </div>
                                          <div class="fenhang">
                                          <div class="office-time-item area_" area-id="19">二楼塑胶8</div>
                                          <div class="office-time-item area_" area-id="20">二楼塑胶9</div>
                                          <div class="office-time-item area_" area-id="21">二楼塑胶10</div>
                                          </div>
                                          <div class="fenhang">
                                          <div class="office-time-item area_" area-id="22">二楼塑胶11</div>
                                          <div class="office-time-item area_" area-id="23">二楼塑胶12</div>
                                    </div>
              </div>"""
        matches = self.extract_area(response)
        for match in matches:
            log_message(match)
        return matches
    


    def fuck_cas(self):
        """
        告诉cas老子cookie有效qnmd
        """
         #登录第二步 将已经获取到的ticket发送给服务器，告诉cas这个cookie有效

        url2 = f"http://gym.替换大学.edu.cn/index.php/index/index/login?type=1&ticket={self.token}"
        headers_login2 = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Connection": "keep-alive",
        "Host": "gym.替换大学.edu.cn",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46",
        "Cookie":f"iPlanetDirectoryPro={self.iPlanetDirectoryPro}"
        }
        print(headers_login2)
        print(url2)

        response2 = self.s.get(url2, headers=headers_login2,timeout=30).text
        #登录第三步
        url3 = "http://gym.替换大学.edu.cn/index.php/index/index/login?type=1"
        response3 = self.s.get(url3, headers=headers_login2,timeout=30).text

        if "登录成功" in response2:
            self.is_fucked_cas=True
            print("登录成功")
            return "登录成功"
        else:
            #print(response2)
            #print(response3)
            print("登录失败")
            return "登录失败"



    def parse_hidden_inputs(self,raw_text):
        try:
            # 移除换行符，避免影响正则匹配
            raw_text = raw_text.replace("\n", "").replace("\r", "")
            
            # 使用正则表达式直接提取各隐藏字段的值
            sign = re.search(r'name="sign"\s+value="([^"]*)"', raw_text).group(1)
            sysid = re.search(r'name="sysid"\s+value="([^"]*)"', raw_text).group(1)
            data = re.search(r'name="data"\s+value="([^"]*)"', raw_text).group(1)
            subsysid = re.search(r'name="subsysid"\s+value="([^"]*)"', raw_text).group(1)
            
            return sign, sysid, data, subsysid
        except Exception as e:
            print(f"解析失败: {str(e)}")
            return None, None, None, None

    def Order(self):

        """
        检查是否可以预约
        """
        

        self.headers_check["Cookie"] = f"PHPSESSID={self.token}, iPlanetDirectoryPro={self.iPlanetDirectoryPro}"
        url = "http://gym.替换大学.edu.cn/index.php/index/item/check.html"
        data_check = {
            "item_id": "3",
            "area_id": self.areaid,
            "date_time": get_date(),
            "data_id": self.dateid,
        }
        print(data_check)
        response1 = self.s.post(url, data=data_check, headers=self.headers_check)
        log_message(response1.text)
        """
        确认后支付
        """
        url = "http://gym.替换大学.edu.cn/index.php/index/pay/index.html"
        order_id=self.get_order_id()
        data_pay={
            "order_id": order_id,
            "item_id": "3",
            "area_id": self.areaid,
            "date_time": get_date(),
            "data_id": self.dateid,
        }
        self.Order_num=order_id
        print(data_pay)
        response2 = self.s.post(url, headers=self.headers_appointment,data=data_pay)
        #log_message(response2.text)
        print("-------------------")
        log_message(response2.url)
        #index.php/index/user/pay.html?order_num='+data[i].order_num+
        log_message(f"http://gym.替换大学.edu.cn/index.php/index/pay/index.html?order_num={order_id}")
        import ast
        msg = ast.literal_eval(response2.text)
        log_message(msg)
        sign=input("sign:")
        sysid="106"
        data=input("data:")
        subsysid="302-02"
        # sign, sysid, data, subsysid = self.parse_hidden_inputs(response2.text)
        log_message(f"sign={sign}, sysid={sysid}, data={data}, subsysid={subsysid}")
        return sign, sysid, data, subsysid


   





    def get_inf(self):
        pre_response = requests.get("http://gym.替换大学.edu.cn/index.php/index/user/index.html", headers=self.headers_appointment,allow_redirects=False)
        
        response = requests.get("http://gym.替换大学.edu.cn/index.php/index/user/index.html?page=1", headers=self.headers_appointment,allow_redirects=False)
        data=self.display_order_info(response.text)
        return data
    
    def display_order_info(self,info):
        reservations = json.loads(info)
        count = 1
        print(reservations)
        # 打印解析后的数据
        for reservation in reservations:
            print(f"订单{count}")
            print(f"项目名称: {reservation['item_name']}")
            print(f"项目ID: {reservation['id']}")
            print(f"场地名称: {reservation['area_name']}")
            print(f"订单号: {reservation['order_num']}")
            print(f"支付金额: {reservation['pay_amount']} 元")
            print(f"日期时间: {reservation['date_time']}")
            for yuyue in reservation['yuyue_list']:
                print(f"  预约ID: {yuyue['id']}")
                print(f"    项目ID: {yuyue['item_id']}")
                print(f"    场地ID: {yuyue['area_id']}")
                print(f"    开始时间: {yuyue['start_time']}")
                print(f"    结束时间: {yuyue['end_time']}")
                print(f"    创建时间: {yuyue['create_time']}")
                print(f"    更新时间: {yuyue['update_time']}")
                print(f"    时间段: {yuyue['time']}")
            print(f"支付状态: {'支付成功' if reservation['pay_status']==2 else '支付失败或未支付'}")
            print("--------------------------------------------------")
            count += 1
        return reservations
    
    """
    以下为测试支付流程
    """



    def get_payment_page(self):
        """获取支付页面"""
        url = f"http://gym.替换大学.edu.cn/index.php/index/user/pay.html?order_num={self.order_num}"
        headers = {
            **self.headers_pay,
            "Host": "gym.替换大学.edu.cn",
            "Upgrade-Insecure-Requests": "1",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Referer": "http://gym.替换大学.edu.cn/index.php/index/user/index.html",
        }
        response = self.s.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        sign = soup.find("input", {"name": "sign"})["value"]
        sysid = soup.find("input", {"name": "sysid"})["value"]
        data = soup.find("input", {"name": "data"})["value"]
        subsysid = soup.find("input", {"name": "subsysid"})["value"]
        return sign, sysid, data, subsysid

    def check_payment_status(self):
        """检查支付状态"""
        url = "http://gym.替换大学.edu.cn/index.php/index/user/check.html"
        headers = {
            **self.headers_pay,
            "Host": "gym.替换大学.edu.cn",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "X-Requested-With": "XMLHttpRequest",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Origin": "http://gym.替换大学.edu.cn",
            "Referer": f"http://gym.替换大学.edu.cn/index.php/index/user/pay.html?order_num={self.order_num}",
        }
        data = {"order_num": self.order_num}
        response = self.s.post(url, headers=headers, data=data)
        return response.json()

    def send_payment_request(self, pay_type="1"):
        """发送支付请求"""
        url = "http://gym.替换大学.edu.cn/index.php/index/user/gopay.html"
        headers = {
            **self.headers_pay,
            "Host": "gym.替换大学.edu.cn",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "X-Requested-With": "XMLHttpRequest",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Origin": "http://gym.替换大学.edu.cn",
            "Referer": f"http://gym.替换大学.edu.cn/index.php/index/user/pay.html?order_num={self.order_num}",
        }
        data = {"order_num": self.order_num, "pay_type": pay_type}
        response = self.s.post(url, headers=headers, data=data)
        return response.json()

    def submit_payment(self, sign, sysid, data, subsysid):
        """提交支付请求"""
        url = "http://pay.替换大学.edu.cn/payment/pay/mobileAppPay.action"
        headers = {
            **self.headers_pay,
            "Host": "pay.替换大学.edu.cn",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Content-Type": "application/x-www-form-urlencoded",
            "Origin": "http://gym.替换大学.edu.cn",
            "Upgrade-Insecure-Requests": "1",
            "Referer": "http://gym.替换大学.edu.cn/",
        }
        payload = {
            "sign": sign,
            "sysid": sysid,
            "data": data,
            "subsysid": subsysid,
            "pay_type": "1",
        }
        response = self.s.post(url, headers=headers, data=payload)
        self.locoaltion = response.headers.get("Location")
        self.jsessionid = response.cookies.get("JSESSIONID")
        log_message(f"支付请求重定向地址: {self.locoaltion}")
        log_message(f"JSESSIONID: {self.jsessionid}")
        
    def send_payment_request(self):
        url = "http://gym.替换大学.edu.cn/index.php/index/user/gopay.html"
        headers = {
            **self.headers_pay,
            "Host": "gym.替换大学.edu.cn",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "X-Requested-With": "XMLHttpRequest",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Origin": "http://gym.替换大学.edu.cn",
            "Referer": f"http://gym.替换大学.edu.cn/index.php/index/user/pay.html?order_num={self.order_num}",
        }
        return self.s.post(url, headers=headers, data={"order_num": self.order_num, "pay_type": "1"}).json()
    
    def process_payment(self):
        """完整支付流程"""
        print("获取支付页面...")
        sign, sysid, data, subsysid = self.get_payment_page()
        log_message(f"Sign: {sign}, SysID: {sysid}, Data: {data}, SubSysID: {subsysid}")
        return sign, sysid, data, subsysid


    



