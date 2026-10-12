import sqlite3
import pandas as pd

# EXTRACT
df = pd.read_csv("data/insurance.csv")

# TRANSFORM
df = df.drop_duplicates()
df = df.dropna()
df["sex"] = df["sex"].str.strip().str.lower()
df["region"] = df["region"].str.strip().str.lower()
df["smoker"] = df["smoker"].str.strip().str.lower()

# Derived columns
df["age_group"] = pd.cut(
    df["age"],
    bins=[17, 30, 45, 60, 100],
    labels=["18-30", "31-45", "46-60", "60+"],
)
df["bmi_category"] = pd.cut(
    df["bmi"],
    bins=[0, 18.5, 25, 30, 100],
    labels=["underweight", "normal", "overweight", "obese"],
)

# LOAD
conn = sqlite3.connect("insurance.db")
df.to_sql("policies", conn, if_exists="replace", index=False)
conn.close()

print(f"Loaded {len(df)} rows into insurance.db")



'''
You created a Windows Task Scheduler task named `InsuranceETL`, not a real cron job, so you stop it with `schtasks`. Pick whichever fits:

**Pause it (you can turn it back on later)**

```powershell
schtasks /change /tn "InsuranceETL" /disable
```

To turn it back on:

```powershell
schtasks /change /tn "InsuranceETL" /enable
```

**Delete it permanently**

```powershell
schtasks /delete /tn "InsuranceETL" /f
```

The `/f` skips the confirmation prompt.

**Check that it worked**

```powershell
schtasks /query /tn "InsuranceETL"
```

If it was deleted, you'll get an error saying the task can't be found. If it was disabled, the status will show `Disabled`.

**If a run is in progress right now**

```powershell
schtasks /end /tn "InsuranceETL"
```

This stops the current run but doesn't prevent future ones, so also disable or delete the task.

**If you ever use real cron on Linux, WSL, or Docker**

```bash
crontab -l      # list your cron jobs
crontab -e      # open the file, then delete the line or put # in front of it
crontab -r      # remove ALL your cron jobs (careful)
```

You can also stop it from the GUI: open **Task Scheduler** from the Start menu, find `InsuranceETL` in the Task Scheduler Library, then right-click and choose **Disable** or **Delete**.

Deleting the task doesn't remove your project files, `run_pipeline.bat`, or `pipeline.log`. It only removes the schedule. I'd keep the `.bat` file, since it's part of your repo.
'''