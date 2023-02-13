
# ---------------------------------------------------------------------------------
# Name: Premium
# Description: Premium prank
# Author: Slick
# Commands:
# premium
# ---------------------------------------------------------------------------------


#             Тут типо слик, если хиккари даст 
#             текст хикка кубиками то я суда поставлю
#              © Copyright 2022
#           https://t.me/hikariatama
#
# 🔒      Licensed under the GNU AGPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# meta developer: @Wiseslick
# scope: SlPrem
# scope: SlPrem 0.0.2

import asyncio
import functools
import random
from urllib.parse import quote_plus

import requests
from telethon.tl.types import Message

from .. import loader, utils

phrases = ["Невозможно", "Хуй там", "Ты думаешь Дуров пидор? да он пидор", "Ты думаешь Дуров хуйло? да он хуйло", "ХЫ", "Дуров сказал купить"]


@loader.tds
class NekosLifeMod(loader.Module):
    """Premium prank"""

    strings = {"name": "Premium prank"}
    strings_ru = {
        "_cmd_doc_premium": "Шутка про прем"

    }


    @loader.unrestricted
    async def premiumcmd(self, message: Message):
        """Premium govno"""
        await utils.answer(
            message,
            "<emoji document_id=4956562374648660535>❕</emoji>"
            f"{(random.choice(phrases))}",
        )

