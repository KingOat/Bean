from .Event import Event, EventType, EventCategory
from overrides import overrides


class KeyEvent(Event):

    def __init__(self, keycode: int) -> None:
        super().__init__()
        self.m_keycode = keycode

    def get_key_code(self) -> int: return self.m_keycode

    @overrides
    def get_category_flags(self) -> int:
        return EventCategory.EventCategoryKeyBoard.value[0] | EventCategory.EventCategoryInput.value[0]


class KeyPressedEvent(KeyEvent):

    def __init__(self, keycode: int, is_repeat: bool) -> None:
        super().__init__(keycode)
        self.m_is_repeat = is_repeat

    @overrides
    def to_string(self) -> str:
        return f"KeyPressedEvent: {self.m_keycode}, (repeat = {self.m_is_repeat})"

    @staticmethod
    def get_static_type() -> EventType:
        return EventType.KeyPressed

    @overrides
    def get_event_type(self) -> EventType:
        return KeyPressedEvent.get_static_type()

    @overrides
    def get_name(self) -> str:
        return "KeyPressed"


class KeyReleasedEvent(KeyEvent):

    def __init__(self, keycode: int) -> None:
        super().__init__(keycode)

    @overrides
    def to_string(self) -> str:
        return f"KeyReleasedEvent: {self.m_keycode}"

    @staticmethod
    def get_static_type() -> EventType:
        return EventType.KeyReleased

    @overrides
    def get_event_type(self) -> EventType:
        return KeyReleasedEvent.get_static_type()

    @overrides
    def get_name(self) -> str:
        return "KeyReleased"


__all__ = [
    "KeyPressedEvent", "KeyReleasedEvent"
]
