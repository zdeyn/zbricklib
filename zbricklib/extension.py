from abc import ABC, abstractmethod
from flask import Flask

class zExtension(ABC):
    _ext_name : str|None = None

    def init_app(self, app : Flask):
        """Initializes the extension with the given Flask app"""
        if self._ext_name is None:
            raise NotImplementedError("Extension name must be set")
        app.extensions[self._ext_name] = self
        self._install_into(app)
    
    @abstractmethod
    def _install_into(self, app : Flask):
        ...