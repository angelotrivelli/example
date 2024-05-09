
from cx_Freeze import Executable, setup


exe_options = {
    "include_files": ["app_icon.ico"],
    "packages": []
}

# Needed to build the msi installer.
# The upgrade code GUID allows us to update an already installed app cleanly.
# You'll want to generate a different GUID if you want multiple versions of the app installed at once.
# add to path should allow this to run from anywhere
msi_options = {
    'upgrade_code': '{dddf903f-a781-44ba-aded-cc10b711495d}',
    'add_to_path': True
}

# this is for a cli app, so we don't need a base
base = None

    
the_application = [Executable(script        = "app.py",
                              base          = base,
                              shortcut_name = "example [1.0.0]",
                              shortcut_dir  = "DesktopFolder",
                              icon          = "app_icon.ico")]

setup(
    name = "example_application",
    version = "1.0.0",
    description = "exercise cx-freeze setup script for building a python app with msi installer",
    executables = the_application,
    options = {"build_exe": exe_options,
               "bdist_msi": msi_options},
)




