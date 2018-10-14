#!/usr/bin/env python

import re


class ChatSerializer(object):
    LEGACY_COLOR_CHAR = u"\u00A7"
    LEGACY_STRIP_COLOR_PATTERN = re.compile(LEGACY_COLOR_CHAR + "[0-9a-fk-or]")
    COLOR_CODES = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                   "a", "b", "c", "d", "e", "f",
                   "k", "l", "m", "n", "o", "r"]

    @staticmethod
    def strip_colors(chat):
        if isinstance(chat, basestring):
            return ChatSerializer.LEGACY_STRIP_COLOR_PATTERN.sub("", chat)

        text = u""

        if "translate" in chat:
            text += chat["translate"]

        if "text" in chat:
            text += chat["text"]

        if "extra" in chat:
            for i in chat["extra"]:
                text += i["text"]

        return ChatSerializer.LEGACY_STRIP_COLOR_PATTERN.sub("", text)

    @staticmethod
    def translate_legacy(text, code="&"):
        text = unicode(text)
        code = unicode(code)
        translated = list(text)

        for i in range(len(text) - 1):
            if text[i] == code and text[i + 1] in ChatSerializer.COLOR_CODES:
                translated[i] = ChatSerializer.LEGACY_COLOR_CHAR
                translated[i + 1] = text[i + 1]

        return "".join(translated)
