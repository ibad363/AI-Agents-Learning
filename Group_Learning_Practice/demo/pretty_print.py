from pydantic import BaseModel
from dataclasses import asdict, is_dataclass
from typing import Any
from rich import print_json
import inspect
import json

def serialize(obj: Any) -> Any:
    if isinstance(obj, BaseModel):
        return serialize(obj.dict())
    elif is_dataclass(obj):
        return serialize(asdict(obj))
    elif isinstance(obj, dict):
        return {
            str(k): serialize(v)
            for k, v in obj.items()
            if not inspect.isroutine(v) and not inspect.isfunction(v)
        }
    elif isinstance(obj, (list, tuple, set)):
        return [serialize(v) for v in obj]
    elif hasattr(obj, "__dict__"):
        return serialize({
            k: v for k, v in vars(obj).items()
            if not inspect.isroutine(v) and not inspect.isfunction(v)
        })
    else:
        try:
            json.dumps(obj)
            return obj
        except TypeError:
            return str(obj)

def print_pretty_json(data: Any):
    try:
        serialized_data = serialize(data)
        print_json(data=serialized_data)
    except Exception as e:
        print(f"[!] Failed to serialize object: {e}")
        print(repr(data))