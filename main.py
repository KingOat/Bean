import Bean

if __name__ == '__main__':
    e: Bean.WindowResizeEvent = Bean.WindowResizeEvent(1280, 720)
    v: Bean.MouseButtonPressedEvent = Bean.MouseButtonPressedEvent(16)

    if v.is_in_category(Bean.EventCategory.EventCategoryApplication):
        Bean.BN_INFO(v)
    Bean.BN_DEBUG(e)

    app = Bean.Application()

