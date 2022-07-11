from .Event import Event, EventType, EventCategory
from overrides import overrides


class MouseMovedEvent(Event):

    def __init__(self, x: float, y: float) -> None:
        super().__init__()
        self.m_mouse_x, self.m_mouse_y = x, y

    def get_x(self) -> float: return self.m_mouse_x

    def get_y(self) -> float: return self.m_mouse_y

    @overrides
    def to_string(self) -> str:
        return f"MouseMovedEvent: ({self.m_mouse_x}, {self.m_mouse_y})"

    @staticmethod
    def get_static_type() -> EventType:
        return EventType.MouseMoved

    @overrides
    def get_event_type(self) -> EventType:
        return MouseMovedEvent.get_static_type()

    @overrides
    def get_name(self) -> str:
        return "MouseMoved"

    @overrides
    def get_category_flags(self) -> int:
        return EventCategory.EventCategoryMouse.value[0] | EventCategory.EventCategoryInput.value[0]


class MouseScrolledEvent(Event):

    def __init__(self, x_offset: float, y_offset: float) -> None:
        super().__init__()
        self.m_x_offset, self.m_y_offset = x_offset, y_offset

    def get_x_offset(self) -> float: return self.m_x_offset

    def get_y_offset(self) -> float: return self.m_y_offset

    @overrides
    def to_string(self) -> str:
        return f"MouseScrolledEvent: ({self.m_x_offset}, {self.m_y_offset})"

    @staticmethod
    def get_static_type() -> EventType:
        return EventType.MouseScrolled

    @overrides
    def get_event_type(self) -> EventType:
        return MouseScrolledEvent.get_static_type()

    @overrides
    def get_name(self) -> str:
        return "MouseScrolled"

    @overrides
    def get_category_flags(self) -> int:
        return EventCategory.EventCategoryMouse.value[0] | EventCategory.EventCategoryInput.value[0]


class MouseButtonEvent(Event):

    def __init__(self, mouse_code: int) -> None:
        super().__init__()
        self.m_button = mouse_code

    def get_mouse_button(self) -> int: return self.m_button

    @overrides
    def get_category_flags(self) -> int:
        return EventCategory.EventCategoryMouse.value[0] | EventCategory.EventCategoryInput.value[0] | EventCategory.EventCategoryMouseButton.value


class MouseButtonPressedEvent(MouseButtonEvent):

    def __init__(self, mouse_code: int) -> None:
        super().__init__(mouse_code)

    @overrides
    def to_string(self) -> str:
        return f"MouseButtonPressedEvent: {self.m_button}"

    @staticmethod
    def get_static_type() -> EventType:
        return EventType.MouseButtonPressed

    @overrides
    def get_event_type(self) -> EventType:
        return MouseButtonPressedEvent.get_static_type()

    @overrides
    def get_name(self) -> str:
        return "MouseButtonPressed"


class MouseButtonReleasedEvent(MouseButtonEvent):

    def __init__(self, mouse_code: int) -> None:
        super().__init__(mouse_code)

    @overrides
    def to_string(self) -> str:
        return f"MouseButtonReleasedEvent: {self.m_button}"

    @staticmethod
    def get_static_type() -> EventType:
        return EventType.MouseButtonReleased

    @overrides
    def get_event_type(self) -> EventType:
        return MouseButtonReleasedEvent.get_static_type()

    @overrides
    def get_name(self) -> str:
        return "MouseButtonReleased"


__all__ = [
    "MouseMovedEvent", "MouseScrolledEvent",
    "MouseButtonPressedEvent", "MouseButtonReleasedEvent"
]
