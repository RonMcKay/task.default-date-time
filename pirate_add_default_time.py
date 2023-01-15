#!/usr/bin/python
from __future__ import print_function

from datetime import datetime, time

from tasklib import Task

DEFAULT_TIME = time(19, 0, 0)  # Your wanted default time


def is_local_midnight(timestamp: datetime) -> bool:
    return timestamp.astimezone(timestamp.astimezone().tzinfo).time() == time(
        0, 0, 0
    )


def set_default_time(timestamp: datetime) -> datetime:
    return timestamp.astimezone(timestamp.astimezone().tzinfo).replace(
        hour=DEFAULT_TIME.hour,
        minute=DEFAULT_TIME.minute,
        second=DEFAULT_TIME.second,
    )


def hook_default_time(task: Task) -> None:
    if task["due"] and is_local_midnight(task["due"]):
        task["due"] = set_default_time(task["due"])
        print("Default due time has been set.")
