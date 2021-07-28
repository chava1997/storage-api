from os import environ
from mimetypes import guess_type
from pathlib import Path

try:
    storage_dir = Path(environ["STORAGE_DIR"]).resolve()
except KeyError:
    print("No storage directory set")
    storage_dir = None


def get_file_to_store(collection, filename, update=False):
    target = (storage_dir / collection / filename)
    if target.exists() and not update:
        raise Exception("File already exists")
    target.parent.mkdir(exist_ok=True, parents=True)
    return target


def store_bytes(collection, filename, blob, update=False):
    target = get_file_to_store(collection, filename, update=update)
    target.write_bytes(blob)


def store_string(collection, filename, text, update=False):
    target = get_file_to_store(collection, filename, update=update)
    target.write_text(text)


def query_storage(path=""):
    target = (storage_dir / path)
    if not target.exists():
        raise Exception("Does not exists")
    elif target.is_dir():
        return dict(
            path=str(target.relative_to(storage_dir)),
            type="directory",
            content=[str(p.relative_to(storage_dir)) for p in target.iterdir()]
        )
    elif target.is_file():
        mime = (guess_type(str(target)) or ["application/octet-stream"])[0]
        return dict(
            path=str(target.relative_to(storage_dir)),
            type="file",
            metadata=dict(
                mime=mime,
                size=target.stat().st_size,
            )
        )
    return {}


def get_storage_file(path=""):
    target = (storage_dir / path)
    if not target.exists() or not target.is_file():
        raise Exception("Does not exists")
    mime = (guess_type(str(target)) or ["application/octet-stream"])[0]
    return mime, target.read_bytes()
