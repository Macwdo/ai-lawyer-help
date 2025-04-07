import tempfile
from contextlib import contextmanager


class FileUtils:
    def __init__(self):
        pass

    @contextmanager
    def temp_folder(self):
        tempfile.tempdir = tempfile.TemporaryDirectory()
        try:
            yield tempfile.tempdir.name

        finally:
            tempfile.tempdir.cleanup()

    @contextmanager
    def copy_bytes_to_temp_file(self, bytes: bytes, extension: str):
        with tempfile.NamedTemporaryFile(suffix=extension) as tmp_file:
            try:
                tmp_file.write(bytes)
                tmp_file.flush()
                yield tmp_file.name

            finally:
                tmp_file.close()

    @contextmanager
    def write_tmp_pdf(self, bytes: bytes):
        with self.copy_bytes_to_temp_file(bytes=bytes, extension=".pdf") as tmp_path:
            yield tmp_path
