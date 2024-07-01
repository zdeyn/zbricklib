import pytest
from flask import Flask
from unittest.mock import MagicMock

from zbricklib.extension import zExtension

class TestExtensionWithoutName(zExtension):
    def _install_into(self, app):
        pass

class TestExtensionWithName(zExtension):
    _ext_name = "test_extension"

    def _install_into(self, app):
        pass

def test_init_app_raises_not_implemented_error():
    app = Flask(__name__)
    ext = TestExtensionWithoutName()
    
    with pytest.raises(NotImplementedError, match="Extension name must be set"):
        ext.init_app(app)

def test_init_app_embeds_extension(mocker):
    app = Flask(__name__)
    ext = TestExtensionWithName()
    
    mock_install_into = mocker.patch.object(ext, '_install_into', autospec=True)
    ext.init_app(app)
    
    assert app.extensions["test_extension"] == ext
    mock_install_into.assert_called_once_with(app)

def test_install_into_called(mocker):
    app = Flask(__name__)
    ext = TestExtensionWithName()

    mock_install_into = mocker.patch.object(ext, '_install_into', autospec=True)
    ext.init_app(app)

    mock_install_into.assert_called_once_with(app)
