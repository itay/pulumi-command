# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from . import _utilities
import typing
# Export this package's modules as members:
from .provider import *

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_command.local as local
    import pulumi_command.remote as remote
else:
    local = _utilities.lazy_import('pulumi_command.local')
    remote = _utilities.lazy_import('pulumi_command.remote')

_utilities.register(
    resource_modules="""
[
 {
  "pkg": "command",
  "mod": "local",
  "fqn": "pulumi_command.local",
  "classes": {
   "command:local:Command": "Command"
  }
 },
 {
  "pkg": "command",
  "mod": "remote",
  "fqn": "pulumi_command.remote",
  "classes": {
   "command:remote:Command": "Command"
  }
 }
]
""",
    resource_packages="""
[
 {
  "pkg": "command",
  "token": "pulumi:providers:command",
  "fqn": "pulumi_command",
  "class": "Provider"
 }
]
"""
)