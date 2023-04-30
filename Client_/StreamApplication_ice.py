# -*- coding: utf-8 -*-
#
# Copyright (c) ZeroC, Inc. All rights reserved.
#
#
# Ice version 3.7.2
#
# <auto-generated>
#
# Generated from file `StreamApplication.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

from sys import version_info as _version_info_
import Ice, IcePy

# Start of module app
_M_app = Ice.openModule('app')
__name__ = 'app'

if 'Song' not in _M_app.__dict__:
    _M_app.Song = Ice.createTempClass()
    class Song(Ice.Value):
        def __init__(self, name='', path='', artist='', album='', genre='', year=''):
            self.name = name
            self.path = path
            self.artist = artist
            self.album = album
            self.genre = genre
            self.year = year

        def ice_id(self):
            return '::app::Song'

        @staticmethod
        def ice_staticId():
            return '::app::Song'

        def __str__(self):
            return IcePy.stringify(self, _M_app._t_Song)

        __repr__ = __str__

    _M_app._t_Song = IcePy.defineValue('::app::Song', Song, -1, (), False, False, None, (
        ('name', (), IcePy._t_string, False, 0),
        ('path', (), IcePy._t_string, False, 0),
        ('artist', (), IcePy._t_string, False, 0),
        ('album', (), IcePy._t_string, False, 0),
        ('genre', (), IcePy._t_string, False, 0),
        ('year', (), IcePy._t_string, False, 0)
    ))
    Song._ice_type = _M_app._t_Song

    _M_app.Song = Song
    del Song

if '_t_songList' not in _M_app.__dict__:
    _M_app._t_songList = IcePy.defineSequence('::app::songList', (), _M_app._t_Song)

_M_app._t_StreamApplication = IcePy.defineValue('::app::StreamApplication', Ice.Value, -1, (), False, True, None, ())

if 'StreamApplicationPrx' not in _M_app.__dict__:
    _M_app.StreamApplicationPrx = Ice.createTempClass()
    class StreamApplicationPrx(Ice.ObjectPrx):

        def ajoutMusic(self, s, context=None):
            return _M_app.StreamApplication._op_ajoutMusic.invoke(self, ((s, ), context))

        def ajoutMusicAsync(self, s, context=None):
            return _M_app.StreamApplication._op_ajoutMusic.invokeAsync(self, ((s, ), context))

        def begin_ajoutMusic(self, s, _response=None, _ex=None, _sent=None, context=None):
            return _M_app.StreamApplication._op_ajoutMusic.begin(self, ((s, ), _response, _ex, _sent, context))

        def end_ajoutMusic(self, _r):
            return _M_app.StreamApplication._op_ajoutMusic.end(self, _r)

        def suppMusic(self, name, context=None):
            return _M_app.StreamApplication._op_suppMusic.invoke(self, ((name, ), context))

        def suppMusicAsync(self, name, context=None):
            return _M_app.StreamApplication._op_suppMusic.invokeAsync(self, ((name, ), context))

        def begin_suppMusic(self, name, _response=None, _ex=None, _sent=None, context=None):
            return _M_app.StreamApplication._op_suppMusic.begin(self, ((name, ), _response, _ex, _sent, context))

        def end_suppMusic(self, _r):
            return _M_app.StreamApplication._op_suppMusic.end(self, _r)

        def findByName(self, nom, context=None):
            return _M_app.StreamApplication._op_findByName.invoke(self, ((nom, ), context))

        def findByNameAsync(self, nom, context=None):
            return _M_app.StreamApplication._op_findByName.invokeAsync(self, ((nom, ), context))

        def begin_findByName(self, nom, _response=None, _ex=None, _sent=None, context=None):
            return _M_app.StreamApplication._op_findByName.begin(self, ((nom, ), _response, _ex, _sent, context))

        def end_findByName(self, _r):
            return _M_app.StreamApplication._op_findByName.end(self, _r)

        def findByAlbum(self, album, context=None):
            return _M_app.StreamApplication._op_findByAlbum.invoke(self, ((album, ), context))

        def findByAlbumAsync(self, album, context=None):
            return _M_app.StreamApplication._op_findByAlbum.invokeAsync(self, ((album, ), context))

        def begin_findByAlbum(self, album, _response=None, _ex=None, _sent=None, context=None):
            return _M_app.StreamApplication._op_findByAlbum.begin(self, ((album, ), _response, _ex, _sent, context))

        def end_findByAlbum(self, _r):
            return _M_app.StreamApplication._op_findByAlbum.end(self, _r)

        def findByArtist(self, artist, context=None):
            return _M_app.StreamApplication._op_findByArtist.invoke(self, ((artist, ), context))

        def findByArtistAsync(self, artist, context=None):
            return _M_app.StreamApplication._op_findByArtist.invokeAsync(self, ((artist, ), context))

        def begin_findByArtist(self, artist, _response=None, _ex=None, _sent=None, context=None):
            return _M_app.StreamApplication._op_findByArtist.begin(self, ((artist, ), _response, _ex, _sent, context))

        def end_findByArtist(self, _r):
            return _M_app.StreamApplication._op_findByArtist.end(self, _r)

        def findByGenre(self, genre, context=None):
            return _M_app.StreamApplication._op_findByGenre.invoke(self, ((genre, ), context))

        def findByGenreAsync(self, genre, context=None):
            return _M_app.StreamApplication._op_findByGenre.invokeAsync(self, ((genre, ), context))

        def begin_findByGenre(self, genre, _response=None, _ex=None, _sent=None, context=None):
            return _M_app.StreamApplication._op_findByGenre.begin(self, ((genre, ), _response, _ex, _sent, context))

        def end_findByGenre(self, _r):
            return _M_app.StreamApplication._op_findByGenre.end(self, _r)

        def findByYear(self, year, context=None):
            return _M_app.StreamApplication._op_findByYear.invoke(self, ((year, ), context))

        def findByYearAsync(self, year, context=None):
            return _M_app.StreamApplication._op_findByYear.invokeAsync(self, ((year, ), context))

        def begin_findByYear(self, year, _response=None, _ex=None, _sent=None, context=None):
            return _M_app.StreamApplication._op_findByYear.begin(self, ((year, ), _response, _ex, _sent, context))

        def end_findByYear(self, _r):
            return _M_app.StreamApplication._op_findByYear.end(self, _r)

        def getAll(self, context=None):
            return _M_app.StreamApplication._op_getAll.invoke(self, ((), context))

        def getAllAsync(self, context=None):
            return _M_app.StreamApplication._op_getAll.invokeAsync(self, ((), context))

        def begin_getAll(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_app.StreamApplication._op_getAll.begin(self, ((), _response, _ex, _sent, context))

        def end_getAll(self, _r):
            return _M_app.StreamApplication._op_getAll.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_app.StreamApplicationPrx.ice_checkedCast(proxy, '::app::StreamApplication', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_app.StreamApplicationPrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::app::StreamApplication'
    _M_app._t_StreamApplicationPrx = IcePy.defineProxy('::app::StreamApplication', StreamApplicationPrx)

    _M_app.StreamApplicationPrx = StreamApplicationPrx
    del StreamApplicationPrx

    _M_app.StreamApplication = Ice.createTempClass()
    class StreamApplication(Ice.Object):

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::app::StreamApplication')

        def ice_id(self, current=None):
            return '::app::StreamApplication'

        @staticmethod
        def ice_staticId():
            return '::app::StreamApplication'

        def ajoutMusic(self, s, current=None):
            raise NotImplementedError("servant method 'ajoutMusic' not implemented")

        def suppMusic(self, name, current=None):
            raise NotImplementedError("servant method 'suppMusic' not implemented")

        def findByName(self, nom, current=None):
            raise NotImplementedError("servant method 'findByName' not implemented")

        def findByAlbum(self, album, current=None):
            raise NotImplementedError("servant method 'findByAlbum' not implemented")

        def findByArtist(self, artist, current=None):
            raise NotImplementedError("servant method 'findByArtist' not implemented")

        def findByGenre(self, genre, current=None):
            raise NotImplementedError("servant method 'findByGenre' not implemented")

        def findByYear(self, year, current=None):
            raise NotImplementedError("servant method 'findByYear' not implemented")

        def getAll(self, current=None):
            raise NotImplementedError("servant method 'getAll' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_app._t_StreamApplicationDisp)

        __repr__ = __str__

    _M_app._t_StreamApplicationDisp = IcePy.defineClass('::app::StreamApplication', StreamApplication, (), None, ())
    StreamApplication._ice_type = _M_app._t_StreamApplicationDisp

    StreamApplication._op_ajoutMusic = IcePy.Operation('ajoutMusic', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_app._t_Song, False, 0),), (), ((), IcePy._t_bool, False, 0), ())
    StreamApplication._op_suppMusic = IcePy.Operation('suppMusic', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0),), (), ((), IcePy._t_bool, False, 0), ())
    StreamApplication._op_findByName = IcePy.Operation('findByName', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0),), (), ((), _M_app._t_songList, False, 0), ())
    StreamApplication._op_findByAlbum = IcePy.Operation('findByAlbum', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0),), (), ((), _M_app._t_songList, False, 0), ())
    StreamApplication._op_findByArtist = IcePy.Operation('findByArtist', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0),), (), ((), _M_app._t_songList, False, 0), ())
    StreamApplication._op_findByGenre = IcePy.Operation('findByGenre', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0),), (), ((), _M_app._t_songList, False, 0), ())
    StreamApplication._op_findByYear = IcePy.Operation('findByYear', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0),), (), ((), _M_app._t_songList, False, 0), ())
    StreamApplication._op_getAll = IcePy.Operation('getAll', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_app._t_songList, False, 0), ())

    _M_app.StreamApplication = StreamApplication
    del StreamApplication

# End of module app
