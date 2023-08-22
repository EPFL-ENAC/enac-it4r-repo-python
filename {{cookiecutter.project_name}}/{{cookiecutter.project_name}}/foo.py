import sys
import appeal
app = appeal.Appeal()


def bar() -> str:
    """Returns the Python version used to run this script.

    Returns
    -------
    str
        Python version
    """
    return sys.version


@app.command()
def hello(name : str) -> None:
    """Prints a greeting to the console.

    Parameters
    ----------
    name : str
        Name of the person to greet
    """
    print(f"Hello, {name}!")


app.main()
