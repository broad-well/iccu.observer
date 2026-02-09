
def compact_params(my2025: bool):
  return [
    [ # "[BMS] Coolant temperature 2":
      13035180, "COOLANT-TEMP2", -40, 80
    ],
    [ # "[BMS] Operating Time":
      13035248, "TOTAL OPTIME", 0, 100000
    ],
    [ # "[BMS] State of Charge BMS":
      13035250, "SOC", 0, 100
    ],
    [ # "[HVAC] Coolant temperature 1":
      13035264, "COOLANT-TEMP1", -40, 100
    ],
    [ # "[HVAC] Humidity sensor for automatic defogger":
      13035284, "HUMIDITY", 0, 100
    ],
    [ # "[HVAC] Indoor Temperature":
      13035188, "INDOOR-TEMP", -40, 100
    ],
    [ # "[HVAC] Outdoor Temperature":
      13035187, "OUTDOOR-TEMP", -40, 100
    ],
    [ # "[ICCU] Aux. Battery Current":
      13035418 if my2025 else 13035386, "12V-CURRENT", -100, 100
    ],
    [ # "[ICCU] Aux. Battery State of Charge":
      13035419 if my2025 else 13035387, "12V-SOC", 0, 100
    ],
    [ # "[ICCU] Aux. Battery Temperature":
      13035420 if my2025 else 13035389, "12V-TEMP", -40, 100
    ],
    [ # "[ICCU] Aux. Battery Voltage":
      13035421 if my2025 else 13035388, "12V-VOLTAGE", 0, 20
    ],
    [ # "[ICCU] LDC Input Voltage":
      13035422 if my2025 else 13035382, "LDC-V_in", 0, 2000
    ],
    [ # "[ICCU] LDC Output Voltage":
      13035424 if my2025 else 13035383, "LDC-V_out", 0, 20
    ],
    [ # "[ICCU] LDC Output Current":
      13035423 if my2025 else 13035384, "LDC-I_out", 0, 400
    ],
    [ # "[ICCU] LDC Temperature":
      13035425 if my2025 else 13035385, "LDC-TEMP", -40, 100
    ],
    [ # "[PS] Absolute wheels turn angle":
      13035286, "WHEEL-ANGLE", -360, 360
    ],
    [ # "[VCS] Vehicle speed (high res.)":
      13035350, "SPEED", 0, 300
    ],
    [ # "[VCMS] Charging socket connected":
      13035311, "CHARGING", 0, 1
    ],
    [ # "[VCMS] EVSE Output Current":
      13035334, "EVSE-I_out", 0, 500
    ],
    [ # "[VCMS] EVSE Output Voltage":
      13035333, "EVSE-V_out", 0, 1000
    ],
    [ # "[VCMS] EVSE Target Current":
      13035346, "EVSE-I_target", 0, 500
    ],
    [ # "[VCMS] EVSE Target Voltage":
      13035347, "EVSE-V_target", 0, 1000
    ]
  ]

def build_item(compact_param, x, y, width, height):
  return {
    "ItemType": 0,
    "Maximum": compact_param[3],
    "Minimum": compact_param[2],
    "PID_Id": compact_param[0],
    "ShowDefaultBackground": True,
    "FrameSize": 1.0,
    "BackgroundColor": "4278190080",
    "FrameColor": "4278190080",
    "TitleTextColor": "4294967295",
    "TitleFontSize": 10.0,
    "ValueNormalTextColor": "4294967295",
    "ValueFontSize": 24.0,
    "UnitsTextColor": "4294967295",
    "UnitsFontSize": 10.0,
    "GaugeLabelColor": "4294967295",
    "GaugeRimColor": "4294967295",
    "GaugeTickColor": "4294967295",
    "GaugePointerColor": "4292542464",
    "ChartLineColor": "4294967295",
    "GaugeRedLineColor": "4294901760",
    "GaugeShowRedLine": False,
    "GaugeRedLineStart": 0.0,
    "GaugeRedLineFinish": 0.0,
    "ValueUseLCDFont": False,
    "PositionX": x,
    "PositionY": y,
    "DesiredWidth": width,
    "DesiredHeight": height,
    "LinearScaleSize": 25.0,
    "PlaySound": False,
    "SoundName": "airhorn",
    "SoundStart": 0.0,
    "ValueFormat": 2,
    "LowWarningColor": "4289583334",
    "ShowLowWarning": False,
    "LowWarningStart": 0.0,
    "PlaySoundLow": False,
    "SoundNameLow": "airhorn",
    "SoundStartLow": 0.0,
    "GaugeKnobColor": "4285563024",
    "CustomName": compact_param[1],
    "OverrideName": True,
    "UseCustomMinMax": False,
    "ShowValue": True,
    "LinearOrientationHorizontal": True,
    "SegmentCount": 0,
    "CustomInterval": 5.0,
    "UseCustomInterval": False,
    "CornerRadius": {
      "Left": 0.0,
      "Top": 0.0,
      "Right": 0.0,
      "Bottom": 0.0,
      "HorizontalThickness": 0.0,
      "VerticalThickness": 0.0,
      "IsEmpty": True
    },
    "MinMaxAvgFontSize": 9.0,
    "ShowMinMax": False,
    "ShowAvg": False,
    "MinMaxAvgColor": "4294944000",
    "SetMinMaxAvgOnlyVisibleArea": True,
    "GradientColor1": "4279388832",
    "GradientColor2": "4278659698",
    "GradientOffsetPoint1": 0.153,
    "GradientOffsetPoint2": 0.984,
    "GaugeShowMinMaxMarkers": False,
    "GradientStartPoint": { "X": 0.0, "Y": 0.0, "IsEmpty": True },
    "GradientEndPoint": { "X": 1.0, "Y": 1.0, "IsEmpty": False },
    "CiruclarGaugeWidth": 12.0,
    "GaugeBlueLineColor": "4278190335",
    "GaugeShowBlueLine": False,
    "GaugeBlueLineStart": 0.0,
    "GaugeBlueLineFinish": 0.0,
    "ShowMinMaxPointers": False,
    "MinMaxPointersColor": "4294944000",
    "ChartItemType": 0,
    "LiveDataShowTime": 15,
    "ChartValuePositionCenter": False,
    "ChartLineWidth": 1,
    "PID_IDs": [],
    "HighWarningColor": "4289583334",
    "HighWarningStart": 0.0,
    "ShowHighWarning": False,
    "IndicatorBackgroundLowColor": "4278190335",
    "IndicatorBackgroundHighColor": "4294901760"
  }

def build_signature(my, y, width):
  return {
    "ItemType": 5,
    "Maximum": 100.0,
    "Minimum": 0.0,
    "PID_Id": -1,
    "ShowDefaultBackground": False,
    "FrameSize": 1.0,
    "BackgroundColor": "4281084972",
    "FrameColor": "4278190080",
    "TitleTextColor": "4294967295",
    "TitleFontSize": 17.0,
    "ValueNormalTextColor": "4294967295",
    "ValueFontSize": 33.0,
    "UnitsTextColor": "4294967295",
    "UnitsFontSize": 22.0,
    "GaugeLabelColor": "4294967295",
    "GaugeRimColor": "4294967295",
    "GaugeTickColor": "4294967295",
    "GaugePointerColor": "4292542464",
    "ChartLineColor": "4294967295",
    "GaugeRedLineColor": "4294901760",
    "GaugeShowRedLine": False,
    "GaugeRedLineStart": 0.0,
    "GaugeRedLineFinish": 0.0,
    "ValueUseLCDFont": False,
    "PositionX": width/2 - 150/2,
    "PositionY": y,
    "DesiredWidth": 150.0,
    "DesiredHeight": 60.0,
    "LinearScaleSize": 25.0,
    "PlaySound": False,
    "SoundName": "airhorn",
    "SoundStart": 0.0,
    "ValueFormat": 2,
    "LowWarningColor": "4289583334",
    "ShowLowWarning": False,
    "LowWarningStart": 100.0,
    "PlaySoundLow": False,
    "SoundNameLow": "airhorn",
    "SoundStartLow": 0.0,
    "GaugeKnobColor": "4285563024",
    "CustomName": "ICCU.OBSERVER " + my,
    "OverrideName": True,
    "UseCustomMinMax": False,
    "ShowValue": True,
    "LinearOrientationHorizontal": True,
    "SegmentCount": 0,
    "CustomInterval": 5.0,
    "UseCustomInterval": False,
    "CornerRadius": {
      "Left": 0.0,
      "Top": 0.0,
      "Right": 0.0,
      "Bottom": 0.0,
      "HorizontalThickness": 0.0,
      "VerticalThickness": 0.0,
      "IsEmpty": True
    },
    "MinMaxAvgFontSize": 9.0,
    "ShowMinMax": False,
    "ShowAvg": False,
    "MinMaxAvgColor": "4294944000",
    "SetMinMaxAvgOnlyVisibleArea": True,
    "GradientColor1": "4278215680",
    "GradientColor2": "4278222848",
    "GradientOffsetPoint1": 0.15,
    "GradientOffsetPoint2": 0.98,
    "GaugeShowMinMaxMarkers": False,
    "GradientStartPoint": { "X": 0.0, "Y": 0.0, "IsEmpty": True },
    "GradientEndPoint": { "X": 1.0, "Y": 1.0, "IsEmpty": False },
    "CiruclarGaugeWidth": 12.0,
    "GaugeBlueLineColor": "4278190335",
    "GaugeShowBlueLine": False,
    "GaugeBlueLineStart": 0.0,
    "GaugeBlueLineFinish": 0.0,
    "ShowMinMaxPointers": False,
    "MinMaxPointersColor": "4294944000",
    "ChartItemType": 0,
    "LiveDataShowTime": 15,
    "ChartValuePositionCenter": False,
    "ChartLineWidth": 1,
    "PID_IDs": [],
    "HighWarningColor": "4289583334",
    "HighWarningStart": 100.0,
    "ShowHighWarning": False,
    "IndicatorBackgroundLowColor": "4278190335",
    "IndicatorBackgroundHighColor": "4294901760"
  }

def build_dash(params, my: str):
  container_width = 600
  dash = {"ItemsCount": 0, "Items": [], "Title": "iccu.observer", "DashboardType": 8, "UpdateInBackground": True}
  ys = [0] * 3 + [110] * 4 + [220] * 4 + [320] * 4 + [430] * 2 + [540] * 5
  rows = [3, 4, 4, 4, 2, 5]
  row_i, row_j = 0, 0
  for i, compact in enumerate(params):
    y = ys[i]
    x = row_j / rows[row_i] * container_width
    dash["Items"].append(build_item(compact, x, y, container_width / rows[row_i], 100))
    row_j += 1
    if row_j == rows[row_i]:
      row_i += 1
      row_j = 0
  dash["Items"].append(build_signature(my, 650, container_width))
  return dash


if __name__ == "__main__":
  import json
  with open("2025_dashboard.json", "w") as dashout:
    json.dump([build_dash(compact_params(True), "MY2025+")], dashout)

  with open("2022-4_dashboard.json", "w") as dashout:
    json.dump([build_dash(compact_params(False), "MY21-24")], dashout)
