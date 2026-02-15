# %%
from typing import Callable
import pandas as pd
import sys
from pathlib import Path

input_file = Path(sys.argv[1])
df = pd.read_csv(sys.argv[1])
df['time'] = pd.TimedeltaIndex(df['time'])

df_resampled = df.ffill(limit=20).set_index('time')\
    .resample('s').ffill(limit=20)\
    .dropna(axis=1, how='all')

df_notimedelta = df_resampled.reset_index()
df_notimedelta['time'] = (df_notimedelta['time'] - df_notimedelta['time'].min()).dt.total_seconds()

def standardize_unit(df: pd.DataFrame, prefix: str, units: dict[str, Callable[[pd.Series], pd.Series]], target_unit: str):
    target_col = f"{prefix} ({target_unit})"
    if target_col in df.columns:
        return
    for unit, transformer in units.items():
        source_col = f"{prefix} ({unit})"
        if source_col in df.columns:
            df[target_col] = transformer(df[source_col])
            print("Transforming", source_col, "to", target_col)
            df.drop(source_col, axis=1, inplace=True)
            return
    raise ValueError("No matching columns found")

# ICCU rename
for col in df_notimedelta.columns:
    if "[ICCU/2025]" in col:
        replacement = {col: col.replace("[ICCU/2025]", "[ICCU]")}
        print("Replacing", replacement)
        df_notimedelta.rename(columns=replacement, inplace=True)

temps = [
    "[BMS] Battery Inlet Temperature",
    "[BMS] Battery Max Temperature",
    "[BMS] Battery Min Temperature",
    "[BMS] Coolant temperature 2",
    "[HVAC] Coolant temperature 1",
    "[HVAC] Indoor Temperature",
    "[HVAC] Inverter temperature",
    "[HVAC] Outdoor Temperature",
    "[ICCU] Aux. Battery Temperature",
    "[ICCU] LDC Temperature",
    "[ICCU] OBC Temperature A",
    "[ICCU] OBC Temperature B"
]
for temp in temps:
    try:
        standardize_unit(df_notimedelta, temp, {"℉": lambda s: (s - 32)*5/9}, "℃")
    except ValueError as e:
        print(e)
        print("Skipping", temp)

speeds = [
    "[VCS] Vehicle speed (high res.)",
    "[HVAC] Real Vehicle Speed"
]
for speed in speeds:
    standardize_unit(df_notimedelta, speed, {"mph": lambda s: s * 1.609}, "km/h")

standardize_unit(df_notimedelta, "Distance travelled", {"miles": lambda s: s * 1.609}, "km")
standardize_unit(df_notimedelta, "HV EV Battery Power", {"hp": lambda s: s / 1.341}, "kW")

df_notimedelta['12V device load (A)'] = df_notimedelta['[ICCU] LDC Output Current (A)'] - df_notimedelta['[ICCU] Aux. Battery Current (A)']

output_file = input_file
df_notimedelta.to_csv(str(output_file.with_name("cleaned-" + input_file.name)), index=False)
