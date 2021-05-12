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
