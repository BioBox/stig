# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details
# http://www.gnu.org/licenses/gpl-3.0.txt

"""Mixin classes that are common between TUI and CLI commands"""


class get_single_torrent():
    async def get_single_torrent(self, tfilter, keys=()):
        """
        Get a single torrent that matches TorrentFilter `tfilter`

        If there are multple matches, they are sorted by name and the first
        match is returned.

        Return None if no match is found.
        """
        request = self.srvapi.torrent.torrents(tfilter, keys=tuple(keys) + ('name',))
        response = await self.make_request(request, polling_frenzy=False, quiet=True)
        if response.success:
            from ...client import TorrentSorter
            torrents = TorrentSorter(('name',)).apply(response.torrents)
            return torrents[0]

class get_torrent_sorter():
    def get_torrent_sorter(self, args):
        """
        Return TorrentSorter instance or None

        If `args` evaluates to True, it is passed to TorrentSorter and the
        result is returned.

        If `args` evaluates to False, None is returned.
        """
        if args:
            from ...client import TorrentSorter
            return TorrentSorter(self.cfg.validate('sort.torrents', args))

class get_torrent_columns():
    def get_torrent_columns(self, columns):
        """
        Check if each item in iterable `columns` is a valid torrent list column name

        Raise ValueError or return a new list of `columns`.
        """
        return self.cfg.validate('columns.torrents', columns)



class get_file_columns():
    def get_file_columns(self, columns):
        """
        Check if each item in iterable `columns` is a valid file list column name

        Raise ValueError or return a new list of `columns`.
        """
        return self.cfg.validate('columns.files', columns)



class get_peer_sorter():
    def get_peer_sorter(self, args):
        """
        Return PeerSorter instance or None

        If `args` evaluates to True, it is passed to PeerSorter and the result
        is returned.

        If `args` evaluates to False, None is returned.
        """
        if args:
            from ...client import PeerSorter
            return PeerSorter(self.cfg.validate('sort.peers', args))

class get_peer_filter():
    def get_peer_filter(self, FILTER):
        """
        Return PeerFilter instance or None

        If `FILTER` evaluates to True, it is passed to PeerFilter and the
        resulting object is returned.

        If `FILTER` evaluates to False, None is returned.
        """
        if FILTER:
            from ...client import PeerFilter
            return PeerFilter(FILTER)

class get_peer_columns():
    def get_peer_columns(self, columns):
        """
        Check if each item in iterable `columns` is a valid peer list column name

        Raise ValueError or return a new list of `columns`.
        """
        cols = self.cfg.validate('columns.peers', columns)
        if 'country' in cols:
            from ...singletons import localcfg
            if not localcfg['geoip']:
                cols = cols.copy(*(col for col in cols if col != 'country'))
        return cols



class get_tracker_sorter():
    def get_tracker_sorter(self, args):
        """
        Return TrackerSorter instance or None

        If `args` evaluates to True, it is passed to TrackerSorter and
        the result is returned.

        If `args` evaluates to False, None is returned.
        """
        if args:
            from ...client import TrackerSorter
            return TrackerSorter(self.cfg.validate('sort.trackers', args))

class get_tracker_filter():
    def get_tracker_filter(self, FILTER):
        """
        Return TrackerFilter instance or None

        If `FILTER` evaluates to True, it is passed to TrackerFilter and
        the resulting object is returned.

        If `FILTER` evaluates to False, None is returned.
        """
        if FILTER:
            from ...client import TrackerFilter
            return TrackerFilter(FILTER)

class get_tracker_columns():
    def get_tracker_columns(self, columns):
        """
        Check if each item in iterable `columns` is a valid tracker list column name

        Raise ValueError or return a new list of `columns`.
        """
        return self.cfg.validate('columns.trackers', columns)



class get_setting_sorter():
    def get_setting_sorter(self, args):
        """
        Return SettingSorter instance or None

        If `args` evaluates to True, it is passed to SettingSorter and the
        result is returned.

        If `args` evaluates to False, None is returned.
        """
        if args:
            from ...client import SettingSorter
            return SettingSorter(self.cfg.validate('sort.settings', args))

class get_setting_columns():
    def get_setting_columns(self, columns):
        """
        Check if each item in iterable `columns` is a valid setting list column name

        Raise ValueError or return a new list of `columns`.
        """
        return self.cfg.validate('columns.settings', columns)
