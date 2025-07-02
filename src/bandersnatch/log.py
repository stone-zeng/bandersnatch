# This is mainly factored out into a separate module so I can ignore it in
# coverage analysis. Unfortunately this is really hard to test as the Python
# logging module won't allow reasonable teardown. :(
import logging
from typing import Any


def setup_logging(args: Any):
    logging.basicConfig(
        format="%(asctime)s %(levelname)s: %(message)s (%(filename)s:%(lineno)d)"
    )
    logger = logging.getLogger("bandersnatch")
    logger.setLevel(logging.DEBUG if args.debug else logging.INFO)
