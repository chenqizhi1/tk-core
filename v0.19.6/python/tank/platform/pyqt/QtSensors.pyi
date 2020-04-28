# This Python file uses the following encoding: utf-8
#############################################################################
##
## Copyright (C) 2019 The Qt Company Ltd.
## Contact: https://www.qt.io/licensing/
##
## This file is part of Qt for Python.
##
## $QT_BEGIN_LICENSE:LGPL$
## Commercial License Usage
## Licensees holding valid commercial Qt licenses may use this file in
## accordance with the commercial license agreement provided with the
## Software or, alternatively, in accordance with the terms contained in
## a written agreement between you and The Qt Company. For licensing terms
## and conditions see https://www.qt.io/terms-conditions. For further
## information use the contact form at https://www.qt.io/contact-us.
##
## GNU Lesser General Public License Usage
## Alternatively, this file may be used under the terms of the GNU Lesser
## General Public License version 3 as published by the Free Software
## Foundation and appearing in the file LICENSE.LGPL3 included in the
## packaging of this file. Please review the following information to
## ensure the GNU Lesser General Public License version 3 requirements
## will be met: https://www.gnu.org/licenses/lgpl-3.0.html.
##
## GNU General Public License Usage
## Alternatively, this file may be used under the terms of the GNU
## General Public License version 2.0 or (at your option) the GNU General
## Public license version 3 or any later version approved by the KDE Free
## Qt Foundation. The licenses are as published by the Free Software
## Foundation and appearing in the file LICENSE.GPL2 and LICENSE.GPL3
## included in the packaging of this file. Please review the following
## information to ensure the GNU General Public License requirements will
## be met: https://www.gnu.org/licenses/gpl-2.0.html and
## https://www.gnu.org/licenses/gpl-3.0.html.
##
## $QT_END_LICENSE$
##
#############################################################################

"""
This file contains the exact signatures for all functions in module
PySide2.QtSensors, except for defaults which are replaced by "...".
"""

# Module PySide2.QtSensors
import PySide2
from PySide2.support.signature import typing
from PySide2.support.signature.mapping import (
    Virtual, Missing, Invalid, Default, Instance)

class Object(object): pass

import shiboken2 as Shiboken
Shiboken.Object = Object

import PySide2.QtCore
import PySide2.QtSensors


class QAccelerometer(PySide2.QtSensors.QSensor):

    def __init__(self, parent:PySide2.QtCore.QObject=...): ...
    def accelerationMode(self) -> PySide2.QtSensors.QAccelerometer.AccelerationMode: ...
    def reading(self) -> PySide2.QtSensors.QAccelerometerReading: ...
    def setAccelerationMode(self, accelerationMode:PySide2.QtSensors.QAccelerometer.AccelerationMode): ...


class QAccelerometerFilter(PySide2.QtSensors.QSensorFilter):

    def __init__(self): ...
    @typing.overload
    def filter(self, reading:PySide2.QtSensors.QAccelerometerReading) -> bool: ...
    @typing.overload
    def filter(self, reading:PySide2.QtSensors.QSensorReading) -> bool: ...


class QAccelerometerReading(PySide2.QtSensors.QSensorReading):

    def __init__(self, parent:PySide2.QtCore.QObject): ...
    def copyValuesFrom(self, other:PySide2.QtSensors.QSensorReading): ...
    def setX(self, x:float): ...
    def setY(self, y:float): ...
    def setZ(self, z:float): ...
    def x(self) -> float: ...
    def y(self) -> float: ...
    def z(self) -> float: ...


class QAltimeter(PySide2.QtSensors.QSensor):

    def __init__(self, parent:PySide2.QtCore.QObject=...): ...
    def reading(self) -> PySide2.QtSensors.QAltimeterReading: ...


class QAltimeterFilter(PySide2.QtSensors.QSensorFilter):

    def __init__(self): ...
    @typing.overload
    def filter(self, reading:PySide2.QtSensors.QAltimeterReading) -> bool: ...
    @typing.overload
    def filter(self, reading:PySide2.QtSensors.QSensorReading) -> bool: ...


class QAltimeterReading(PySide2.QtSensors.QSensorReading):

    def __init__(self, parent:PySide2.QtCore.QObject): ...
    def altitude(self) -> float: ...
    def copyValuesFrom(self, other:PySide2.QtSensors.QSensorReading): ...
    def setAltitude(self, altitude:float): ...


class QAmbientLightFilter(PySide2.QtSensors.QSensorFilter):

    def __init__(self): ...
    @typing.overload
    def filter(self, reading:PySide2.QtSensors.QAmbientLightReading) -> bool: ...
    @typing.overload
    def filter(self, reading:PySide2.QtSensors.QSensorReading) -> bool: ...


class QAmbientLightReading(PySide2.QtSensors.QSensorReading):

    def __init__(self, parent:PySide2.QtCore.QObject): ...
    def copyValuesFrom(self, other:PySide2.QtSensors.QSensorReading): ...
    def lightLevel(self) -> PySide2.QtSensors.QAmbientLightReading.LightLevel: ...
    def setLightLevel(self, lightLevel:PySide2.QtSensors.QAmbientLightReading.LightLevel): ...


class QAmbientLightSensor(PySide2.QtSensors.QSensor):

    def __init__(self, parent:PySide2.QtCore.QObject=...): ...
    def reading(self) -> PySide2.QtSensors.QAmbientLightReading: ...


class QAmbientTemperatureFilter(PySide2.QtSensors.QSensorFilter):

    def __init__(self): ...
    @typing.overload
    def filter(self, reading:PySide2.QtSensors.QAmbientTemperatureReading) -> bool: ...
    @typing.overload
    def filter(self, reading:PySide2.QtSensors.QSensorReading) -> bool: ...


class QAmbientTemperatureReading(PySide2.QtSensors.QSensorReading):

    def __init__(self, parent:PySide2.QtCore.QObject): ...
    def copyValuesFrom(self, other:PySide2.QtSensors.QSensorReading): ...
    def setTemperature(self, temperature:float): ...
    def temperature(self) -> float: ...


class QAmbientTemperatureSensor(PySide2.QtSensors.QSensor):

    def __init__(self, parent:PySide2.QtCore.QObject=...): ...
    def reading(self) -> PySide2.QtSensors.QAmbientTemperatureReading: ...


class QCompass(PySide2.QtSensors.QSensor):

    def __init__(self, parent:PySide2.QtCore.QObject=...): ...
    def reading(self) -> PySide2.QtSensors.QCompassReading: ...


class QCompassFilter(PySide2.QtSensors.QSensorFilter):

    def __init__(self): ...
    @typing.overload
    def filter(self, reading:PySide2.QtSensors.QCompassReading) -> bool: ...
    @typing.overload
    def filter(self, reading:PySide2.QtSensors.QSensorReading) -> bool: ...


class QCompassReading(PySide2.QtSensors.QSensorReading):

    def __init__(self, parent:PySide2.QtCore.QObject): ...
    def azimuth(self) -> float: ...
    def calibrationLevel(self) -> float: ...
    def copyValuesFrom(self, other:PySide2.QtSensors.QSensorReading): ...
    def setAzimuth(self, azimuth:float): ...
    def setCalibrationLevel(self, calibrationLevel:float): ...


class QDistanceFilter(PySide2.QtSensors.QSensorFilter):

    def __init__(self): ...
    @typing.overload
    def filter(self, reading:PySide2.QtSensors.QDistanceReading) -> bool: ...
    @typing.overload
    def filter(self, reading:PySide2.QtSensors.QSensorReading) -> bool: ...


class QDistanceReading(PySide2.QtSensors.QSensorReading):

    def __init__(self, parent:PySide2.QtCore.QObject): ...
    def copyValuesFrom(self, other:PySide2.QtSensors.QSensorReading): ...
    def distance(self) -> float: ...
    def setDistance(self, distance:float): ...


class QDistanceSensor(PySide2.QtSensors.QSensor):

    def __init__(self, parent:PySide2.QtCore.QObject=...): ...
    def reading(self) -> PySide2.QtSensors.QDistanceReading: ...


class QGyroscope(PySide2.QtSensors.QSensor):

    def __init__(self, parent:PySide2.QtCore.QObject=...): ...
    def reading(self) -> PySide2.QtSensors.QGyroscopeReading: ...


class QGyroscopeFilter(PySide2.QtSensors.QSensorFilter):

    def __init__(self): ...
    @typing.overload
    def filter(self, reading:PySide2.QtSensors.QGyroscopeReading) -> bool: ...
    @typing.overload
    def filter(self, reading:PySide2.QtSensors.QSensorReading) -> bool: ...


class QGyroscopeReading(PySide2.QtSensors.QSensorReading):

    def __init__(self, parent:PySide2.QtCore.QObject): ...
    def copyValuesFrom(self, other:PySide2.QtSensors.QSensorReading): ...
    def setX(self, x:float): ...
    def setY(self, y:float): ...
    def setZ(self, z:float): ...
    def x(self) -> float: ...
    def y(self) -> float: ...
    def z(self) -> float: ...


class QHolsterFilter(PySide2.QtSensors.QSensorFilter):

    def __init__(self): ...
    @typing.overload
    def filter(self, reading:PySide2.QtSensors.QHolsterReading) -> bool: ...
    @typing.overload
    def filter(self, reading:PySide2.QtSensors.QSensorReading) -> bool: ...


class QHolsterReading(PySide2.QtSensors.QSensorReading):

    def __init__(self, parent:PySide2.QtCore.QObject): ...
    def copyValuesFrom(self, other:PySide2.QtSensors.QSensorReading): ...
    def holstered(self) -> bool: ...
    def setHolstered(self, holstered:bool): ...


class QHolsterSensor(PySide2.QtSensors.QSensor):

    def __init__(self, parent:PySide2.QtCore.QObject=...): ...
    def reading(self) -> PySide2.QtSensors.QHolsterReading: ...


class QHumidityFilter(PySide2.QtSensors.QSensorFilter):

    def __init__(self): ...
    @typing.overload
    def filter(self, reading:PySide2.QtSensors.QHumidityReading) -> bool: ...
    @typing.overload
    def filter(self, reading:PySide2.QtSensors.QSensorReading) -> bool: ...


class QHumidityReading(PySide2.QtSensors.QSensorReading):

    def __init__(self, parent:PySide2.QtCore.QObject): ...
    def absoluteHumidity(self) -> float: ...
    def copyValuesFrom(self, other:PySide2.QtSensors.QSensorReading): ...
    def relativeHumidity(self) -> float: ...
    def setAbsoluteHumidity(self, value:float): ...
    def setRelativeHumidity(self, percent:float): ...


class QHumiditySensor(PySide2.QtSensors.QSensor):

    def __init__(self, parent:PySide2.QtCore.QObject=...): ...
    def reading(self) -> PySide2.QtSensors.QHumidityReading: ...


class QIRProximityFilter(PySide2.QtSensors.QSensorFilter):

    def __init__(self): ...
    @typing.overload
    def filter(self, reading:PySide2.QtSensors.QIRProximityReading) -> bool: ...
    @typing.overload
    def filter(self, reading:PySide2.QtSensors.QSensorReading) -> bool: ...


class QIRProximityReading(PySide2.QtSensors.QSensorReading):

    def __init__(self, parent:PySide2.QtCore.QObject): ...
    def copyValuesFrom(self, other:PySide2.QtSensors.QSensorReading): ...
    def reflectance(self) -> float: ...
    def setReflectance(self, reflectance:float): ...


class QIRProximitySensor(PySide2.QtSensors.QSensor):

    def __init__(self, parent:PySide2.QtCore.QObject=...): ...
    def reading(self) -> PySide2.QtSensors.QIRProximityReading: ...


class QLidFilter(PySide2.QtSensors.QSensorFilter):

    def __init__(self): ...
    @typing.overload
    def filter(self, reading:PySide2.QtSensors.QLidReading) -> bool: ...
    @typing.overload
    def filter(self, reading:PySide2.QtSensors.QSensorReading) -> bool: ...


class QLidReading(PySide2.QtSensors.QSensorReading):

    def __init__(self, parent:PySide2.QtCore.QObject): ...
    def backLidClosed(self) -> bool: ...
    def copyValuesFrom(self, other:PySide2.QtSensors.QSensorReading): ...
    def frontLidClosed(self) -> bool: ...
    def setBackLidClosed(self, closed:bool): ...
    def setFrontLidClosed(self, closed:bool): ...


class QLidSensor(PySide2.QtSensors.QSensor):

    def __init__(self, parent:PySide2.QtCore.QObject=...): ...
    def reading(self) -> PySide2.QtSensors.QLidReading: ...


class QLightFilter(PySide2.QtSensors.QSensorFilter):

    def __init__(self): ...
    @typing.overload
    def filter(self, reading:PySide2.QtSensors.QLightReading) -> bool: ...
    @typing.overload
    def filter(self, reading:PySide2.QtSensors.QSensorReading) -> bool: ...


class QLightReading(PySide2.QtSensors.QSensorReading):

    def __init__(self, parent:PySide2.QtCore.QObject): ...
    def copyValuesFrom(self, other:PySide2.QtSensors.QSensorReading): ...
    def lux(self) -> float: ...
    def setLux(self, lux:float): ...


class QLightSensor(PySide2.QtSensors.QSensor):

    def __init__(self, parent:PySide2.QtCore.QObject=...): ...
    def fieldOfView(self) -> float: ...
    def reading(self) -> PySide2.QtSensors.QLightReading: ...
    def setFieldOfView(self, fieldOfView:float): ...


class QMagnetometer(PySide2.QtSensors.QSensor):

    def __init__(self, parent:PySide2.QtCore.QObject=...): ...
    def reading(self) -> PySide2.QtSensors.QMagnetometerReading: ...
    def returnGeoValues(self) -> bool: ...
    def setReturnGeoValues(self, returnGeoValues:bool): ...


class QMagnetometerFilter(PySide2.QtSensors.QSensorFilter):

    def __init__(self): ...
    @typing.overload
    def filter(self, reading:PySide2.QtSensors.QMagnetometerReading) -> bool: ...
    @typing.overload
    def filter(self, reading:PySide2.QtSensors.QSensorReading) -> bool: ...


class QMagnetometerReading(PySide2.QtSensors.QSensorReading):

    def __init__(self, parent:PySide2.QtCore.QObject): ...
    def calibrationLevel(self) -> float: ...
    def copyValuesFrom(self, other:PySide2.QtSensors.QSensorReading): ...
    def setCalibrationLevel(self, calibrationLevel:float): ...
    def setX(self, x:float): ...
    def setY(self, y:float): ...
    def setZ(self, z:float): ...
    def x(self) -> float: ...
    def y(self) -> float: ...
    def z(self) -> float: ...


class QOrientationFilter(PySide2.QtSensors.QSensorFilter):

    def __init__(self): ...
    @typing.overload
    def filter(self, reading:PySide2.QtSensors.QOrientationReading) -> bool: ...
    @typing.overload
    def filter(self, reading:PySide2.QtSensors.QSensorReading) -> bool: ...


class QOrientationReading(PySide2.QtSensors.QSensorReading):

    def __init__(self, parent:PySide2.QtCore.QObject): ...
    def copyValuesFrom(self, other:PySide2.QtSensors.QSensorReading): ...
    def orientation(self) -> PySide2.QtSensors.QOrientationReading.Orientation: ...
    def setOrientation(self, orientation:PySide2.QtSensors.QOrientationReading.Orientation): ...


class QOrientationSensor(PySide2.QtSensors.QSensor):

    def __init__(self, parent:PySide2.QtCore.QObject=...): ...
    def reading(self) -> PySide2.QtSensors.QOrientationReading: ...


class QPressureFilter(PySide2.QtSensors.QSensorFilter):

    def __init__(self): ...
    @typing.overload
    def filter(self, reading:PySide2.QtSensors.QPressureReading) -> bool: ...
    @typing.overload
    def filter(self, reading:PySide2.QtSensors.QSensorReading) -> bool: ...


class QPressureReading(PySide2.QtSensors.QSensorReading):

    def __init__(self, parent:PySide2.QtCore.QObject): ...
    def copyValuesFrom(self, other:PySide2.QtSensors.QSensorReading): ...
    def pressure(self) -> float: ...
    def setPressure(self, pressure:float): ...
    def setTemperature(self, temperature:float): ...
    def temperature(self) -> float: ...


class QPressureSensor(PySide2.QtSensors.QSensor):

    def __init__(self, parent:PySide2.QtCore.QObject=...): ...
    def reading(self) -> PySide2.QtSensors.QPressureReading: ...


class QProximityFilter(PySide2.QtSensors.QSensorFilter):

    def __init__(self): ...
    @typing.overload
    def filter(self, reading:PySide2.QtSensors.QProximityReading) -> bool: ...
    @typing.overload
    def filter(self, reading:PySide2.QtSensors.QSensorReading) -> bool: ...


class QProximityReading(PySide2.QtSensors.QSensorReading):

    def __init__(self, parent:PySide2.QtCore.QObject): ...
    def close(self) -> bool: ...
    def copyValuesFrom(self, other:PySide2.QtSensors.QSensorReading): ...
    def setClose(self, close:bool): ...


class QProximitySensor(PySide2.QtSensors.QSensor):

    def __init__(self, parent:PySide2.QtCore.QObject=...): ...
    def reading(self) -> PySide2.QtSensors.QProximityReading: ...


class QRotationFilter(PySide2.QtSensors.QSensorFilter):

    def __init__(self): ...
    @typing.overload
    def filter(self, reading:PySide2.QtSensors.QRotationReading) -> bool: ...
    @typing.overload
    def filter(self, reading:PySide2.QtSensors.QSensorReading) -> bool: ...


class QRotationReading(PySide2.QtSensors.QSensorReading):

    def __init__(self, parent:PySide2.QtCore.QObject): ...
    def copyValuesFrom(self, other:PySide2.QtSensors.QSensorReading): ...
    def setFromEuler(self, x:float, y:float, z:float): ...
    def x(self) -> float: ...
    def y(self) -> float: ...
    def z(self) -> float: ...


class QRotationSensor(PySide2.QtSensors.QSensor):

    def __init__(self, parent:PySide2.QtCore.QObject=...): ...
    def hasZ(self) -> bool: ...
    def reading(self) -> PySide2.QtSensors.QRotationReading: ...
    def setHasZ(self, hasZ:bool): ...


class QSensor(PySide2.QtCore.QObject):

    def __init__(self, type:PySide2.QtCore.QByteArray, parent:PySide2.QtCore.QObject=...): ...
    def addFilter(self, filter:PySide2.QtSensors.QSensorFilter): ...
    def availableDataRates(self) -> typing.List: ...
    def axesOrientationMode(self) -> PySide2.QtSensors.QSensor.AxesOrientationMode: ...
    def backend(self) -> PySide2.QtSensors.QSensorBackend: ...
    def bufferSize(self) -> int: ...
    def connectToBackend(self) -> bool: ...
    def currentOrientation(self) -> int: ...
    def dataRate(self) -> int: ...
    @staticmethod
    def defaultSensorForType(type:PySide2.QtCore.QByteArray) -> PySide2.QtCore.QByteArray: ...
    def description(self) -> str: ...
    def efficientBufferSize(self) -> int: ...
    def error(self) -> int: ...
    def filters(self) -> typing.List: ...
    def identifier(self) -> PySide2.QtCore.QByteArray: ...
    def isActive(self) -> bool: ...
    def isAlwaysOn(self) -> bool: ...
    def isBusy(self) -> bool: ...
    def isConnectedToBackend(self) -> bool: ...
    def isFeatureSupported(self, feature:PySide2.QtSensors.QSensor.Feature) -> bool: ...
    def maxBufferSize(self) -> int: ...
    def outputRange(self) -> int: ...
    def outputRanges(self) -> typing.List: ...
    def reading(self) -> PySide2.QtSensors.QSensorReading: ...
    def removeFilter(self, filter:PySide2.QtSensors.QSensorFilter): ...
    @staticmethod
    def sensorTypes() -> typing.List: ...
    @staticmethod
    def sensorsForType(type:PySide2.QtCore.QByteArray) -> typing.List: ...
    def setActive(self, active:bool): ...
    def setAlwaysOn(self, alwaysOn:bool): ...
    def setAxesOrientationMode(self, axesOrientationMode:PySide2.QtSensors.QSensor.AxesOrientationMode): ...
    def setBufferSize(self, bufferSize:int): ...
    def setCurrentOrientation(self, currentOrientation:int): ...
    def setDataRate(self, rate:int): ...
    def setEfficientBufferSize(self, efficientBufferSize:int): ...
    def setIdentifier(self, identifier:PySide2.QtCore.QByteArray): ...
    def setMaxBufferSize(self, maxBufferSize:int): ...
    def setOutputRange(self, index:int): ...
    def setSkipDuplicates(self, skipDuplicates:bool): ...
    def setUserOrientation(self, userOrientation:int): ...
    def skipDuplicates(self) -> bool: ...
    def start(self) -> bool: ...
    def stop(self): ...
    def type(self) -> PySide2.QtCore.QByteArray: ...
    def userOrientation(self) -> int: ...


class QSensorBackend(PySide2.QtCore.QObject):

    def __init__(self, sensor:PySide2.QtSensors.QSensor, parent:PySide2.QtCore.QObject=...): ...
    def addDataRate(self, min:float, max:float): ...
    def addOutputRange(self, min:float, max:float, accuracy:float): ...
    def isFeatureSupported(self, feature:PySide2.QtSensors.QSensor.Feature) -> bool: ...
    def newReadingAvailable(self): ...
    def reading(self) -> PySide2.QtSensors.QSensorReading: ...
    def sensor(self) -> PySide2.QtSensors.QSensor: ...
    def sensorBusy(self): ...
    def sensorError(self, error:int): ...
    def sensorStopped(self): ...
    def setDataRates(self, otherSensor:PySide2.QtSensors.QSensor): ...
    def setDescription(self, description:str): ...
    def start(self): ...
    def stop(self): ...


class QSensorBackendFactory(Shiboken.Object):

    def __init__(self): ...
    def createBackend(self, sensor:PySide2.QtSensors.QSensor) -> PySide2.QtSensors.QSensorBackend: ...


class QSensorChangesInterface(Shiboken.Object):

    def __init__(self): ...
    def sensorsChanged(self): ...


class QSensorFilter(Shiboken.Object):

    def __init__(self): ...
    def filter(self, reading:PySide2.QtSensors.QSensorReading) -> bool: ...
    def setSensor(self, sensor:PySide2.QtSensors.QSensor): ...


class QSensorGestureManager(PySide2.QtCore.QObject):

    def __init__(self, parent:PySide2.QtCore.QObject=...): ...
    def gestureIds(self) -> typing.List: ...
    def recognizerSignals(self, recognizerId:str) -> typing.List: ...
    def registerSensorGestureRecognizer(self, recognizer:PySide2.QtSensors.QSensorGestureRecognizer) -> bool: ...
    @staticmethod
    def sensorGestureRecognizer(id:str) -> PySide2.QtSensors.QSensorGestureRecognizer: ...


class QSensorGesturePluginInterface(Shiboken.Object):

    def __init__(self): ...
    def createRecognizers(self) -> typing.List: ...
    def name(self) -> str: ...
    def supportedIds(self) -> typing.List: ...


class QSensorGestureRecognizer(PySide2.QtCore.QObject):

    def __init__(self, parent:PySide2.QtCore.QObject=...): ...
    def create(self): ...
    def createBackend(self): ...
    def gestureSignals(self) -> typing.List: ...
    def id(self) -> str: ...
    def isActive(self) -> bool: ...
    def start(self) -> bool: ...
    def startBackend(self): ...
    def stop(self) -> bool: ...
    def stopBackend(self): ...


class QSensorManager(Shiboken.Object):

    def __init__(self): ...
    @staticmethod
    def createBackend(sensor:PySide2.QtSensors.QSensor) -> PySide2.QtSensors.QSensorBackend: ...
    @staticmethod
    def isBackendRegistered(type:PySide2.QtCore.QByteArray, identifier:PySide2.QtCore.QByteArray) -> bool: ...
    @staticmethod
    def registerBackend(type:PySide2.QtCore.QByteArray, identifier:PySide2.QtCore.QByteArray, factory:PySide2.QtSensors.QSensorBackendFactory): ...
    @staticmethod
    def setDefaultBackend(type:PySide2.QtCore.QByteArray, identifier:PySide2.QtCore.QByteArray): ...
    @staticmethod
    def unregisterBackend(type:PySide2.QtCore.QByteArray, identifier:PySide2.QtCore.QByteArray): ...


class QSensorPluginInterface(Shiboken.Object):

    def __init__(self): ...
    def registerSensors(self): ...


class QSensorReading(PySide2.QtCore.QObject):

    def copyValuesFrom(self, other:PySide2.QtSensors.QSensorReading): ...
    def setTimestamp(self, timestamp:int): ...
    def timestamp(self) -> int: ...
    def value(self, index:int) -> typing.Any: ...
    def valueCount(self) -> int: ...


class QTapFilter(PySide2.QtSensors.QSensorFilter):

    def __init__(self): ...
    @typing.overload
    def filter(self, reading:PySide2.QtSensors.QSensorReading) -> bool: ...
    @typing.overload
    def filter(self, reading:PySide2.QtSensors.QTapReading) -> bool: ...


class QTapReading(PySide2.QtSensors.QSensorReading):

    def __init__(self, parent:PySide2.QtCore.QObject): ...
    def copyValuesFrom(self, other:PySide2.QtSensors.QSensorReading): ...
    def isDoubleTap(self) -> bool: ...
    def setDoubleTap(self, doubleTap:bool): ...
    def setTapDirection(self, tapDirection:PySide2.QtSensors.QTapReading.TapDirection): ...
    def tapDirection(self) -> PySide2.QtSensors.QTapReading.TapDirection: ...


class QTapSensor(PySide2.QtSensors.QSensor):

    def __init__(self, parent:PySide2.QtCore.QObject=...): ...
    def reading(self) -> PySide2.QtSensors.QTapReading: ...
    def returnDoubleTapEvents(self) -> bool: ...
    def setReturnDoubleTapEvents(self, returnDoubleTapEvents:bool): ...


class QTiltFilter(PySide2.QtSensors.QSensorFilter):

    def __init__(self): ...
    @typing.overload
    def filter(self, reading:PySide2.QtSensors.QSensorReading) -> bool: ...
    @typing.overload
    def filter(self, reading:PySide2.QtSensors.QTiltReading) -> bool: ...


class QTiltReading(PySide2.QtSensors.QSensorReading):

    def __init__(self, parent:PySide2.QtCore.QObject): ...
    def copyValuesFrom(self, other:PySide2.QtSensors.QSensorReading): ...
    def setXRotation(self, x:float): ...
    def setYRotation(self, y:float): ...
    def xRotation(self) -> float: ...
    def yRotation(self) -> float: ...


class QTiltSensor(PySide2.QtSensors.QSensor):

    def __init__(self, parent:PySide2.QtCore.QObject=...): ...
    def calibrate(self): ...
    def reading(self) -> PySide2.QtSensors.QTiltReading: ...


class qoutputrange(Shiboken.Object):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, qoutputrange:PySide2.QtSensors.qoutputrange): ...
    def __copy__(self): ...

# eof
