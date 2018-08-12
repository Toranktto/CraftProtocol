#!/usr/bin/env python

import re


class ChatSerializer(object):
    LEGACY_COLOR_CHAR = u"\u00A7"
    LEGACY_STRIP_COLOR_PATTERN = re.compile(LEGACY_COLOR_CHAR + "[0-9a-fk-or]")

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
            if text[i] == code and "0123456789abcdefklmnor".find(text[i + 1]) > -1:
                translated[i] = ChatSerializer.LEGACY_COLOR_CHAR
                translated[i + 1] = text[i + 1]

        return "".join(translated)
