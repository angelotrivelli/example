from cx_Freeze import Executable, setup

exe_options = {
    "include_files": ["app_icon.ico"],
    "packages": []
}


msi_options = {
    'upgrade_code': '{dddf903f-a781-44ba-aded-cc10b711495d}',
    'add_to_path': True
}

# this is for a cli app, so we don't need a base?
base = None

    
the_application = [Executable(script        = "app.py",
                              target_name   = "my_example",
                              base          = base,
                              shortcut_name = "example [1.0.1]",
                              shortcut_dir  = "DesktopFolder",
                              icon          = "app_icon.ico")]

setup(
    name = "my_example",
    version = "1.0.1",
    description = "exercise cx-freeze setup script for building a python app with msi installer",
    executables = the_application,
    options = {"build_exe": exe_options,
               "bdist_msi": msi_options},
)
