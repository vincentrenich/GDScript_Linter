from typing import List

import typer
from typing_extensions import Annotated

from logger import Logger
from parsemachine import ParseMachine

_log_file_name = "logs/{date}_{time}.log"
logger: Logger

def lint_file(in_file_name: str, out_file_name: str):
    file_text: List[str] = []
    try:
        with open(in_file_name, "r", encoding="utf-8") as f:
            logger.log(f"Reading {in_file_name}")
            for line in f:
                out_line: str = parse_line(line)
            logger.log(f"Finished reading {in_file_name}")
    except FileNotFoundError:
        logger.log(f"{in_file_name} does not exist")
        return -1
    except IOError:
        logger.log(f"Error reading {in_file_name}")
        return -1
    logger.log(f"Linting {in_file_name}")
    logger.log(f"Finished linting {in_file_name}")
    try:
        with open(in_file_name, "w", encoding="utf-8") as f:
            logger.log(f"Writing to {out_file_name}")
            logger.log(f"Finished writing to {out_file_name}")
    except IOError:
        logger.log(f"Error writing {out_file_name}")
        return -1
    return 0


app = typer.Typer(help="Lint provided GDScript files.", no_args_is_help=True,context_settings={"help_option_names": ["-h", "--help"]})

@app.command()
def lint_files(
    in_files: Annotated[List[str], typer.Argument(help="Files to lint")],
    verbose: Annotated[bool, typer.Option("--verbose", "-v", help="Enable verbose output")] = False,
    out_files: Annotated[List[str], typer.Option("--output", "-o", help="Output files from linting. If fewer output files are specified than input files, the remaining input files will be overwritten")] = []
):
    """
    Lint provided GDScript files.
    """
    logger.verbose = verbose
    for i, in_file in enumerate(in_files):
        if i < len(out_files):
            out_file = out_files[i]
        else:
            out_file = in_file
        lint_file(in_file, out_file)


if __name__ == "__main__":
    logger = Logger(_log_file_name)
    app()

