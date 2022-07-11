from enum import Enum


def bit(x: int) -> int:
    return 1 << x


class EventType(Enum):
    Null = 0
    WindowClose, WindowResize, WindowFocus, WindowLostFocus, WindowMoved = range(1, 6)
    AppTick, AppUpdate, AppRender = range(6, 9)
    KeyPressed, KeyReleased, KeyTyped = range(9, 12)
    MouseButtonPressed, MouseButtonReleased, MouseMoved, MouseScrolled = range(12, 16)


class EventCategory(Enum):
    Null = 0
    EventCategoryApplication = bit(0)
    EventCategoryInput = bit(1),
    EventCategoryKeyBoard = bit(2),
    EventCategoryMouse = bit(3),
    EventCategoryMouseButton = bit(4)


class Event:

    def __init__(self) -> None:
        pass

    def get_event_type(self) -> EventType:
        pass

    def get_name(self) -> str:
        pass

    def get_category_flags(self) -> int:
        pass

    def to_string(self) -> str:
        pass

    def is_in_category(self, category: EventCategory) -> bool:
        return bool(self.get_category_flags() and category)

    def __repr__(self) -> str:
        return self.to_string()


class EventDispatcher:

    def __init__(self, event: Event) -> None:
        self.m_event = event

    def dispatch(self) -> bool:
        pass


__all__ = [
    "EventType", "EventCategory"
]
