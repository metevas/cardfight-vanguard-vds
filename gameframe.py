# -*- coding: utf-8 -*-

#   This file is part of CFVVDS.
#
#    CFVVDS is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    CFVVDS is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with CFVVDS; if not, write to the Free Software
#    Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

import wx, sys, os
from gamecontrols import *

class GameFrame(wx.Frame):
    def __init__(self, engine):
        self._engine = engine
        wx.Frame.__init__(self, parent=None, title="CRAY ONLINE", size=(1280,720), style=wx.MINIMIZE_BOX | wx.CAPTION | wx.CLOSE_BOX | wx.SYSTEM_MENU)
        self.SetIcon(wx.IconFromLocation(wx.IconLocation(os.path.join(self._engine.BaseDirectory,'mooseduel16x16.ico'))))
        self.CenterOnScreen()
        self.Game = GamePanel(self, self._engine)
        self.Bind(wx.EVT_CLOSE, self.OnExit)
    
    def OnExit(self, event=None):
        self.Game.OnClose()
        self.Destroy()
