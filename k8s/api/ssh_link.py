import paramiko

def ssh_linking(cmd):
    #创建ssh对象
    ssh = paramiko.SSHClient()
    #允许连接不在knows_hosts文件中的主机
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #连接服务器
    ssh.connect(hostname='192.168.10.17', port=22, username='root', password='123456')
    # 执行命令
    stdin, stdout, stderr = ssh.exec_command(cmd)
    # 获取命令结果
    result = stdout.read()
    # 关闭连接
    ssh.close()
    # print("api输出:",result.decode('utf-8'))

    return result.decode('utf-8')





