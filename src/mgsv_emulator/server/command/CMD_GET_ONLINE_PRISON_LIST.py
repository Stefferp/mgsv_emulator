from command.Command import Command

class CMD_GET_ONLINE_PRISON_LIST(Command):

    def execute(self, data):
        return self._receiver.action(data)
