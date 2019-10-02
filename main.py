import sys
import time
import openvr

openvr.init(openvr.VRApplication_Overlay)
ids = []

leftId = openvr.VRSystem().getTrackedDeviceIndexForControllerRole(openvr.TrackedControllerRole_LeftHand)
rightId = openvr.VRSystem().getTrackedDeviceIndexForControllerRole(openvr.TrackedControllerRole_RightHand)


def to_percent(value):
    return str(value*100)[0:4]


while True:
    overlay = openvr.IVROverlay()
    notification = openvr.IVRNotifications()
    left_battery = openvr.VRSystem().getFloatTrackedDeviceProperty(leftId, openvr.Prop_DeviceBatteryPercentage_Float)
    right_battery = openvr.VRSystem().getFloatTrackedDeviceProperty(rightId, openvr.Prop_DeviceBatteryPercentage_Float)

    if left_battery < 0.15:
        try:
            openvr.IVRNotifications.createNotification(notification, overlay.createOverlay(overlayKey='battery',
                                                                                           overlayName=''),
                                                       0, openvr.EVRNotificationType_Persistent,
                                                       "Left Battery low: \n %s %%" % (
                                                       to_percent(left_battery)),
                                                       openvr.EVRNotificationStyle_Application, None)
        except openvr.error_code.NotificationError_OK:  # why would this throw an error
            pass
    if right_battery < 0.15:
        try:
            openvr.IVRNotifications.createNotification(notification, overlay.createOverlay(overlayKey='battery',
                                                                                           overlayName=''),
                                                       0, openvr.EVRNotificationType_Persistent,
                                                       "Right Battery low: \n %s %%" % (
                                                       to_percent(right_battery)),
                                                       openvr.EVRNotificationStyle_Application, None)
        except openvr.error_code.NotificationError_OK:  # why would this throw an error
            pass

    time.sleep(60)
