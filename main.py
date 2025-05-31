from gym import Gym, gogogo
from login import login_main
import msvcrt
import os
import sys
import time
import requests
import configparser
import ctypes
from log import log_message, clear_log, setup_logger
from flask import Flask, render_template_string, request, redirect, make_response




def main():
    ctypes.windll.kernel32.SetConsoleOutputCP(65001)
    gym = Gym()

    options = ["手动开抢(设置好场馆后直接)", "登录(抢场地不要点)", "设置待抢场馆信息", 
               "获取场地信息", "获取预约信息", "校准时间",
               "设置自动抢场地(demo)", "清空日志","手动提交给cas认证","设置用户名密码","设置是否抢两个场地","退出程序","一条路服务(dev)","手动支付"]
    selected_option = 0
    log_message("程序已启动")
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # 显示当前校准后的时间
        # 显示当前校准后的时间
        current_time = gym.get_current_time()
        print(f"当前时间: {current_time.strftime('%Y-%m-%d %H:%M:%S')}")

        # 计算服务器时间
        adjusted_time = current_time + gym.time_diff
        print(f"服务器时间: {adjusted_time.strftime('%Y-%m-%d %H:%M:%S')}")

        # 计算服务器 12:00 时本地真实时间
        server_noon = adjusted_time.replace(hour=12, minute=0, second=0, microsecond=0)
        exptime = server_noon - gym.time_diff  # 计算本地 12:00 的真实时间
        print(f"exp_time: {exptime.strftime('%Y-%m-%d %H:%M:%S')}")

        # 其他信息
        print(f"时间是否已校准: {'是' if gym.is_time_calibrated else '否'}")
        print(f"token={gym.token}  areaid={gym.areaid}  dataid={gym.dateid}")
        print(f"username={gym.username}  password={gym.password}")
        #print(f"是否抢两个场地: {gym.isOrder2}")
        #if gym.isOrder2:
            #print(f"第二个场地信息: areaid2={gym.areaid2}  dataid2={gym.dateid2}")
        print("------------------------------------- ")
        
        for i, option in enumerate(options):
            print("-> " if i == selected_option else "   ", option)

        key = msvcrt.getch()
        if key == b'\xe0':  # Arrow key prefix
            key = msvcrt.getch()
            if key == b'H':  # Up arrow
                selected_option = (selected_option - 1) % len(options)
            elif key == b'P':  # Down arrow
                selected_option = (selected_option + 1) % len(options)
        elif key == b'\r':  # Enter key
            os.system('cls' if os.name == 'nt' else 'clear')
            

            if selected_option == 1:
                #登录
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
                        retry_or_return = input("输入 'R' 返回主菜单或按回车键重试: ").upper()
                        if retry_or_return == 'R':
                            # 用户选择返回主菜单
                            break
                if cas_cookie is not None:
                    gym.set_cookie(cas_cookie)
                    gym.login()

            elif selected_option == 2:
                # 设置待抢场馆信息
                print("设置area_id和data_id\n")
                config = configparser.ConfigParser()
                config.read('config.ini', encoding='utf-8')
                gym.areaid = input("area_id: ")
                gym.set_area_id(gym.areaid)
                config.set('DEFAULT', 'areaid', gym.areaid)
                gym.dateid = input("data_id: ")
                gym.set_date_id(gym.dateid)
                config.set('DEFAULT', 'dateid', gym.dateid)
                """
                if gym.isOrder2:
                    print("设置第二个场馆信息\n")
                    gym.areaid2 = input("area_id2: ")
                    config.set('DEFAULT', 'areaid2', gym.areaid2)
                    gym.dateid2 = input("data_id2: ")
                    config.set('DEFAULT', 'dateid2', gym.dateid2)
                """

                with open('config.ini', 'w', encoding='utf-8') as configfile:
                    config.write(configfile)
            elif selected_option == 3:
                # 获取场地信息
                gym.print_area_id()
            elif selected_option == 4:
                # 获取预约信息
                print(gym.get_inf())
            elif selected_option == 5:
                gym.calibrate_time()

            elif selected_option == 6:
                # 设置自动抢场地
                
                    gym.wait_until_noon()
                    print("\n按任意键继续...")
                    msvcrt.getch()  # Wait for key press
                    
            elif selected_option == 7:
                # 清空日志
                clear_log()
            elif selected_option == 8:
                #手动提交给cas认证
                if gym.token == "未登录，请先登录":
                    print("请先登录")
                else:
                    gym.fuck_cas()
                    
            elif selected_option == 11:
                print("程序已退出。")
                sys.exit(0)
            
            elif selected_option == 0:
                #登录
                gogogo(gym)
            
            elif selected_option == 9:
                # 设置用户名密码
                name = input("username: ")
                password = input("password: ")
                gym.username = name
                gym.password = password
                
                # 写入 config.ini 文件
                config = configparser.ConfigParser()
                config.read('config.ini', encoding='utf-8')
                config.set('DEFAULT', 'username', name)
                config.set('DEFAULT', 'password', password)
                with open('config.ini', 'w', encoding='utf-8') as configfile:
                    config.write(configfile)
                print("用户名和密码已保存到 config.ini 文件")

            elif selected_option==10 :
                """
                gym.isOrder2 = True if input("是否抢两个场地？(y/n): ") == "y" else False
                config = configparser.ConfigParser()
                config.read('config.ini', encoding='utf-8') 
                config.set('DEFAULT', 'isOrder2', str(gym.isOrder2))
                with open('config.ini', 'w', encoding='utf-8') as configfile:
                    config.write(configfile)
                """
                print("抢两个场地只要****,****")




            elif selected_option == 12:
                # 先抢
                
                #支付
                #info=gym.get_inf()
                #gym.order_num=info[0]['order_num']
                
                global sign, sysid, data, subsysid
                sign, sysid, data, subsysid = gogogo(gym)
                print("sign:", sign, "sysid:", sysid, "data:", data, "subsysid:", subsysid)
                #gym.send_payment_request()
                app.run(port=5000,host="0.0.0.0")
                
                    
            elif selected_option == 13:

                sign=input("sign:")
                sysid="106"
                data=input("data:")
                subsysid="302-02"
                app.run(port=5000,host="0.0.0.0")

            if selected_option != 6:  # 对于自动抢场地，我们不需要等待按键
                print("\n按任意键继续...")
                msvcrt.getch() 




app = Flask(__name__)

@app.route('/')
def final_step():
    # 让用户手动提交支付请求
    return f"""
    <form action="http://pay.替换大学.edu.cn/payment/pay/mobileAppPay.action" method="POST">
        <input type="hidden" name="sign" value="{sign}" />
        <input type="hidden" name="sysid" value="{sysid}" />
        <input type="hidden" name="data" value="{data}" />
        <input type="hidden" name="subsysid" value="{subsysid}" />
        <input type="hidden" name="pay_type" value="1" />
        <button type="submit">手动完成支付</button>
    </form>
    """


if __name__ == "__main__":
    setup_logger()
    main()