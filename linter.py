from typing import List

import typer
from typing_extensions import Annotated


def lint_file(file_name: str, verbose: bool):
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            if verbose:
                print(f"Linting {file_name}...")
            if verbose:
                print(f"Finished linting {file_name}...")
    except FileNotFoundError:
        print(f"{file_name} does not exist.")
    except IOError:
        print(f"Error reading {file_name}.")
    except:
        print(f"Other error with {file_name}.")


app = typer.Typer(help="Lint provided GDScript files.", no_args_is_help=True,context_settings={"help_option_names": ["-h", "--help"]})

@app.command()
def lint_files(
    files: Annotated[List[str], typer.Argument(help="Files to lint")],
    verbose: Annotated[bool, typer.Option("--verbose", "-v", help="Enable verbose output")] = False
):
    """
    Lint provided GDScript files.
    """
    for file in files:
        lint_file(file, verbose)


if __name__ == "__main__":
    app()

