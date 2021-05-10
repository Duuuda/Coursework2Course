from abc import abstractmethod


class BaseWindow:
    @abstractmethod
    def _init_ui(self):
        raise NotImplementedError('This method must be overridden')
