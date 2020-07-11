# -*- coding: utf-8 -*-

"""
lazybot.commands
~~~~~~~~~~~~~~~~~~~~~
A module holding commands and auto-response functions
for a discord bot.
"""

from .CommandColor import CommandColor
from .CommandGradYear import CommandGradYear
from .CommandHelp import StraightforwardHelp
from .MiscFun import MiscFun

__all__ = ["CommandColor", "CommandGradYear", "StraightforwardHelp", "MiscFun"]
