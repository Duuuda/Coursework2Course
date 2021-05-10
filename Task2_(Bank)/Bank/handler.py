from Bank import commands
from django.conf import settings


def handler(input_text: str) -> str:
    def _unknown_command(*_, **__):
        return 'Unknown command'

    output_text = list()
    input_text = input_text.replace('\r', '')
    for num, line in enumerate(input_text.split('\n')):
        if num < settings.MAXIMUM_NUMBER_OF_COMMANDS:
            if line != '' and not line.isspace():
                sliced_line = line.split()
                command_name, arguments = sliced_line[0].strip().lower(), sliced_line[1:]
                command = getattr(commands, command_name, _unknown_command)
                output_text.append(command(*arguments))
            else:
                output_text.append('Unknown command')
        else:
            break
    return '\n'.join(output_text)

# def handler(script: str) -> str:
#     def _unknown_command(*_, **__):
#         print(_, __)
#         return 'Unknown command'
#
#     result = list()
#     n = 0
#     print(script.split('\n'))
#     for line in script.split('\n'):
#         if n < settings.COMMANDS_MAX_COUNT:
#             if line != '' and not line.isspace():
#                 words = line.split()
#                 command_name, arguments = words[0], words[1:]
#                 print(command_name)
#                 result.append(getattr(commands, command_name.lower(), _unknown_command)(*arguments))
#         else:
#             break
#         n += 1
#     if len(result):
#         return '\n'.join(result)
#     else:
#         return 'Enter the commands!!!'
