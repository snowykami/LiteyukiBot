import nonebot
from nonebot.log import logger
from nonebot.plugin import PluginMetadata
from playwright.async_api import Browser

from .browser import (
    get_browser as get_browser,
    get_new_page as get_new_page,
    shutdown_browser as shutdown_browser,
)
from .data_source import (
    capture_element as capture_element,
    html_to_pic as html_to_pic,
    md_to_pic as md_to_pic,
    template_to_html as template_to_html,
    template_to_pic as template_to_pic,
    text_to_pic as text_to_pic,
)

__plugin_meta__ = PluginMetadata(
    name="nonebot-plugin-htmlrender",
    description="通过浏览器渲染图片",
    usage="提供多个易用API md_to_pic html_to_pic text_to_pic template_to_pic capture_element 等",
    type="library",
    homepage="https://github.com/kexue-z/nonebot-plugin-htmlrender",
    extra={},
)

browser: Browser