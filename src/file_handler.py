class FileHandler:

    @staticmethod
    def read(filename: str) -> str:
        return open(filename).read()

    @staticmethod
    def write(filename: str, content) -> None:
        file = open(filename, "w")
        file.write(content)
        file.close()