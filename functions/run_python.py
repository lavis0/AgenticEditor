import os
import subprocess
from google.genai import types

def run_python(working_directory, file_path):
    working_dir_abs = os.path.abspath(working_directory)
    file_path_abs = ''

    if file_path:
        file_path_abs = os.path.abspath(os.path.join(working_directory, file_path))
    if not file_path_abs.startswith(working_dir_abs):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(file_path_abs):
        return f'Error: File "{file_path}" not found.'
    if not file_path_abs.endswith('py'):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        process_output = subprocess.run(['python3', file_path_abs],
                                        cwd=working_dir_abs,
                                        timeout=30,
                                        capture_output=True)
        stdout = process_output.stdout.decode('utf-8')
        stderr = process_output.stderr.decode('utf-8')
    except Exception as e:
        return f"Error: executing Python file: {e}"

    output_return_code = process_output.returncode
    output_stdout = 'STDOUT:'
    output_stderr = 'STDERR:'

    output = (output_stdout + '\n'
              + stdout + '\n'
              + output_stderr + '\n'
              + stderr + '\n')

    if output_return_code != 0:
        output += f'Process exited with code {output_return_code}.'

    if (len(stdout) + len(stderr)) == 0:
        return 'No output produced.'

    return output

schema_run_python = types.FunctionDeclaration(
        name="run_python",
        description="Returns the stdout, stderr and return code (if failed)"
                    "of a python file in a specified location,"
                    "constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="The path to the python file to run/execute,"
                                "relative to the working directory. ",
                ),
            },
        ),
    )