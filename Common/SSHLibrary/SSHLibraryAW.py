#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Created on 2020年10月9日
@author: LiuBin
@note: excel operation
"""

import SSHLibrary


class SSHLibraryAW(SSHLibrary.SSHLibrary):
    def open_connection_login(self, ip, username, password, delay='0.5 seconds'):
        session = self.open_connection(host=ip, alias=None, port=22, timeout=None, newline=None, prompt=None,
                                       term_type=None, width=1024, height=None, path_separator=None, encoding=None)
        self.login(username, password, delay)
        return session

    def execute_cmd(self, session, command, timeout, cmd='#'):
        self.switch_connection(session)
        self.set_client_configuration(timeout)
        self.write(command)
        output = self.read_until(cmd)
        print(output)
        return output

if __name__ == '__main__':
    ssh_aw = SSHLibraryAW()
    connect_index = ssh_aw.open_connection_login('192.168.47.128', 'root', 'Huawei@123')
    ssh_aw.execute_cmd(connect_index,'mkdir /liubin01', 3, cmd='#')
