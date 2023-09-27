class OpenFile:
    """Context manager for files"""

    def __init__(self, file, method):
        self.file = open(file, method)

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

