from typing import TypeVar, Type, Iterable, Dict, List, Union, get_args, Tuple, Optional
import pydantic

from aind_behavior_services.rig import CameraController, CameraTypes, AindBehaviorRigModel

T = TypeVar("T")


def get_cameras(
    rig_instance: AindBehaviorRigModel, exclude_without_video_writer: bool = True
) -> Dict[str, CameraTypes]:
    cameras: dict[str, CameraTypes] = {}
    camera_controllers = [x[1] for x in get_fields_of_type(rig_instance, CameraController)]

    for controller in camera_controllers:
        if exclude_without_video_writer:
            these_cameras = {k: v for k, v in controller.cameras.items() if v.video_writer is not None}
        else:
            these_cameras = controller.cameras
        cameras.update(these_cameras)
    return cameras


ISearchable = Union[pydantic.BaseModel, Dict, List]
_ISearchableTypeChecker = tuple(get_args(ISearchable))  # pre-compute for performance


def get_fields_of_type(
    searchable: ISearchable,
    target_type: Type[T],
    *args,
    is_recursive: bool = True,
    stop_recursion_on_type: bool = True,
    **kwargs,
) -> List[Tuple[Optional[str], T]]:
    _iterable: Iterable
    _is_type: bool
    result: List[Tuple[Optional[str], T]] = []

    if isinstance(searchable, dict):
        _iterable = searchable.items()
    elif isinstance(searchable, list):
        _iterable = list(zip([None for _ in range(len(searchable))], searchable))
    elif isinstance(searchable, pydantic.BaseModel):
        _iterable = {k: getattr(searchable, k) for k in searchable.model_fields.keys()}.items()
    else:
        raise ValueError(f"Unsupported model type: {type(searchable)}")

    for name, field in _iterable:
        _is_type = False
        if isinstance(field, target_type):
            result.append((name, field))
            _is_type = True
        if is_recursive and isinstance(field, _ISearchableTypeChecker) and not (stop_recursion_on_type and _is_type):
            result.extend(
                get_fields_of_type(
                    field,
                    target_type,
                    is_recursive=is_recursive,
                    stop_recursion_on_type=stop_recursion_on_type,
                )
            )
    return result
