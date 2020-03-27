from ..... import utils as ytm_utils
from ... import containers

__all__ = __name__.split('.')[-1:]

def _parse(self, data):
    contents = ytm_utils.get_nested(data, 'contents', 'singleColumnBrowseResultsRenderer', 'tabs', 0, 'tabRenderer', 'content', 'sectionListRenderer', 'contents', 0, 'musicShelfRenderer', 'contents') # , ...)

    albums_data = []

    for item in contents:
        item = ytm_utils.get_nested(item, 'musicResponsiveListItemRenderer')

        item_menu_items = ytm_utils.get_nested(item, 'menu', 'menuRenderer', 'items', default=())
        item_menu_items_map = {}

        for item_menu_item in item_menu_items:
            item_menu_item = ytm_utils.first_key(item_menu_item)

            item_menu_item_text = ytm_utils.get_nested(item_menu_item, 'text', 'runs', 0, 'text')

            if not item_menu_item_text:
                item_menu_item_text = ytm_utils.get_nested(item_menu_item, 'defaultText', 'runs', 0, 'text')

            if not item_menu_item_text:
                return # raise

            item_menu_item_identifier = item_menu_item_text.strip().lower().replace(' ', '_')

            item_menu_items_map[item_menu_item_identifier] = item_menu_item

        item_badges = ytm_utils.get_nested(item, 'badges', default=())
        item_badges_map = {}

        for badge in item_badges:
            badge = ytm_utils.first_key(badge)

            badge_label = ytm_utils.get_nested(badge, 'accessibilityData', 'accessibilityData', 'label')

            if not badge_label:
                return # raise/log

            badge_identifier = badge_label.strip().lower().replace(' ', '_')

            item_badges_map[badge_identifier] = badge

        item_album_page_type = ytm_utils.get_nested(item, 'navigationEndpoint', 'browseEndpoint', 'browseEndpointContextSupportedConfigs', 'browseEndpointContextMusicConfig', 'pageType')
        item_album_id = ytm_utils.get_nested(item, 'navigationEndpoint', 'browseEndpoint', 'browseId')
        item_album_params = ytm_utils.get_nested(item, 'navigationEndpoint', 'browseEndpoint', 'params')

        item_album_name = ytm_utils.get_nested(item, 'flexColumns', 0, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'text')
        item_type = ytm_utils.get_nested(item, 'flexColumns', 1, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 0, 'text')
        item_year = ytm_utils.get_nested(item, 'flexColumns', 1, 'musicResponsiveListItemFlexColumnRenderer', 'text', 'runs', 2, 'text', func=int)
        item_thumbnail = ytm_utils.get_nested(item, 'thumbnail', 'musicThumbnailRenderer', 'thumbnail', 'thumbnails', -1)

        item_shuffle_playlist_params = ytm_utils.get_nested(item_menu_items_map, 'shuffle_play', 'navigationEndpoint', 'watchPlaylistEndpoint', 'params')
        item_shuffle_playlist_id = ytm_utils.get_nested(item_menu_items_map, 'shuffle_play', 'navigationEndpoint', 'watchPlaylistEndpoint', 'playlistId')

        item_radio_playlist_params = ytm_utils.get_nested(item_menu_items_map, 'start_radio', 'navigationEndpoint', 'watchPlaylistEndpoint', 'params')
        item_radio_playlist_id = ytm_utils.get_nested(item_menu_items_map, 'start_radio', 'navigationEndpoint', 'watchPlaylistEndpoint', 'playlistId')

        item_explicit = 'explicit' in item_badges_map

        item_data = \
        {
            'name': item_album_name,
            'id': item_album_id,
            'type': item_type,
            'year': item_year,
            'explicit': item_explicit,
            'params': item_album_params,
            'thumbnail': item_thumbnail,
            'shuffle': \
            {
                'params': item_shuffle_playlist_params,
                'playlist_id': item_shuffle_playlist_id,
            },
            'radio': \
            {
                'params': item_radio_playlist_params,
                'playlist_id': item_radio_playlist_id,
            },
        }

        item_obj = containers.ArtistAlbum(self.api, item_data)

        albums_data.append(item_obj)

    return albums_data
