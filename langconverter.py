# coding: utf-8

class cached_property(object):
    def __init__(self, func):
        self.__doc__ = getattr(func, '__doc__')
        self.__name__ = getattr(func, '__name__')
        self.__module__ = getattr(func, '__module__')
        self.func = func

    def __get__(self, obj, cls):
        if obj is None:
            return self
        value = obj.__dict__[self.func.__name__] = self.func(obj)
        return value


class LangMap(object):
    def __init__(self, *pairs):
        self._map = list(pairs)

    def add(self, code_pairs):
        for pair in code_pairs:
            if self._map.index(pair):
                continue
            else:
                self._map.append(pair)

    def match_bing(self, bing_code):
        result = list(filter(lambda pair: pair[0] == bing_code, self._map))
        if not result:
            return None
        return result[0][1]

    def match_other(self, other_code):
        result = list(filter(lambda pair: pair[1] == other_code, self._map))
        if not result:
            return None
        return result[0][0]

    @cached_property
    def bing_set(self):
        return set(map(lambda pair: pair[0], self._map))

    @cached_property
    def other_set(self):
        return set(map(lambda pair: pair[1], self._map))


class LangConverter(object):
    code = None

    def __init__(self, code):
        if code not in bing_lang_codes:
            raise ValueError('lang_code is not bing lang code')
        self.code = code

    @classmethod
    def __from_lang(cls, code, lang_map):
        if code not in lang_map.other_set:
            raise ValueError('code not found')
        bing_code = lang_map.match_other(code)
        return cls(bing_code)

    def __to_lang(self, lang_map):
        lang_code = lang_map.match_bing(self.code)
        return lang_code

    @classmethod
    def from_nltk(cls, code):
        return cls.__from_lang(code, bing_nltk_map)

    def to_nltk(self):
        return self.__to_lang(bing_nltk_map)

    @classmethod
    def from_langid(cls, code):
        return cls.__from_lang(code, bing_langid_map)

    def to_langid(self):
        return self.__to_lang(bing_langid_map)


bing_nltk_map = LangMap(('en', 'en'),
                        ('ja', 'ja'),
                        ('zh-CHS', 'zh'),
                        ('de', 'de'),
                        ('fr', 'fr'),
                        ('es', 'es'),
                        ('ko', 'ko')
                        )

bing_langid_map = LangMap(('en', 'en'),
                          ('ja', 'ja'),
                          ('zh-CHS', 'zh'),
                          ('de', 'de'),
                          ('fr', 'fr'),
                          ('es', 'es'),
                          ('ko', 'ko')
                          )

bing_lang_codes = bing_nltk_map.bing_set | bing_langid_map.bing_set


if __name__ == '__main__':
    a = LangConverter.from_langid('zh')
    print(a.code)
