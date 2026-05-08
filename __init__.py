# -*- coding: utf-8 -*-
"""
/***************************************************************************
 FreehandRasterGeoreferencer
                                 A QGIS plugin
 Interactive georeferencing of rasters
                             -------------------
        copyright            : (C) 2018 by Guilhem Vellut
        email                : guilhem.vellut@gmail.com
        version 0.9          : (C) 2026 by 02nowicki - Pawel Nowicki
        Qt5 -> Qt6 migration for QGIS 4.0.2 compatibility
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""


def classFactory(iface):
    from .freehandrastergeoreferencer import FreehandRasterGeoreferencer
    return FreehandRasterGeoreferencer(iface)
