from __clrclasses__.Autodesk.AutoCAD.ApplicationServices import BeginDoubleClickEventHandler as _n_0_t_0
from __clrclasses__.Autodesk.AutoCAD.ApplicationServices import PreTranslateMessageEventHandler as _n_0_t_1
from __clrclasses__.Autodesk.AutoCAD.ApplicationServices import SystemVariableChangedEventHandler as _n_0_t_2
from __clrclasses__.Autodesk.AutoCAD.ApplicationServices import SystemVariableChangingEventHandler as _n_0_t_3
from __clrclasses__.Autodesk.AutoCAD.ApplicationServices import DocumentCollection as _n_0_t_4
from __clrclasses__.Autodesk.AutoCAD.ApplicationServices import LongTransactionManager as _n_0_t_5
from __clrclasses__.Autodesk.AutoCAD.ApplicationServices import RecentDocumentCollection as _n_0_t_6
from __clrclasses__.Autodesk.AutoCAD.ApplicationServices import UnmanagedResources as _n_0_t_7
from __clrclasses__.Autodesk.AutoCAD.ApplicationServices import UserConfigurationManager as _n_0_t_8
from __clrclasses__.Autodesk.AutoCAD.ApplicationServices import WhoHasInfo as _n_0_t_9
from __clrclasses__.Autodesk.AutoCAD.DatabaseServices import ResultBuffer as _n_1_t_0
from __clrclasses__.Autodesk.AutoCAD.Publishing import Publisher as _n_2_t_0
from __clrclasses__.Autodesk.AutoCAD.Windows import Window as _n_3_t_0
from __clrclasses__.System import EventHandler as _n_4_t_0
from __clrclasses__.System import Version as _n_4_t_1
from __clrclasses__.System import Uri as _n_4_t_2
from __clrclasses__.System import Nullable as _n_4_t_3
from __clrclasses__.System import IntPtr as _n_4_t_4
from __clrclasses__.System import MulticastDelegate as _n_4_t_5
from __clrclasses__.System import ICloneable as _n_4_t_6
from __clrclasses__.System import IAsyncResult as _n_4_t_7
from __clrclasses__.System import Type as _n_4_t_8
from __clrclasses__.System import AsyncCallback as _n_4_t_9
from __clrclasses__.System.Runtime.Serialization import ISerializable as _n_5_t_0
from __clrclasses__.System.Windows import Window as _n_6_t_0
import typing
class Application(object):
    @property
    def DocumentManager(self) -> _n_0_t_4:"""DocumentManager { get; } -> DocumentCollection"""
    @property
    def HasPickFirst(self) -> bool:"""HasPickFirst { get; } -> bool"""
    @property
    def IsInBackgroundMode(self) -> bool:"""IsInBackgroundMode { get; } -> bool"""
    @property
    def IsInPlaceServer(self) -> bool:"""IsInPlaceServer { get; } -> bool"""
    @property
    def IsQuiescent(self) -> bool:"""IsQuiescent { get; } -> bool"""
    @property
    def LongTransactionManager(self) -> _n_0_t_5:"""LongTransactionManager { get; } -> LongTransactionManager"""
    @property
    def MainWindow(self) -> _n_3_t_0:"""MainWindow { get; } -> Window"""
    @property
    def Publisher(self) -> _n_2_t_0:"""Publisher { get; } -> Publisher"""
    @property
    def RecentDocuments(self) -> _n_0_t_6:"""RecentDocuments { get; } -> RecentDocumentCollection"""
    @property
    def UnmanagedResources(self) -> _n_0_t_7:"""UnmanagedResources { get; } -> UnmanagedResources"""
    @property
    def UserConfigurationManager(self) -> _n_0_t_8:"""UserConfigurationManager { get; } -> UserConfigurationManager"""
    @property
    def Version(self) -> _n_4_t_1:"""Version { get; } -> Version"""
    @property
    def BeginDoubleClick(self) -> _n_0_t_0:
        """BeginDoubleClick Event: BeginDoubleClickEventHandler"""
    @property
    def BeginQuit(self) -> _n_4_t_0:
        """BeginQuit Event: EventHandler"""
    @property
    def EnterModal(self) -> _n_4_t_0:
        """EnterModal Event: EventHandler"""
    @property
    def Idle(self) -> _n_4_t_0:
        """Idle Event: EventHandler"""
    @property
    def LeaveModal(self) -> _n_4_t_0:
        """LeaveModal Event: EventHandler"""
    @property
    def PreTranslateMessage(self) -> _n_0_t_1:
        """PreTranslateMessage Event: PreTranslateMessageEventHandler"""
    @property
    def QuitAborted(self) -> _n_4_t_0:
        """QuitAborted Event: EventHandler"""
    @property
    def QuitWillStart(self) -> _n_4_t_0:
        """QuitWillStart Event: EventHandler"""
    @property
    def SystemVariableChanged(self) -> _n_0_t_2:
        """SystemVariableChanged Event: SystemVariableChangedEventHandler"""
    @property
    def SystemVariableChanging(self) -> _n_0_t_3:
        """SystemVariableChanging Event: SystemVariableChangingEventHandler"""
    @staticmethod
    def EvaluateDiesel(dieselCmd: str) -> str:...
    @staticmethod
    def GetSystemVariable(name: str) -> object:...
    @staticmethod
    def GetWhoHasInfo(pathname: str) -> _n_0_t_9:...
    @staticmethod
    def Invoke(args: _n_1_t_0) -> _n_1_t_0:...
    @staticmethod
    def IsFileLocked(pathname: str) -> bool:...
    @staticmethod
    def LoadJSScript(urlJSFile: _n_4_t_2):...
    @staticmethod
    def Quit():...
    @staticmethod
    def SetSystemVariable(name: str, value: object):...
    @staticmethod
    def ShowAlertDialog(message: str):...
    @staticmethod
    def ShowModalWindow(owner: _n_4_t_4, formToShow: _n_6_t_0, persistSizeAndPosition: bool) -> _n_4_t_3[bool]:...
    @staticmethod
    def ShowModalWindow(owner: _n_6_t_0, formToShow: _n_6_t_0, persistSizeAndPosition: bool) -> _n_4_t_3[bool]:...
    @staticmethod
    def ShowModalWindow(owner: _n_4_t_4, formToShow: _n_6_t_0) -> _n_4_t_3[bool]:...
    @staticmethod
    def ShowModalWindow(owner: _n_6_t_0, formToShow: _n_6_t_0) -> _n_4_t_3[bool]:...
    @staticmethod
    def ShowModalWindow(formToShow: _n_6_t_0) -> _n_4_t_3[bool]:...
    @staticmethod
    def ShowModelessWindow(owner: _n_4_t_4, formToShow: _n_6_t_0, persistSizeAndPosition: bool):...
    @staticmethod
    def ShowModelessWindow(owner: _n_6_t_0, formToShow: _n_6_t_0, persistSizeAndPosition: bool):...
    @staticmethod
    def ShowModelessWindow(owner: _n_4_t_4, formToShow: _n_6_t_0):...
    @staticmethod
    def ShowModelessWindow(owner: _n_6_t_0, formToShow: _n_6_t_0):...
    @staticmethod
    def ShowModelessWindow(formToShow: _n_6_t_0):...
    @staticmethod
    def TryGetSystemVariable(name: str) -> object:...
    @staticmethod
    def UpdateScreen():...
class CreateContextMenuHandler(_n_4_t_5, _n_4_t_6, _n_5_t_0):
    def __init__(self, A_0: object, A_1: _n_4_t_4) -> CreateContextMenuHandler:...
    def BeginInvoke(self, type: _n_4_t_8, callback: _n_4_t_9, obj: object) -> _n_4_t_7:...
    def EndInvoke(self, result: _n_4_t_7) -> object:...
    def Invoke(self, type: _n_4_t_8) -> object:...
class EnableWinFormHandler(_n_4_t_5, _n_4_t_6, _n_5_t_0):
    def __init__(self, A_0: object, A_1: _n_4_t_4) -> EnableWinFormHandler:...
    def BeginInvoke(self, o: object, enable: bool, callback: _n_4_t_9, obj: object) -> _n_4_t_7:...
    def EndInvoke(self, result: _n_4_t_7) -> bool:...
    def Invoke(self, o: object, enable: bool) -> bool:...
class FilterMessageWinFormsHandler(_n_4_t_5, _n_4_t_6, _n_5_t_0):
    def __init__(self, A_0: object, A_1: _n_4_t_4) -> FilterMessageWinFormsHandler:...
    def BeginInvoke(self, msg: object, callback: _n_4_t_9, obj: object) -> _n_4_t_7:...
    def EndInvoke(self, result: _n_4_t_7) -> bool:...
    def Invoke(self, msg: object) -> bool:...
class OnIdleWinFormsHandler(_n_4_t_5, _n_4_t_6, _n_5_t_0):
    def __init__(self, A_0: object, A_1: _n_4_t_4) -> OnIdleWinFormsHandler:...
    def BeginInvoke(self, callback: _n_4_t_9, obj: object) -> _n_4_t_7:...
    def EndInvoke(self, result: _n_4_t_7):...
    def Invoke(self):...
class OnWinFormsLoadedHandler(_n_4_t_5, _n_4_t_6, _n_5_t_0):
    def __init__(self, A_0: object, A_1: _n_4_t_4) -> OnWinFormsLoadedHandler:...
    def BeginInvoke(self, callback: _n_4_t_9, obj: object) -> _n_4_t_7:...
    def EndInvoke(self, result: _n_4_t_7):...
    def Invoke(self):...
class OnWpfLoadedHandler(_n_4_t_5, _n_4_t_6, _n_5_t_0):
    def __init__(self, A_0: object, A_1: _n_4_t_4) -> OnWpfLoadedHandler:...
    def BeginInvoke(self, callback: _n_4_t_9, obj: object) -> _n_4_t_7:...
    def EndInvoke(self, result: _n_4_t_7):...
    def Invoke(self):...
class PreProcessMessageWinFormsHandler(_n_4_t_5, _n_4_t_6, _n_5_t_0):
    def __init__(self, A_0: object, A_1: _n_4_t_4) -> PreProcessMessageWinFormsHandler:...
    def BeginInvoke(self, msg: object, callback: _n_4_t_9, obj: object) -> _n_4_t_7:...
    def EndInvoke(self, result: _n_4_t_7) -> bool:...
    def Invoke(self, msg: object) -> bool:...
