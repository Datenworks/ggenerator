from subprocess import Popen, PIPE


class Shell(object):
    def __init__(self):
        pass

    def execute(self, command):
        process = Popen(command, stdout=PIPE, stderr=PIPE)
        output, error = process.communicate()
        if process.returncode > 0 and error:
            raise ShellError(error.decode())

        return output.decode()


class ShellError(Exception):
    pass
