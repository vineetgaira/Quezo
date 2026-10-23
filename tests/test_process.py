import pytest

from quezo.models.process import Process


def make_process(**overrides: object) -> Process:
    values: dict[str, object] = {
        "process_id": "P1",
        "arrival_time": 1,
        "burst_time": 5,
        "priority": 2,
    }
    values.update(overrides)
    return Process(**values)  # type: ignore[arg-type]


def test_validate_process_id_accepts_non_empty_string() -> None:
    make_process(process_id=" P1 ").validate_process_id()


@pytest.mark.parametrize("process_id", [None, 1, []])
def test_validate_process_id_rejects_non_string(process_id: object) -> None:
    with pytest.raises(TypeError, match="process_id must be string"):
        make_process(process_id=process_id).validate_process_id()


@pytest.mark.parametrize("process_id", ["", " ", "\t\n"])
def test_validate_process_id_rejects_empty_or_whitespace(process_id: str) -> None:
    with pytest.raises(ValueError, match="process_id cannot be empty or whitespace"):
        make_process(process_id=process_id).validate_process_id()


def test_validate_other_accepts_valid_values_and_empty_dependencies() -> None:
    make_process().validate_other()


def test_validate_other_accepts_valid_dependencies() -> None:
    make_process(dependencies=("P0", "P2")).validate_other()


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("arrival_time", "1"),
        ("arrival_time", True),
        ("burst_time", 5.0),
        ("priority", None),
    ],
)
def test_validate_other_requires_integer_fields(field: str, value: object) -> None:
    with pytest.raises(TypeError, match=f"{field} must be integer"):
        make_process(**{field: value}).validate_other()


@pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        ("arrival_time", -1, "arrival_time cannot be negative"),
        ("burst_time", 0, "burst_time must be greater than zero"),
        ("burst_time", -1, "burst_time must be greater than zero"),
        ("priority", -1, "priority cannot be negative"),
    ],
)
def test_validate_other_rejects_out_of_range_values(
    field: str, value: int, message: str
) -> None:
    with pytest.raises(ValueError, match=message):
        make_process(**{field: value}).validate_other()


@pytest.mark.parametrize("dependencies", [[], ["P0"], "P0", None])
def test_validate_other_requires_dependencies_tuple(dependencies: object) -> None:
    with pytest.raises(TypeError, match="dependencies must be tuple"):
        make_process(dependencies=dependencies).validate_other()


@pytest.mark.parametrize("dependencies", [("P0", " "), ("P0", ""), ("P0", 2)])
def test_validate_other_rejects_invalid_dependency_entries(
    dependencies: tuple[object, ...],
) -> None:
    with pytest.raises(ValueError, match="dependencies must contain non-empty strings"):
        make_process(dependencies=dependencies).validate_other()
