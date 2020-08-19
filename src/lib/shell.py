from subprocess import Popen, PIPE


class Shell(object):
    def __init__(self):
        pass

    def execute(self, command):
        returncode, output, error = self.execute_command(command)
        if returncode > 0 and error:
            raise ShellError(error.decode())

        return output.decode()

    def execute_command(self, command):
        process = Popen(command, stdout=PIPE, stderr=PIPE)
        output, error = process.communicate()
        return process.returncode, output, error


class ShellError(Exception):
    pass
