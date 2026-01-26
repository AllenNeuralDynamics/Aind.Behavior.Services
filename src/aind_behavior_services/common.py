from typing import Annotated, List

from pydantic import BaseModel, Field, RootModel


class Point2f(BaseModel):
    """Represents a 2D point with float coordinates."""

    x: float = Field(description="X coordinate of the point (px)")
    y: float = Field(description="Y coordinate of the point (px)")


class Rect(BaseModel):
    """Represents a rectangle defined by its top-left corner, width, and height."""

    x: int = Field(default=0, ge=0, description="X coordinate of the top-left corner")
    y: int = Field(default=0, ge=0, description="Y coordinate of the top-left corner")
    width: int = Field(default=0, ge=0, description="Width of the rectangle")
    height: int = Field(default=0, ge=0, description="Height of the rectangle")


class Circle(BaseModel):
    """Represents a circle defined by its center point and radius."""

    center: Point2f = Field(default=Point2f(x=0, y=0), description="Center of the circle (px)", validate_default=True)
    radius: float = Field(default=1, ge=0, description="Radius of the circle (px)")


class Vector3(BaseModel):
    """Represents a 3D vector with float coordinates."""

    x: float = Field(default=0, description="X coordinate of the vector")
    y: float = Field(default=0, description="Y coordinate of the vector")
    z: float = Field(default=0, description="Z coordinate of the vector")



ValuePair = Annotated[List[float], Field(min_length=2, max_length=2)]


class LookUpTable(RootModel):
    """A lookup table consisting of pairs of float values."""
    root: List[ValuePair] = Field(validate_default=True, min_length=2)
