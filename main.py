import Bean

if __name__ == '__main__':
    logger = Bean.Log()

    logger.get_core_logger().debug("Hello")
    logger.get_core_logger().error("watch out")

    app = Bean.Application()

