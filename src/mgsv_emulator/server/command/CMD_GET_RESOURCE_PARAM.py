from command.Command import Command

class CMD_GET_RESOURCE_PARAM(Command):

    def execute(self, data):
        return self._receiver.action(data)

