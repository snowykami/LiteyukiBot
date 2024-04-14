import nonebot.plugin

from liteyuki.utils import init_log
from liteyuki.utils.base.data_manager import InstalledPlugin, plugin_db
from liteyuki.utils.base.resource import load_resources
from liteyuki.utils.message.tools import check_for_package

load_resources()
init_log()

nonebot.plugin.load_plugins("liteyuki/plugins")
nonebot.plugin.load_plugins("plugins")

# 从数据库读取已安装的插件
installed_plugins: list[InstalledPlugin] = plugin_db.all(InstalledPlugin())
if installed_plugins:
    for installed_plugin in installed_plugins:
        if not check_for_package(installed_plugin.module_name):
            nonebot.logger.error(f"{installed_plugin.module_name} not installed, but in loading database. please run `npm fixup` in chat to reinstall it.")
        else:
            nonebot.load_plugin(installed_plugin.module_name)
