def run_python_code(code: str, expected_output: str) -> bool:
    import subprocess

    # Execute the provided Python code
    process = subprocess.Popen(
        ['python3', '-c', code],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    stdout, stderr = process.communicate()

    # Decode the output and error messages
    output = stdout.decode().strip()
    error = stderr.decode().strip()

    # Check for errors during execution
    if error:
        print(f"Error: {error}")
        return False

    # Validate the output against the expected output
    return output == expected_output