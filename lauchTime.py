#-*- coding:utf-8 _*-
"""
@author:Duan jun ming
@file: lauchTime.py
@time: 2018/09/21
qq:1032241157
"""
import os


class app(object):

    def __init__(self):
        self.data = ""
        self.content =""


    def get_appLaunchTime(self):
        #冷启动的adb命令
        cmd="adb shell am start -W -n  	com.woqutz.didi/com.ryg.dynamicload.DLProxyFragmentActivity"
        self.content = os.popen(cmd)


    def stop_app(self):
        #停止app的命令
        cmd ="adb shell am force-stop com.woqutz.didi"
        os.popen(cmd)

    def get_timedata(self):
        for line in self.content.readlines():
            if "ThisTime" in line:
                 thisTime = line.split(":")[1]
                 break
        return thisTime


class Controller(object):
    def run(self):
        pass

if __name__ == "__main__":
    app = app()
    #print(app.get_appLaunchTime())
    app.get_appLaunchTime()
    thisTime = app.get_timedata()
    print(thisTime)
