from pathlib import Path

class RTMValidatorError(Exception):
    pass


class RTMValidatorFileNotFoundError(RTMValidatorError):
    pass


# try:
#     raise RTMValidatorFileNotFoundError("\nSilly goose, that file doesn't exist!")
# except RTMValidatorError as e:
#     print(e)

path = Path('.')
print(path)
print(path.exists())
print(path.suffix in '.xlsx .xls'.split())
