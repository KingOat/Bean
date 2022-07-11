from .Event import Event, EventType, EventCategory
from overrides import overrides


class WindowResizeEvent(Event):

    def __init__(self, width: int, height: int) -> None:
        super().__init__()
        self.m_width, self.m_height = width, height

    def get_width(self) -> int: return self.m_width

    def get_height(self) -> int: return self.m_height

    @overrides
    def to_string(self) -> str:
        return f"WindowResizeEvent: ({self.m_width}, {self.m_height})"

    @staticmethod
    def get_static_type() -> EventType:
        return EventType.WindowResize

    @overrides
    def get_event_type(self) -> EventType:
        return WindowResizeEvent.get_static_type()

    @overrides
    def get_name(self) -> str:
        return "WindowResize"

    @overrides
    def get_category_flags(self) -> int:
        return EventCategory.EventCategoryApplication.value[0]


class WindowCloseEvent(Event):

    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def get_static_type() -> EventType:
        return EventType.WindowClose

    @overrides
    def get_event_type(self) -> EventType:
        return WindowCloseEvent.get_static_type()

    @overrides
    def get_name(self) -> str:
        return "WindowClose"

    @overrides
    def get_category_flags(self) -> int:
        return EventCategory.EventCategoryApplication.value[0]


class AppTickEvent(Event):

    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def get_static_type() -> EventType:
        return EventType.AppTick

    @overrides
    def get_event_type(self) -> EventType:
        return AppTickEvent.get_static_type()

    @overrides
    def get_name(self) -> str:
        return "AppTick"

    @overrides
    def get_category_flags(self) -> int:
        return EventCategory.EventCategoryApplication.value[0]


class AppUpdateEvent(Event):

    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def get_static_type() -> EventType:
        return EventType.AppUpdate

    @overrides
    def get_event_type(self) -> EventType:
        return AppUpdateEvent.get_static_type()

    @overrides
    def get_name(self) -> str:
        return "AppUpdate"

    @overrides
    def get_category_flags(self) -> int:
        return EventCategory.EventCategoryApplication.value[0]


class AppRenderEvent(Event):

    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def get_static_type() -> EventType:
        return EventType.AppRender

    @overrides
    def get_event_type(self) -> EventType:
        return AppRenderEvent.get_static_type()

    @overrides
    def get_name(self) -> str:
        return "AppRender"

    @overrides
    def get_category_flags(self) -> int:
        return EventCategory.EventCategoryApplication.value[0]


__all__ = [
    "WindowResizeEvent", "WindowCloseEvent",
    "AppTickEvent", "AppUpdateEvent", "AppRenderEvent"
]
