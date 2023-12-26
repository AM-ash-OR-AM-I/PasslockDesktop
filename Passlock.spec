# -*- mode: python ; coding: utf-8 -*-
from kivymd import hooks_path as kivymd_hooks_path

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('all_files/', '.'), ('fonts/', 'fonts/'), ('icons/pass.png', '.')],
    hiddenimports=[],
    hookspath=[kivymd_hooks_path],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['numpy', 'jedi', 'psutil', 'tk', 'ipython', 'tcl', 'tcl8', 'tornado', 'cv2'],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Passlock',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['icons/pass.png'],
)
app = BUNDLE(
    exe,
    name='Passlock.app',
    icon='icons/pass.png',
    bundle_identifier=None,
)
