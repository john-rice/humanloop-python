# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from humanloop.paths.completion_deployed import Api

from humanloop.paths import PathValues

path = PathValues.COMPLETIONDEPLOYED