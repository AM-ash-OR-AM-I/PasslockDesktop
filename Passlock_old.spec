# -*- mode: python ; coding: utf-8 -*-
from kivy_deps import sdl2, glew

from kivymd import hooks_path as kivymd_hooks_path

block_cipher = None


a = Analysis(
    ['main.py'],
    pathex=["all_files\\"],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[kivymd_hooks_path],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['numpy', 'jedi', 'psutil', 'tk', 'ipython', 'tcl', 'tcl8', 'tornado', 'cv2'],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Passlock',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='icon\\pass_256.ico',
)
coll = COLLECT(
    exe,
    Tree("all_files\\"),
    a.binaries,
    a.zipfiles,
    a.datas,
    *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Passlock',
)