#include <windows.h>
#include <winnt.h>
#include <stdio.h>

VOID DumpListOfExport(VOID *lib);

VOID DumpListOfExport(VOID *lib) 
{
	PIMAGE_DOS_HEADER MZ = (PIMAGE_DOS_HEADER)lib;
	PIMAGE_NT_HEADERS PE = (PIMAGE_NT_HEADERS)((LPBYTE)MZ + MZ->e_lfanew);
	PIMAGE_EXPORT_DIRECTORY export = (PIMAGE_EXPORT_DIRECTORY)((LPBYTE)lib + PE->OptionalHeader.DataDirectory[IMAGE_DIRECTORY_ENTRY_EXPORT].VirtualAddress);
	
	DWORD *exportName = (DWORD*)((LPBYTE)lib + export->AddressOfNames);

	DWORD i = 0;
	for (i; i < export->NumberOfNames; i++) 
    {
		printf(">>FUNC;%s<<\n", lib + exportName[i]);
	}	
}

int main (int argc, char **argv) 
{
    CHAR *dll = argv[1];

    printf(">>FILE;%s<<\n", dll);
    // ignore error message, when a dependent dll is missing #https://stackoverflow.com/a/4265916
    SetErrorMode(SEM_NOOPENFILEERRORBOX | SEM_FAILCRITICALERRORS);
    HANDLE hDll = LoadLibrary(dll);
	SetErrorMode(0);

    if (hDll == NULL) 
    {
        printf(">>FAIL<<\n");
        ExitProcess(0);
    }

    DumpListOfExport(hDll);
    CloseHandle(hDll);
    return 0;
}


