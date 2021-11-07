class StringHelper:
    @classmethod
    def last_substring(cls, text, separator):
        array = text.split(separator)
        return array[len(array) - 1]
