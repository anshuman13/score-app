import pandas as pd

temp_intervals = {pd.Interval(left=31, right=35, closed='right'): 3,
                  pd.Interval(left=35, right=36, closed='right'): 1,
                  pd.Interval(left=36, right=38, closed='right'): 0,
                  pd.Interval(left=38, right=39, closed='right'): 1,
                  pd.Interval(left=39, right=42, closed='right'): 2}

hr_intervals = {pd.Interval(left=25, right=40, closed='right'): 3,
                pd.Interval(left=40, right=50, closed='right'): 1,
                pd.Interval(left=50, right=90, closed='right'): 0,
                pd.Interval(left=90, right=110, closed='right'): 1,
                pd.Interval(left=110, right=130, closed='right'): 2,
                pd.Interval(left=130, right=220, closed='right'): 3}

rr_intervals = {pd.Interval(left=3, right=8, closed='right'): 3,
                pd.Interval(left=8, right=11, closed='right'): 1,
                pd.Interval(left=11, right=20, closed='right'): 0,
                pd.Interval(left=20, right=24, closed='right'): 2,
                pd.Interval(left=24, right=60, closed='right'): 3}