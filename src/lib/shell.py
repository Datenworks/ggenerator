from subprocess import Popen, PIPE


class Shell(object):
    def __init__(self):
        pass

    def execute(self, command):
        process = Popen(command, stdout=PIPE)
        output, error = process.communicate()

        if error:
            raise ShellError(error)

        return output.decode()


class ShellError(Exception):
    pass
