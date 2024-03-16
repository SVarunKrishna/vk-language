"""VK Programming Language"""
from . import ast, lexer, parser, runner, utils

__all__ = ["parser", "ast", "lexer", "runner", "utils"]

__version__ = "1.0.0"
__version_str__ = (
    f"VK Programming Language v{__version__}."
    + "\nVK Programming Language is a custom programming language inspired by VK."
    + "\nCreated by Varun Krishna (beasovacompany@gmail.com) Beasova Corporation ."
)

vk = runner.VKRunner()
