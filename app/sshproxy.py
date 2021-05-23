import logging
import json
import time
from sshtunnel import SSHTunnelForwarder

# 配置日志
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S')


class sshproxy:
    def __init__(self, filename):
        _fp = open(filename, encoding="utf-8")
        logging.info("get file {}".format(filename))
        self._jsonconfig = json.load(_fp)
        # print(self._jsonconfig)
        _fp.close()
        self._proxy = []

    def startproxy(self):

        for item in self._jsonconfig:
            name = item["name"]
            status = item['status']
            ssh_ip = item["ssh_ip"]
            ssh_port = item["ssh_port"]
            ssh_username = item["ssh_username"]
            ssh_pkey = item["ssh_pkey"]
            remote_bind_addr = item["remote_bind_addr"]
            remote_bind_port = item["remote_bind_port"]
            local_port = item["local_port"]
            if (status != 'ENABLE'):
                logging.info("proxy {} status != ENABLE then get next proxy".format(name))
                continue
            _server = SSHTunnelForwarder(
                (ssh_ip, ssh_port),  # 指定ssh登录的跳转机的address，端口号
                ssh_username=ssh_username,  # 跳转机的用户
                ssh_password=ssh_pkey,  # 私钥路径
                remote_bind_address=(remote_bind_addr, remote_bind_port),
                local_bind_address=('127.0.0.1', local_port)
            )
            logging.info("start proxy {} remort addr={} remort port={} local port={}".format(name, remote_bind_addr,
                                                                                             remote_bind_port,
                                                                                             local_port))
            _server.start()
            self._proxy.append(_server)

    def waitend(self):
        while True:
            a = input("Press Enter to quit...")
            if a == '': break
            time.sleep(1)
        logging.info("exit sshproxy")
        for _server in self._proxy:
            _server.close()
        time.sleep(5)


if __name__ == '__main__':
    _sshproxy = sshproxy("proxy.json")
    _sshproxy.startproxy();
    _sshproxy.waitend();
