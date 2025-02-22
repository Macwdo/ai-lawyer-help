from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent.parent

load_dotenv()

from .apps import *  # noqa
from .auth import *  # noqa
from .aws import *  # noqa
from .base import *  # noqa
from .database import *  # noqa
from .enviroment import *  # noqa
from .files import *  # noqa
from .i18n import *  # noqa
from .middlewares import *  # noqa
from .tests import *  # noqa
