
import win32api, win32con, time

# retrieves the cursor's position:
# win32gui.GetCursorPos(point)





#def GetMousePos(x,y):


for x in range(0, 5):
	input('Hover mouse cursor for pos %d, then press enter')	
	pos1x, pos1y = win32api.GetCursorPos()

print(pos1x, pos1y)
input('Hover mouse cursor for pos 1, then press enter')
pos2x, pos2y = win32api.GetCursorPos()
print(pos1, pos2)
input('Hover mouse cursor for pos 1, then press enter')
pos1, pos2 = win32api.GetCursorPos()
print(pos1, pos2)

#win32api.SetCursorPos((x,y))
#win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
#win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
	
	
#hours = 1
#minutes = 20
#	
#hours_to_sec = hours * 60 * 60
#minutes_to_sec = minutes * 60
#time.sleep( hours_to_sec + minutes_to_sec )
#click(1200,400)
#time.sleep(3)
#click(1200,400)

input('Press ENTER to exit')
exit
