@echo off
REM ===========================================================
REM Insurance ETL pipeline runner
REM Scheduled with Windows Task Scheduler, task name: InsuranceETL
REM Runs etl.py and analyze.py and appends output to pipeline.log
REM ===========================================================
REM
REM HOW TO MANAGE THE SCHEDULED TASK (run these in PowerShell)
REM
REM Run it now to test:
REM     schtasks /run /tn "InsuranceETL"
REM
REM Check status:
REM     schtasks /query /tn "InsuranceETL"
REM
REM Pause it (can be turned back on later):
REM     schtasks /change /tn "InsuranceETL" /disable
REM
REM Turn it back on:
REM     schtasks /change /tn "InsuranceETL" /enable
REM
REM Stop a run that is in progress (future runs still happen):
REM     schtasks /end /tn "InsuranceETL"
REM
REM Delete it permanently:
REM     schtasks /delete /tn "InsuranceETL" /f
REM
REM GUI option: open Task Scheduler, find InsuranceETL in the
REM Task Scheduler Library, right-click, Disable or Delete.
REM
REM NOTE: paths below are specific to my machine. Adjust them
REM if you run this elsewhere.
REM ===========================================================



cd /d E:\Learn_python\insurance-etl
echo [%date% %time%] Pipeline started >> pipeline.log
"C:\Users\Kolisetty\AppData\Local\Programs\Python\Python314\python.exe" etl.py >> pipeline.log 2>&1
"C:\Users\Kolisetty\AppData\Local\Programs\Python\Python314\python.exe" analyze.py >> pipeline.log 2>&1
echo [%date% %time%] Pipeline finished >> pipeline.


