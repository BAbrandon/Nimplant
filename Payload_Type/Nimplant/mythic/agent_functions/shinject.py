from CommandBase import *
import json
from MythicFileRPC import *


class ShInjectArguments(TaskArguments):

    def __init__(self, command_line):
        super().__init__(command_line)
        self.args = {
            "pid": CommandParameter(name="PID", type=ParameterType.Number),
            "shellcode": CommandParameter(name="Shellcode File", type=ParameterType.File)
        }

    async def parse_arguments(self):
        if len(self.command_line) == 0:
            raise Exception("No arguments given.\n\tUsage: {}".format(ShInjectCommand.help_cmd))
        if self.command_line[0] != "{":
            raise Exception("Require JSON blob, but got raw command line.\n\tUsage: {}".format(ShInjectCommand.help_cmd))
        self.load_args_from_json_string(self.command_line)
        


class ShInjectCommand(CommandBase):
    cmd = "shinject"
    needs_admin = False
    help_cmd = "shinject (modal popup)"
    description = "Inject shellcode into a remote process."
    version = 1
    is_exit = False
    is_file_browse = False
    is_process_list = False
    is_download_file = False
    is_upload_file = False
    is_remove_file = False
    author = "@NotoriousRebel"
    argument_class = ShInjectArguments
    attackmapping = []

    async def create_tasking(self, task: MythicTask) -> MythicTask:
        resp = await MythicFileRPC(task).register_file(task.args.get_arg("shellcode"))
        if resp.status == MythicStatus.Success:
            task.args.add_arg("shellcode", resp.agent_file_id)
        else:
            raise Exception(f"Failed to host shellcode file: {resp.error_message}")
        return task

    async def process_response(self, response: AgentResponse):
        pass