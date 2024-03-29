=========
Changelog
=========

Version 1.2.0
=============
- feat: Updated documentation links for PyPI publishing
- feat: Added documentation workflow

Version 1.1.2
=============
- bug(fix) Update `pandas.read_csv` function call to avoid deprecated positional arguments

Version 1.1.1
=============
- bug(fix) Correct issue with alpha characters in station ID string [#32](https://github.com/GenSci/NDBC/issues/32)
- bug(fix) Prevent continuous year looping when URLs fail.

Version 1.1.0
=============
- Added support for multiple data package retrieval through a more general `get_data()` function.
- Added deprecation flags to `get_stdmet()` function, which is being replaced by more general `get_data()`.
- Improved bad data flag detection and replacement with `np.NAN` values.
- Added property decorated getter functions for all identified data packages

Version 1.0.1
==============
- Modified month URL kwargs to better handle selecting months in the previous year. (fixes issue #20)
- Added `__repr__()` method so users can see the station ID when calling the object in the terminal
- Added demonstration Jupyter Notebook to make package usage clear.
