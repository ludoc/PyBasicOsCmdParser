from subprocess import Popen, PIPE
class BasicOsCmdParser:

    def hostnameFqdn(self):
        p = Popen(['/bin/hostname', '-f'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output, err = p.communicate()
        return output.decode("utf-8")[:-1]

    def passwdInfo(self):
        p = Popen(['/bin/cat', '/etc/passwd'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output, err = p.communicate()
        output = output.decode("utf-8")[:-1].split('\n')
        result = {}
        for user in output:
            parsedUser = user.split(':')
            result[parsedUser[0]] = ({'username' : parsedUser[0],
                            'password' : parsedUser[1],
                            'uid' : parsedUser[2],
                            'gid' : parsedUser[3],
                            'user_info' : parsedUser[4],
                            'home' : parsedUser[5],
                            'shell' : parsedUser[6]})
        return result

    def shadowInfo(self):
        p = Popen(['/bin/cat', '/etc/shadow'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output, err = p.communicate()
        output = output.decode("utf-8")[:-1].split('\n')
        result = {}
        for user in output:
            parsedUser = user.split(':')
            result[parsedUser[0]] = ({'username' : parsedUser[0],
                            'password' : parsedUser[1],
                            'lastchanged' : parsedUser[2],
                            'min_day' : parsedUser[3],
                            'password_expire' : parsedUser[4],
                            'warn' : parsedUser[5],
                            'inactive' : parsedUser[6],
                            'account_expire' : parsedUser[7]})
        return result
