import datetime

class Logger:
    log_file_name: str
    verbose: bool

    def __init__(self, log_file_name: str, verbose: bool = False) -> None:
        date_time = datetime.datetime.now(datetime.UTC)
        self.log_file_name = log_file_name.format(date=date_time.strftime("%Y%m%d"), time=date_time.strftime("%H%M%S"))
        self.verbose = verbose

    def log(self, message: str, verbose: bool = False) -> bool:
        if self.verbose or verbose:
            print(message)
        try:
            with open(self.log_file_name, "a", encoding="utf-8") as f:
                f.write(f"[{datetime.datetime.now(datetime.UTC)}] {message}\n")
        except IOError:
            print(f"Error writing {self.log_file_name}.")
            return False
        return True
