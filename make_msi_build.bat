@echo off
if "%1"=="" (set version=1.0.0) else (set version=%1)
set AdvancedInstaller="C:\Program Files (x86)\Caphyon\Advanced Installer 18.2\bin\x86\AdvancedInstaller.com"
set app_name=Passlock
set org_name=Passlock
set build_dir=%cd%\dist\passlock\
set icon_path=%cd%\icons\passlock.ico
set path_to_project=%cd%\%app_name%.aip
echo "Building %app_name% with version %version%"
%AdvancedInstaller% /newproject %path_to_project% -overwrite
%AdvancedInstaller% /edit %path_to_project% /SetVersion %version%
%AdvancedInstaller% /edit %path_to_project% /SetProperty ProductName="%app_name%"
%AdvancedInstaller% /edit %path_to_project% /SetProperty Manufacturer="%org_name%"
%AdvancedInstaller% /edit %path_to_project% /SetProperty PackageVersion=%version%
%AdvancedInstaller% /edit %path_to_project% /SetPackageName %app_name%_%version%_x86.msi -buildname DefaultBuild
%AdvancedInstaller% /edit %path_to_project% /SetIcon -icon "%icon_path%"
%AdvancedInstaller% /edit %path_to_project% /AddFolder APPDIR %build_dir%
%AdvancedInstaller% /edit %path_to_project% /NewShortcut -name %app_name% -dir DesktopFolder -target APPDIR\passlock\%app_name%.exe -icon %icon_path%
%AdvancedInstaller% /edit %path_to_project% /NewShortcut -name %app_name% -dir ProgramMenuFolder -target APPDIR\passlock\%app_name%.exe -icon %icon_path%
%AdvancedInstaller% /build %path_to_project%