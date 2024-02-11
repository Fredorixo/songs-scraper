from .main import main
from asyncio import run
from apify.log import ActorLogFormatter
from logging import StreamHandler, getLogger, DEBUG, INFO

handler = StreamHandler()
handler.setFormatter(ActorLogFormatter())

apify_logger = getLogger('apify')
apify_logger.setLevel(DEBUG)
apify_logger.addHandler(handler)

run(main())