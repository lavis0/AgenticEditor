from google.genai import types

from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.run_python import schema_run_python
from functions.write_file import schema_write_file

from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.run_python import run_python
from functions.write_file import write_file

from config import WORKING_DIR

def call_function(call, verbose=False):
    if verbose:
        print(f'Calling function: {call.name}({call.args})')
    else:
        print(f' - Calling function: {call.name}')

    func_dict = {
        'get_files_info': get_files_info,
        'get_file_content': get_file_content,
        'run_python': run_python,
        'write_file': write_file
    }

    if call.name in func_dict:
        # prevent modifications to working_directory
        args = dict(call.args)
        args["working_directory"] = WORKING_DIR

        result = func_dict[call.name](**call.args)
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=call.name,
                    response={"result": result},
                )
            ],
        )
    else:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=call.name,
                    response={"error": f"Unknown function: {call.name}"},
                )
            ],
        )


available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python,
        schema_write_file,
    ]
)