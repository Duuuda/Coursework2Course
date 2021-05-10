from typing import Tuple, IO


class WordManager:
    __slots__ = ('_word', '_count')

    def __init__(self, word: str, count: int):
        self._word = word
        self._count = count

    @property
    def word(self) -> str:
        return self._word

    @property
    def count(self) -> int:
        return self._count

    @property
    def for_write(self) -> str:
        return f'{self._word} {self._count}'

    def __str__(self) -> str:
        return f'Word: {self._word}, Count: {self._count}'

    def __repr__(self) -> str:
        return self.__str__()


class FileManager:
    __slots__ = ('words', '_printing')

    def __init__(self, file_io: IO[str], low_case: bool = False, close_the_file: bool = False, printing: bool = False):
        text = file_io.read().replace('\n', ' ')
        if close_the_file:
            file_io.close()
        if low_case:
            self.words = text.lower().split()
        else:
            self.words = text.split()
        self._printing = printing

    @property
    def words_analytics(self) -> Tuple[WordManager]:
        unique_words = set(self.words)
        analytics = list()
        for unique_word in unique_words:
            analytics.append((self.words.count(unique_word), unique_word))
        analytics.sort()
        analytics.sort(key=lambda tpl: tpl[0], reverse=True)
        result = tuple(map(lambda tpl: WordManager(*tpl[::-1]), analytics))
        if self._printing:
            print(*result, sep='\n')
        return result


def main():
    try:
        with open('resource_1.txt', 'r', encoding='UTF-8') as file:
            file_manager = FileManager(file, printing=False)
    except FileNotFoundError:
        print('File "resource_1.txt" not found!')
        input()
        raise SystemExit

    analytics = file_manager.words_analytics

    with open('result_1.txt', 'w+', encoding='UTF-8') as file:
        file.writelines(map(lambda wm: wm.for_write + '\n', analytics))


if __name__ == '__main__':
    main()
