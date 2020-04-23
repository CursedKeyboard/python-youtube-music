from .BaseType import BaseType
from . import utils

__type__ = __name__.split('.')[-1]
__all__  = (__type__,)

class HomeContinuation(BaseType):
    _patterns = \
    (
        utils.pattern \
        (
            '4qmFsg',
            'KM',
            'ARIMRkVtdXNpY19ob21lG',
            'nxDQU42VkVOcVFVRkJSMVoxUVVGR1NGRm5RVUpTTUVsQlFWRkNSMUpYTVRGak',
            '1teHFXREpvZG1KWFZVRkJVVUZCUVZGR1JFRkJRVUpCUVVWQlFVRkZRa0pCUjFSM',
            utils.entropy(5),
            'JRVUp',
            utils.entropy(16),
            '2UVdwSlFRJTNEJTNE',
        ),
        utils.pattern \
        (
            '4qmFsg',
            'Lb',
            'ARIMRkVtdXNpY19ob21lG',
            'soBQ0F',
            utils.entropy(1),
            'NmtBRkRha0ZCUVVkV2RVRkJSa2hSWjBGQ1VqQkpRVUZSUWtkU1Z6RX',
            'hZekpzYWxneWFIWmlWMVZCUVZGQlFVRlJSa1JCUVVGQ1FVRkZRVUZCUlVKQ1FVZFVk',
            utils.entropy(4),
            'VVV',
            utils.entropy(19),
            'IwRnFTWFJIYVhSVFVrVk9UVkZWY3pGa1dHeG1Z',
            utils.entropy(78),
            'UzRA%3D%3D',
        ),
    )