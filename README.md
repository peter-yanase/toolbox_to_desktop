# toolbox_to_desktop

This is a simple script that exports desktop entries from a toolbox on Fedora Silverblue.

## How to use

1. Run the script.
2. Search for application(s).
3. Restart system.

## Notes

1. The container name is set to the default value on Silverblue 37: `fedora-toolbox-37"`, if your toolbox has a different name, change the variable in the script. (See the line with the comment.)
2. If a launcher does not work, open the generated `.desktop` file in `~/.local/share/applications/` and try modifying it some more. For example, you could try changing `dbusactivatable` or `terminal` to `false`.

## History

This script was inspired by [A6GibKm's Silverblue tools](https://github.com/A6GibKm/silverblue-tools). I found their toolbox-export script overtly complicated considering the simplicity of the task at hand so I made a different solution.

## Dependencies

Python 3.5 or above.

## References:

- [https://stackoverflow.com/questions/49748390/how-to-make-a-new-path-object-from-parts-of-a-current-path-with-pathlib](https://stackoverflow.com/questions/49748390/how-to-make-a-new-path-object-from-parts-of-a-current-path-with-pathlib)
- [https://github.com/A6GibKm/silverblue-tools/blob/master/toolbox-export](https://github.com/A6GibKm/silverblue-tools/blob/master/toolbox-export)
- [https://ask.fedoraproject.org/t/silverblue-desktop-file-for-container-application-not-working/2801](https://ask.fedoraproject.org/t/silverblue-desktop-file-for-container-application-not-working/2801)
- [https://stackoverflow.com/questions/33625931/copy-file-with-pathlib-in-python](https://stackoverflow.com/questions/33625931/copy-file-with-pathlib-in-python)
- [https://community.spiceworks.com/topic/2242613-fedora-30-setting-file-association-with-non-standard-application](https://community.spiceworks.com/topic/2242613-fedora-30-setting-file-association-with-non-standard-application)
- [https://github.com/gnunn1/tilix/issues/345](https://github.com/gnunn1/tilix/issues/345)
- [https://stackoverflow.com/questions/1093322/how-do-i-check-which-version-of-python-is-running-my-script](https://stackoverflow.com/questions/1093322/how-do-i-check-which-version-of-python-is-running-my-script)
- [https://www.reddit.com/r/Fedora/comments/yvhfmh/is_it_possible_to_pin_an_app_in_dock_or_desktop/](https://www.reddit.com/r/Fedora/comments/yvhfmh/is_it_possible_to_pin_an_app_in_dock_or_desktop/)
- [https://www.reddit.com/r/Fedora/comments/rs1agz/silverblue_how_to_create_working_desktop_files/](https://www.reddit.com/r/Fedora/comments/rs1agz/silverblue_how_to_create_working_desktop_files/)
- [https://www.reddit.com/r/Fedora/comments/z1j5dx/tutorial_adding_gui_apps_from_toolbox_to_your/](https://www.reddit.com/r/Fedora/comments/z1j5dx/tutorial_adding_gui_apps_from_toolbox_to_your/)
