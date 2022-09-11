import os
import uuid

from django.db import models
from django.utils.deconstruct import deconstructible


@deconstructible
class PathAndRename:
    def __init__(self, sub_path: str) -> None:
        self.path = sub_path

    def __call__(self, instance: models.Model, filename: str) -> str:
        ext = filename.split(".")[-1]
        filename = f"{{{uuid.uuid4()}}}.{{{ext}}}"

        return os.path.join(self.path, filename)
