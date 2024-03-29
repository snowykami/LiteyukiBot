from nonebot.plugin import PluginMetadata

from liteyuki.utils.data_manager import *
from liteyuki.utils.language import get_default_lang
from .core import *
from .loader import *
from .webdash import *

__author__ = "snowykami"
__plugin_meta__ = PluginMetadata(
    name="轻雪主程序",
    description="轻雪主程序插件，包含了许多初始化的功能",
    usage="",
    homepage="https://github.com/snowykami/LiteyukiBot",
    extra={
            "liteyuki"  : True,
            "toggleable": False,
    }
)

sys_lang = get_default_lang()
nonebot.logger.info(sys_lang.get("main.current_language", LANG=sys_lang.get("language.name")))
nonebot.logger.info(sys_lang.get("main.enable_webdash", URL=f"http://127.0.0.1:{config.get('port', 20216)}"))
