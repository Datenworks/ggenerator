from subprocess import Popen, PIPE


class Shell(object):
    def __init__(self):
        pass

    def execute(self, command):
        process = Popen(command, stdout=PIPE, stderr=PIPE)
        output, error = process.communicate()
        if error or process.returncode > 0:
            raise ShellError(error.decode())

        return output.decode()


class ShellError(Exception):
    pass
