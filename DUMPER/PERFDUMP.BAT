

echo ^>^>DUMP;v1.0.1; > DUMP.TXT
ver >> DUMP.TXT
echo ^<^< >> DUMP.TXT


for %%f in (C:\windows\system32\*.dll) do (
 DUMPEXPO.exe %%~nf >> DUMP.TXT
)



echo ^>^>DONE^<^< >> DUMP.TXT

pause






