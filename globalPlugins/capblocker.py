import globalPluginHandler
import keyboardHandler
import winInputHook

orig_internal_keyDownEvent = None
def internal_keyDownEvent(vkCode,scanCode,extended,injected):
	keyboardHandler.lastNVDAModifier = None
	return orig_internal_keyDownEvent(vkCode,scanCode,extended,injected)

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def __init__(self):
		global orig_internal_keyDownEvent
		super().__init__()
		orig_internal_keyDownEvent = keyboardHandler.internal_keyDownEvent
		keyboardHandler.internal_keyDownEvent = orig_internal_keyDownEvent 
		winInputHook.keyDownCallback = internal_keyDownEvent
