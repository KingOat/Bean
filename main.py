import Bean

if __name__ == '__main__':
    Bean.BN_DEBUG("debug")
    Bean.BN_INFO("info")
    Bean.BN_WARNING("Warning")
    Bean.BN_ERROR("Error")
    Bean.BN_CRITICAL("critical")

    app = Bean.Application()

