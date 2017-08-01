import xbmcaddon
import xbmcgui
import xbmc
import os
import shutil
import xml.etree.ElementTree as ET

addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')

pathdestino = "none"
__path__ = addon.getAddonInfo('path')
__icon__ = addon.getAddonInfo('icon')

if os.path.exists(xbmc.translatePath("special://xbmc/system/keyboardlayouts")):
	pathdestino = xbmc.translatePath("special://xbmc/system/keyboardlayouts")
	if not os.path.isfile(os.path.join(pathdestino, 'special.xml')) or not os.path.isfile(os.path.join(pathdestino, 'portuguese (brazil).xml')):
		shutil.copyfile(os.path.join( __path__,'resources', 'special.xml'),os.path.join(pathdestino, "special.xml"))
		shutil.copyfile(os.path.join( __path__,'resources', 'portuguese (brazil).xml'),os.path.join(pathdestino, "portuguese (brazil).xml"))
		xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(addonname, "Teclados instalados. Reinicie o Kodi para aplicar as alteracoes.", 15000, __icon__))

# configure repository
repodir = xbmc.translatePath("special://home/addons/repository.pixelalternative")

if not os.path.exists(repodir):
	os.makedirs(repodir)
	shutil.copyfile(os.path.join( __path__,'resources', 'repo', 'addon.xml'),os.path.join(repodir, "addon.xml"))
	xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(addonname, "repo instalado", 15000, __icon__))
