#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: paramiko-test.py
@time: 2018/3/5 11:11
"""

import paramiko

# 创建ssh对象
ssh = paramiko.SSHClient()
# 允许链接不存在knows_host文件的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh链接 主机
ssh.connect(hostname='192.168.42.133', port=22, username='peter', password='123456')
# 执行命令
try:
    stdin, stdout, stderr = ssh.exec_command('sudo -S apt-get remove sl')
    stdin.write("123456\r\n")
    stdin.flush()
except Exception, e:
    print e
ssh.close()
#
#
# # 公钥进行链接
# private_key = paramiko.RSAKey.from_private_key_file('/home/auto/.ssh/id_rsa')
# # 创建SSH对象
# ssh = paramiko.SSHClient()
# # 允许连接不在know_hosts文件中的主机
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# # 连接服务器
# ssh.connect(hostname='192.168.7.250', port=22, username='root', key=private_key)
# # 执行命令
# stdin, stdout, stderr = ssh.exec_command('df')
# # 获取命令结果
# result = stdout.read()
# # 关闭连接
# ssh.close()


# 文件上传下载
# transport = paramiko.Transport(('192.168.7.250', 22))
# transport.connect(username='root', password='qazwsx')
# sftp = paramiko.SFTPClient.from_transport(transport)
# # 将test.ini 上传至服务器 /tmp/test.py
# sftp.put('test.ini', '/root/test.ini')
# # 将remove_path 下载到本地 local_path
# sftp.get('/root/t.log', 't.log')
# transport.close()

# 基于密钥的文件上传与下载
# private_key = paramiko.RSAKey.from_private_key_file('/home/id_sra')
# transport = paramiko.Transport(('192.168.7.250', 22))
# transport.connect(username='root', password=123456)
# sftp = paramiko.SFTPClient.from_transport(transport)
# sftp.put('test.ini', '/root/test.ini')
# # 将remove_path 下载到本地 local_path
# sftp.get('/root/t.log', 't.log')
# transport.close()