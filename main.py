import sys
import time
import openvr

openvr.init(openvr.VRApplication_Overlay)
ids = []
for i in range(openvr.k_unMaxTrackedDeviceCount):
    if openvr.VRSystem().getTrackedDeviceClass(i) == 2:
        ids.append(i)

leftId = openvr.VRSystem().getTrackedDeviceIndexForControllerRole(openvr.TrackedControllerRole_LeftHand)
rightId = openvr.VRSystem().getTrackedDeviceIndexForControllerRole(openvr.TrackedControllerRole_RightHand)

print(leftId, rightId)
for i in ids:
    controller_status = openvr.VRSystem().getFloatTrackedDeviceProperty(i, openvr.Prop_DeviceBatteryPercentage_Float)
    print(controller_status)
    sys.stdout.flush()
    time.sleep(0.01)
overlay = openvr.IVROverlay()
notification = openvr.IVRNotifications()
left_battery = str(openvr.VRSystem().getFloatTrackedDeviceProperty(leftId, openvr.Prop_DeviceBatteryPercentage_Float) * 100)[0:4]
right_battery = str(openvr.VRSystem().getFloatTrackedDeviceProperty(rightId, openvr.Prop_DeviceBatteryPercentage_Float) * 100)[0:4]
try:
    openvr.IVRNotifications.createNotification(notification, overlay.createOverlay(overlayKey='battery', overlayName='batteryNotification') , 0, openvr.EVRNotificationType_Persistent, "left: %s %% \n right: %s %%" % (left_battery, right_battery), openvr.EVRNotificationStyle_Application, None)
except openvr.error_code.NotificationError_OK:
    pass
time.sleep(5)
openvr.shutdown()
