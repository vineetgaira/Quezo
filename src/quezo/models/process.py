from dataclasses import dataclass


@dataclass
class Process:
    process_id: str
    arrival_time: int
    burst_time: int
    priority: int
    dependencies: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        self.validate_process_id()
        self.validate_other()

    def validate_process_id(self) -> None:
        if not isinstance(self.process_id, str):
            raise TypeError("process_id must be string.")

        if not self.process_id.strip():
            raise ValueError("process_id cannot be empty or whitespace.")

    def validate_other(self) -> None:
        fields = {
            "arrival_time": self.arrival_time,
            "burst_time": self.burst_time,
            "priority": self.priority,
        }

        for name, value in fields.items():
            if type(value) is not int:
                raise TypeError(f"{name} must be integer.")

        if self.arrival_time < 0:
            raise ValueError("arrival_time cannot be negative.")

        if self.burst_time <= 0:
            raise ValueError("burst_time must be greater than zero.")

        if self.priority < 0:
            raise ValueError("priority cannot be negative.")

        if not isinstance(self.dependencies, tuple):
            raise TypeError("dependencies must be tuple.")

        if not all(
            isinstance(dependency, str) and dependency.strip()
            for dependency in self.dependencies
        ):
            raise ValueError("dependencies must contain non-empty strings.")
