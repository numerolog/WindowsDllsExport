# DUMPEXPO.EXE (Mr-Un1k0d3r/WindowsDllsExport)
A list of all the DLLs export in C:\windows\system32\

The idea is to find some interesting export that can be used to evade some detection.

The list was extracted from the following builds:

```
(new dumper version)
Windows XP Build 2600 x86

(previous dumper version)
Windows 10 Build 19043
Windows 11 Build 22000
```

# Generate The List By Yourself

(new dumper version)

DUMPEXPO.c can be compiled and run locally (on linux we can use build.sh).

DUMPEXPO.exe can be used to gather the information on your system.

```
C:\DUMPER> PERFDUMP.BAT
```

(previous dumper version)

DumpExport.c can be compiled and run locally.

DumpExport.exe can be used to gather the information on your system.

```
PS> foreach($dll in gci -Path C:\windows\system32\ -Filter *.dll) { .\dumpexport.exe $($dll.Name) | out-file -FilePath .\$($dll.Name).txt -Encoding ASCII }
```

# Sqlite Database 

the `exports.db` is a sqlite3 database that contains the dll name and the export name in a table defined as following

`table|exports|exports|2|CREATE TABLE exports (dllname text, exportname text)`

The sqlite database can be imported into `sqlite_web` to query the database from a web interface.

`pip3 install sqlite_web`

Copy the `exports.db` and run `sqlite_web` using the following command

```
sqlite_web -H 0.0.0.0 -p 80 -r -x /opt/exports/exports.db
```

The `sqlite_web` interface can be queried as shown below

![query](https://github.com/Mr-Un1k0d3r/WindowsDllsExport/raw/main/query.png)

# JSON Format

A json file is also available `exports.json`

# Original authors
Mr.Un1k0d3r RingZer0 Team
