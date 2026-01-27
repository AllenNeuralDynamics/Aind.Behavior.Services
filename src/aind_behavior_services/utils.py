import datetime
import logging
import os
import subprocess
from os import PathLike
from pathlib import Path
from string import capwords
from subprocess import CompletedProcess
from typing import Dict, Iterable, List, Optional, Tuple, Type, TypeVar, Union, cast, get_args

import pydantic
from pydantic import BaseModel

logger = logging.getLogger(__name__)


T = TypeVar("T")

TModel = TypeVar("TModel", bound=BaseModel)


def snake_to_pascal_case(s: str) -> str:
    """
    Converts a snake_case string to PascalCase.

    Args:
        s (str): The snake_case string to be converted.

    Returns:
        str: The PascalCase string.
    """
    return "".join(map(capwords, s.split("_")))


def pascal_to_snake_case(s: str) -> str:
    """
    Converts a PascalCase string to snake_case.

    Args:
        s (str): The PascalCase string to be converted.

    Returns:
        str: The snake_case string.
    """
    result = ""
    for i, char in enumerate(s):
        if char.isupper():
            if i != 0:
                result += "_"
            result += char.lower()
        else:
            result += char
    return result


def screaming_snake_case_to_pascal_case(s: str) -> str:
    """
    Converts a SCREAMING_SNAKE_CASE string to PascalCase.

    Args:
        s (str): The SCREAMING_SNAKE_CASE string to be converted.

    Returns:
        str: The PascalCase string.
    """
    words = s.split("_")
    return "".join(word.capitalize() for word in words)


def _build_bonsai_process_command(
    workflow_file: PathLike | str,
    bonsai_exe: PathLike | str = "bonsai/bonsai.exe",
    is_editor_mode: bool = True,
    is_start_flag: bool = True,
    layout: Optional[PathLike | str] = None,
    additional_properties: Optional[Dict[str, str]] = None,
) -> str:
    output_cmd: str = f'"{bonsai_exe}" "{workflow_file}"'
    if is_editor_mode:
        if is_start_flag:
            output_cmd += " --start"
    else:
        output_cmd += " --no-editor"
        if layout is not None:
            output_cmd += f' --visualizer-layout:"{layout}"'

    if additional_properties:
        for param, value in additional_properties.items():
            output_cmd += f' -p:"{param}"="{value}"'

    return output_cmd


def run_bonsai_process(
    workflow_file: PathLike | str,
    bonsai_exe: PathLike | str = "bonsai/bonsai.exe",
    is_editor_mode: bool = True,
    is_start_flag: bool = True,
    layout: Optional[PathLike | str] = None,
    additional_properties: Optional[Dict[str, str]] = None,
    cwd: Optional[PathLike | str] = None,
    timeout: Optional[float] = None,
    print_cmd: bool = False,
) -> CompletedProcess:
    if not Path(bonsai_exe).exists():
        has_setup = (Path(bonsai_exe).parent / "setup.ps1").exists()
        m = f"Bonsai executable not found at {bonsai_exe}." + (
            " A 'setup.ps1' file exists in the target directory, consider running it." if has_setup else ""
        )
        raise FileNotFoundError(m)

    output_cmd = _build_bonsai_process_command(
        workflow_file=workflow_file,
        bonsai_exe=bonsai_exe,
        is_editor_mode=is_editor_mode,
        is_start_flag=is_start_flag,
        layout=layout,
        additional_properties=additional_properties,
    )
    if cwd is None:
        cwd = os.getcwd()
    if print_cmd:
        logging.debug(output_cmd)
    return subprocess.run(output_cmd, cwd=cwd, check=True, timeout=timeout, capture_output=True)


def open_bonsai_process(
    workflow_file: PathLike | str,
    bonsai_exe: PathLike | str = "bonsai/bonsai.exe",
    is_editor_mode: bool = True,
    is_start_flag: bool = True,
    layout: Optional[PathLike | str] = None,
    additional_properties: Optional[Dict[str, str]] = None,
    log_file_name: Optional[str] = None,
    cwd: Optional[PathLike | str] = None,
    creation_flags: Optional[int] = None,
    print_cmd: bool = False,
) -> subprocess.Popen:
    output_cmd = _build_bonsai_process_command(
        workflow_file=workflow_file,
        bonsai_exe=bonsai_exe,
        is_editor_mode=is_editor_mode,
        is_start_flag=is_start_flag,
        layout=layout,
        additional_properties=additional_properties,
    )

    if cwd is None:
        cwd = os.getcwd()
    if creation_flags is None:
        creation_flags = subprocess.CREATE_NEW_CONSOLE

    if log_file_name is None:
        if print_cmd:
            logging.debug(output_cmd)
        return subprocess.Popen(output_cmd, cwd=cwd, creationflags=creation_flags)
    else:
        logging_cmd = f'powershell -ep Bypass -c "& {output_cmd} *>&1 | tee -a {log_file_name}"'
        if print_cmd:
            logging.debug(logging_cmd)
        return subprocess.Popen(logging_cmd, cwd=cwd, creationflags=creation_flags)


def format_datetime(value: datetime.datetime, is_tz_strict: bool = False) -> str:
    if value.tzinfo is None:
        if is_tz_strict:
            raise ValueError("Datetime object must be timezone-aware")
        return value.strftime("%Y-%m-%dT%H%M%S")
    elif value.tzinfo.utcoffset(value) == datetime.timedelta(0):
        return value.strftime("%Y-%m-%dT%H%M%SZ")
    else:
        return value.strftime("%Y-%m-%dT%H%M%S%z")


def now() -> datetime.datetime:
    """Returns the current time as a timezone unaware datetime."""
    return datetime.datetime.now()


def utcnow() -> datetime.datetime:
    """Returns the current time as a timezone aware datetime in UTC."""
    return datetime.datetime.now(datetime.timezone.utc)


def tznow() -> datetime.datetime:
    """Returns the current time as a timezone aware datetime in the local timezone."""
    return utcnow().astimezone()


def model_from_json_file(json_path: os.PathLike | str, model: type[TModel]) -> TModel:
    with open(Path(json_path), "r", encoding="utf-8") as file:
        return model.model_validate_json(file.read())


ISearchable = Union[pydantic.BaseModel, Dict, List]
_ISearchableTypeChecker = tuple(get_args(ISearchable))  # pre-compute for performance


def get_fields_of_type(
    searchable: ISearchable,
    target_type: Type[T],
    *,
    recursive: bool = True,
    stop_recursion_on_type: bool = True,
) -> List[Tuple[Optional[str], T]]:
    _iterable: Iterable
    _is_type: bool
    result: List[Tuple[Optional[str], T]] = []

    if isinstance(searchable, dict):
        _iterable = searchable.items()
    elif isinstance(searchable, list):
        _iterable = list(zip([None for _ in range(len(searchable))], searchable))
    elif isinstance(searchable, pydantic.BaseModel):
        _iterable = {k: getattr(searchable, k) for k in type(searchable).model_fields.keys()}.items()
    else:
        raise ValueError(f"Unsupported model type: {type(searchable)}")

    for name, field in _iterable:
        _is_type = False
        if isinstance(field, target_type):
            result.append((name, field))
            _is_type = True
        if recursive and isinstance(field, _ISearchableTypeChecker) and not (stop_recursion_on_type and _is_type):
            result.extend(
                get_fields_of_type(
                    cast(ISearchable, field),
                    target_type,
                    recursive=recursive,
                    stop_recursion_on_type=stop_recursion_on_type,
                )
            )
    return result


def get_commit_hash(repository: Optional[PathLike] = None) -> str:
    """Get the commit hash of the repository."""
    import git

    if repository is None:
        repo = git.Repo(search_parent_directories=True)
    else:
        repo = git.Repo(repository)
    return repo.head.commit.hexsha
