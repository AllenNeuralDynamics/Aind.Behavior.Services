# Import core types
from typing import List, Literal, Optional, Self

from pydantic import Field, model_validator

import aind_behavior_services.utils
from aind_behavior_services import __semver__
from aind_behavior_services.base import DefaultAwareDatetime, SchemaVersionedModel


class AindBehaviorSessionModel(SchemaVersionedModel):
    version: Literal[__semver__] = __semver__
    experiment: Optional[str] = Field(default=None, description="Name of the experiment")
    experimenter: List[str] = Field(default=[], description="Name of the experimenter")
    date: DefaultAwareDatetime = Field(
        default_factory=aind_behavior_services.utils.utcnow, description="Date of the experiment", validate_default=True
    )
    root_path: str = Field(..., description="Root path where data will be logged")
    session_name: Optional[str] = Field(
        default=None,
        description="Name of the session. This will be used to create a folder in the root path. If not provided, it will be generated using subject and date.",
    )
    subject: str = Field(..., description="Name of the subject")
    experiment_version: str = Field(
        default="",
        description="Version of the experiment",
        deprecated="This field is deprecated and will be removed in future versions.",
    )
    notes: Optional[str] = Field(default=None, description="Notes about the experiment")
    commit_hash: Optional[str] = Field(default=None, description="Commit hash of the repository")
    allow_dirty_repo: bool = Field(default=False, description="Allow running from a dirty repository")
    skip_hardware_validation: bool = Field(default=False, description="Skip hardware validation")

    @model_validator(mode="after")
    def generate_session_name_default(self) -> Self:
        if self.session_name is None:
            self.session_name = f"{self.subject}_{aind_behavior_services.utils.format_datetime(self.date)}"
        return self
