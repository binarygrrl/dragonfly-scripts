
from dragonfly import Text
from dragonfly.actions.keyboard import Keyboard

specialCharacterTranslations = {
    "?\\question-mark": "?",
    ":\\colon": ":",
    ";\\semicolon": ";",
    "*\\asterisk": "*",
    "~\\tilde": "~",
    ",\\comma": ",",
    ".\\period": ".",
    ".\\dot": ".",
    "/\\slash": "/",
    "_\\underscore": "_",
    "!\\exclamation-mark": "!",
    "@\\at-sign": "@",
    "\\backslash": "\\",
    "(\\left-parenthesis": "(",
    ")\\right-parenthesis": ")",
    "[\\left-square-bracket": "[",
    "]\\right-square-bracket": "]",
    "{\\left-curly-bracket": "{",
    "}\\right-curly-bracket": "}",
    "<\\left-angle-bracket": "<",
    ">\\right-angle-bracket": ">",
    "|\\vertical-bar": "|",
    "$\\dollar-sign": "$",
    "=\\equals-sign": "=",
    "+\\plus-sign": "+",
    "-\\minus-sign": "-",
    "--\dash": "-",
    "-\hyphen": "-",
    "\"\right-double-quote": "\"",
    "\"\left-double-quote": "\"",
}


class SCText(Text):  # Special Characters Text.
    def _parse_spec(self, spec):
        """Overrides the normal Text class behavior. To handle dictation of
        special characters like / . _

        """
        for text, char in specialCharacterTranslations.items():
            spec = spec.replace(" %s " % text, char)
            spec = spec.replace(" %s" % text, char)
            spec = spec.replace("%s " % text, char)
            spec = spec.replace("%s" % text, char)
        events = []
        for character in spec:
            if character in self._specials:
                typeable = self._specials[character]
            else:
                typeable = Keyboard.get_typeable(character)
            events.extend(typeable.events(self._pause))
        return events

normalTextTranslations = {
    "?\\question-mark": "question-mark",
    ":\\colon": "colon",
    ";\\semicolon": "semicolon",
    "*\\asterisk": "asterisk",
    "~\\tilde": "tilde",
    ",\\comma": "comma",
    ".\\period": "period",
    ".\\dot": "dot",
    "/\\slash": "slash",
    "_\\underscore": "underscore",
    "!\\exclamation-mark": "exclamation-mark",
    "@\\at-sign": "at-sign",
    "\\backslash": "backslash",
    "(\\left-parenthesis": "left-parenthesis",
    ")\\right-parenthesis": "right-parenthesis",
    "[\\left-square-bracket": "left-square-bracket",
    "]\\right-square-bracket": "right-square-bracket",
    "{\\left-curly-bracket": "left-curly-bracket",
    "}\\right-curly-bracket": "right-curly-bracket",
    "<\\left-angle-bracket": "left-angle-bracket",
    ">\\right-angle-bracket": "right-angle-bracket",
    "|\\vertical-bar": "vertical-bar",
    "$\\dollar-sign": "dollar-sign",
    "=\\equals-sign": "equals-sign",
    "+\\plus-sign": "plus-sign",
    "-\\minus-sign": "minus-sign",
    "--\dash": "dash",
    "-\hyphen": "hyphen",
}


class NTText(Text):  # Normal Text Text.
    def _parse_spec(self, spec):
        """Overrides the normal Text class behavior. To handle dictation of
        special characters like / . _

        """
        for text, char in normalTextTranslations.items():
            spec = spec.replace(" %s " % text, char)
            spec = spec.replace(" %s" % text, char)
            spec = spec.replace("%s " % text, char)
            spec = spec.replace("%s" % text, char)
        events = []
        for character in spec:
            if character in self._specials:
                typeable = self._specials[character]
            else:
                typeable = Keyboard.get_typeable(character)
            events.extend(typeable.events(self._pause))
        return events