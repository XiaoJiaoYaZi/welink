import paramiko
import re
from time import sleep
import time

# 定义一个类，表示一台远端linux主机
class Linux(object):
    # 通过IP, 用户名，密码，超时时间初始化一个远程Linux主机
    def __init__(self, ip, port,username, password, timeout=30):
        self.ip = ip
        self.port = port
        self.username = username
        self.password = password
        self.timeout = timeout
        # transport和chanel
        self.t = ''
        self.chan = ''
        # 链接失败的重试次数
        self.try_times = 3

    # 调用该方法连接远程主机
    def connect(self):
        while True:
            # 连接过程中可能会抛出异常，比如网络不通、链接超时
            try:
                self.t = paramiko.Transport(sock=(self.ip, self.port))
                self.t.connect(username=self.username, password=self.password)
                self.chan = self.t.open_session()
                self.chan.settimeout(self.timeout)
                self.chan.get_pty()
                self.chan.invoke_shell()
                # 如果没有抛出异常说明连接成功，直接返回
                print(u'连接%s成功' % self.ip)
                # 接收到的网络数据解码为str
                print(self.chan.recv(65535).decode('utf-8'))
                return True
            # 这里不对可能的异常如socket.error, socket.timeout细化，直接一网打尽
            except Exception as e1:
                if self.try_times != 0:
                    print(u'连接%s失败，进行重试' % self.ip)
                    self.try_times -= 1
                else:
                    print('重试3次失败，结束程序')
                    return False

    # 断开连接
    def close(self):
        self.chan.close()
        self.t.close()

    # 发送要执行的命令
    def send(self, cmd):
        cmd += '\r'
        # 通过命令执行提示符来判断命令是否执行完成
        p = re.compile(r'\[([\s\S]*)\]([\s\S]*)\[([\s\S]*)\]')
        p1 = re.compile(r'~\]#')
        p3 = re.compile(r'\[([\s\S]*)\]\$')
        print(cmd)
        result = ''
        # 发送要执行的命令
        self.chan.send(cmd)
        # 回显很长的命令可能执行较久，通过循环分批次取回回显
        start = time.time()
        while True:
            sleep(0.5)
            if time.time() -start >20:
                break
            ret = self.chan.recv(65535)
            ret = ret.decode('utf-8')
            result += ret
            ret = result.split('\r\n')[-1]
            if  not p3.search(ret) and not p1.search(ret) :
                #if not p3.search(result):
                continue

            rrr = result.split('\r\n')[-1]
            sss = result.replace(rrr,'')
            print(sss)
            return sss,rrr
        return '查询超时',''

# l = Linux('10.1.63.127',55519,'welinkde','aUmMZbhZ88Am31llaAgykfjYhArcjjWA')
# l.connect()
# print(l.send('kafka-consumer-groups.sh --bootstrap-server 10.1.63.127:9092 --list --new-consumer'))
# print(l.send('kafka-run-class.sh kafka.admin.ConsumerGroupCommand --bootstrap-server 10.1.63.127:9092 --describe --group 10.1.120.83.IndvdPkgTmpltQueue'))