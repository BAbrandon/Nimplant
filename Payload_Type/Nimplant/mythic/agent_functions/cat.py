from mythic_payloadtype_container.MythicCommandBase import *
import json


class CatArguments(TaskArguments):
    def __init__(self, command_line, **kwargs):
        super().__init__(command_line, **kwargs)
        self.args = []

    async def parse_arguments(self):
        pass


class CatCommand(CommandBase):
    cmd = "cat"
    needs_admin = False
    help_cmd = "cat [file path]"
    description = "Cat a file via nim functions."
    version = 2
    author = "@NotoriousRebel"
    argument_class = CatArguments
    attackmapping = ["T1005"]

    async def create_tasking(self, task: MythicTask) -> MythicTask:
        return task

    async def process_response(self, response: AgentResponse):
        pass