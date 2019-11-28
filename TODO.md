* 1) .tox/py37/lib/python3.7/enum.py line 426 - replace the frame hack if a blessed way to know the calling 
* 2) .tox/py37/lib/python3.7/types.py line 201 - Implement this in C. 
* 3) .tox/py37/lib/python3.7/types.py line 256 - Implement this in C. 
* 4) .tox/py37/lib/python3.7/site-packages/numpy/lib/npyio.py line 423 - Use contextlib.ExitStack once we drop Python 2 
* 5) .tox/py37/lib/python3.7/site-packages/numpy/lib/npyio.py line 982 - emit portability warning? 
* 6) .tox/py37/lib/python3.7/site-packages/numpy/lib/_datasource.py line 143 - .zip support, .tar support? 
* 7) .tox/py37/lib/python3.7/site-packages/numpy/lib/_datasource.py line 415 - Doesn't handle compressed files! 
* 8) .tox/py37/lib/python3.7/site-packages/numpy/lib/_datasource.py line 487 - This should be more robust.  Handles case where path includes 
* 9) .tox/py37/lib/python3.7/site-packages/numpy/lib/_datasource.py line 605 - There is no support for opening a file for writing which 
* 10) .tox/py37/lib/python3.7/site-packages/numpy/lib/_datasource.py line 608 - Add a ``subdir`` parameter for specifying the subdirectory 
* 11) .tox/py37/lib/python3.7/site-packages/numpy/lib/mixins.py line 168 - handle the optional third argument for __pow__? 
* 12) .tox/py37/lib/python3.7/site-packages/numpy/lib/tests/test_io.py line 298 - specify exact message 
* 13) .tox/py37/lib/python3.7/site-packages/numpy/lib/tests/test_mixins.py line 89 - test div on Python 2, only 
* 14) .tox/py37/lib/python3.7/site-packages/numpy/ma/tests/test_old_ma.py line 656 - FIXME: Find out what the following raises a warning in r8247 
* 15) .tox/py37/lib/python3.7/site-packages/numpy/ma/tests/test_core.py line 5049 - Test masked_object, masked_equal, ... 
* 16) .tox/py37/lib/python3.7/site-packages/numpy/random/tests/test_random.py line 986 - Include test for randint once it can broadcast 
* 17) .tox/py37/lib/python3.7/site-packages/numpy/random/tests/test_random.py line 1644 - Uncomment once randint can broadcast arguments 
* 18) .tox/py37/lib/python3.7/site-packages/numpy/linalg/tests/test_linalg.py line 1704 - are there no other tests for cholesky? 
* 19) .tox/py37/lib/python3.7/site-packages/numpy/f2py/crackfortran.py line 135 -  
* 20) .tox/py37/lib/python3.7/site-packages/numpy/f2py/crackfortran.py line 1880 -  
* 21) .tox/py37/lib/python3.7/site-packages/numpy/f2py/crackfortran.py line 2438 - test .eq., .neq., etc replacements. 
* 22) .tox/py37/lib/python3.7/site-packages/numpy/f2py/crackfortran.py line 3127 -  
* 23) .tox/py37/lib/python3.7/site-packages/numpy/polynomial/_polybase.py line 308 - we're stuck with disabling math formatting until we handle 
* 24) .tox/py37/lib/python3.7/site-packages/numpy/core/numeric.py line 463 - this works around .astype(bool) not working properly (gh-9847) 
* 25) .tox/py37/lib/python3.7/site-packages/numpy/core/_add_newdocs.py line 1897 - ). 
* 26) .tox/py37/lib/python3.7/site-packages/numpy/core/_add_newdocs.py line 6823 - work out how to put this on the base class, np.floating 
* 27) .tox/py37/lib/python3.7/site-packages/numpy/core/_dtype.py line 182 - this path can never be reached 
* 28) .tox/py37/lib/python3.7/site-packages/numpy/core/_dtype.py line 191 - this duplicates the C append_metastr_to_string 
* 29) .tox/py37/lib/python3.7/site-packages/numpy/core/include/numpy/multiarray_api.txt line 426 - For NumPy 2.0, this could accept an order parameter which 
* 30) .tox/py37/lib/python3.7/site-packages/numpy/core/include/numpy/multiarray_api.txt line 690 - For NumPy 2.0, add a NPY_CASTING parameter. 
* 31) .tox/py37/lib/python3.7/site-packages/numpy/core/include/numpy/multiarray_api.txt line 964 - In NumPy 2.0, should make the iteration order a parameter. 
* 32) .tox/py37/lib/python3.7/site-packages/numpy/core/tests/test_datetime.py line 825 - Changing to 'same_kind' or 'safe' casting in the ufuncs by 
* 33) .tox/py37/lib/python3.7/site-packages/numpy/core/tests/test_datetime.py line 1358 - Allowing unsafe casting by 
* 34) .tox/py37/lib/python3.7/site-packages/numpy/core/tests/test_datetime.py line 2274 - add absolute (gold standard) time span limit strings 
* 35) .tox/py37/lib/python3.7/site-packages/numpy/core/tests/test_multiarray.py line 6479 - test for multidimensional 
* 36) .tox/py37/lib/python3.7/site-packages/numpy/core/tests/test_umath_complex.py line 14 - branch cuts (use Pauli code) 
* 37) .tox/py37/lib/python3.7/site-packages/numpy/core/tests/test_umath_complex.py line 15 - conj 'symmetry' 
* 38) .tox/py37/lib/python3.7/site-packages/numpy/core/tests/test_umath_complex.py line 16 - FPU exceptions 
* 39) .tox/py37/lib/python3.7/site-packages/numpy/core/tests/test_umath_complex.py line 25 - replace with a check on whether platform-provided C99 funcs are used 
* 40) .tox/py37/lib/python3.7/site-packages/numpy/core/tests/test_umath_complex.py line 28 - This can be xfail when the generator functions are got rid of. 
* 41) .tox/py37/lib/python3.7/site-packages/numpy/core/tests/test_umath_complex.py line 124 - This can be xfail when the generator functions are got rid of. 
* 42) .tox/py37/lib/python3.7/site-packages/numpy/core/tests/test_umath_complex.py line 469 - This can be xfail when the generator functions are got rid of. 
* 43) .tox/py37/lib/python3.7/site-packages/numpy/distutils/npy_pkg_config.py line 377 -  
* 44) .tox/py37/lib/python3.7/site-packages/numpy/distutils/fcompiler/intel.py line 26 - could use -Xlinker here, if it's supported 
* 45) .tox/py37/lib/python3.7/site-packages/numpy/distutils/fcompiler/__init__.py line 1029 - implement get_f90flags and use it in _compile similarly to get_f77flags 
* 46) .tox/py37/lib/python3.7/site-packages/numpy/distutils/fcompiler/gnu.py line 272 - could use -Xlinker here, if it's supported 
* 47) .tox/py37/lib/python3.7/site-packages/numpy/distutils/command/build_src.py line 539 - --inplace support for sdist command 
* 48) .tox/py37/lib/python3.7/site-packages/pluggy/manager.py line 142 - remove when we drop implprefix in 1.0 
* 49) .tox/py37/lib/python3.7/site-packages/pip/_vendor/retrying.py line 84 - add chaining of stop behaviors 
* 50) .tox/py37/lib/python3.7/site-packages/pip/_vendor/retrying.py line 102 - add chaining of wait behaviors 
* 51) .tox/py37/lib/python3.7/site-packages/pip/_vendor/retrying.py line 132 - simplify retrying by Exception types 
* 52) .tox/py37/lib/python3.7/site-packages/pip/_vendor/pep517/wrappers.py line 129 - Is this over-engineered? Maybe frontends only need to 
* 53) .tox/py37/lib/python3.7/site-packages/pip/_vendor/cachecontrol/controller.py line 181 - There is an assumption that the result will be a 
* 54) .tox/py37/lib/python3.7/site-packages/pip/_vendor/cachecontrol/filewrapper.py line 47 - Add some logging here... 
* 55) .tox/py37/lib/python3.7/site-packages/pip/_vendor/requests/adapters.py line 502 - Remove this in 3.0.0: see #2811 
* 56) .tox/py37/lib/python3.7/site-packages/pip/_vendor/requests/hooks.py line 20 - response is the only one 
* 57) .tox/py37/lib/python3.7/site-packages/pip/_vendor/packaging/tags.py line 88 - Is using py_version_nodot for interpreter version critical? 
* 58) .tox/py37/lib/python3.7/site-packages/pip/_vendor/packaging/tags.py line 229 - Need to care about 32-bit PPC for ppc64 through 10.2? 
* 59) .tox/py37/lib/python3.7/site-packages/pip/_vendor/packaging/requirements.py line 86 - Can we test whether something is contained within a requirement? 
* 60) .tox/py37/lib/python3.7/site-packages/pip/_vendor/packaging/requirements.py line 89 - Can we normalize the name and extra name? 
* 61) .tox/py37/lib/python3.7/site-packages/pip/_vendor/urllib3/connection.py line 178 - Fix tunnel so it doesn't depend on self.sock state. 
* 62) .tox/py37/lib/python3.7/site-packages/pip/_vendor/urllib3/exceptions.py line 238 - (t-8ch): Stop inheriting from AssertionError in v2.0. 
* 63) .tox/py37/lib/python3.7/site-packages/pip/_vendor/urllib3/connectionpool.py line 481 - Add optional support for socket.gethostbyname checking. 
* 64) .tox/py37/lib/python3.7/site-packages/pip/_vendor/urllib3/contrib/securetransport.py line 627 - should I do clean shutdown here? Do I have to? 
* 65) .tox/py37/lib/python3.7/site-packages/pip/_vendor/urllib3/contrib/securetransport.py line 787 - Well, crap. 
* 66) .tox/py37/lib/python3.7/site-packages/pip/_vendor/urllib3/contrib/securetransport.py line 797 - Update in line with above. 
* 67) .tox/py37/lib/python3.7/site-packages/pip/_vendor/urllib3/util/url.py line 406 - Remove this when we break backwards compatibility. 
* 68) .tox/py37/lib/python3.7/site-packages/pip/_vendor/html5lib/serializer.py line 302 - Add namespace support here 
* 69) .tox/py37/lib/python3.7/site-packages/pip/_vendor/chardet/sbcsgroupprober.py line 57 - Restore Hungarian encodings (iso-8859-2 and windows-1250) 
* 70) .tox/py37/lib/python3.7/site-packages/pip/_vendor/distlib/version.py line 259 - fill this out 
* 71) .tox/py37/lib/python3.7/site-packages/pip/_vendor/distlib/version.py line 507 - unintended side-effect on, e.g., "2003.05.09" 
* 72) .tox/py37/lib/python3.7/site-packages/pip/_vendor/distlib/util.py line 396 - check k, v for valid values 
* 73) .tox/py37/lib/python3.7/site-packages/pip/_vendor/distlib/metadata.py line 272 - document the mapping API and UNKNOWN default key 
* 74) .tox/py37/lib/python3.7/site-packages/pip/_vendor/distlib/metadata.py line 633 - could add iter* variants 
* 75) .tox/py37/lib/python3.7/site-packages/pip/_vendor/distlib/metadata.py line 1046 - other fields such as contacts 
* 76) .tox/py37/lib/python3.7/site-packages/pip/_vendor/distlib/locators.py line 759 - Note: this cache is never actually cleared. It's assumed that 
* 77) .tox/py37/lib/python3.7/site-packages/pip/_vendor/distlib/locators.py line 922 - SHA256 digest 
* 78) .tox/py37/lib/python3.7/site-packages/pip/_vendor/distlib/wheel.py line 788 - version verification 
* 79) .tox/py37/lib/python3.7/site-packages/pip/_vendor/msgpack/fallback.py line 627 - should we eliminate the recursion? 
* 80) .tox/py37/lib/python3.7/site-packages/pip/_vendor/msgpack/fallback.py line 631 - check whether we need to call `list_hook` 
* 81) .tox/py37/lib/python3.7/site-packages/pip/_vendor/msgpack/fallback.py line 639 - is the interaction between `list_hook` and `use_list` ok? 
* 82) .tox/py37/lib/python3.7/site-packages/pip/_vendor/msgpack/fallback.py line 644 - check whether we need to call hooks 
* 83) .tox/py37/lib/python3.7/site-packages/pip/_internal/wheel.py line 348 - Investigate and break this up. 
* 84) .tox/py37/lib/python3.7/site-packages/pip/_internal/wheel.py line 349 - Look into moving this into a dedicated class for representing an 
* 85) .tox/py37/lib/python3.7/site-packages/pip/_internal/wheel.py line 702 - Maybe move the class into the models sub-package 
* 86) .tox/py37/lib/python3.7/site-packages/pip/_internal/wheel.py line 703 - Maybe move the install code into this class 
* 87) .tox/py37/lib/python3.7/site-packages/pip/_internal/wheel.py line 811 - improve this behavior 
* 88) .tox/py37/lib/python3.7/site-packages/pip/_internal/wheel.py line 1110 - by @pradyunsg 
* 89) .tox/py37/lib/python3.7/site-packages/pip/_internal/req/req_file.py line 232 - Why not use `comes_from='-r {} (line {})'` here as well? 
* 90) .tox/py37/lib/python3.7/site-packages/pip/_internal/req/req_file.py line 349 - handle space after '\'. 
* 91) .tox/py37/lib/python3.7/site-packages/pip/_internal/operations/prepare.py line 124 - Breakup into smaller functions 
* 92) .tox/py37/lib/python3.7/site-packages/pip/_internal/utils/logging.py line 33 - eliminate the need to use "import as" once mypy addresses some 
* 93) .tox/py37/lib/python3.7/site-packages/pip/_internal/utils/logging.py line 45 - eliminate the need to import Fore once mypy addresses some of its 
* 94) .tox/py37/lib/python3.7/site-packages/pip/_internal/utils/logging.py line 157 - Use Formatter.default_time_format after dropping PY2. 
* 95) .tox/py37/lib/python3.7/site-packages/pip/_internal/utils/misc.py line 819 - remove this when we drop PY2 support. 
* 96) .tox/py37/lib/python3.7/site-packages/pip/_internal/cli/base_command.py line 134 - Try to get these passing down from the command? 
* 97) .tox/py37/lib/python3.7/site-packages/NDBC/NDBC.py line 319 - (ryan@gensci.org): Build out function to look for values that are all '9' and replace them with None or NaN to indicate lack of valid data. 
* 98) .tox/py37/lib/python3.7/site-packages/requests/adapters.py line 502 - Remove this in 3.0.0: see #2811 
* 99) .tox/py37/lib/python3.7/site-packages/requests/hooks.py line 20 - response is the only one 
* 100) .tox/py37/lib/python3.7/site-packages/packaging/tags.py line 88 - Is using py_version_nodot for interpreter version critical? 
* 101) .tox/py37/lib/python3.7/site-packages/packaging/tags.py line 229 - Need to care about 32-bit PPC for ppc64 through 10.2? 
* 102) .tox/py37/lib/python3.7/site-packages/packaging/requirements.py line 86 - Can we test whether something is contained within a requirement? 
* 103) .tox/py37/lib/python3.7/site-packages/packaging/requirements.py line 89 - Can we normalize the name and extra name? 
* 104) .tox/py37/lib/python3.7/site-packages/_pytest/logging.py line 85 - optimize this by introducing an option that tells the 
* 105) .tox/py37/lib/python3.7/site-packages/_pytest/main.py line 681 - remove parametrized workaround once collection structure contains parametrization 
* 106) .tox/py37/lib/python3.7/site-packages/_pytest/junitxml.py line 516 - breasks for --dist=each 
* 107) .tox/py37/lib/python3.7/site-packages/_pytest/runner.py line 243 - investigate unification 
* 108) .tox/py37/lib/python3.7/site-packages/_pytest/terminal.py line 996 - revisit after marks scope would be fixed 
* 109) .tox/py37/lib/python3.7/site-packages/_pytest/cacheprovider.py line 388 - evaluate generating upward relative paths 
* 110) .tox/py37/lib/python3.7/site-packages/_pytest/mark/evaluate.py line 54 - Investigate why SyntaxError.offset is Optional, and if it can be None here. 
* 111) .tox/py37/lib/python3.7/site-packages/_pytest/config/__init__.py line 299 - DeprecationWarning, people should use hookimpl 
* 112) .tox/py37/lib/python3.7/site-packages/_pytest/assertion/__init__.py line 56 - (typing): Add a protocol for mark_rewrite() and use it 
* 113) .tox/py37/lib/python3.7/site-packages/urllib3/connection.py line 178 - Fix tunnel so it doesn't depend on self.sock state. 
* 114) .tox/py37/lib/python3.7/site-packages/urllib3/exceptions.py line 238 - (t-8ch): Stop inheriting from AssertionError in v2.0. 
* 115) .tox/py37/lib/python3.7/site-packages/urllib3/connectionpool.py line 481 - Add optional support for socket.gethostbyname checking. 
* 116) .tox/py37/lib/python3.7/site-packages/urllib3/contrib/securetransport.py line 627 - should I do clean shutdown here? Do I have to? 
* 117) .tox/py37/lib/python3.7/site-packages/urllib3/contrib/securetransport.py line 787 - Well, crap. 
* 118) .tox/py37/lib/python3.7/site-packages/urllib3/contrib/securetransport.py line 797 - Update in line with above. 
* 119) .tox/py37/lib/python3.7/site-packages/urllib3/util/url.py line 406 - Remove this when we break backwards compatibility. 
* 120) .tox/py37/lib/python3.7/site-packages/dateutil/rrule.py line 1181 - Check -numweeks for next year. 
* 121) .tox/py37/lib/python3.7/site-packages/dateutil/parser/_parser.py line 55 - pandas.core.tools.datetimes imports this explicitly.  Might be worth 
* 122) .tox/py37/lib/python3.7/site-packages/dateutil/parser/_parser.py line 271 - "Tues" 
* 123) .tox/py37/lib/python3.7/site-packages/dateutil/parser/_parser.py line 273 - "Thurs" 
* 124) .tox/py37/lib/python3.7/site-packages/dateutil/parser/_parser.py line 278 - "Febr" 
* 125) .tox/py37/lib/python3.7/site-packages/dateutil/parser/_parser.py line 297 - ERA = ["AD", "BC", "CE", "BCE", "Stardate", 
* 126) .tox/py37/lib/python3.7/site-packages/dateutil/parser/_parser.py line 780 - not hit in tests 
* 127) .tox/py37/lib/python3.7/site-packages/dateutil/parser/_parser.py line 818 - check that l[i + 1] is integer? 
* 128) .tox/py37/lib/python3.7/site-packages/dateutil/parser/_parser.py line 826 - Check that l[i+3] is minute-like? 
* 129) .tox/py37/lib/python3.7/site-packages/dateutil/parser/_parser.py line 913 - Check if res attributes already set. 
* 130) .tox/py37/lib/python3.7/site-packages/dateutil/parser/_parser.py line 937 - checking that hour/minute/second are not 
* 131) .tox/py37/lib/python3.7/site-packages/dateutil/parser/_parser.py line 944 - try/except for this? 
* 132) .tox/py37/lib/python3.7/site-packages/dateutil/parser/_parser.py line 1035 - Are we sure this is the right condition here? 
* 133) .tox/py37/lib/python3.7/site-packages/dateutil/parser/_parser.py line 1103 - Every usage of this function sets res.second to the return 
* 134) .tox/py37/lib/python3.7/site-packages/dateutil/parser/_parser.py line 1123 - Is this going to admit a lot of false-positives for when we 
* 135) .tox/py37/lib/python3.7/site-packages/dateutil/zoneinfo/__init__.py line 25 - switch to FileNotFoundError? 
* 136) .tox/py37/lib/python3.7/site-packages/dateutil/zoneinfo/__init__.py line 76 - Remove after deprecation period. 
* 137) .tox/py37/lib/python3.7/site-packages/dateutil/tz/_factories.py line 43 - Maybe this should be under a lock? 
* 138) .tox/py37/lib/python3.7/site-packages/dateutil/tz/_factories.py line 68 - Maybe this should be under a lock? 
* 139) .tox/py37/lib/python3.7/site-packages/chardet/sbcsgroupprober.py line 57 - Restore Hungarian encodings (iso-8859-2 and windows-1250) 
* 140) .tox/py37/lib/python3.7/site-packages/setuptools/_vendor/packaging/requirements.py line 83 - Can we test whether something is contained within a requirement? 
* 141) .tox/py37/lib/python3.7/site-packages/setuptools/_vendor/packaging/requirements.py line 86 - Can we normalize the name and extra name? 
* 142) .tox/py37/lib/python3.7/site-packages/setuptools/command/easy_install.py line 1109 - self.report_extras(req, dist) 
* 143) .tox/py37/lib/python3.7/site-packages/setuptools/command/install_lib.py line 54 - is it necessary to short-circuit here? i.e. what's the cost 
* 144) .tox/py37/lib/python3.7/site-packages/bs4/dammit.py line 77 - Ideally we would be able to recognize all HTML 5 named 
* 145) .tox/py37/lib/python3.7/site-packages/bs4/builder/_lxml.py line 104 - Issue a warning if parser is present but not a 
* 146) .tox/py37/lib/python3.7/site-packages/bs4/builder/_html5lib.py line 113 - Why is the parser 'html.parser' here? To avoid an 
* 147) .tox/py37/lib/python3.7/site-packages/bs4/builder/_html5lib.py line 156 - Why is the parser 'html.parser' here? To avoid an 
* 148) .tox/py37/lib/python3.7/site-packages/bs4/builder/_html5lib.py line 284 - This has O(n^2) performance, for input like 
* 149) .tox/py37/lib/python3.7/site-packages/bs4/builder/_html5lib.py line 412 - This code has no test coverage and I'm not sure 
* 150) .tox/py37/lib/python3.7/site-packages/pkg_resources/_vendor/packaging/requirements.py line 83 - Can we test whether something is contained within a requirement? 
* 151) .tox/py37/lib/python3.7/site-packages/pkg_resources/_vendor/packaging/requirements.py line 86 - Can we normalize the name and extra name? 
* 152) .tox/py37/lib/python3.7/site-packages/pandas/__init__.py line 195 - remove Panel compat in 1.0 
* 153) .tox/py37/lib/python3.7/site-packages/pandas/io/parquet.py line 167 - Support 'ab' 
* 154) .tox/py37/lib/python3.7/site-packages/pandas/io/sql.py line 592 - support for multiIndex 
* 155) .tox/py37/lib/python3.7/site-packages/pandas/io/sql.py line 1013 - Refine integer size. 
* 156) .tox/py37/lib/python3.7/site-packages/pandas/io/sql.py line 1753 - (wesm): unused? 
* 157) .tox/py37/lib/python3.7/site-packages/pandas/io/parsers.py line 435 - get_filepath_or_buffer could return 
* 158) .tox/py37/lib/python3.7/site-packages/pandas/io/stata.py line 354 - If/when pandas supports more than datetime64[ns], this should be 
* 159) .tox/py37/lib/python3.7/site-packages/pandas/io/stata.py line 1850 - is the next line needed above in the data(...) method? 
* 160) .tox/py37/lib/python3.7/site-packages/pandas/io/stata.py line 1983 - expand to handle datetime to integer conversion 
* 161) .tox/py37/lib/python3.7/site-packages/pandas/io/stata.py line 2020 - Refactor to combine type with format 
* 162) .tox/py37/lib/python3.7/site-packages/pandas/io/stata.py line 2021 - expand this to handle a default datetime format? 
* 163) .tox/py37/lib/python3.7/site-packages/pandas/io/stata.py line 2619 - expand to handle datetime to integer conversion 
* 164) .tox/py37/lib/python3.7/site-packages/pandas/io/clipboard/clipboards.py line 108 - https://github.com/asweigart/pyperclip/issues/43 
* 165) .tox/py37/lib/python3.7/site-packages/pandas/io/formats/style.py line 519 - namespace all the pandas keys 
* 166) .tox/py37/lib/python3.7/site-packages/pandas/io/formats/css.py line 94 - resolve other font-relative units 
* 167) .tox/py37/lib/python3.7/site-packages/pandas/io/formats/css.py line 106 - support % 
* 168) .tox/py37/lib/python3.7/site-packages/pandas/io/formats/css.py line 248 - don't lowercase case sensitive parts of values (strings) 
* 169) .tox/py37/lib/python3.7/site-packages/pandas/io/formats/excel.py line 81 - memoize? 
* 170) .tox/py37/lib/python3.7/site-packages/pandas/io/formats/excel.py line 93 - handle cell width and height: needs support in pandas.io.excel 
* 171) .tox/py37/lib/python3.7/site-packages/pandas/io/formats/excel.py line 119 - text-indent, padding-left -> alignment.indent 
* 172) .tox/py37/lib/python3.7/site-packages/pandas/io/formats/excel.py line 194 - perhaps allow for special properties 
* 173) .tox/py37/lib/python3.7/site-packages/pandas/io/formats/html.py line 301 - Refactor to remove code duplication with code 
* 174) .tox/py37/lib/python3.7/site-packages/pandas/io/formats/html.py line 308 - Refactor to use _get_column_name_list from 
* 175) .tox/py37/lib/python3.7/site-packages/pandas/io/formats/html.py line 334 - Refactor to remove code duplication with code block 
* 176) .tox/py37/lib/python3.7/site-packages/pandas/io/formats/html.py line 341 - Refactor to use _get_column_name_list from 
* 177) .tox/py37/lib/python3.7/site-packages/pandas/io/excel/_openpyxl.py line 497 - replace with openpyxl constants 
* 178) .tox/py37/lib/python3.7/site-packages/pandas/io/excel/_xlsxwriter.py line 118 - support other fill patterns 
* 179) .tox/py37/lib/python3.7/site-packages/pandas/io/json/_normalize.py line 264 - handle record value which are lists, at least error 
* 180) .tox/py37/lib/python3.7/site-packages/pandas/io/json/_json.py line 283 - Do this timedelta properly in objToJSON.c See GH #15137 
* 181) .tox/py37/lib/python3.7/site-packages/pandas/tests/test_nanops.py line 842 - unused? 
* 182) .tox/py37/lib/python3.7/site-packages/pandas/tests/test_algos.py line 191 - (wesm): unused? 
* 183) .tox/py37/lib/python3.7/site-packages/pandas/tests/test_algos.py line 909 - same for (timedelta) 
* 184) .tox/py37/lib/python3.7/site-packages/pandas/tests/test_multilevel.py line 890 - what should join do with names ? 
* 185) .tox/py37/lib/python3.7/site-packages/pandas/tests/test_multilevel.py line 1103 - groupby with level_values drops names 
* 186) .tox/py37/lib/python3.7/site-packages/pandas/tests/test_expressions.py line 175 - FIGURE OUT HOW TO GET IT TO WORK... 
* 187) .tox/py37/lib/python3.7/site-packages/pandas/tests/test_strings.py line 212 - get rid of these xfails 
* 188) .tox/py37/lib/python3.7/site-packages/pandas/tests/test_strings.py line 251 - get rid of these xfails 
* 189) .tox/py37/lib/python3.7/site-packages/pandas/tests/test_strings.py line 1837 - unused 
* 190) .tox/py37/lib/python3.7/site-packages/pandas/tests/test_strings.py line 2544 - see GH 18463 
* 191) .tox/py37/lib/python3.7/site-packages/pandas/tests/test_base.py line 1070 - (GH-24559): Remove the filterwarnings 
* 192) .tox/py37/lib/python3.7/site-packages/pandas/tests/test_base.py line 1124 - (GH-24559): Remove the filterwarnings 
* 193) .tox/py37/lib/python3.7/site-packages/pandas/tests/indexing/test_chaining_and_caching.py line 383 - (wesm): unused? 
* 194) .tox/py37/lib/python3.7/site-packages/pandas/tests/indexing/test_coercion.py line 179 - _GH12747 The result must be int") 
* 195) .tox/py37/lib/python3.7/site-packages/pandas/tests/indexing/test_coercion.py line 183 - _GH12747 The result must be float") 
* 196) .tox/py37/lib/python3.7/site-packages/pandas/tests/indexing/test_coercion.py line 187 - _GH12747 The result must be complex") 
* 197) .tox/py37/lib/python3.7/site-packages/pandas/tests/indexing/test_coercion.py line 327 - _GH12747 The result must be float") 
* 198) .tox/py37/lib/python3.7/site-packages/pandas/tests/indexing/test_indexing.py line 293 - (wesm): unused? 
* 199) .tox/py37/lib/python3.7/site-packages/pandas/tests/indexing/test_partial.py line 175 - #15657, these are left as object and not coerced 
* 200) .tox/py37/lib/python3.7/site-packages/pandas/tests/indexing/multiindex/test_xs.py line 195 - move to another module or refactor 
* 201) .tox/py37/lib/python3.7/site-packages/pandas/tests/indexing/multiindex/test_xs.py line 205 - move to another module or refactor 
* 202) .tox/py37/lib/python3.7/site-packages/pandas/tests/indexing/multiindex/test_xs.py line 217 - move to another module or refactor 
* 203) .tox/py37/lib/python3.7/site-packages/pandas/tests/indexing/multiindex/test_setitem.py line 260 - (wesm): unused? 
* 204) .tox/py37/lib/python3.7/site-packages/pandas/tests/indexing/interval/test_interval_new.py line 131 - with non-existing intervals ? 
* 205) .tox/py37/lib/python3.7/site-packages/pandas/tests/indexing/interval/test_interval_new.py line 213 - KeyError is the appropriate error? 
* 206) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_object.py line 75 - parametrize 
* 207) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_object.py line 156 - Moved from tests.series.test_operators; needs cleanup 
* 208) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_object.py line 167 - parametrize over box 
* 209) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_object.py line 185 - cleanup & parametrize over box 
* 210) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_object.py line 233 - cleanup & parametrize over box 
* 211) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_datetime64.py line 95 - moved from tests.series.test_operators; needs cleanup 
* 212) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_datetime64.py line 374 - implement _assert_tzawareness_compat for the reverse 
* 213) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_datetime64.py line 380 - moved from tests.indexes.test_base; parametrize and de-duplicate 
* 214) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_datetime64.py line 1201 - parametrize over timezone? 
* 215) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_datetime64.py line 1271 - parametrize over the scalar being added?  radd?  sub? 
* 216) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_datetime64.py line 1336 - redundant with test_dt64arr_add_sub_DateOffset?  that includes 
* 217) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_datetime64.py line 1507 - __sub__, __rsub__ 
* 218) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_datetime64.py line 1533 - overlap with test_dt64arr_add_mixed_offset_array? 
* 219) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_datetime64.py line 1629 - box + de-duplicate 
* 220) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_datetime64.py line 1793 - Decide if this ought to work. 
* 221) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_datetime64.py line 1808 - This next block of tests came from tests.series.test_operators, 
* 222) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_datetime64.py line 1844 - (jreback) __rsub__ should raise? 
* 223) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_datetime64.py line 1946 - this block also needs to be de-duplicated and parametrized 
* 224) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_datetime64.py line 2264 - A couple other tests belong in this section.  Move them in 
* 225) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_datetime64.py line 2335 - Most of this block is moved from series or frame tests, needs 
* 226) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_datetime64.py line 2351 - unused 
* 227) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_period.py line 43 - parameterize over boxes 
* 228) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_period.py line 60 - moved from test_datetime64; de-duplicate with version below 
* 229) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_period.py line 127 - could also box idx? 
* 230) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_period.py line 168 - Could parametrize over boxes for idx? 
* 231) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_period.py line 246 - De-duplicate with test_pi_cmp_nat 
* 232) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_period.py line 322 - needs parametrization+de-duplication 
* 233) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_period.py line 472 - parametrize over boxes for other? 
* 234) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_period.py line 514 - parametrize over boxes for other? 
* 235) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_period.py line 831 - Some of these are misnomers because of non-Tick DateOffsets 
* 236) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_timedelta64.py line 66 - All of these need to be parametrized over box 
* 237) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_timedelta64.py line 186 - better name 
* 238) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_timedelta64.py line 380 - (wesm): unused? 
* 239) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_timedelta64.py line 449 - Needs more informative name, probably split up into 
* 240) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_timedelta64.py line 485 - parametrize over boxes 
* 241) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_timedelta64.py line 554 - moved from frame tests; needs parametrization/de-duplication 
* 242) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_timedelta64.py line 570 - moved from tests.indexes.timedeltas.test_arithmetic; needs 
* 243) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_timedelta64.py line 666 - moved from tests.series.test_operators, needs splitting, cleanup, 
* 244) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_timedelta64.py line 865 - parametrize over box for pi? 
* 245) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_timedelta64.py line 888 - parametrize over scalar datetime types? 
* 246) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_timedelta64.py line 907 - parametrize over types of datetime scalar? 
* 247) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_timedelta64.py line 999 - separate/parametrize 
* 248) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_timedelta64.py line 1060 - Add DataFrame in here? 
* 249) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_timedelta64.py line 1084 - this was taken from tests.series.test_ops; de-duplicate 
* 250) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_timedelta64.py line 1105 - this was taken from tests.series.test_ops; de-duplicate 
* 251) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_timedelta64.py line 1174 - parametrize over [add, sub, radd, rsub]? 
* 252) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_timedelta64.py line 1287 - this was taken from tests.series.test_operators; de-duplicate 
* 253) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_timedelta64.py line 1355 - combine with test_td64arr_add_offset_index by parametrizing 
* 254) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_timedelta64.py line 1452 - separate/parametrize add/sub test? 
* 255) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_timedelta64.py line 1490 - Moved from tests.series.test_operators; needs cleanup 
* 256) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_timedelta64.py line 1579 - Put Series/DataFrame in others? 
* 257) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_timedelta64.py line 1788 - Is this redundant with test_td64arr_floordiv_tdlike_scalar? 
* 258) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_timedelta64.py line 1817 - operations with timedelta-like arrays, numeric arrays, 
* 259) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_timedelta64.py line 2059 - Should we be parametrizing over types for `ser` too? 
* 260) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_timedelta64.py line 2079 - Should we be parametrizing over types for `ser` too? 
* 261) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_timedelta64.py line 2090 - the direct operation TimedeltaIndex / Series still 
* 262) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_timedelta64.py line 2114 - Should we skip this case sooner or test something else? 
* 263) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_numeric.py line 81 - also check name retentention 
* 264) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_numeric.py line 120 - also check name retentention 
* 265) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_numeric.py line 165 - de-duplicate with test_numeric_arr_mul_tdscalar 
* 266) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_numeric.py line 174 - also test non-nanosecond timedelta64 and Tick objects; 
* 267) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_numeric.py line 689 - This came from series.test.test_operators, needs cleanup 
* 268) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_numeric.py line 702 - this came from tests.series.test_analytics, needs cleanup and 
* 269) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_numeric.py line 746 - This came from series.test.test_operators, needs cleanup 
* 270) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_numeric.py line 772 - This came from series.test.test_operators, needs cleanup 
* 271) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_numeric.py line 796 - This came from series.test.test_operators, needs cleanup 
* 272) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_numeric.py line 826 - taken from tests.frame.test_operators, needs cleanup 
* 273) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_numeric.py line 871 - taken from tests.series.test_operators; needs cleanup 
* 274) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_numeric.py line 912 - taken from tests.series.test_operators; needs cleanup 
* 275) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_numeric.py line 1071 - moved from tests.series.test_operators; needs cleanup 
* 276) .tox/py37/lib/python3.7/site-packages/pandas/tests/arithmetic/test_numeric.py line 1126 - mod, divmod? 
* 277) .tox/py37/lib/python3.7/site-packages/pandas/tests/reshape/test_concat.py line 48 - Replace with sort once keyword changes. 
* 278) .tox/py37/lib/python3.7/site-packages/pandas/tests/reshape/test_melt.py line 572 - unused? 
* 279) .tox/py37/lib/python3.7/site-packages/pandas/tests/reshape/merge/test_merge.py line 1363 - check_names on merge? 
* 280) .tox/py37/lib/python3.7/site-packages/pandas/tests/reshape/merge/test_merge.py line 2020 - might reconsider current raise behaviour, see issue 24782 
* 281) .tox/py37/lib/python3.7/site-packages/pandas/tests/reshape/merge/test_merge.py line 2032 - might reconsider current raise behaviour, see GH24782 
* 282) .tox/py37/lib/python3.7/site-packages/pandas/tests/resample/test_resample_api.py line 257 - once GH 14008 is fixed, move these tests into 
* 283) .tox/py37/lib/python3.7/site-packages/pandas/tests/resample/test_base.py line 185 - fix resample w/ TimedeltaIndex 
* 284) .tox/py37/lib/python3.7/site-packages/pandas/tests/io/test_feather.py line 114 - make the warning work with check_stacklevel=True 
* 285) .tox/py37/lib/python3.7/site-packages/pandas/tests/io/test_feather.py line 120 - make the warning work with check_stacklevel=True 
* 286) .tox/py37/lib/python3.7/site-packages/pandas/tests/io/parser/test_common.py line 930 - FTP testing 
* 287) .tox/py37/lib/python3.7/site-packages/pandas/tests/io/parser/test_mangle_dupes.py line 16 - add test for condition "mangle_dupe_cols=False" 
* 288) .tox/py37/lib/python3.7/site-packages/pandas/tests/io/formats/test_console.py line 6 - (py27): replace with mock 
* 289) .tox/py37/lib/python3.7/site-packages/pandas/tests/io/formats/test_to_html.py line 275 - split this test 
* 290) .tox/py37/lib/python3.7/site-packages/pandas/tests/io/formats/test_to_html.py line 368 - split this test 
* 291) .tox/py37/lib/python3.7/site-packages/pandas/tests/io/formats/test_css.py line 63 - we should be checking that in other cases no warnings are raised 
* 292) .tox/py37/lib/python3.7/site-packages/pandas/tests/io/excel/test_readers.py line 109 - add index to xls file) 
* 293) .tox/py37/lib/python3.7/site-packages/pandas/tests/io/excel/test_readers.py line 123 - add index to xls file) 
* 294) .tox/py37/lib/python3.7/site-packages/pandas/tests/io/excel/test_readers.py line 135 - add index to xls, read xls ignores index name ? 
* 295) .tox/py37/lib/python3.7/site-packages/pandas/tests/io/excel/test_readers.py line 144 - add index to xls file 
* 296) .tox/py37/lib/python3.7/site-packages/pandas/tests/io/excel/test_readers.py line 255 - add index to file 
* 297) .tox/py37/lib/python3.7/site-packages/pandas/tests/io/excel/test_readers.py line 503 - remove once on master 
* 298) .tox/py37/lib/python3.7/site-packages/pandas/tests/io/excel/test_xlrd.py line 37 - test for openpyxl as well 
* 299) .tox/py37/lib/python3.7/site-packages/pandas/tests/io/json/test_json_table_schema.py line 177 - datedate.date? datetime.time? 
* 300) .tox/py37/lib/python3.7/site-packages/pandas/tests/io/json/test_json_table_schema.py line 184 -  
* 301) .tox/py37/lib/python3.7/site-packages/pandas/tests/io/json/test_json_table_schema.py line 189 - I think before is_categorical_dtype(Categorical) 
* 302) .tox/py37/lib/python3.7/site-packages/pandas/tests/io/json/test_pandas.py line 183 - not executed. fix this. 
* 303) .tox/py37/lib/python3.7/site-packages/pandas/tests/io/json/test_pandas.py line 1435 - there is a near-identical test for pytables; can we share? 
* 304) .tox/py37/lib/python3.7/site-packages/pandas/tests/io/pytables/test_pytables.py line 54 -  
* 305) .tox/py37/lib/python3.7/site-packages/pandas/tests/tools/test_numeric.py line 399 - PeriodDtype, so support it in to_numeric. 
* 306) .tox/py37/lib/python3.7/site-packages/pandas/tests/scalar/timedelta/test_timedelta.py line 783 - unused? 
* 307) .tox/py37/lib/python3.7/site-packages/pandas/tests/scalar/timedelta/test_arithmetic.py line 494 - GH-19761. Change to TypeError. 
* 308) .tox/py37/lib/python3.7/site-packages/pandas/tests/scalar/period/test_asfreq.py line 425 - unused? 
* 309) .tox/py37/lib/python3.7/site-packages/pandas/tests/groupby/test_function.py line 174 - min, max *should* handle 
* 310) .tox/py37/lib/python3.7/site-packages/pandas/tests/groupby/test_groupby.py line 471 - groupby get drops names 
* 311) .tox/py37/lib/python3.7/site-packages/pandas/tests/groupby/test_groupby.py line 1122 - Ensure warning isn't emitted in the first place 
* 312) .tox/py37/lib/python3.7/site-packages/pandas/tests/groupby/test_grouping.py line 693 - should prob allow a str of Interval work as well 
* 313) .tox/py37/lib/python3.7/site-packages/pandas/tests/groupby/test_whitelist.py line 337 - check groupby with > 1 col ? 
* 314) .tox/py37/lib/python3.7/site-packages/pandas/tests/groupby/aggregate/test_aggregate.py line 36 - (wesm): unused 
* 315) .tox/py37/lib/python3.7/site-packages/pandas/tests/groupby/aggregate/test_aggregate.py line 444 - we currently raise on multiple lambdas. We could *maybe* 
* 316) .tox/py37/lib/python3.7/site-packages/pandas/tests/arrays/test_datetimes.py line 111 - merge this into tests/arithmetic/test_datetime64 once it is 
* 317) .tox/py37/lib/python3.7/site-packages/pandas/tests/arrays/test_datetimes.py line 134 - add list and tuple, and object-dtype once those 
* 318) .tox/py37/lib/python3.7/site-packages/pandas/tests/arrays/test_integer.py line 319 - (extension) 
* 319) .tox/py37/lib/python3.7/site-packages/pandas/tests/arrays/test_integer.py line 689 - (#22346): preserve Int64 dtype 
* 320) .tox/py37/lib/python3.7/site-packages/pandas/tests/arrays/test_integer.py line 812 - (jreback) - these need testing / are broken 
* 321) .tox/py37/lib/python3.7/site-packages/pandas/tests/arrays/test_datetimelike.py line 11 - more freq variants 
* 322) .tox/py37/lib/python3.7/site-packages/pandas/tests/arrays/test_datetimelike.py line 22 - non-monotone indexes; NaTs, different start dates 
* 323) .tox/py37/lib/python3.7/site-packages/pandas/tests/arrays/test_datetimelike.py line 37 - non-monotone indexes; NaTs, different start dates, timezones 
* 324) .tox/py37/lib/python3.7/site-packages/pandas/tests/arrays/test_datetimelike.py line 50 - flesh this out 
* 325) .tox/py37/lib/python3.7/site-packages/pandas/tests/arrays/test_timedeltas.py line 42 - why TypeError for 'category' but ValueError for i8? 
* 326) .tox/py37/lib/python3.7/site-packages/pandas/tests/arrays/categorical/test_repr.py line 150 - (wesm): exceeding 80 characters in the console is not good 
* 327) .tox/py37/lib/python3.7/site-packages/pandas/tests/arrays/categorical/test_indexing.py line 265 - (Categorical): identify other places where this may be 
* 328) .tox/py37/lib/python3.7/site-packages/pandas/tests/arrays/interval/test_ops.py line 57 - modify this test when implemented 
* 329) .tox/py37/lib/python3.7/site-packages/pandas/tests/arrays/sparse/test_accessor.py line 13 - collect other Series accessor tests 
* 330) .tox/py37/lib/python3.7/site-packages/pandas/tests/arrays/sparse/test_libsparse.py line 448 - index variables are not used...is that right? 
* 331) .tox/py37/lib/python3.7/site-packages/pandas/tests/reductions/test_reductions.py line 1045 - deprecate numeric_only argument for Categorical and use 
* 332) .tox/py37/lib/python3.7/site-packages/pandas/tests/reductions/test_stat_reductions.py line 46 - flesh this out with different frequencies 
* 333) .tox/py37/lib/python3.7/site-packages/pandas/tests/indexes/test_base.py line 880 - decide on True behaviour 
* 334) .tox/py37/lib/python3.7/site-packages/pandas/tests/indexes/test_base.py line 904 - Replace with fixturesult 
* 335) .tox/py37/lib/python3.7/site-packages/pandas/tests/indexes/test_base.py line 930 - decide on True behaviour 
* 336) .tox/py37/lib/python3.7/site-packages/pandas/tests/indexes/test_base.py line 960 - decide on True behaviour 
* 337) .tox/py37/lib/python3.7/site-packages/pandas/tests/indexes/test_base.py line 970 - Replace with fixturesult 
* 338) .tox/py37/lib/python3.7/site-packages/pandas/tests/indexes/test_base.py line 983 - replace with fixturesult 
* 339) .tox/py37/lib/python3.7/site-packages/pandas/tests/indexes/test_base.py line 1023 - Replace with fixturesult 
* 340) .tox/py37/lib/python3.7/site-packages/pandas/tests/indexes/test_base.py line 1050 - replace with fixture 
* 341) .tox/py37/lib/python3.7/site-packages/pandas/tests/indexes/test_base.py line 1106 - replace with fixture 
* 342) .tox/py37/lib/python3.7/site-packages/pandas/tests/indexes/test_base.py line 1173 - replace with fixturesult 
* 343) .tox/py37/lib/python3.7/site-packages/pandas/tests/indexes/test_base.py line 1259 - decide on True behaviour 
* 344) .tox/py37/lib/python3.7/site-packages/pandas/tests/indexes/test_base.py line 1442 - make this a dedicated test with parametrized methods 
* 345) .tox/py37/lib/python3.7/site-packages/pandas/tests/indexes/test_base.py line 1770 - Parametrize these after replacing self.strIndex with fixture 
* 346) .tox/py37/lib/python3.7/site-packages/pandas/tests/indexes/test_base.py line 1788 - Parametrize these after replacing self.strIndex with fixture 
* 347) .tox/py37/lib/python3.7/site-packages/pandas/tests/indexes/test_base.py line 1804 - Parametrize numeric and str tests after self.strIndex fixture 
* 348) .tox/py37/lib/python3.7/site-packages/pandas/tests/indexes/test_base.py line 1912 - Remove function? GH 19728 
* 349) .tox/py37/lib/python3.7/site-packages/pandas/tests/indexes/period/test_indexing.py line 570 - This method came from test_period; de-dup with version above 
* 350) .tox/py37/lib/python3.7/site-packages/pandas/tests/indexes/period/test_indexing.py line 618 - This method came from test_period; de-dup with version above 
* 351) .tox/py37/lib/python3.7/site-packages/pandas/tests/indexes/period/test_astype.py line 66 - de-duplicate this version (from test_ops) with the one above 
* 352) .tox/py37/lib/python3.7/site-packages/pandas/tests/indexes/timedeltas/test_indexing.py line 118 - This method came from test_timedelta; de-dup with version above 
* 353) .tox/py37/lib/python3.7/site-packages/pandas/tests/indexes/timedeltas/test_arithmetic.py line 206 - after #24365 this probably belongs in scalar tests 
* 354) .tox/py37/lib/python3.7/site-packages/pandas/tests/indexes/timedeltas/test_ops.py line 127 - (wesm): unused? 
* 355) .tox/py37/lib/python3.7/site-packages/pandas/tests/indexes/interval/test_interval_new.py line 288 - we may also want to test get_indexer for the case when 
* 356) .tox/py37/lib/python3.7/site-packages/pandas/tests/indexes/interval/test_setops.py line 161 - standardize return type of non-union setops type(self vs other) 
* 357) .tox/py37/lib/python3.7/site-packages/pandas/tests/indexes/multi/test_integrity.py line 52 - (GH-24559): Remove the FutureWarning 
* 358) .tox/py37/lib/python3.7/site-packages/pandas/tests/indexes/multi/test_missing.py line 15 - Remove or Refactor.  Not Implemented for MultiIndex 
* 359) .tox/py37/lib/python3.7/site-packages/pandas/tests/indexes/multi/test_indexing.py line 69 - Try creating a UnicodeDecodeError in exception message 
* 360) .tox/py37/lib/python3.7/site-packages/pandas/tests/indexes/multi/test_set_ops.py line 196 - decide on True behaviour 
* 361) .tox/py37/lib/python3.7/site-packages/pandas/tests/indexes/multi/test_set_ops.py line 221 - decide on True behaviour 
* 362) .tox/py37/lib/python3.7/site-packages/pandas/tests/indexes/multi/test_set_ops.py line 301 - decide on True behaviour 
* 363) .tox/py37/lib/python3.7/site-packages/pandas/tests/indexes/multi/test_set_ops.py line 324 - decide on True behaviour 
* 364) .tox/py37/lib/python3.7/site-packages/pandas/tests/indexes/multi/test_set_ops.py line 348 - decide on True behaviour 
* 365) .tox/py37/lib/python3.7/site-packages/pandas/tests/indexes/multi/test_analytics.py line 77 - reshape 
* 366) .tox/py37/lib/python3.7/site-packages/pandas/tests/indexes/multi/test_analytics.py line 155 - Remove Commented Code 
* 367) .tox/py37/lib/python3.7/site-packages/pandas/tests/indexes/datetimes/test_timezones.py line 565 - belongs outside tz_localize tests? 
* 368) .tox/py37/lib/python3.7/site-packages/pandas/tests/indexes/datetimes/test_indexing.py line 220 - This method came from test_datetime; de-dup with version above 
* 369) .tox/py37/lib/python3.7/site-packages/pandas/tests/indexes/datetimes/test_setops.py line 36 - moved from test_datetimelike; dedup with version below 
* 370) .tox/py37/lib/python3.7/site-packages/pandas/tests/indexes/datetimes/test_setops.py line 186 - moved from test_datetimelike; de-duplicate with version below 
* 371) .tox/py37/lib/python3.7/site-packages/pandas/tests/indexes/datetimes/test_construction.py line 42 - parametrize over DatetimeIndex/DatetimeArray 
* 372) .tox/py37/lib/python3.7/site-packages/pandas/tests/indexes/datetimes/test_construction.py line 737 - (GH-24559): Remove the xfail for the tz-aware case. 
* 373) .tox/py37/lib/python3.7/site-packages/pandas/tests/indexes/datetimes/test_construction.py line 768 - (GH-24559): Remove xfail 
* 374) .tox/py37/lib/python3.7/site-packages/pandas/tests/extension/test_integer.py line 116 - see https://github.com/pandas-dev/pandas/issues/22023 
* 375) .tox/py37/lib/python3.7/site-packages/pandas/tests/extension/test_integer.py line 134 - reverse operators result in object dtype 
* 376) .tox/py37/lib/python3.7/site-packages/pandas/tests/extension/test_integer.py line 137 - reverse operators result in object dtype 
* 377) .tox/py37/lib/python3.7/site-packages/pandas/tests/extension/test_integer.py line 146 - pow on Int arrays gives different result with NA 
* 378) .tox/py37/lib/python3.7/site-packages/pandas/tests/extension/test_integer.py line 185 - (jreback) once integrated this would 
* 379) .tox/py37/lib/python3.7/site-packages/pandas/tests/extension/test_sparse.py line 294 - (SparseArray.__setitem__ will preserve dtype.") 
* 380) .tox/py37/lib/python3.7/site-packages/pandas/tests/extension/test_numpy.py line 191 - remove?") 
* 381) .tox/py37/lib/python3.7/site-packages/pandas/tests/extension/test_categorical.py line 114 - remove this once Categorical.take is fixed 
* 382) .tox/py37/lib/python3.7/site-packages/pandas/tests/extension/list/array.py line 127 - Use a regular dict. See _NDFrameIndexer._setitem_with_indexer 
* 383) .tox/py37/lib/python3.7/site-packages/pandas/tests/extension/json/test_json.py line 199 - (EA.factorize): see if _values_for_factorize allows this. 
* 384) .tox/py37/lib/python3.7/site-packages/pandas/tests/extension/json/array.py line 189 - Use a regular dict. See _NDFrameIndexer._setitem_with_indexer 
* 385) .tox/py37/lib/python3.7/site-packages/pandas/tests/extension/decimal/test_decimal.py line 92 - (EA): select_dtypes 
* 386) .tox/py37/lib/python3.7/site-packages/pandas/tests/extension/decimal/test_decimal.py line 207 - (extension) 
* 387) .tox/py37/lib/python3.7/site-packages/pandas/tests/window/test_moments.py line 2269 - xref gh-15826 
* 388) .tox/py37/lib/python3.7/site-packages/pandas/tests/window/test_moments.py line 2384 - (jreback), needed to add preserve_nan=False 
* 389) .tox/py37/lib/python3.7/site-packages/pandas/tests/tseries/offsets/test_offsets.py line 68 - Remove: This is not used outside of tests 
* 390) .tox/py37/lib/python3.7/site-packages/pandas/tests/tseries/offsets/test_offsets_properties.py line 45 - Choose the min/max values more systematically 
* 391) .tox/py37/lib/python3.7/site-packages/pandas/tests/tseries/offsets/test_offsets_properties.py line 108 - test for that case separately 
* 392) .tox/py37/lib/python3.7/site-packages/pandas/tests/tseries/offsets/test_offsets_properties.py line 124 - Check randomly assorted entries, not just first/last 
* 393) .tox/py37/lib/python3.7/site-packages/pandas/tests/tseries/offsets/test_offsets_properties.py line 127 - reason? 
* 394) .tox/py37/lib/python3.7/site-packages/pandas/tests/plotting/test_datetimelike.py line 712 -  
* 395) .tox/py37/lib/python3.7/site-packages/pandas/tests/plotting/test_datetimelike.py line 863 - (GH14330, GH14322) 
* 396) .tox/py37/lib/python3.7/site-packages/pandas/tests/plotting/test_datetimelike.py line 1209 - color cycle problems 
* 397) .tox/py37/lib/python3.7/site-packages/pandas/tests/plotting/test_datetimelike.py line 1249 - color cycle problems 
* 398) .tox/py37/lib/python3.7/site-packages/pandas/tests/plotting/test_datetimelike.py line 1265 - color cycle problems 
* 399) .tox/py37/lib/python3.7/site-packages/pandas/tests/plotting/test_datetimelike.py line 1279 - color cycle problems 
* 400) .tox/py37/lib/python3.7/site-packages/pandas/tests/plotting/test_datetimelike.py line 1569 - (statsmodels 0.10.0): Remove the statsmodels check 
* 401) .tox/py37/lib/python3.7/site-packages/pandas/tests/plotting/test_backend.py line 59 - the docs recommend importlib.util.module_from_spec. But this works for now. 
* 402) .tox/py37/lib/python3.7/site-packages/pandas/tests/plotting/test_backend.py line 65 - https://github.com/pandas-dev/pandas/issues/27517 
* 403) .tox/py37/lib/python3.7/site-packages/pandas/tests/plotting/test_frame.py line 250 - add MultiIndex test 
* 404) .tox/py37/lib/python3.7/site-packages/pandas/tests/plotting/test_frame.py line 2243 - outside this func? 
* 405) .tox/py37/lib/python3.7/site-packages/pandas/tests/plotting/test_frame.py line 2427 - need better way to test. This just does existence. 
* 406) .tox/py37/lib/python3.7/site-packages/pandas/tests/internals/test_internals.py line 278 - merge with mixed type? 
* 407) .tox/py37/lib/python3.7/site-packages/pandas/tests/internals/test_internals.py line 703 - should this be pytest.skip? 
* 408) .tox/py37/lib/python3.7/site-packages/pandas/tests/dtypes/test_common.py line 493 - (jreback), this is slightly suspect 
* 409) .tox/py37/lib/python3.7/site-packages/pandas/tests/dtypes/test_dtypes.py line 70 - (GH 26403): Remove when default ordered becomes False 
* 410) .tox/py37/lib/python3.7/site-packages/pandas/tests/series/test_combine_concat.py line 277 - move? 
* 411) .tox/py37/lib/python3.7/site-packages/pandas/tests/series/test_combine_concat.py line 290 - release-note: concat sparse dtype 
* 412) .tox/py37/lib/python3.7/site-packages/pandas/tests/series/test_combine_concat.py line 301 - release-note: concat sparse dtype 
* 413) .tox/py37/lib/python3.7/site-packages/pandas/tests/series/test_timezones.py line 260 - De-duplicate with test below 
* 414) .tox/py37/lib/python3.7/site-packages/pandas/tests/series/test_missing.py line 999 - what is this test doing? why are result an expected 
* 415) .tox/py37/lib/python3.7/site-packages/pandas/tests/series/test_missing.py line 1004 - release-note fillna performance warning 
* 416) .tox/py37/lib/python3.7/site-packages/pandas/tests/series/test_operators.py line 48 - unused 
* 417) .tox/py37/lib/python3.7/site-packages/pandas/tests/series/test_operators.py line 158 - Fix this exception - needs to be fixed! (see GH5035) 
* 418) .tox/py37/lib/python3.7/site-packages/pandas/tests/series/test_operators.py line 681 - this returned NotImplemented earlier, what to do? 
* 419) .tox/py37/lib/python3.7/site-packages/pandas/tests/series/indexing/test_datetime.py line 634 - unused? 
* 420) .tox/py37/lib/python3.7/site-packages/pandas/tests/series/indexing/test_indexing.py line 733 - unused 
* 421) .tox/py37/lib/python3.7/site-packages/pandas/tests/sparse/series/test_series.py line 719 - sp_zero is not used anywhere...remove? 
* 422) .tox/py37/lib/python3.7/site-packages/pandas/tests/sparse/series/test_series.py line 750 - expected is not used anywhere...remove? 
* 423) .tox/py37/lib/python3.7/site-packages/pandas/tests/sparse/series/test_series.py line 783 - These aren't used 
* 424) .tox/py37/lib/python3.7/site-packages/pandas/tests/sparse/frame/test_apply.py line 94 - no non-unique columns supported in sparse yet 
* 425) .tox/py37/lib/python3.7/site-packages/pandas/tests/sparse/frame/test_frame.py line 119 - test data is copied from inputs 
* 426) .tox/py37/lib/python3.7/site-packages/pandas/tests/sparse/frame/test_frame.py line 210 - x_sparse is unused...fix 
* 427) .tox/py37/lib/python3.7/site-packages/pandas/tests/sparse/frame/test_frame.py line 217 - y_sparse is unsused...fix 
* 428) .tox/py37/lib/python3.7/site-packages/pandas/tests/frame/test_join.py line 140 - should this check_names ? 
* 429) .tox/py37/lib/python3.7/site-packages/pandas/tests/frame/test_constructors.py line 86 - (wesm), incomplete test? 
* 430) .tox/py37/lib/python3.7/site-packages/pandas/tests/frame/test_constructors.py line 2022 - (wesm): unused 
* 431) .tox/py37/lib/python3.7/site-packages/pandas/tests/frame/test_missing.py line 239 - make stronger assertion here, GH 25640 
* 432) .tox/py37/lib/python3.7/site-packages/pandas/tests/frame/test_missing.py line 712 - (wesm): unused? 
* 433) .tox/py37/lib/python3.7/site-packages/pandas/tests/frame/test_repr_info.py line 133 - (wesm): is this supposed to be used? 
* 434) .tox/py37/lib/python3.7/site-packages/pandas/tests/frame/test_to_csv.py line 150 - remove renaming when GH 10875 is solved 
* 435) .tox/py37/lib/python3.7/site-packages/pandas/tests/frame/test_to_csv.py line 507 - to_csv drops column name 
* 436) .tox/py37/lib/python3.7/site-packages/pandas/tests/frame/test_to_csv.py line 523 - to_csv drops column name 
* 437) .tox/py37/lib/python3.7/site-packages/pandas/tests/frame/test_to_csv.py line 584 - to_csv drops column name 
* 438) .tox/py37/lib/python3.7/site-packages/pandas/tests/frame/test_to_csv.py line 600 - to_csv drops column name 
* 439) .tox/py37/lib/python3.7/site-packages/pandas/tests/frame/test_to_csv.py line 897 - to_csv drops column name 
* 440) .tox/py37/lib/python3.7/site-packages/pandas/tests/frame/test_block_internals.py line 411 - (wesm): unused? 
* 441) .tox/py37/lib/python3.7/site-packages/pandas/tests/frame/test_operators.py line 201 - belongs elsewhere 
* 442) .tox/py37/lib/python3.7/site-packages/pandas/tests/frame/test_operators.py line 251 - not sure what's correct here. 
* 443) .tox/py37/lib/python3.7/site-packages/pandas/tests/frame/test_arithmetic.py line 149 - test_bool_flex_frame needs a better name 
* 444) .tox/py37/lib/python3.7/site-packages/pandas/tests/frame/test_axis_select_reindex.py line 598 - (wesm): unused? 
* 445) .tox/py37/lib/python3.7/site-packages/pandas/tests/frame/test_timeseries.py line 520 - actually check that this worked. 
* 446) .tox/py37/lib/python3.7/site-packages/pandas/tests/frame/test_timeseries.py line 946 - untested 
* 447) .tox/py37/lib/python3.7/site-packages/pandas/tests/frame/test_alter_axes.py line 1020 - should reset_index check_names ? 
* 448) .tox/py37/lib/python3.7/site-packages/pandas/tests/frame/test_analytics.py line 972 - Ensure warning isn't emitted in the first place 
* 449) .tox/py37/lib/python3.7/site-packages/pandas/tests/frame/test_analytics.py line 2142 - (wesm): unused? 
* 450) .tox/py37/lib/python3.7/site-packages/pandas/tests/frame/test_analytics.py line 2306 - (jreback) 
* 451) .tox/py37/lib/python3.7/site-packages/pandas/tests/frame/test_analytics.py line 2464 - (wesm): unused 
* 452) .tox/py37/lib/python3.7/site-packages/pandas/tests/frame/test_dtypes.py line 576 - (wesm): verification? 
* 453) .tox/py37/lib/python3.7/site-packages/pandas/compat/pickle_compat.py line 63 - When FrozenNDArray is removed, add 
* 454) .tox/py37/lib/python3.7/site-packages/pandas/util/testing.py line 1191 - Use .array 
* 455) .tox/py37/lib/python3.7/site-packages/pandas/util/_validators.py line 275 - Change to keyword-only args and remove all this 
* 456) .tox/py37/lib/python3.7/site-packages/pandas/tseries/offsets.py line 367 - Does this make sense for the general case?  It would help 
* 457) .tox/py37/lib/python3.7/site-packages/pandas/tseries/offsets.py line 371 - Combine this with BusinessMixin version by defining a whitelisted 
* 458) .tox/py37/lib/python3.7/site-packages/pandas/tseries/offsets.py line 460 - standardize `_offset` vs `offset` naming convention 
* 459) .tox/py37/lib/python3.7/site-packages/pandas/tseries/offsets.py line 1138 - going through __new__ raises on call to _validate_frequency; 
* 460) .tox/py37/lib/python3.7/site-packages/pandas/tseries/offsets.py line 1732 - handle n here... 
* 461) .tox/py37/lib/python3.7/site-packages/pandas/tseries/offsets.py line 1803 - handle n here... 
* 462) .tox/py37/lib/python3.7/site-packages/pandas/tseries/offsets.py line 1821 - Consider combining QuarterOffset and YearOffset __init__ at some 
* 463) .tox/py37/lib/python3.7/site-packages/pandas/tseries/offsets.py line 1875 - going through __new__ raises on call to _validate_frequency; 
* 464) .tox/py37/lib/python3.7/site-packages/pandas/tseries/offsets.py line 1898 - This is basically the same as BQuarterEnd 
* 465) .tox/py37/lib/python3.7/site-packages/pandas/tseries/offsets.py line 1945 - there may be a more performant way to do this 
* 466) .tox/py37/lib/python3.7/site-packages/pandas/tseries/offsets.py line 1961 - going through __new__ raises on call to _validate_frequency; 
* 467) .tox/py37/lib/python3.7/site-packages/pandas/tseries/offsets.py line 2475 - Why does this handle the 0 case the opposite of others? 
* 468) .tox/py37/lib/python3.7/site-packages/pandas/tseries/offsets.py line 2601 - Should Tick have its own apply_index? 
* 469) .tox/py37/lib/python3.7/site-packages/pandas/tseries/converter.py line 4 - `_matplotlib` module should be private, so the plotting backend 
* 470) .tox/py37/lib/python3.7/site-packages/pandas/plotting/_matplotlib/core.py line 255 - unused? 
* 471) .tox/py37/lib/python3.7/site-packages/pandas/plotting/_matplotlib/core.py line 311 - use Matplotlib public API when available 
* 472) .tox/py37/lib/python3.7/site-packages/pandas/plotting/_matplotlib/timeseries.py line 1 - Use the fact that axis can have units to simplify the process 
* 473) .tox/py37/lib/python3.7/site-packages/pandas/plotting/_matplotlib/converter.py line 385 - (wesm) unused? 
* 474) .tox/py37/lib/python3.7/site-packages/pandas/plotting/_matplotlib/converter.py line 451 - (wesm): unused? 
* 475) .tox/py37/lib/python3.7/site-packages/pandas/plotting/_matplotlib/converter.py line 817 - Check the following : is it really info['fmt'] ? 
* 476) .tox/py37/lib/python3.7/site-packages/pandas/core/frame.py line 1192 - speed up Series case 
* 477) .tox/py37/lib/python3.7/site-packages/pandas/core/frame.py line 2331 - a generic formatter wld b in DataFrameFormatter 
* 478) .tox/py37/lib/python3.7/site-packages/pandas/core/frame.py line 4647 - (https://github.com/pandas-dev/pandas/issues/24206) 
* 479) .tox/py37/lib/python3.7/site-packages/pandas/core/frame.py line 5040 - this can be combined with Series.sort_index impl as 
* 480) .tox/py37/lib/python3.7/site-packages/pandas/core/frame.py line 5784 - Support other joins 
* 481) .tox/py37/lib/python3.7/site-packages/pandas/core/frame.py line 6637 - _shallow_copy(subset)? 
* 482) .tox/py37/lib/python3.7/site-packages/pandas/core/frame.py line 7902 - Make other agg func handle axis=None properly 
* 483) .tox/py37/lib/python3.7/site-packages/pandas/core/frame.py line 7928 - combine with hasattr(result, 'dtype') further down 
* 484) .tox/py37/lib/python3.7/site-packages/pandas/core/frame.py line 8498 - this should be seriously cythonized 
* 485) .tox/py37/lib/python3.7/site-packages/pandas/core/window.py line 1085 - default is for backward compat 
* 486) .tox/py37/lib/python3.7/site-packages/pandas/core/missing.py line 500 - for int-dtypes we make a copy, but for everything else this 
* 487) .tox/py37/lib/python3.7/site-packages/pandas/core/nanops.py line 107 - (GH-18976) update all the nanops methods to 
* 488) .tox/py37/lib/python3.7/site-packages/pandas/core/nanops.py line 341 - what about datetime64tz?  PeriodDtype? 
* 489) .tox/py37/lib/python3.7/site-packages/pandas/core/apply.py line 228 - mixed type case 
* 490) .tox/py37/lib/python3.7/site-packages/pandas/core/base.py line 1007 - (GH-24345): Avoid potential double copy 
* 491) .tox/py37/lib/python3.7/site-packages/pandas/core/api.py line 48 - Remove import when statsmodels updates #18264 
* 492) .tox/py37/lib/python3.7/site-packages/pandas/core/generic.py line 4469 - Decide if we care about having different examples for different 
* 493) .tox/py37/lib/python3.7/site-packages/pandas/core/generic.py line 4570 - speed up on homogeneous DataFrame objects 
* 494) .tox/py37/lib/python3.7/site-packages/pandas/core/generic.py line 10423 - Not sure if above is correct - need someone to confirm. 
* 495) .tox/py37/lib/python3.7/site-packages/pandas/core/algorithms.py line 69 - this should be uint8) 
* 496) .tox/py37/lib/python3.7/site-packages/pandas/core/algorithms.py line 92 - ) 
* 497) .tox/py37/lib/python3.7/site-packages/pandas/core/algorithms.py line 446 - (extension) 
* 498) .tox/py37/lib/python3.7/site-packages/pandas/core/algorithms.py line 800 - handle uint8 
* 499) .tox/py37/lib/python3.7/site-packages/pandas/core/algorithms.py line 1647 - (EA): Remove these if / elifs as datetimeTZ, interval, become EAs 
* 500) .tox/py37/lib/python3.7/site-packages/pandas/core/common.py line 257 - verify whether any path hits this except #18819 (invalid) 
* 501) .tox/py37/lib/python3.7/site-packages/pandas/core/common.py line 325 - used only once in indexing; belongs elsewhere? 
* 502) .tox/py37/lib/python3.7/site-packages/pandas/core/indexing.py line 129 - (ix): most/all of the TypeError cases here are for ix, 
* 503) .tox/py37/lib/python3.7/site-packages/pandas/core/indexing.py line 134 - The AttributeError is for IntervalIndex which 
* 504) .tox/py37/lib/python3.7/site-packages/pandas/core/indexing.py line 580 - (EA): ExtensionBlock.setitem this causes issues with 
* 505) .tox/py37/lib/python3.7/site-packages/pandas/core/series.py line 221 - Remove after CategoricalDtype defaults to ordered=False 
* 506) .tox/py37/lib/python3.7/site-packages/pandas/core/series.py line 247 - See if we can avoid these copies 
* 507) .tox/py37/lib/python3.7/site-packages/pandas/core/series.py line 806 - handle DataFrame 
* 508) .tox/py37/lib/python3.7/site-packages/pandas/core/series.py line 837 - dataframe 
* 509) .tox/py37/lib/python3.7/site-packages/pandas/core/series.py line 1868 - integrate bottleneck 
* 510) .tox/py37/lib/python3.7/site-packages/pandas/core/series.py line 1927 - Add option for bins like value_counts() 
* 511) .tox/py37/lib/python3.7/site-packages/pandas/core/series.py line 3321 - this can be combined with DataFrame.sort_index impl as 
* 512) .tox/py37/lib/python3.7/site-packages/pandas/core/series.py line 4069 - deprecate numeric_only argument for Categorical and use 
* 513) .tox/py37/lib/python3.7/site-packages/pandas/core/series.py line 4080 - remove hasattr check after TimedeltaIndex has `std` method 
* 514) .tox/py37/lib/python3.7/site-packages/pandas/core/series.py line 4092 - (EA) dispatch to Index 
* 515) .tox/py37/lib/python3.7/site-packages/pandas/core/series.py line 4439 - remove when the default Categorical.take behavior changes 
* 516) .tox/py37/lib/python3.7/site-packages/pandas/core/reshape/melt.py line 30 - what about the existing index? 
* 517) .tox/py37/lib/python3.7/site-packages/pandas/core/reshape/pivot.py line 19 - Fix this dependency 
* 518) .tox/py37/lib/python3.7/site-packages/pandas/core/reshape/merge.py line 147 - , should _merge_pieces do this? 
* 519) .tox/py37/lib/python3.7/site-packages/pandas/core/reshape/merge.py line 544 - transformations?? 
* 520) .tox/py37/lib/python3.7/site-packages/pandas/core/reshape/merge.py line 545 - only copy DataFrames when modification necessary 
* 521) .tox/py37/lib/python3.7/site-packages/pandas/core/reshape/merge.py line 1883 - needs tests for case where lk is integer-dtype 
* 522) .tox/py37/lib/python3.7/site-packages/pandas/core/reshape/merge.py line 1891 - Needs tests for non-matching dtypes 
* 523) .tox/py37/lib/python3.7/site-packages/pandas/core/computation/eval.py line 52 - validate this in a more general way (thinking of future engines 
* 524) .tox/py37/lib/python3.7/site-packages/pandas/core/computation/eval.py line 358 - Filter the warnings we actually care about here. 
* 525) .tox/py37/lib/python3.7/site-packages/pandas/core/groupby/groupby.py line 406 - Better repr for GroupBy object 
* 526) .tox/py37/lib/python3.7/site-packages/pandas/core/groupby/groupby.py line 1264 - implement at Cython level? 
* 527) .tox/py37/lib/python3.7/site-packages/pandas/core/groupby/groupby.py line 1934 - (GH-10710): Ideally, we could write this as 
* 528) .tox/py37/lib/python3.7/site-packages/pandas/core/groupby/generic.py line 57 - (typing) the return value on this callable should be any *scalar*. 
* 529) .tox/py37/lib/python3.7/site-packages/pandas/core/groupby/generic.py line 59 - validate types on ScalarResult and move to _typing 
* 530) .tox/py37/lib/python3.7/site-packages/pandas/core/groupby/generic.py line 135 - the actual managing of mgr_locs is a PITA 
* 531) .tox/py37/lib/python3.7/site-packages/pandas/core/groupby/generic.py line 1224 - should we do this inside II? 
* 532) .tox/py37/lib/python3.7/site-packages/pandas/core/groupby/generic.py line 1339 - Remove this conditional when #23918 is fixed 
* 533) .tox/py37/lib/python3.7/site-packages/pandas/core/groupby/generic.py line 1733 - (Py35): When we drop python 3.5, change this to 
* 534) .tox/py37/lib/python3.7/site-packages/pandas/core/groupby/generic.py line 1735 - aggspec type: typing.OrderedDict[str, List[AggScalar]] 
* 535) .tox/py37/lib/python3.7/site-packages/pandas/core/groupby/generic.py line 1751 - Can't use, because mypy doesn't like us setting __name__ 
* 536) .tox/py37/lib/python3.7/site-packages/pandas/core/groupby/ops.py line 558 - min_count 
* 537) .tox/py37/lib/python3.7/site-packages/pandas/core/groupby/ops.py line 584 -  
* 538) .tox/py37/lib/python3.7/site-packages/pandas/core/groupby/grouper.py line 468 - These if-block and else-block are almost same. 
* 539) .tox/py37/lib/python3.7/site-packages/pandas/core/arrays/timedeltas.py line 997 - watch out for overflows 
* 540) .tox/py37/lib/python3.7/site-packages/pandas/core/arrays/timedeltas.py line 1056 - watch out for overflows when converting from lower-resolution 
* 541) .tox/py37/lib/python3.7/site-packages/pandas/core/arrays/period.py line 568 - remove 
* 542) .tox/py37/lib/python3.7/site-packages/pandas/core/arrays/period.py line 713 - disallow unit-less timedelta64 
* 543) .tox/py37/lib/python3.7/site-packages/pandas/core/arrays/interval.py line 653 - This try/except will be repeated. 
* 544) .tox/py37/lib/python3.7/site-packages/pandas/core/arrays/interval.py line 733 - Could skip verify_integrity here. 
* 545) .tox/py37/lib/python3.7/site-packages/pandas/core/arrays/interval.py line 844 - implement this is a non-naive way! 
* 546) .tox/py37/lib/python3.7/site-packages/pandas/core/arrays/interval.py line 853 - integrate with categorical and make generic 
* 547) .tox/py37/lib/python3.7/site-packages/pandas/core/arrays/sparse.py line 455 - (GH-23092): pass copy=False. Need to fix astype_nansafe 
* 548) .tox/py37/lib/python3.7/site-packages/pandas/core/arrays/sparse.py line 628 - make kind=None, and use data.kind? 
* 549) .tox/py37/lib/python3.7/site-packages/pandas/core/arrays/sparse.py line 666 - disentangle the fill_value dtype inference from 
* 550) .tox/py37/lib/python3.7/site-packages/pandas/core/arrays/sparse.py line 688 - avoid double copy when dtype forces cast. 
* 551) .tox/py37/lib/python3.7/site-packages/pandas/core/arrays/sparse.py line 800 - (SparseArray.__setitem__): remove special cases in 
* 552) .tox/py37/lib/python3.7/site-packages/pandas/core/arrays/sparse.py line 1115 - this logic is surely elsewhere 
* 553) .tox/py37/lib/python3.7/site-packages/pandas/core/arrays/sparse.py line 1116 - this could be more efficient 
* 554) .tox/py37/lib/python3.7/site-packages/pandas/core/arrays/sparse.py line 1120 - I think we can avoid densifying when masking a 
* 555) .tox/py37/lib/python3.7/site-packages/pandas/core/arrays/sparse.py line 1266 - may need to coerce array to fill value 
* 556) .tox/py37/lib/python3.7/site-packages/pandas/core/arrays/sparse.py line 1322 - wraparound 
* 557) .tox/py37/lib/python3.7/site-packages/pandas/core/arrays/sparse.py line 1777 - look into _wrap_result 
* 558) .tox/py37/lib/python3.7/site-packages/pandas/core/arrays/sparse.py line 1813 - make this more flexible than just ndarray... 
* 559) .tox/py37/lib/python3.7/site-packages/pandas/core/arrays/sparse.py line 1932 - copy 
* 560) .tox/py37/lib/python3.7/site-packages/pandas/core/arrays/datetimes.py line 61 - (GH-24559): Remove warning, int_as_wall_time parameter. 
* 561) .tox/py37/lib/python3.7/site-packages/pandas/core/arrays/datetimes.py line 533 - consider re-implementing _cached_range; GH#17914 
* 562) .tox/py37/lib/python3.7/site-packages/pandas/core/arrays/datetimes.py line 1298 - consider privatizing (discussion in GH#23113) 
* 563) .tox/py37/lib/python3.7/site-packages/pandas/core/arrays/datetimes.py line 1857 - We do not have tests specific to string-dtypes, 
* 564) .tox/py37/lib/python3.7/site-packages/pandas/core/arrays/datetimes.py line 1915 - should this be deepcopy? 
* 565) .tox/py37/lib/python3.7/site-packages/pandas/core/arrays/datetimes.py line 2034 - deprecate this behavior to instead treat symmetrically 
* 566) .tox/py37/lib/python3.7/site-packages/pandas/core/arrays/datetimes.py line 2055 - cases where we need to do another pass through this func, 
* 567) .tox/py37/lib/python3.7/site-packages/pandas/core/arrays/datetimes.py line 2062 - We have no tests for these 
* 568) .tox/py37/lib/python3.7/site-packages/pandas/core/arrays/numpy_.py line 257 - (_values_for_fillna): remove this 
* 569) .tox/py37/lib/python3.7/site-packages/pandas/core/arrays/array_.py line 269 - (BooleanArray): handle this type 
* 570) .tox/py37/lib/python3.7/site-packages/pandas/core/arrays/integer.py line 354 - (jreback) make this better 
* 571) .tox/py37/lib/python3.7/site-packages/pandas/core/arrays/integer.py line 437 - (jreback) what if we have a non-na float as a fill value? 
* 572) .tox/py37/lib/python3.7/site-packages/pandas/core/arrays/integer.py line 557 - (extension) 
* 573) .tox/py37/lib/python3.7/site-packages/pandas/core/arrays/integer.py line 565 - (extension) 
* 574) .tox/py37/lib/python3.7/site-packages/pandas/core/arrays/datetimelike.py line 386 - Remove Datetime & DatetimeTZ formatters. 
* 575) .tox/py37/lib/python3.7/site-packages/pandas/core/arrays/datetimelike.py line 715 - (GH-23179): Add ExtensionArray.map 
* 576) .tox/py37/lib/python3.7/site-packages/pandas/core/arrays/datetimelike.py line 771 - (GH-20300): remove this 
* 577) .tox/py37/lib/python3.7/site-packages/pandas/core/arrays/datetimelike.py line 1258 - infer freq? 
* 578) .tox/py37/lib/python3.7/site-packages/pandas/core/arrays/datetimelike.py line 1330 - infer freq? 
* 579) .tox/py37/lib/python3.7/site-packages/pandas/core/arrays/datetimelike.py line 1357 - Can we simplify/generalize these cases at all? 
* 580) .tox/py37/lib/python3.7/site-packages/pandas/core/arrays/datetimelike.py line 1454 - skipna is broken with max. 
* 581) .tox/py37/lib/python3.7/site-packages/pandas/core/ops/__init__.py line 130 - what if they both have np.nan for their names? 
* 582) .tox/py37/lib/python3.7/site-packages/pandas/core/ops/__init__.py line 302 - Why None for mod but '%' for rmod? 
* 583) .tox/py37/lib/python3.7/site-packages/pandas/core/ops/__init__.py line 368 - can we make a no-copy implementation? 
* 584) .tox/py37/lib/python3.7/site-packages/pandas/core/ops/__init__.py line 704 - I don't think the functions defined by bool_method are tested 
* 585) .tox/py37/lib/python3.7/site-packages/pandas/core/ops/__init__.py line 1082 -  
* 586) .tox/py37/lib/python3.7/site-packages/pandas/core/ops/__init__.py line 1134 - same for tuples? 
* 587) .tox/py37/lib/python3.7/site-packages/pandas/core/ops/__init__.py line 1310 - Can we do this before the is_integer_dtype check? 
* 588) .tox/py37/lib/python3.7/site-packages/pandas/core/ops/__init__.py line 1611 - This should be moved to the array? 
* 589) .tox/py37/lib/python3.7/site-packages/pandas/core/indexes/period.py line 252 - We can do some of these with no-copy / coercion? 
* 590) .tox/py37/lib/python3.7/site-packages/pandas/core/indexes/period.py line 281 - raising on floats is tested, but maybe not useful. 
* 591) .tox/py37/lib/python3.7/site-packages/pandas/core/indexes/period.py line 316 - When this deprecation is enforced, PeriodIndex.freq can 
* 592) .tox/py37/lib/python3.7/site-packages/pandas/core/indexes/period.py line 329 - simplify, figure out type of values 
* 593) .tox/py37/lib/python3.7/site-packages/pandas/core/indexes/period.py line 364 - (DatetimeArray): Avoid double-boxing 
* 594) .tox/py37/lib/python3.7/site-packages/pandas/core/indexes/period.py line 549 - should probably raise on `how` here, so we don't ignore it. 
* 595) .tox/py37/lib/python3.7/site-packages/pandas/core/indexes/period.py line 946 - (DatetimeArray): remove 
* 596) .tox/py37/lib/python3.7/site-packages/pandas/core/indexes/frozen.py line 71 - Consider deprecating these in favor of `union` (xref gh-15506) 
* 597) .tox/py37/lib/python3.7/site-packages/pandas/core/indexes/category.py line 561 - Investigate an alternative implementation with 
* 598) .tox/py37/lib/python3.7/site-packages/pandas/core/indexes/range.py line 780 - Do attrs get handled reliably? 
* 599) .tox/py37/lib/python3.7/site-packages/pandas/core/indexes/base.py line 123 - docstring? 
* 600) .tox/py37/lib/python3.7/site-packages/pandas/core/indexes/base.py line 160 - docstring? 
* 601) .tox/py37/lib/python3.7/site-packages/pandas/core/indexes/base.py line 833 - (GH-24559): Remove this block, use the following elif. 
* 602) .tox/py37/lib/python3.7/site-packages/pandas/core/indexes/base.py line 2547 - (EA): setops-refactor, clean all this up 
* 603) .tox/py37/lib/python3.7/site-packages/pandas/core/indexes/base.py line 2632 - standardize return type of non-union setops type(self vs other) 
* 604) .tox/py37/lib/python3.7/site-packages/pandas/core/indexes/base.py line 2647 - (EA): setops-refactor, clean all this up 
* 605) .tox/py37/lib/python3.7/site-packages/pandas/core/indexes/base.py line 3591 - sort=False here for backwards compat. It may 
* 606) .tox/py37/lib/python3.7/site-packages/pandas/core/indexes/base.py line 3595 - sort=True here for backwards compat. It may 
* 607) .tox/py37/lib/python3.7/site-packages/pandas/core/indexes/base.py line 3925 - (EA): remove index types as they become extension arrays 
* 608) .tox/py37/lib/python3.7/site-packages/pandas/core/indexes/base.py line 4847 - if we are a MultiIndex, we can do better 
* 609) .tox/py37/lib/python3.7/site-packages/pandas/core/indexes/base.py line 5495 - rmod? rdivmod? 
* 610) .tox/py37/lib/python3.7/site-packages/pandas/core/indexes/api.py line 40 - there are many places that rely on these private methods existing in 
* 611) .tox/py37/lib/python3.7/site-packages/pandas/core/indexes/api.py line 129 - handle index names! 
* 612) .tox/py37/lib/python3.7/site-packages/pandas/core/indexes/api.py line 214 - remove once pd.concat sort default changes 
* 613) .tox/py37/lib/python3.7/site-packages/pandas/core/indexes/interval.py line 1112 - integrate with categorical and make generic 
* 614) .tox/py37/lib/python3.7/site-packages/pandas/core/indexes/interval.py line 1290 - arithmetic operations 
* 615) .tox/py37/lib/python3.7/site-packages/pandas/core/indexes/accessors.py line 52 - use to_period_array 
* 616) .tox/py37/lib/python3.7/site-packages/pandas/core/indexes/datetimes.py line 59 - If we knew what was going in to **d, we might be able to 
* 617) .tox/py37/lib/python3.7/site-packages/pandas/core/indexes/datetimes.py line 522 - we shouldn't be setting attributes like this; 
* 618) .tox/py37/lib/python3.7/site-packages/pandas/core/indexes/datetimes.py line 556 - we shouldn't be setting attributes like this; 
* 619) .tox/py37/lib/python3.7/site-packages/pandas/core/indexes/datetimes.py line 622 - consider re-implementing freq._should_cache for fastpath 
* 620) .tox/py37/lib/python3.7/site-packages/pandas/core/indexes/numeric.py line 373 - (jreback); this can change once we have an EA Index type 
* 621) .tox/py37/lib/python3.7/site-packages/pandas/core/indexes/multi.py line 1484 - what if a level contains tuples?? 
* 622) .tox/py37/lib/python3.7/site-packages/pandas/core/indexes/multi.py line 3215 - Index.union returns other when `len(self)` is 0. 
* 623) .tox/py37/lib/python3.7/site-packages/pandas/core/util/hashing.py line 230 - GH 15362 
* 624) .tox/py37/lib/python3.7/site-packages/pandas/core/internals/managers.py line 60 - flexible with index=None and/or items=None 
* 625) .tox/py37/lib/python3.7/site-packages/pandas/core/internals/managers.py line 416 - (EA): may interfere with ExtensionBlock.setitem for blocks 
* 626) .tox/py37/lib/python3.7/site-packages/pandas/core/internals/managers.py line 622 - assert/validate that `d` is always a scalar? 
* 627) .tox/py37/lib/python3.7/site-packages/pandas/core/internals/managers.py line 815 - (Block.get_values): Make DatetimeTZBlock.get_values 
* 628) .tox/py37/lib/python3.7/site-packages/pandas/core/internals/managers.py line 833 - https://github.com/pandas-dev/pandas/issues/22791 
* 629) .tox/py37/lib/python3.7/site-packages/pandas/core/internals/managers.py line 1039 - (EA): Remove an is_extension_ when all extension types satisfy 
* 630) .tox/py37/lib/python3.7/site-packages/pandas/core/internals/managers.py line 1364 - infer dtypes other than float64 from fill_value 
* 631) .tox/py37/lib/python3.7/site-packages/pandas/core/internals/construction.py line 202 - What about re-joining object columns? 
* 632) .tox/py37/lib/python3.7/site-packages/pandas/core/internals/construction.py line 250 - See if we can avoid these copies 
* 633) .tox/py37/lib/python3.7/site-packages/pandas/core/internals/concat.py line 1 - Needs a better name; too many modules are already called "concat" 
* 634) .tox/py37/lib/python3.7/site-packages/pandas/core/internals/concat.py line 404 - should this be ju.block._can_hold_na? 
* 635) .tox/py37/lib/python3.7/site-packages/pandas/core/internals/blocks.py line 645 - (extension) 
* 636) .tox/py37/lib/python3.7/site-packages/pandas/core/internals/blocks.py line 996 - this prob needs some better checking 
* 637) .tox/py37/lib/python3.7/site-packages/pandas/core/internals/blocks.py line 1527 - cleanup this special case. 
* 638) .tox/py37/lib/python3.7/site-packages/pandas/core/internals/blocks.py line 1533 - NonConsolidatableMixin shape 
* 639) .tox/py37/lib/python3.7/site-packages/pandas/core/internals/blocks.py line 2011 - (SparseArray.__setitem__): remove this if condition 
* 640) .tox/py37/lib/python3.7/site-packages/pandas/core/internals/blocks.py line 2644 - remove the np.int64 support once coerce_values and 
* 641) .tox/py37/lib/python3.7/site-packages/pandas/core/internals/blocks.py line 2801 - Refactor when convert_objects is removed since there will be 1 path 
* 642) .tox/py37/lib/python3.7/site-packages/pandas/core/internals/blocks.py line 2833 - allow EA once reshape is supported 
* 643) .tox/py37/lib/python3.7/site-packages/pandas/core/internals/blocks.py line 2880 - (ExtensionArray): remove is_extension_type 
* 644) .tox/py37/lib/python3.7/site-packages/pandas/core/internals/blocks.py line 3185 - (CategoricalBlock.where): 
* 645) .tox/py37/lib/python3.7/site-packages/pandas/core/internals/blocks.py line 3280 - This is no longer hit internally; does it need to be retained 
* 646) .tox/py37/lib/python3.7/site-packages/pandas/core/internals/blocks.py line 3315 - https://github.com/pandas-dev/pandas/issues/23023 
* 647) .tox/py37/lib/python3.7/site-packages/pandas/core/dtypes/cast.py line 190 - (DatetimeArray): merge with previous elif 
* 648) .tox/py37/lib/python3.7/site-packages/pandas/core/dtypes/cast.py line 898 - why not timedelta? 
* 649) .tox/py37/lib/python3.7/site-packages/pandas/core/dtypes/common.py line 636 - Consider making Period an instance of PeriodDtype 
* 650) .tox/py37/lib/python3.7/site-packages/pandas/core/dtypes/common.py line 672 - Consider making Interval an instance of IntervalDtype 
* 651) .tox/py37/lib/python3.7/site-packages/pandas/core/dtypes/common.py line 740 - gh-15585: consider making the checks stricter. 
* 652) .tox/py37/lib/python3.7/site-packages/pandas/core/dtypes/common.py line 1672 - (jreback) 
* 653) .tox/py37/lib/python3.7/site-packages/pandas/core/dtypes/common.py line 1972 - (jreback) 
* 654) .tox/py37/lib/python3.7/site-packages/pandas/core/dtypes/concat.py line 538 - Fix join unit generation so we aren't passed this. 
* 655) .tox/py37/lib/python3.7/site-packages/pandas/core/dtypes/dtypes.py line 23 - (GH26403): Replace with Optional[bool] or bool 
* 656) .tox/py37/lib/python3.7/site-packages/pandas/core/dtypes/dtypes.py line 216 - Document public vs. private API 
* 657) .tox/py37/lib/python3.7/site-packages/pandas/core/dtypes/dtypes.py line 443 - hash_array doesn't handle mixed types. It casts 
* 658) .tox/py37/lib/python3.7/site-packages/pandas/core/dtypes/dtypes.py line 592 - remove if block when ordered=None as default is deprecated 
* 659) .tox/py37/lib/python3.7/site-packages/pandas/core/dtypes/dtypes.py line 742 - (py3): Change this pass to `raise TypeError(msg) from e` 
* 660) .tox/py37/lib/python3.7/site-packages/pandas/core/dtypes/dtypes.py line 758 - update this. 
* 661) .tox/py37/lib/python3.7/site-packages/pandas/core/sparse/frame.py line 213 - figure out how to handle this case, all nan's? 
* 662) .tox/py37/lib/python3.7/site-packages/pandas/core/sparse/frame.py line 575 - be a bit more intelligent here 
* 663) .tox/py37/lib/python3.7/site-packages/pandas/core/sparse/frame.py line 739 - fill value handling 
* 664) .tox/py37/lib/python3.7/site-packages/pandas/core/sparse/frame.py line 1019 - Figure out whether this can be reached. 
* 665) .tox/py37/lib/python3.7/site-packages/pandas/core/sparse/scipy_sparse.py line 36 - how to do this better? cleanly slice nonnull_labels given the 
* 666) .tox/py37/lib/python3.7/site-packages/pandas/core/sparse/scipy_sparse.py line 43 - these two lines can replace the code below but 
* 667) .tox/py37/lib/python3.7/site-packages/pandas/core/sparse/scipy_sparse.py line 145 - (SparseSeries): remove this and the sparse_series keyword. 
* 668) .tox/py37/lib/python3.7/site-packages/pandas/core/sparse/scipy_sparse.py line 148 - specify kind? 
* 669) .tox/py37/lib/python3.7/site-packages/pandas/core/sparse/series.py line 92 - Most of this should be refactored and shared with Series 
* 670) .tox/py37/lib/python3.7/site-packages/pandas/core/sparse/series.py line 145 - See if this can be shared 
* 671) .tox/py37/lib/python3.7/site-packages/pandas/core/sparse/series.py line 336 - Document difference from Series.__getitem__, deprecate, 
* 672) .tox/py37/lib/python3.7/site-packages/pandas/core/sparse/series.py line 506 - https://github.com/pandas-dev/pandas/issues/22314 
* 673) .tox/py37/lib/python3.7/site-packages/pandas/core/sparse/series.py line 522 - remove? 
* 674) .tox/py37/lib/python3.7/site-packages/pandas/core/sparse/series.py line 577 - SparseSeries.isna is Sparse, while Series.isna is dense 
* 675) .tox/py37/lib/python3.7/site-packages/pandas/core/sparse/series.py line 604 - make more efficient 
* 676) NDBC/NDBC.py line 319 - (ryan@gensci.org): Build out function to look for values 
* 677) NDBC/NDBC.py line 326 - (ryan@gensci.org): Determine how to iterate over all data 
* 678) venv/lib/python3.6/site-packages/numpy/lib/npyio.py line 458 - Use contextlib.ExitStack once we drop Python 2 
* 679) venv/lib/python3.6/site-packages/numpy/lib/npyio.py line 1041 - emit portability warning? 
* 680) venv/lib/python3.6/site-packages/numpy/lib/_datasource.py line 148 - .zip support, .tar support? 
* 681) venv/lib/python3.6/site-packages/numpy/lib/_datasource.py line 426 - Doesn't handle compressed files! 
* 682) venv/lib/python3.6/site-packages/numpy/lib/_datasource.py line 498 - This should be more robust.  Handles case where path includes 
* 683) venv/lib/python3.6/site-packages/numpy/lib/_datasource.py line 616 - There is no support for opening a file for writing which 
* 684) venv/lib/python3.6/site-packages/numpy/lib/_datasource.py line 619 - Add a ``subdir`` parameter for specifying the subdirectory 
* 685) venv/lib/python3.6/site-packages/numpy/lib/mixins.py line 180 - handle the optional third argument for __pow__? 
* 686) venv/lib/python3.6/site-packages/numpy/lib/tests/test_io.py line 310 - specify exact message 
* 687) venv/lib/python3.6/site-packages/numpy/lib/tests/test_mixins.py line 92 - test div on Python 2, only 
* 688) venv/lib/python3.6/site-packages/numpy/ma/tests/test_old_ma.py line 725 - FIXME: Find out what the following raises a warning in r8247 
* 689) venv/lib/python3.6/site-packages/numpy/ma/tests/test_core.py line 5715 - Test masked_object, masked_equal, ... 
* 690) venv/lib/python3.6/site-packages/numpy/random/tests/test_random.py line 1122 - Include test for randint once it can broadcast 
* 691) venv/lib/python3.6/site-packages/numpy/random/tests/test_random.py line 1781 - Uncomment once randint can broadcast arguments 
* 692) venv/lib/python3.6/site-packages/numpy/linalg/tests/test_linalg.py line 1755 - are there no other tests for cholesky? 
* 693) venv/lib/python3.6/site-packages/numpy/f2py/crackfortran.py line 135 -  
* 694) venv/lib/python3.6/site-packages/numpy/f2py/crackfortran.py line 2189 -  
* 695) venv/lib/python3.6/site-packages/numpy/f2py/crackfortran.py line 2782 - test .eq., .neq., etc replacements. 
* 696) venv/lib/python3.6/site-packages/numpy/f2py/crackfortran.py line 3532 -  
* 697) venv/lib/python3.6/site-packages/numpy/polynomial/_polybase.py line 310 - we're stuck with disabling math formatting until we handle 
* 698) venv/lib/python3.6/site-packages/numpy/core/numeric.py line 576 - this works around .astype(bool) not working properly (gh-9847) 
* 699) venv/lib/python3.6/site-packages/numpy/core/_add_newdocs.py line 2096 - ). 
* 700) venv/lib/python3.6/site-packages/numpy/core/_add_newdocs.py line 8205 - work out how to put this on the base class, np.floating 
* 701) venv/lib/python3.6/site-packages/numpy/core/_dtype.py line 172 - this path can never be reached 
* 702) venv/lib/python3.6/site-packages/numpy/core/_dtype.py line 181 - this duplicates the C append_metastr_to_string 
* 703) venv/lib/python3.6/site-packages/numpy/core/include/numpy/multiarray_api.txt line 426 - For NumPy 2.0, this could accept an order parameter which 
* 704) venv/lib/python3.6/site-packages/numpy/core/include/numpy/multiarray_api.txt line 690 - For NumPy 2.0, add a NPY_CASTING parameter. 
* 705) venv/lib/python3.6/site-packages/numpy/core/include/numpy/multiarray_api.txt line 964 - In NumPy 2.0, should make the iteration order a parameter. 
* 706) venv/lib/python3.6/site-packages/numpy/core/tests/test_datetime.py line 980 - Changing to 'same_kind' or 'safe' casting in the ufuncs by 
* 707) venv/lib/python3.6/site-packages/numpy/core/tests/test_datetime.py line 1534 - Allowing unsafe casting by 
* 708) venv/lib/python3.6/site-packages/numpy/core/tests/test_datetime.py line 2709 - add absolute (gold standard) time span limit strings 
* 709) venv/lib/python3.6/site-packages/numpy/core/tests/test_multiarray.py line 6795 - test for multidimensional 
* 710) venv/lib/python3.6/site-packages/numpy/core/tests/test_umath_complex.py line 18 - branch cuts (use Pauli code) 
* 711) venv/lib/python3.6/site-packages/numpy/core/tests/test_umath_complex.py line 19 - conj 'symmetry' 
* 712) venv/lib/python3.6/site-packages/numpy/core/tests/test_umath_complex.py line 20 - FPU exceptions 
* 713) venv/lib/python3.6/site-packages/numpy/core/tests/test_umath_complex.py line 30 - replace with a check on whether platform-provided C99 funcs are used 
* 714) venv/lib/python3.6/site-packages/numpy/core/tests/test_umath_complex.py line 33 - This can be xfail when the generator functions are got rid of. 
* 715) venv/lib/python3.6/site-packages/numpy/core/tests/test_umath_complex.py line 129 - This can be xfail when the generator functions are got rid of. 
* 716) venv/lib/python3.6/site-packages/numpy/core/tests/test_umath_complex.py line 477 - This can be xfail when the generator functions are got rid of. 
* 717) venv/lib/python3.6/site-packages/numpy/distutils/npy_pkg_config.py line 417 -  
* 718) venv/lib/python3.6/site-packages/numpy/distutils/fcompiler/intel.py line 38 - could use -Xlinker here, if it's supported 
* 719) venv/lib/python3.6/site-packages/numpy/distutils/fcompiler/__init__.py line 1182 - implement get_f90flags and use it in _compile similarly to get_f77flags 
* 720) venv/lib/python3.6/site-packages/numpy/distutils/fcompiler/gnu.py line 276 - could use -Xlinker here, if it's supported 
* 721) venv/lib/python3.6/site-packages/numpy/distutils/command/build_src.py line 565 - --inplace support for sdist command 
* 722) venv/lib/python3.6/site-packages/zope/interface/adapter.py line 498 - add invalidation when a provided interface changes, in case 
* 723) venv/lib/python3.6/site-packages/zope/interface/interface.py line 491 - It would ne nice if: 
* 724) venv/lib/python3.6/site-packages/zope/interface/declarations.py line 257 - need old style __implements__ compatibility? 
* 725) venv/lib/python3.6/site-packages/zope/interface/declarations.py line 270 - need old style __implements__ compatibility? 
* 726) venv/lib/python3.6/site-packages/zope/interface/tests/test_declarations.py line 456 - Figure out P3 story 
* 727) venv/lib/python3.6/site-packages/zope/interface/tests/test_declarations.py line 463 - Figure out P3 story 
* 728) venv/lib/python3.6/site-packages/zope/interface/tests/test_declarations.py line 685 - Py3 story 
* 729) venv/lib/python3.6/site-packages/zope/interface/tests/test_declarations.py line 783 - Py3 story 
* 730) venv/lib/python3.6/site-packages/zope/interface/tests/test_odd_declarations.py line 68 - We are going to need more magic to make classProvides work with odd 
* 731) venv/lib/python3.6/site-packages/zope/interface/tests/test_odd_declarations.py line 238 - _test_classProvides_fails_for_odd_class(self): 
* 732) venv/lib/python3.6/site-packages/nose/result.py line 35 - ) that extend the errors/failures/success triad. 
* 733) venv/lib/python3.6/site-packages/nose/util.py line 39 - empty directories look like non-directory files 
* 734) venv/lib/python3.6/site-packages/nose/inspector.py line 164 -  
* 735) venv/lib/python3.6/site-packages/nose/inspector.py line 167 -  
* 736) venv/lib/python3.6/site-packages/nose/loader.py line 206 - is this try/except needed? 
* 737) venv/lib/python3.6/site-packages/nose/loader.py line 581 - is this try/except needed? 
* 738) venv/lib/python3.6/site-packages/nose/plugins/errorclass.py line 19 - ' that is considered a failure, 
* 739) venv/lib/python3.6/site-packages/nose/plugins/errorclass.py line 25 - ', isfailure=True) 
* 740) venv/lib/python3.6/site-packages/nose/plugins/errorclass.py line 34 - ', True)),) 
* 741) venv/lib/python3.6/site-packages/nose/plugins/errorclass.py line 66 - is printed. 
* 742) venv/lib/python3.6/site-packages/nose/plugins/errorclass.py line 69 - I need to test something 
* 743) venv/lib/python3.6/site-packages/nose/plugins/errorclass.py line 82 - runTest (....TestTodo) 
* 744) venv/lib/python3.6/site-packages/nose/plugins/attrib.py line 250 - is there a need for case-sensitive value comparison? 
* 745) venv/lib/python3.6/site-packages/nose/plugins/prof.py line 149 - is this trying to catch just the case where not 
* 746) venv/lib/python3.6/site-packages/DateTime/interfaces.py line 35 - determine whether this method really is part of the public API 
* 747) venv/lib/python3.6/site-packages/requests/adapters.py line 554 - Remove this in 3.0.0: see #2811 
* 748) venv/lib/python3.6/site-packages/requests/hooks.py line 21 - response is the only one 
* 749) venv/lib/python3.6/site-packages/urllib3/connection.py line 178 - Fix tunnel so it doesn't depend on self.sock state. 
* 750) venv/lib/python3.6/site-packages/urllib3/exceptions.py line 238 - (t-8ch): Stop inheriting from AssertionError in v2.0. 
* 751) venv/lib/python3.6/site-packages/urllib3/connectionpool.py line 481 - Add optional support for socket.gethostbyname checking. 
* 752) venv/lib/python3.6/site-packages/urllib3/contrib/securetransport.py line 627 - should I do clean shutdown here? Do I have to? 
* 753) venv/lib/python3.6/site-packages/urllib3/contrib/securetransport.py line 787 - Well, crap. 
* 754) venv/lib/python3.6/site-packages/urllib3/contrib/securetransport.py line 797 - Update in line with above. 
* 755) venv/lib/python3.6/site-packages/urllib3/util/url.py line 405 - Remove this when we break backwards compatibility. 
* 756) venv/lib/python3.6/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/retrying.py line 99 - add chaining of stop behaviors 
* 757) venv/lib/python3.6/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/retrying.py line 119 - add chaining of wait behaviors 
* 758) venv/lib/python3.6/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/retrying.py line 154 - simplify retrying by Exception types 
* 759) venv/lib/python3.6/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/pep517/wrappers.py line 52 - Is this over-engineered? Maybe frontends only need to 
* 760) venv/lib/python3.6/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/cachecontrol/controller.py line 181 - There is an assumption that the result will be a 
* 761) venv/lib/python3.6/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/cachecontrol/filewrapper.py line 47 - Add some logging here... 
* 762) venv/lib/python3.6/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/requests/adapters.py line 554 - Remove this in 3.0.0: see #2811 
* 763) venv/lib/python3.6/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/requests/hooks.py line 21 - response is the only one 
* 764) venv/lib/python3.6/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/packaging/requirements.py line 91 - Can we test whether something is contained within a requirement? 
* 765) venv/lib/python3.6/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/packaging/requirements.py line 94 - Can we normalize the name and extra name? 
* 766) venv/lib/python3.6/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/urllib3/connection.py line 179 - Fix tunnel so it doesn't depend on self.sock state. 
* 767) venv/lib/python3.6/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/urllib3/exceptions.py line 238 - (t-8ch): Stop inheriting from AssertionError in v2.0. 
* 768) venv/lib/python3.6/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/urllib3/connectionpool.py line 472 - Add optional support for socket.gethostbyname checking. 
* 769) venv/lib/python3.6/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/urllib3/contrib/securetransport.py line 592 - should I do clean shutdown here? Do I have to? 
* 770) venv/lib/python3.6/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/urllib3/contrib/securetransport.py line 731 - Well, crap. 
* 771) venv/lib/python3.6/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/urllib3/contrib/securetransport.py line 741 - Update in line with above. 
* 772) venv/lib/python3.6/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/html5lib/serializer.py line 324 - Add namespace support here 
* 773) venv/lib/python3.6/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/chardet/sbcsgroupprober.py line 63 - Restore Hungarian encodings (iso-8859-2 and windows-1250) 
* 774) venv/lib/python3.6/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/distlib/version.py line 269 - fill this out 
* 775) venv/lib/python3.6/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/distlib/version.py line 529 - unintended side-effect on, e.g., "2003.05.09" 
* 776) venv/lib/python3.6/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/distlib/util.py line 423 - check k, v for valid values 
* 777) venv/lib/python3.6/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/distlib/metadata.py line 356 - document the mapping API and UNKNOWN default key 
* 778) venv/lib/python3.6/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/distlib/metadata.py line 727 - could add iter* variants 
* 779) venv/lib/python3.6/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/distlib/metadata.py line 1147 - other fields such as contacts 
* 780) venv/lib/python3.6/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/distlib/locators.py line 812 - Note: this cache is never actually cleared. It's assumed that 
* 781) venv/lib/python3.6/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/distlib/locators.py line 980 - SHA256 digest 
* 782) venv/lib/python3.6/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/distlib/wheel.py line 796 - version verification 
* 783) venv/lib/python3.6/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/msgpack/fallback.py line 645 - should we eliminate the recursion? 
* 784) venv/lib/python3.6/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/msgpack/fallback.py line 649 - check whether we need to call `list_hook` 
* 785) venv/lib/python3.6/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/msgpack/fallback.py line 657 - is the interaction between `list_hook` and `use_list` ok? 
* 786) venv/lib/python3.6/site-packages/pip-19.0.3-py3.6.egg/pip/_vendor/msgpack/fallback.py line 662 - check whether we need to call hooks 
* 787) venv/lib/python3.6/site-packages/pip-19.0.3-py3.6.egg/pip/_internal/wheel.py line 324 - Investigate and break this up. 
* 788) venv/lib/python3.6/site-packages/pip-19.0.3-py3.6.egg/pip/_internal/wheel.py line 325 - Look into moving this into a dedicated class for representing an 
* 789) venv/lib/python3.6/site-packages/pip-19.0.3-py3.6.egg/pip/_internal/wheel.py line 681 - Maybe move the class into the models sub-package 
* 790) venv/lib/python3.6/site-packages/pip-19.0.3-py3.6.egg/pip/_internal/wheel.py line 682 - Maybe move the install code into this class 
* 791) venv/lib/python3.6/site-packages/pip-19.0.3-py3.6.egg/pip/_internal/wheel.py line 1023 - by @pradyunsg 
* 792) venv/lib/python3.6/site-packages/pip-19.0.3-py3.6.egg/pip/_internal/req/req_install.py line 823 - Investigate if this should be kept in InstallRequirement 
* 793) venv/lib/python3.6/site-packages/pip-19.0.3-py3.6.egg/pip/_internal/req/req_file.py line 234 - Why not use `comes_from='-r {} (line {})'` here as well? 
* 794) venv/lib/python3.6/site-packages/pip-19.0.3-py3.6.egg/pip/_internal/req/req_file.py line 348 - handle space after '\'. 
* 795) venv/lib/python3.6/site-packages/pip-19.0.3-py3.6.egg/pip/_internal/operations/prepare.py line 226 - Modify to reduce indentation needed 
* 796) venv/lib/python3.6/site-packages/pip-19.0.3-py3.6.egg/pip/_internal/operations/prepare.py line 250 - Breakup into smaller functions 
* 797) venv/lib/python3.6/site-packages/pip-19.0.3-py3.6.egg/pip/_internal/cli/base_command.py line 154 - Try to get these passing down from the command? 
* 798) venv/lib/python3.6/site-packages/click/_termui_impl.py line 403 - This never terminates if the passed generator never terminates. 
* 799) venv/lib/python3.6/site-packages/dateutil/rrule.py line 1281 - Check -numweeks for next year. 
* 800) venv/lib/python3.6/site-packages/dateutil/parser/_parser.py line 55 - pandas.core.tools.datetimes imports this explicitly.  Might be worth 
* 801) venv/lib/python3.6/site-packages/dateutil/parser/_parser.py line 290 - "Tues" 
* 802) venv/lib/python3.6/site-packages/dateutil/parser/_parser.py line 292 - "Thurs" 
* 803) venv/lib/python3.6/site-packages/dateutil/parser/_parser.py line 299 - "Febr" 
* 804) venv/lib/python3.6/site-packages/dateutil/parser/_parser.py line 320 - ERA = ["AD", "BC", "CE", "BCE", "Stardate", 
* 805) venv/lib/python3.6/site-packages/dateutil/parser/_parser.py line 823 - not hit in tests 
* 806) venv/lib/python3.6/site-packages/dateutil/parser/_parser.py line 861 - check that l[i + 1] is integer? 
* 807) venv/lib/python3.6/site-packages/dateutil/parser/_parser.py line 871 - Check that l[i+3] is minute-like? 
* 808) venv/lib/python3.6/site-packages/dateutil/parser/_parser.py line 964 - Check if res attributes already set. 
* 809) venv/lib/python3.6/site-packages/dateutil/parser/_parser.py line 988 - checking that hour/minute/second are not 
* 810) venv/lib/python3.6/site-packages/dateutil/parser/_parser.py line 995 - try/except for this? 
* 811) venv/lib/python3.6/site-packages/dateutil/parser/_parser.py line 1093 - Are we sure this is the right condition here? 
* 812) venv/lib/python3.6/site-packages/dateutil/parser/_parser.py line 1165 - Every usage of this function sets res.second to the return 
* 813) venv/lib/python3.6/site-packages/dateutil/parser/_parser.py line 1185 - Is this going to admit a lot of false-positives for when we 
* 814) venv/lib/python3.6/site-packages/dateutil/zoneinfo/__init__.py line 25 - switch to FileNotFoundError? 
* 815) venv/lib/python3.6/site-packages/dateutil/zoneinfo/__init__.py line 80 - Remove after deprecation period. 
* 816) venv/lib/python3.6/site-packages/dateutil/tz/_factories.py line 42 - Maybe this should be under a lock? 
* 817) venv/lib/python3.6/site-packages/dateutil/tz/_factories.py line 65 - Maybe this should be under a lock? 
* 818) venv/lib/python3.6/site-packages/chardet/sbcsgroupprober.py line 63 - Restore Hungarian encodings (iso-8859-2 and windows-1250) 
* 819) venv/lib/python3.6/site-packages/bs4/dammit.py line 71 - Ideally we would be able to recognize all HTML 5 named 
* 820) venv/lib/python3.6/site-packages/bs4/builder/_lxml.py line 99 - Issue a warning if parser is present but not a 
* 821) venv/lib/python3.6/site-packages/bs4/builder/_html5lib.py line 267 - This has O(n^2) performance, for input like 
* 822) venv/lib/python3.6/site-packages/bs4/builder/_html5lib.py line 404 - This code has no test coverage and I'm not sure 
* 823) venv/lib/python3.6/site-packages/pandas/__init__.py line 195 - remove Panel compat in 1.0 
* 824) venv/lib/python3.6/site-packages/pandas/io/parquet.py line 167 - Support 'ab' 
* 825) venv/lib/python3.6/site-packages/pandas/io/sql.py line 592 - support for multiIndex 
* 826) venv/lib/python3.6/site-packages/pandas/io/sql.py line 1013 - Refine integer size. 
* 827) venv/lib/python3.6/site-packages/pandas/io/sql.py line 1753 - (wesm): unused? 
* 828) venv/lib/python3.6/site-packages/pandas/io/parsers.py line 435 - get_filepath_or_buffer could return 
* 829) venv/lib/python3.6/site-packages/pandas/io/stata.py line 354 - If/when pandas supports more than datetime64[ns], this should be 
* 830) venv/lib/python3.6/site-packages/pandas/io/stata.py line 1850 - is the next line needed above in the data(...) method? 
* 831) venv/lib/python3.6/site-packages/pandas/io/stata.py line 1983 - expand to handle datetime to integer conversion 
* 832) venv/lib/python3.6/site-packages/pandas/io/stata.py line 2020 - Refactor to combine type with format 
* 833) venv/lib/python3.6/site-packages/pandas/io/stata.py line 2021 - expand this to handle a default datetime format? 
* 834) venv/lib/python3.6/site-packages/pandas/io/stata.py line 2619 - expand to handle datetime to integer conversion 
* 835) venv/lib/python3.6/site-packages/pandas/io/clipboard/clipboards.py line 108 - https://github.com/asweigart/pyperclip/issues/43 
* 836) venv/lib/python3.6/site-packages/pandas/io/formats/style.py line 519 - namespace all the pandas keys 
* 837) venv/lib/python3.6/site-packages/pandas/io/formats/css.py line 94 - resolve other font-relative units 
* 838) venv/lib/python3.6/site-packages/pandas/io/formats/css.py line 106 - support % 
* 839) venv/lib/python3.6/site-packages/pandas/io/formats/css.py line 248 - don't lowercase case sensitive parts of values (strings) 
* 840) venv/lib/python3.6/site-packages/pandas/io/formats/excel.py line 81 - memoize? 
* 841) venv/lib/python3.6/site-packages/pandas/io/formats/excel.py line 93 - handle cell width and height: needs support in pandas.io.excel 
* 842) venv/lib/python3.6/site-packages/pandas/io/formats/excel.py line 119 - text-indent, padding-left -> alignment.indent 
* 843) venv/lib/python3.6/site-packages/pandas/io/formats/excel.py line 194 - perhaps allow for special properties 
* 844) venv/lib/python3.6/site-packages/pandas/io/formats/html.py line 301 - Refactor to remove code duplication with code 
* 845) venv/lib/python3.6/site-packages/pandas/io/formats/html.py line 308 - Refactor to use _get_column_name_list from 
* 846) venv/lib/python3.6/site-packages/pandas/io/formats/html.py line 334 - Refactor to remove code duplication with code block 
* 847) venv/lib/python3.6/site-packages/pandas/io/formats/html.py line 341 - Refactor to use _get_column_name_list from 
* 848) venv/lib/python3.6/site-packages/pandas/io/excel/_openpyxl.py line 497 - replace with openpyxl constants 
* 849) venv/lib/python3.6/site-packages/pandas/io/excel/_xlsxwriter.py line 118 - support other fill patterns 
* 850) venv/lib/python3.6/site-packages/pandas/io/json/_normalize.py line 264 - handle record value which are lists, at least error 
* 851) venv/lib/python3.6/site-packages/pandas/io/json/_json.py line 283 - Do this timedelta properly in objToJSON.c See GH #15137 
* 852) venv/lib/python3.6/site-packages/pandas/tests/test_nanops.py line 842 - unused? 
* 853) venv/lib/python3.6/site-packages/pandas/tests/test_algos.py line 191 - (wesm): unused? 
* 854) venv/lib/python3.6/site-packages/pandas/tests/test_algos.py line 909 - same for (timedelta) 
* 855) venv/lib/python3.6/site-packages/pandas/tests/test_multilevel.py line 890 - what should join do with names ? 
* 856) venv/lib/python3.6/site-packages/pandas/tests/test_multilevel.py line 1103 - groupby with level_values drops names 
* 857) venv/lib/python3.6/site-packages/pandas/tests/test_expressions.py line 175 - FIGURE OUT HOW TO GET IT TO WORK... 
* 858) venv/lib/python3.6/site-packages/pandas/tests/test_strings.py line 212 - get rid of these xfails 
* 859) venv/lib/python3.6/site-packages/pandas/tests/test_strings.py line 251 - get rid of these xfails 
* 860) venv/lib/python3.6/site-packages/pandas/tests/test_strings.py line 1837 - unused 
* 861) venv/lib/python3.6/site-packages/pandas/tests/test_strings.py line 2544 - see GH 18463 
* 862) venv/lib/python3.6/site-packages/pandas/tests/test_base.py line 1070 - (GH-24559): Remove the filterwarnings 
* 863) venv/lib/python3.6/site-packages/pandas/tests/test_base.py line 1124 - (GH-24559): Remove the filterwarnings 
* 864) venv/lib/python3.6/site-packages/pandas/tests/indexing/test_chaining_and_caching.py line 383 - (wesm): unused? 
* 865) venv/lib/python3.6/site-packages/pandas/tests/indexing/test_coercion.py line 179 - _GH12747 The result must be int") 
* 866) venv/lib/python3.6/site-packages/pandas/tests/indexing/test_coercion.py line 183 - _GH12747 The result must be float") 
* 867) venv/lib/python3.6/site-packages/pandas/tests/indexing/test_coercion.py line 187 - _GH12747 The result must be complex") 
* 868) venv/lib/python3.6/site-packages/pandas/tests/indexing/test_coercion.py line 327 - _GH12747 The result must be float") 
* 869) venv/lib/python3.6/site-packages/pandas/tests/indexing/test_indexing.py line 293 - (wesm): unused? 
* 870) venv/lib/python3.6/site-packages/pandas/tests/indexing/test_partial.py line 175 - #15657, these are left as object and not coerced 
* 871) venv/lib/python3.6/site-packages/pandas/tests/indexing/multiindex/test_xs.py line 195 - move to another module or refactor 
* 872) venv/lib/python3.6/site-packages/pandas/tests/indexing/multiindex/test_xs.py line 205 - move to another module or refactor 
* 873) venv/lib/python3.6/site-packages/pandas/tests/indexing/multiindex/test_xs.py line 217 - move to another module or refactor 
* 874) venv/lib/python3.6/site-packages/pandas/tests/indexing/multiindex/test_setitem.py line 260 - (wesm): unused? 
* 875) venv/lib/python3.6/site-packages/pandas/tests/indexing/interval/test_interval_new.py line 131 - with non-existing intervals ? 
* 876) venv/lib/python3.6/site-packages/pandas/tests/indexing/interval/test_interval_new.py line 213 - KeyError is the appropriate error? 
* 877) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_object.py line 75 - parametrize 
* 878) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_object.py line 156 - Moved from tests.series.test_operators; needs cleanup 
* 879) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_object.py line 167 - parametrize over box 
* 880) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_object.py line 185 - cleanup & parametrize over box 
* 881) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_object.py line 233 - cleanup & parametrize over box 
* 882) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_datetime64.py line 95 - moved from tests.series.test_operators; needs cleanup 
* 883) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_datetime64.py line 374 - implement _assert_tzawareness_compat for the reverse 
* 884) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_datetime64.py line 380 - moved from tests.indexes.test_base; parametrize and de-duplicate 
* 885) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_datetime64.py line 1201 - parametrize over timezone? 
* 886) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_datetime64.py line 1271 - parametrize over the scalar being added?  radd?  sub? 
* 887) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_datetime64.py line 1336 - redundant with test_dt64arr_add_sub_DateOffset?  that includes 
* 888) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_datetime64.py line 1507 - __sub__, __rsub__ 
* 889) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_datetime64.py line 1533 - overlap with test_dt64arr_add_mixed_offset_array? 
* 890) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_datetime64.py line 1629 - box + de-duplicate 
* 891) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_datetime64.py line 1793 - Decide if this ought to work. 
* 892) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_datetime64.py line 1808 - This next block of tests came from tests.series.test_operators, 
* 893) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_datetime64.py line 1844 - (jreback) __rsub__ should raise? 
* 894) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_datetime64.py line 1946 - this block also needs to be de-duplicated and parametrized 
* 895) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_datetime64.py line 2264 - A couple other tests belong in this section.  Move them in 
* 896) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_datetime64.py line 2335 - Most of this block is moved from series or frame tests, needs 
* 897) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_datetime64.py line 2351 - unused 
* 898) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_period.py line 43 - parameterize over boxes 
* 899) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_period.py line 60 - moved from test_datetime64; de-duplicate with version below 
* 900) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_period.py line 127 - could also box idx? 
* 901) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_period.py line 168 - Could parametrize over boxes for idx? 
* 902) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_period.py line 246 - De-duplicate with test_pi_cmp_nat 
* 903) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_period.py line 322 - needs parametrization+de-duplication 
* 904) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_period.py line 472 - parametrize over boxes for other? 
* 905) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_period.py line 514 - parametrize over boxes for other? 
* 906) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_period.py line 831 - Some of these are misnomers because of non-Tick DateOffsets 
* 907) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_timedelta64.py line 66 - All of these need to be parametrized over box 
* 908) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_timedelta64.py line 186 - better name 
* 909) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_timedelta64.py line 380 - (wesm): unused? 
* 910) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_timedelta64.py line 449 - Needs more informative name, probably split up into 
* 911) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_timedelta64.py line 485 - parametrize over boxes 
* 912) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_timedelta64.py line 554 - moved from frame tests; needs parametrization/de-duplication 
* 913) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_timedelta64.py line 570 - moved from tests.indexes.timedeltas.test_arithmetic; needs 
* 914) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_timedelta64.py line 666 - moved from tests.series.test_operators, needs splitting, cleanup, 
* 915) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_timedelta64.py line 865 - parametrize over box for pi? 
* 916) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_timedelta64.py line 888 - parametrize over scalar datetime types? 
* 917) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_timedelta64.py line 907 - parametrize over types of datetime scalar? 
* 918) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_timedelta64.py line 999 - separate/parametrize 
* 919) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_timedelta64.py line 1060 - Add DataFrame in here? 
* 920) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_timedelta64.py line 1084 - this was taken from tests.series.test_ops; de-duplicate 
* 921) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_timedelta64.py line 1105 - this was taken from tests.series.test_ops; de-duplicate 
* 922) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_timedelta64.py line 1174 - parametrize over [add, sub, radd, rsub]? 
* 923) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_timedelta64.py line 1287 - this was taken from tests.series.test_operators; de-duplicate 
* 924) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_timedelta64.py line 1355 - combine with test_td64arr_add_offset_index by parametrizing 
* 925) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_timedelta64.py line 1452 - separate/parametrize add/sub test? 
* 926) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_timedelta64.py line 1490 - Moved from tests.series.test_operators; needs cleanup 
* 927) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_timedelta64.py line 1579 - Put Series/DataFrame in others? 
* 928) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_timedelta64.py line 1788 - Is this redundant with test_td64arr_floordiv_tdlike_scalar? 
* 929) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_timedelta64.py line 1817 - operations with timedelta-like arrays, numeric arrays, 
* 930) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_timedelta64.py line 2059 - Should we be parametrizing over types for `ser` too? 
* 931) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_timedelta64.py line 2079 - Should we be parametrizing over types for `ser` too? 
* 932) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_timedelta64.py line 2090 - the direct operation TimedeltaIndex / Series still 
* 933) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_timedelta64.py line 2114 - Should we skip this case sooner or test something else? 
* 934) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_numeric.py line 81 - also check name retentention 
* 935) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_numeric.py line 120 - also check name retentention 
* 936) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_numeric.py line 165 - de-duplicate with test_numeric_arr_mul_tdscalar 
* 937) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_numeric.py line 174 - also test non-nanosecond timedelta64 and Tick objects; 
* 938) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_numeric.py line 689 - This came from series.test.test_operators, needs cleanup 
* 939) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_numeric.py line 702 - this came from tests.series.test_analytics, needs cleanup and 
* 940) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_numeric.py line 746 - This came from series.test.test_operators, needs cleanup 
* 941) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_numeric.py line 772 - This came from series.test.test_operators, needs cleanup 
* 942) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_numeric.py line 796 - This came from series.test.test_operators, needs cleanup 
* 943) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_numeric.py line 826 - taken from tests.frame.test_operators, needs cleanup 
* 944) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_numeric.py line 871 - taken from tests.series.test_operators; needs cleanup 
* 945) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_numeric.py line 912 - taken from tests.series.test_operators; needs cleanup 
* 946) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_numeric.py line 1071 - moved from tests.series.test_operators; needs cleanup 
* 947) venv/lib/python3.6/site-packages/pandas/tests/arithmetic/test_numeric.py line 1126 - mod, divmod? 
* 948) venv/lib/python3.6/site-packages/pandas/tests/reshape/test_concat.py line 48 - Replace with sort once keyword changes. 
* 949) venv/lib/python3.6/site-packages/pandas/tests/reshape/test_melt.py line 572 - unused? 
* 950) venv/lib/python3.6/site-packages/pandas/tests/reshape/merge/test_merge.py line 1363 - check_names on merge? 
* 951) venv/lib/python3.6/site-packages/pandas/tests/reshape/merge/test_merge.py line 2020 - might reconsider current raise behaviour, see issue 24782 
* 952) venv/lib/python3.6/site-packages/pandas/tests/reshape/merge/test_merge.py line 2032 - might reconsider current raise behaviour, see GH24782 
* 953) venv/lib/python3.6/site-packages/pandas/tests/resample/test_resample_api.py line 257 - once GH 14008 is fixed, move these tests into 
* 954) venv/lib/python3.6/site-packages/pandas/tests/resample/test_base.py line 185 - fix resample w/ TimedeltaIndex 
* 955) venv/lib/python3.6/site-packages/pandas/tests/io/test_feather.py line 114 - make the warning work with check_stacklevel=True 
* 956) venv/lib/python3.6/site-packages/pandas/tests/io/test_feather.py line 120 - make the warning work with check_stacklevel=True 
* 957) venv/lib/python3.6/site-packages/pandas/tests/io/parser/test_common.py line 930 - FTP testing 
* 958) venv/lib/python3.6/site-packages/pandas/tests/io/parser/test_mangle_dupes.py line 16 - add test for condition "mangle_dupe_cols=False" 
* 959) venv/lib/python3.6/site-packages/pandas/tests/io/formats/test_console.py line 6 - (py27): replace with mock 
* 960) venv/lib/python3.6/site-packages/pandas/tests/io/formats/test_to_html.py line 275 - split this test 
* 961) venv/lib/python3.6/site-packages/pandas/tests/io/formats/test_to_html.py line 368 - split this test 
* 962) venv/lib/python3.6/site-packages/pandas/tests/io/formats/test_css.py line 63 - we should be checking that in other cases no warnings are raised 
* 963) venv/lib/python3.6/site-packages/pandas/tests/io/excel/test_readers.py line 109 - add index to xls file) 
* 964) venv/lib/python3.6/site-packages/pandas/tests/io/excel/test_readers.py line 123 - add index to xls file) 
* 965) venv/lib/python3.6/site-packages/pandas/tests/io/excel/test_readers.py line 135 - add index to xls, read xls ignores index name ? 
* 966) venv/lib/python3.6/site-packages/pandas/tests/io/excel/test_readers.py line 144 - add index to xls file 
* 967) venv/lib/python3.6/site-packages/pandas/tests/io/excel/test_readers.py line 255 - add index to file 
* 968) venv/lib/python3.6/site-packages/pandas/tests/io/excel/test_readers.py line 503 - remove once on master 
* 969) venv/lib/python3.6/site-packages/pandas/tests/io/excel/test_xlrd.py line 37 - test for openpyxl as well 
* 970) venv/lib/python3.6/site-packages/pandas/tests/io/json/test_json_table_schema.py line 177 - datedate.date? datetime.time? 
* 971) venv/lib/python3.6/site-packages/pandas/tests/io/json/test_json_table_schema.py line 184 -  
* 972) venv/lib/python3.6/site-packages/pandas/tests/io/json/test_json_table_schema.py line 189 - I think before is_categorical_dtype(Categorical) 
* 973) venv/lib/python3.6/site-packages/pandas/tests/io/json/test_pandas.py line 183 - not executed. fix this. 
* 974) venv/lib/python3.6/site-packages/pandas/tests/io/json/test_pandas.py line 1435 - there is a near-identical test for pytables; can we share? 
* 975) venv/lib/python3.6/site-packages/pandas/tests/io/pytables/test_pytables.py line 54 -  
* 976) venv/lib/python3.6/site-packages/pandas/tests/tools/test_numeric.py line 399 - PeriodDtype, so support it in to_numeric. 
* 977) venv/lib/python3.6/site-packages/pandas/tests/scalar/timedelta/test_timedelta.py line 783 - unused? 
* 978) venv/lib/python3.6/site-packages/pandas/tests/scalar/timedelta/test_arithmetic.py line 494 - GH-19761. Change to TypeError. 
* 979) venv/lib/python3.6/site-packages/pandas/tests/scalar/period/test_asfreq.py line 425 - unused? 
* 980) venv/lib/python3.6/site-packages/pandas/tests/groupby/test_function.py line 174 - min, max *should* handle 
* 981) venv/lib/python3.6/site-packages/pandas/tests/groupby/test_groupby.py line 471 - groupby get drops names 
* 982) venv/lib/python3.6/site-packages/pandas/tests/groupby/test_groupby.py line 1122 - Ensure warning isn't emitted in the first place 
* 983) venv/lib/python3.6/site-packages/pandas/tests/groupby/test_grouping.py line 693 - should prob allow a str of Interval work as well 
* 984) venv/lib/python3.6/site-packages/pandas/tests/groupby/test_whitelist.py line 337 - check groupby with > 1 col ? 
* 985) venv/lib/python3.6/site-packages/pandas/tests/groupby/aggregate/test_aggregate.py line 36 - (wesm): unused 
* 986) venv/lib/python3.6/site-packages/pandas/tests/groupby/aggregate/test_aggregate.py line 444 - we currently raise on multiple lambdas. We could *maybe* 
* 987) venv/lib/python3.6/site-packages/pandas/tests/arrays/test_datetimes.py line 111 - merge this into tests/arithmetic/test_datetime64 once it is 
* 988) venv/lib/python3.6/site-packages/pandas/tests/arrays/test_datetimes.py line 134 - add list and tuple, and object-dtype once those 
* 989) venv/lib/python3.6/site-packages/pandas/tests/arrays/test_integer.py line 319 - (extension) 
* 990) venv/lib/python3.6/site-packages/pandas/tests/arrays/test_integer.py line 689 - (#22346): preserve Int64 dtype 
* 991) venv/lib/python3.6/site-packages/pandas/tests/arrays/test_integer.py line 812 - (jreback) - these need testing / are broken 
* 992) venv/lib/python3.6/site-packages/pandas/tests/arrays/test_datetimelike.py line 11 - more freq variants 
* 993) venv/lib/python3.6/site-packages/pandas/tests/arrays/test_datetimelike.py line 22 - non-monotone indexes; NaTs, different start dates 
* 994) venv/lib/python3.6/site-packages/pandas/tests/arrays/test_datetimelike.py line 37 - non-monotone indexes; NaTs, different start dates, timezones 
* 995) venv/lib/python3.6/site-packages/pandas/tests/arrays/test_datetimelike.py line 50 - flesh this out 
* 996) venv/lib/python3.6/site-packages/pandas/tests/arrays/test_timedeltas.py line 42 - why TypeError for 'category' but ValueError for i8? 
* 997) venv/lib/python3.6/site-packages/pandas/tests/arrays/categorical/test_repr.py line 150 - (wesm): exceeding 80 characters in the console is not good 
* 998) venv/lib/python3.6/site-packages/pandas/tests/arrays/categorical/test_indexing.py line 265 - (Categorical): identify other places where this may be 
* 999) venv/lib/python3.6/site-packages/pandas/tests/arrays/interval/test_ops.py line 57 - modify this test when implemented 
* 1000) venv/lib/python3.6/site-packages/pandas/tests/arrays/sparse/test_accessor.py line 13 - collect other Series accessor tests 
* 1001) venv/lib/python3.6/site-packages/pandas/tests/arrays/sparse/test_libsparse.py line 448 - index variables are not used...is that right? 
* 1002) venv/lib/python3.6/site-packages/pandas/tests/reductions/test_reductions.py line 1045 - deprecate numeric_only argument for Categorical and use 
* 1003) venv/lib/python3.6/site-packages/pandas/tests/reductions/test_stat_reductions.py line 46 - flesh this out with different frequencies 
* 1004) venv/lib/python3.6/site-packages/pandas/tests/indexes/test_base.py line 880 - decide on True behaviour 
* 1005) venv/lib/python3.6/site-packages/pandas/tests/indexes/test_base.py line 904 - Replace with fixturesult 
* 1006) venv/lib/python3.6/site-packages/pandas/tests/indexes/test_base.py line 930 - decide on True behaviour 
* 1007) venv/lib/python3.6/site-packages/pandas/tests/indexes/test_base.py line 960 - decide on True behaviour 
* 1008) venv/lib/python3.6/site-packages/pandas/tests/indexes/test_base.py line 970 - Replace with fixturesult 
* 1009) venv/lib/python3.6/site-packages/pandas/tests/indexes/test_base.py line 983 - replace with fixturesult 
* 1010) venv/lib/python3.6/site-packages/pandas/tests/indexes/test_base.py line 1023 - Replace with fixturesult 
* 1011) venv/lib/python3.6/site-packages/pandas/tests/indexes/test_base.py line 1050 - replace with fixture 
* 1012) venv/lib/python3.6/site-packages/pandas/tests/indexes/test_base.py line 1106 - replace with fixture 
* 1013) venv/lib/python3.6/site-packages/pandas/tests/indexes/test_base.py line 1173 - replace with fixturesult 
* 1014) venv/lib/python3.6/site-packages/pandas/tests/indexes/test_base.py line 1259 - decide on True behaviour 
* 1015) venv/lib/python3.6/site-packages/pandas/tests/indexes/test_base.py line 1442 - make this a dedicated test with parametrized methods 
* 1016) venv/lib/python3.6/site-packages/pandas/tests/indexes/test_base.py line 1770 - Parametrize these after replacing self.strIndex with fixture 
* 1017) venv/lib/python3.6/site-packages/pandas/tests/indexes/test_base.py line 1788 - Parametrize these after replacing self.strIndex with fixture 
* 1018) venv/lib/python3.6/site-packages/pandas/tests/indexes/test_base.py line 1804 - Parametrize numeric and str tests after self.strIndex fixture 
* 1019) venv/lib/python3.6/site-packages/pandas/tests/indexes/test_base.py line 1912 - Remove function? GH 19728 
* 1020) venv/lib/python3.6/site-packages/pandas/tests/indexes/period/test_indexing.py line 570 - This method came from test_period; de-dup with version above 
* 1021) venv/lib/python3.6/site-packages/pandas/tests/indexes/period/test_indexing.py line 618 - This method came from test_period; de-dup with version above 
* 1022) venv/lib/python3.6/site-packages/pandas/tests/indexes/period/test_astype.py line 66 - de-duplicate this version (from test_ops) with the one above 
* 1023) venv/lib/python3.6/site-packages/pandas/tests/indexes/timedeltas/test_indexing.py line 118 - This method came from test_timedelta; de-dup with version above 
* 1024) venv/lib/python3.6/site-packages/pandas/tests/indexes/timedeltas/test_arithmetic.py line 206 - after #24365 this probably belongs in scalar tests 
* 1025) venv/lib/python3.6/site-packages/pandas/tests/indexes/timedeltas/test_ops.py line 127 - (wesm): unused? 
* 1026) venv/lib/python3.6/site-packages/pandas/tests/indexes/interval/test_interval_new.py line 288 - we may also want to test get_indexer for the case when 
* 1027) venv/lib/python3.6/site-packages/pandas/tests/indexes/interval/test_setops.py line 161 - standardize return type of non-union setops type(self vs other) 
* 1028) venv/lib/python3.6/site-packages/pandas/tests/indexes/multi/test_integrity.py line 52 - (GH-24559): Remove the FutureWarning 
* 1029) venv/lib/python3.6/site-packages/pandas/tests/indexes/multi/test_missing.py line 15 - Remove or Refactor.  Not Implemented for MultiIndex 
* 1030) venv/lib/python3.6/site-packages/pandas/tests/indexes/multi/test_indexing.py line 69 - Try creating a UnicodeDecodeError in exception message 
* 1031) venv/lib/python3.6/site-packages/pandas/tests/indexes/multi/test_set_ops.py line 196 - decide on True behaviour 
* 1032) venv/lib/python3.6/site-packages/pandas/tests/indexes/multi/test_set_ops.py line 221 - decide on True behaviour 
* 1033) venv/lib/python3.6/site-packages/pandas/tests/indexes/multi/test_set_ops.py line 301 - decide on True behaviour 
* 1034) venv/lib/python3.6/site-packages/pandas/tests/indexes/multi/test_set_ops.py line 324 - decide on True behaviour 
* 1035) venv/lib/python3.6/site-packages/pandas/tests/indexes/multi/test_set_ops.py line 348 - decide on True behaviour 
* 1036) venv/lib/python3.6/site-packages/pandas/tests/indexes/multi/test_analytics.py line 77 - reshape 
* 1037) venv/lib/python3.6/site-packages/pandas/tests/indexes/multi/test_analytics.py line 155 - Remove Commented Code 
* 1038) venv/lib/python3.6/site-packages/pandas/tests/indexes/datetimes/test_timezones.py line 565 - belongs outside tz_localize tests? 
* 1039) venv/lib/python3.6/site-packages/pandas/tests/indexes/datetimes/test_indexing.py line 220 - This method came from test_datetime; de-dup with version above 
* 1040) venv/lib/python3.6/site-packages/pandas/tests/indexes/datetimes/test_setops.py line 36 - moved from test_datetimelike; dedup with version below 
* 1041) venv/lib/python3.6/site-packages/pandas/tests/indexes/datetimes/test_setops.py line 186 - moved from test_datetimelike; de-duplicate with version below 
* 1042) venv/lib/python3.6/site-packages/pandas/tests/indexes/datetimes/test_construction.py line 42 - parametrize over DatetimeIndex/DatetimeArray 
* 1043) venv/lib/python3.6/site-packages/pandas/tests/indexes/datetimes/test_construction.py line 737 - (GH-24559): Remove the xfail for the tz-aware case. 
* 1044) venv/lib/python3.6/site-packages/pandas/tests/indexes/datetimes/test_construction.py line 768 - (GH-24559): Remove xfail 
* 1045) venv/lib/python3.6/site-packages/pandas/tests/extension/test_integer.py line 116 - see https://github.com/pandas-dev/pandas/issues/22023 
* 1046) venv/lib/python3.6/site-packages/pandas/tests/extension/test_integer.py line 134 - reverse operators result in object dtype 
* 1047) venv/lib/python3.6/site-packages/pandas/tests/extension/test_integer.py line 137 - reverse operators result in object dtype 
* 1048) venv/lib/python3.6/site-packages/pandas/tests/extension/test_integer.py line 146 - pow on Int arrays gives different result with NA 
* 1049) venv/lib/python3.6/site-packages/pandas/tests/extension/test_integer.py line 185 - (jreback) once integrated this would 
* 1050) venv/lib/python3.6/site-packages/pandas/tests/extension/test_sparse.py line 294 - (SparseArray.__setitem__ will preserve dtype.") 
* 1051) venv/lib/python3.6/site-packages/pandas/tests/extension/test_numpy.py line 191 - remove?") 
* 1052) venv/lib/python3.6/site-packages/pandas/tests/extension/test_categorical.py line 114 - remove this once Categorical.take is fixed 
* 1053) venv/lib/python3.6/site-packages/pandas/tests/extension/json/test_json.py line 199 - (EA.factorize): see if _values_for_factorize allows this. 
* 1054) venv/lib/python3.6/site-packages/pandas/tests/extension/json/array.py line 189 - Use a regular dict. See _NDFrameIndexer._setitem_with_indexer 
* 1055) venv/lib/python3.6/site-packages/pandas/tests/extension/decimal/test_decimal.py line 92 - (EA): select_dtypes 
* 1056) venv/lib/python3.6/site-packages/pandas/tests/extension/decimal/test_decimal.py line 207 - (extension) 
* 1057) venv/lib/python3.6/site-packages/pandas/tests/window/test_moments.py line 2269 - xref gh-15826 
* 1058) venv/lib/python3.6/site-packages/pandas/tests/window/test_moments.py line 2384 - (jreback), needed to add preserve_nan=False 
* 1059) venv/lib/python3.6/site-packages/pandas/tests/tseries/offsets/test_offsets.py line 68 - Remove: This is not used outside of tests 
* 1060) venv/lib/python3.6/site-packages/pandas/tests/tseries/offsets/test_offsets_properties.py line 45 - Choose the min/max values more systematically 
* 1061) venv/lib/python3.6/site-packages/pandas/tests/tseries/offsets/test_offsets_properties.py line 108 - test for that case separately 
* 1062) venv/lib/python3.6/site-packages/pandas/tests/tseries/offsets/test_offsets_properties.py line 124 - Check randomly assorted entries, not just first/last 
* 1063) venv/lib/python3.6/site-packages/pandas/tests/tseries/offsets/test_offsets_properties.py line 127 - reason? 
* 1064) venv/lib/python3.6/site-packages/pandas/tests/plotting/test_datetimelike.py line 712 -  
* 1065) venv/lib/python3.6/site-packages/pandas/tests/plotting/test_datetimelike.py line 863 - (GH14330, GH14322) 
* 1066) venv/lib/python3.6/site-packages/pandas/tests/plotting/test_datetimelike.py line 1209 - color cycle problems 
* 1067) venv/lib/python3.6/site-packages/pandas/tests/plotting/test_datetimelike.py line 1249 - color cycle problems 
* 1068) venv/lib/python3.6/site-packages/pandas/tests/plotting/test_datetimelike.py line 1265 - color cycle problems 
* 1069) venv/lib/python3.6/site-packages/pandas/tests/plotting/test_datetimelike.py line 1279 - color cycle problems 
* 1070) venv/lib/python3.6/site-packages/pandas/tests/plotting/test_datetimelike.py line 1569 - (statsmodels 0.10.0): Remove the statsmodels check 
* 1071) venv/lib/python3.6/site-packages/pandas/tests/plotting/test_backend.py line 59 - the docs recommend importlib.util.module_from_spec. But this works for now. 
* 1072) venv/lib/python3.6/site-packages/pandas/tests/plotting/test_backend.py line 65 - https://github.com/pandas-dev/pandas/issues/27517 
* 1073) venv/lib/python3.6/site-packages/pandas/tests/plotting/test_frame.py line 250 - add MultiIndex test 
* 1074) venv/lib/python3.6/site-packages/pandas/tests/plotting/test_frame.py line 2243 - outside this func? 
* 1075) venv/lib/python3.6/site-packages/pandas/tests/plotting/test_frame.py line 2427 - need better way to test. This just does existence. 
* 1076) venv/lib/python3.6/site-packages/pandas/tests/internals/test_internals.py line 278 - merge with mixed type? 
* 1077) venv/lib/python3.6/site-packages/pandas/tests/internals/test_internals.py line 703 - should this be pytest.skip? 
* 1078) venv/lib/python3.6/site-packages/pandas/tests/dtypes/test_common.py line 493 - (jreback), this is slightly suspect 
* 1079) venv/lib/python3.6/site-packages/pandas/tests/dtypes/test_dtypes.py line 70 - (GH 26403): Remove when default ordered becomes False 
* 1080) venv/lib/python3.6/site-packages/pandas/tests/series/test_combine_concat.py line 277 - move? 
* 1081) venv/lib/python3.6/site-packages/pandas/tests/series/test_combine_concat.py line 290 - release-note: concat sparse dtype 
* 1082) venv/lib/python3.6/site-packages/pandas/tests/series/test_combine_concat.py line 301 - release-note: concat sparse dtype 
* 1083) venv/lib/python3.6/site-packages/pandas/tests/series/test_timezones.py line 260 - De-duplicate with test below 
* 1084) venv/lib/python3.6/site-packages/pandas/tests/series/test_missing.py line 999 - what is this test doing? why are result an expected 
* 1085) venv/lib/python3.6/site-packages/pandas/tests/series/test_missing.py line 1004 - release-note fillna performance warning 
* 1086) venv/lib/python3.6/site-packages/pandas/tests/series/test_operators.py line 48 - unused 
* 1087) venv/lib/python3.6/site-packages/pandas/tests/series/test_operators.py line 158 - Fix this exception - needs to be fixed! (see GH5035) 
* 1088) venv/lib/python3.6/site-packages/pandas/tests/series/test_operators.py line 681 - this returned NotImplemented earlier, what to do? 
* 1089) venv/lib/python3.6/site-packages/pandas/tests/series/indexing/test_datetime.py line 634 - unused? 
* 1090) venv/lib/python3.6/site-packages/pandas/tests/series/indexing/test_indexing.py line 733 - unused 
* 1091) venv/lib/python3.6/site-packages/pandas/tests/sparse/series/test_series.py line 719 - sp_zero is not used anywhere...remove? 
* 1092) venv/lib/python3.6/site-packages/pandas/tests/sparse/series/test_series.py line 750 - expected is not used anywhere...remove? 
* 1093) venv/lib/python3.6/site-packages/pandas/tests/sparse/series/test_series.py line 783 - These aren't used 
* 1094) venv/lib/python3.6/site-packages/pandas/tests/sparse/frame/test_apply.py line 94 - no non-unique columns supported in sparse yet 
* 1095) venv/lib/python3.6/site-packages/pandas/tests/sparse/frame/test_frame.py line 119 - test data is copied from inputs 
* 1096) venv/lib/python3.6/site-packages/pandas/tests/sparse/frame/test_frame.py line 210 - x_sparse is unused...fix 
* 1097) venv/lib/python3.6/site-packages/pandas/tests/sparse/frame/test_frame.py line 217 - y_sparse is unsused...fix 
* 1098) venv/lib/python3.6/site-packages/pandas/tests/frame/test_join.py line 140 - should this check_names ? 
* 1099) venv/lib/python3.6/site-packages/pandas/tests/frame/test_constructors.py line 86 - (wesm), incomplete test? 
* 1100) venv/lib/python3.6/site-packages/pandas/tests/frame/test_constructors.py line 2022 - (wesm): unused 
* 1101) venv/lib/python3.6/site-packages/pandas/tests/frame/test_missing.py line 239 - make stronger assertion here, GH 25640 
* 1102) venv/lib/python3.6/site-packages/pandas/tests/frame/test_missing.py line 712 - (wesm): unused? 
* 1103) venv/lib/python3.6/site-packages/pandas/tests/frame/test_repr_info.py line 133 - (wesm): is this supposed to be used? 
* 1104) venv/lib/python3.6/site-packages/pandas/tests/frame/test_to_csv.py line 150 - remove renaming when GH 10875 is solved 
* 1105) venv/lib/python3.6/site-packages/pandas/tests/frame/test_to_csv.py line 507 - to_csv drops column name 
* 1106) venv/lib/python3.6/site-packages/pandas/tests/frame/test_to_csv.py line 523 - to_csv drops column name 
* 1107) venv/lib/python3.6/site-packages/pandas/tests/frame/test_to_csv.py line 584 - to_csv drops column name 
* 1108) venv/lib/python3.6/site-packages/pandas/tests/frame/test_to_csv.py line 600 - to_csv drops column name 
* 1109) venv/lib/python3.6/site-packages/pandas/tests/frame/test_to_csv.py line 883 - to_csv drops column name 
* 1110) venv/lib/python3.6/site-packages/pandas/tests/frame/test_block_internals.py line 411 - (wesm): unused? 
* 1111) venv/lib/python3.6/site-packages/pandas/tests/frame/test_operators.py line 201 - belongs elsewhere 
* 1112) venv/lib/python3.6/site-packages/pandas/tests/frame/test_operators.py line 251 - not sure what's correct here. 
* 1113) venv/lib/python3.6/site-packages/pandas/tests/frame/test_arithmetic.py line 149 - test_bool_flex_frame needs a better name 
* 1114) venv/lib/python3.6/site-packages/pandas/tests/frame/test_axis_select_reindex.py line 598 - (wesm): unused? 
* 1115) venv/lib/python3.6/site-packages/pandas/tests/frame/test_timeseries.py line 520 - actually check that this worked. 
* 1116) venv/lib/python3.6/site-packages/pandas/tests/frame/test_timeseries.py line 946 - untested 
* 1117) venv/lib/python3.6/site-packages/pandas/tests/frame/test_alter_axes.py line 1020 - should reset_index check_names ? 
* 1118) venv/lib/python3.6/site-packages/pandas/tests/frame/test_analytics.py line 972 - Ensure warning isn't emitted in the first place 
* 1119) venv/lib/python3.6/site-packages/pandas/tests/frame/test_analytics.py line 2142 - (wesm): unused? 
* 1120) venv/lib/python3.6/site-packages/pandas/tests/frame/test_analytics.py line 2306 - (jreback) 
* 1121) venv/lib/python3.6/site-packages/pandas/tests/frame/test_analytics.py line 2464 - (wesm): unused 
* 1122) venv/lib/python3.6/site-packages/pandas/tests/frame/test_dtypes.py line 576 - (wesm): verification? 
* 1123) venv/lib/python3.6/site-packages/pandas/compat/pickle_compat.py line 63 - When FrozenNDArray is removed, add 
* 1124) venv/lib/python3.6/site-packages/pandas/util/testing.py line 1191 - Use .array 
* 1125) venv/lib/python3.6/site-packages/pandas/util/_validators.py line 275 - Change to keyword-only args and remove all this 
* 1126) venv/lib/python3.6/site-packages/pandas/tseries/offsets.py line 367 - Does this make sense for the general case?  It would help 
* 1127) venv/lib/python3.6/site-packages/pandas/tseries/offsets.py line 371 - Combine this with BusinessMixin version by defining a whitelisted 
* 1128) venv/lib/python3.6/site-packages/pandas/tseries/offsets.py line 460 - standardize `_offset` vs `offset` naming convention 
* 1129) venv/lib/python3.6/site-packages/pandas/tseries/offsets.py line 1138 - going through __new__ raises on call to _validate_frequency; 
* 1130) venv/lib/python3.6/site-packages/pandas/tseries/offsets.py line 1732 - handle n here... 
* 1131) venv/lib/python3.6/site-packages/pandas/tseries/offsets.py line 1803 - handle n here... 
* 1132) venv/lib/python3.6/site-packages/pandas/tseries/offsets.py line 1821 - Consider combining QuarterOffset and YearOffset __init__ at some 
* 1133) venv/lib/python3.6/site-packages/pandas/tseries/offsets.py line 1875 - going through __new__ raises on call to _validate_frequency; 
* 1134) venv/lib/python3.6/site-packages/pandas/tseries/offsets.py line 1898 - This is basically the same as BQuarterEnd 
* 1135) venv/lib/python3.6/site-packages/pandas/tseries/offsets.py line 1945 - there may be a more performant way to do this 
* 1136) venv/lib/python3.6/site-packages/pandas/tseries/offsets.py line 1961 - going through __new__ raises on call to _validate_frequency; 
* 1137) venv/lib/python3.6/site-packages/pandas/tseries/offsets.py line 2475 - Why does this handle the 0 case the opposite of others? 
* 1138) venv/lib/python3.6/site-packages/pandas/tseries/offsets.py line 2601 - Should Tick have its own apply_index? 
* 1139) venv/lib/python3.6/site-packages/pandas/tseries/converter.py line 4 - `_matplotlib` module should be private, so the plotting backend 
* 1140) venv/lib/python3.6/site-packages/pandas/plotting/_matplotlib/core.py line 255 - unused? 
* 1141) venv/lib/python3.6/site-packages/pandas/plotting/_matplotlib/core.py line 311 - use Matplotlib public API when available 
* 1142) venv/lib/python3.6/site-packages/pandas/plotting/_matplotlib/timeseries.py line 1 - Use the fact that axis can have units to simplify the process 
* 1143) venv/lib/python3.6/site-packages/pandas/plotting/_matplotlib/converter.py line 385 - (wesm) unused? 
* 1144) venv/lib/python3.6/site-packages/pandas/plotting/_matplotlib/converter.py line 451 - (wesm): unused? 
* 1145) venv/lib/python3.6/site-packages/pandas/plotting/_matplotlib/converter.py line 817 - Check the following : is it really info['fmt'] ? 
* 1146) venv/lib/python3.6/site-packages/pandas/core/frame.py line 1177 - speed up Series case 
* 1147) venv/lib/python3.6/site-packages/pandas/core/frame.py line 2316 - a generic formatter wld b in DataFrameFormatter 
* 1148) venv/lib/python3.6/site-packages/pandas/core/frame.py line 4632 - (https://github.com/pandas-dev/pandas/issues/24206) 
* 1149) venv/lib/python3.6/site-packages/pandas/core/frame.py line 5025 - this can be combined with Series.sort_index impl as 
* 1150) venv/lib/python3.6/site-packages/pandas/core/frame.py line 5769 - Support other joins 
* 1151) venv/lib/python3.6/site-packages/pandas/core/frame.py line 6622 - _shallow_copy(subset)? 
* 1152) venv/lib/python3.6/site-packages/pandas/core/frame.py line 7887 - Make other agg func handle axis=None properly 
* 1153) venv/lib/python3.6/site-packages/pandas/core/frame.py line 7913 - combine with hasattr(result, 'dtype') further down 
* 1154) venv/lib/python3.6/site-packages/pandas/core/frame.py line 8483 - this should be seriously cythonized 
* 1155) venv/lib/python3.6/site-packages/pandas/core/window.py line 1085 - default is for backward compat 
* 1156) venv/lib/python3.6/site-packages/pandas/core/missing.py line 500 - for int-dtypes we make a copy, but for everything else this 
* 1157) venv/lib/python3.6/site-packages/pandas/core/nanops.py line 107 - (GH-18976) update all the nanops methods to 
* 1158) venv/lib/python3.6/site-packages/pandas/core/nanops.py line 341 - what about datetime64tz?  PeriodDtype? 
* 1159) venv/lib/python3.6/site-packages/pandas/core/apply.py line 228 - mixed type case 
* 1160) venv/lib/python3.6/site-packages/pandas/core/base.py line 1007 - (GH-24345): Avoid potential double copy 
* 1161) venv/lib/python3.6/site-packages/pandas/core/api.py line 48 - Remove import when statsmodels updates #18264 
* 1162) venv/lib/python3.6/site-packages/pandas/core/generic.py line 4469 - Decide if we care about having different examples for different 
* 1163) venv/lib/python3.6/site-packages/pandas/core/generic.py line 4570 - speed up on homogeneous DataFrame objects 
* 1164) venv/lib/python3.6/site-packages/pandas/core/generic.py line 10423 - Not sure if above is correct - need someone to confirm. 
* 1165) venv/lib/python3.6/site-packages/pandas/core/algorithms.py line 69 - this should be uint8) 
* 1166) venv/lib/python3.6/site-packages/pandas/core/algorithms.py line 92 - ) 
* 1167) venv/lib/python3.6/site-packages/pandas/core/algorithms.py line 446 - (extension) 
* 1168) venv/lib/python3.6/site-packages/pandas/core/algorithms.py line 800 - handle uint8 
* 1169) venv/lib/python3.6/site-packages/pandas/core/algorithms.py line 1647 - (EA): Remove these if / elifs as datetimeTZ, interval, become EAs 
* 1170) venv/lib/python3.6/site-packages/pandas/core/common.py line 257 - verify whether any path hits this except #18819 (invalid) 
* 1171) venv/lib/python3.6/site-packages/pandas/core/common.py line 325 - used only once in indexing; belongs elsewhere? 
* 1172) venv/lib/python3.6/site-packages/pandas/core/indexing.py line 129 - (ix): most/all of the TypeError cases here are for ix, 
* 1173) venv/lib/python3.6/site-packages/pandas/core/indexing.py line 134 - The AttributeError is for IntervalIndex which 
* 1174) venv/lib/python3.6/site-packages/pandas/core/indexing.py line 580 - (EA): ExtensionBlock.setitem this causes issues with 
* 1175) venv/lib/python3.6/site-packages/pandas/core/series.py line 218 - Remove after CategoricalDtype defaults to ordered=False 
* 1176) venv/lib/python3.6/site-packages/pandas/core/series.py line 244 - See if we can avoid these copies 
* 1177) venv/lib/python3.6/site-packages/pandas/core/series.py line 803 - handle DataFrame 
* 1178) venv/lib/python3.6/site-packages/pandas/core/series.py line 834 - dataframe 
* 1179) venv/lib/python3.6/site-packages/pandas/core/series.py line 1865 - integrate bottleneck 
* 1180) venv/lib/python3.6/site-packages/pandas/core/series.py line 1924 - Add option for bins like value_counts() 
* 1181) venv/lib/python3.6/site-packages/pandas/core/series.py line 3318 - this can be combined with DataFrame.sort_index impl as 
* 1182) venv/lib/python3.6/site-packages/pandas/core/series.py line 4066 - deprecate numeric_only argument for Categorical and use 
* 1183) venv/lib/python3.6/site-packages/pandas/core/series.py line 4077 - remove hasattr check after TimedeltaIndex has `std` method 
* 1184) venv/lib/python3.6/site-packages/pandas/core/series.py line 4089 - (EA) dispatch to Index 
* 1185) venv/lib/python3.6/site-packages/pandas/core/series.py line 4436 - remove when the default Categorical.take behavior changes 
* 1186) venv/lib/python3.6/site-packages/pandas/core/reshape/melt.py line 30 - what about the existing index? 
* 1187) venv/lib/python3.6/site-packages/pandas/core/reshape/pivot.py line 19 - Fix this dependency 
* 1188) venv/lib/python3.6/site-packages/pandas/core/reshape/merge.py line 147 - , should _merge_pieces do this? 
* 1189) venv/lib/python3.6/site-packages/pandas/core/reshape/merge.py line 544 - transformations?? 
* 1190) venv/lib/python3.6/site-packages/pandas/core/reshape/merge.py line 545 - only copy DataFrames when modification necessary 
* 1191) venv/lib/python3.6/site-packages/pandas/core/reshape/merge.py line 1883 - needs tests for case where lk is integer-dtype 
* 1192) venv/lib/python3.6/site-packages/pandas/core/reshape/merge.py line 1891 - Needs tests for non-matching dtypes 
* 1193) venv/lib/python3.6/site-packages/pandas/core/computation/eval.py line 52 - validate this in a more general way (thinking of future engines 
* 1194) venv/lib/python3.6/site-packages/pandas/core/computation/eval.py line 358 - Filter the warnings we actually care about here. 
* 1195) venv/lib/python3.6/site-packages/pandas/core/groupby/groupby.py line 406 - Better repr for GroupBy object 
* 1196) venv/lib/python3.6/site-packages/pandas/core/groupby/groupby.py line 1264 - implement at Cython level? 
* 1197) venv/lib/python3.6/site-packages/pandas/core/groupby/groupby.py line 1934 - (GH-10710): Ideally, we could write this as 
* 1198) venv/lib/python3.6/site-packages/pandas/core/groupby/generic.py line 57 - (typing) the return value on this callable should be any *scalar*. 
* 1199) venv/lib/python3.6/site-packages/pandas/core/groupby/generic.py line 59 - validate types on ScalarResult and move to _typing 
* 1200) venv/lib/python3.6/site-packages/pandas/core/groupby/generic.py line 135 - the actual managing of mgr_locs is a PITA 
* 1201) venv/lib/python3.6/site-packages/pandas/core/groupby/generic.py line 1224 - should we do this inside II? 
* 1202) venv/lib/python3.6/site-packages/pandas/core/groupby/generic.py line 1339 - Remove this conditional when #23918 is fixed 
* 1203) venv/lib/python3.6/site-packages/pandas/core/groupby/generic.py line 1733 - (Py35): When we drop python 3.5, change this to 
* 1204) venv/lib/python3.6/site-packages/pandas/core/groupby/generic.py line 1735 - aggspec type: typing.OrderedDict[str, List[AggScalar]] 
* 1205) venv/lib/python3.6/site-packages/pandas/core/groupby/generic.py line 1751 - Can't use, because mypy doesn't like us setting __name__ 
* 1206) venv/lib/python3.6/site-packages/pandas/core/groupby/ops.py line 558 - min_count 
* 1207) venv/lib/python3.6/site-packages/pandas/core/groupby/ops.py line 584 -  
* 1208) venv/lib/python3.6/site-packages/pandas/core/groupby/grouper.py line 468 - These if-block and else-block are almost same. 
* 1209) venv/lib/python3.6/site-packages/pandas/core/arrays/timedeltas.py line 997 - watch out for overflows 
* 1210) venv/lib/python3.6/site-packages/pandas/core/arrays/timedeltas.py line 1056 - watch out for overflows when converting from lower-resolution 
* 1211) venv/lib/python3.6/site-packages/pandas/core/arrays/period.py line 568 - remove 
* 1212) venv/lib/python3.6/site-packages/pandas/core/arrays/period.py line 713 - disallow unit-less timedelta64 
* 1213) venv/lib/python3.6/site-packages/pandas/core/arrays/interval.py line 653 - This try/except will be repeated. 
* 1214) venv/lib/python3.6/site-packages/pandas/core/arrays/interval.py line 733 - Could skip verify_integrity here. 
* 1215) venv/lib/python3.6/site-packages/pandas/core/arrays/interval.py line 844 - implement this is a non-naive way! 
* 1216) venv/lib/python3.6/site-packages/pandas/core/arrays/interval.py line 853 - integrate with categorical and make generic 
* 1217) venv/lib/python3.6/site-packages/pandas/core/arrays/sparse.py line 455 - (GH-23092): pass copy=False. Need to fix astype_nansafe 
* 1218) venv/lib/python3.6/site-packages/pandas/core/arrays/sparse.py line 628 - make kind=None, and use data.kind? 
* 1219) venv/lib/python3.6/site-packages/pandas/core/arrays/sparse.py line 666 - disentangle the fill_value dtype inference from 
* 1220) venv/lib/python3.6/site-packages/pandas/core/arrays/sparse.py line 688 - avoid double copy when dtype forces cast. 
* 1221) venv/lib/python3.6/site-packages/pandas/core/arrays/sparse.py line 800 - (SparseArray.__setitem__): remove special cases in 
* 1222) venv/lib/python3.6/site-packages/pandas/core/arrays/sparse.py line 1115 - this logic is surely elsewhere 
* 1223) venv/lib/python3.6/site-packages/pandas/core/arrays/sparse.py line 1116 - this could be more efficient 
* 1224) venv/lib/python3.6/site-packages/pandas/core/arrays/sparse.py line 1120 - I think we can avoid densifying when masking a 
* 1225) venv/lib/python3.6/site-packages/pandas/core/arrays/sparse.py line 1266 - may need to coerce array to fill value 
* 1226) venv/lib/python3.6/site-packages/pandas/core/arrays/sparse.py line 1322 - wraparound 
* 1227) venv/lib/python3.6/site-packages/pandas/core/arrays/sparse.py line 1777 - look into _wrap_result 
* 1228) venv/lib/python3.6/site-packages/pandas/core/arrays/sparse.py line 1813 - make this more flexible than just ndarray... 
* 1229) venv/lib/python3.6/site-packages/pandas/core/arrays/sparse.py line 1932 - copy 
* 1230) venv/lib/python3.6/site-packages/pandas/core/arrays/datetimes.py line 61 - (GH-24559): Remove warning, int_as_wall_time parameter. 
* 1231) venv/lib/python3.6/site-packages/pandas/core/arrays/datetimes.py line 533 - consider re-implementing _cached_range; GH#17914 
* 1232) venv/lib/python3.6/site-packages/pandas/core/arrays/datetimes.py line 1298 - consider privatizing (discussion in GH#23113) 
* 1233) venv/lib/python3.6/site-packages/pandas/core/arrays/datetimes.py line 1857 - We do not have tests specific to string-dtypes, 
* 1234) venv/lib/python3.6/site-packages/pandas/core/arrays/datetimes.py line 1915 - should this be deepcopy? 
* 1235) venv/lib/python3.6/site-packages/pandas/core/arrays/datetimes.py line 2034 - deprecate this behavior to instead treat symmetrically 
* 1236) venv/lib/python3.6/site-packages/pandas/core/arrays/datetimes.py line 2055 - cases where we need to do another pass through this func, 
* 1237) venv/lib/python3.6/site-packages/pandas/core/arrays/datetimes.py line 2062 - We have no tests for these 
* 1238) venv/lib/python3.6/site-packages/pandas/core/arrays/numpy_.py line 257 - (_values_for_fillna): remove this 
* 1239) venv/lib/python3.6/site-packages/pandas/core/arrays/array_.py line 269 - (BooleanArray): handle this type 
* 1240) venv/lib/python3.6/site-packages/pandas/core/arrays/integer.py line 354 - (jreback) make this better 
* 1241) venv/lib/python3.6/site-packages/pandas/core/arrays/integer.py line 437 - (jreback) what if we have a non-na float as a fill value? 
* 1242) venv/lib/python3.6/site-packages/pandas/core/arrays/integer.py line 557 - (extension) 
* 1243) venv/lib/python3.6/site-packages/pandas/core/arrays/integer.py line 565 - (extension) 
* 1244) venv/lib/python3.6/site-packages/pandas/core/arrays/datetimelike.py line 386 - Remove Datetime & DatetimeTZ formatters. 
* 1245) venv/lib/python3.6/site-packages/pandas/core/arrays/datetimelike.py line 715 - (GH-23179): Add ExtensionArray.map 
* 1246) venv/lib/python3.6/site-packages/pandas/core/arrays/datetimelike.py line 771 - (GH-20300): remove this 
* 1247) venv/lib/python3.6/site-packages/pandas/core/arrays/datetimelike.py line 1258 - infer freq? 
* 1248) venv/lib/python3.6/site-packages/pandas/core/arrays/datetimelike.py line 1330 - infer freq? 
* 1249) venv/lib/python3.6/site-packages/pandas/core/arrays/datetimelike.py line 1357 - Can we simplify/generalize these cases at all? 
* 1250) venv/lib/python3.6/site-packages/pandas/core/arrays/datetimelike.py line 1454 - skipna is broken with max. 
* 1251) venv/lib/python3.6/site-packages/pandas/core/ops/__init__.py line 130 - what if they both have np.nan for their names? 
* 1252) venv/lib/python3.6/site-packages/pandas/core/ops/__init__.py line 302 - Why None for mod but '%' for rmod? 
* 1253) venv/lib/python3.6/site-packages/pandas/core/ops/__init__.py line 368 - can we make a no-copy implementation? 
* 1254) venv/lib/python3.6/site-packages/pandas/core/ops/__init__.py line 704 - I don't think the functions defined by bool_method are tested 
* 1255) venv/lib/python3.6/site-packages/pandas/core/ops/__init__.py line 1082 -  
* 1256) venv/lib/python3.6/site-packages/pandas/core/ops/__init__.py line 1134 - same for tuples? 
* 1257) venv/lib/python3.6/site-packages/pandas/core/ops/__init__.py line 1310 - Can we do this before the is_integer_dtype check? 
* 1258) venv/lib/python3.6/site-packages/pandas/core/ops/__init__.py line 1611 - This should be moved to the array? 
* 1259) venv/lib/python3.6/site-packages/pandas/core/indexes/period.py line 252 - We can do some of these with no-copy / coercion? 
* 1260) venv/lib/python3.6/site-packages/pandas/core/indexes/period.py line 281 - raising on floats is tested, but maybe not useful. 
* 1261) venv/lib/python3.6/site-packages/pandas/core/indexes/period.py line 316 - When this deprecation is enforced, PeriodIndex.freq can 
* 1262) venv/lib/python3.6/site-packages/pandas/core/indexes/period.py line 329 - simplify, figure out type of values 
* 1263) venv/lib/python3.6/site-packages/pandas/core/indexes/period.py line 364 - (DatetimeArray): Avoid double-boxing 
* 1264) venv/lib/python3.6/site-packages/pandas/core/indexes/period.py line 549 - should probably raise on `how` here, so we don't ignore it. 
* 1265) venv/lib/python3.6/site-packages/pandas/core/indexes/period.py line 946 - (DatetimeArray): remove 
* 1266) venv/lib/python3.6/site-packages/pandas/core/indexes/frozen.py line 71 - Consider deprecating these in favor of `union` (xref gh-15506) 
* 1267) venv/lib/python3.6/site-packages/pandas/core/indexes/category.py line 561 - Investigate an alternative implementation with 
* 1268) venv/lib/python3.6/site-packages/pandas/core/indexes/range.py line 777 - Do attrs get handled reliably? 
* 1269) venv/lib/python3.6/site-packages/pandas/core/indexes/base.py line 123 - docstring? 
* 1270) venv/lib/python3.6/site-packages/pandas/core/indexes/base.py line 160 - docstring? 
* 1271) venv/lib/python3.6/site-packages/pandas/core/indexes/base.py line 833 - (GH-24559): Remove this block, use the following elif. 
* 1272) venv/lib/python3.6/site-packages/pandas/core/indexes/base.py line 2547 - (EA): setops-refactor, clean all this up 
* 1273) venv/lib/python3.6/site-packages/pandas/core/indexes/base.py line 2632 - standardize return type of non-union setops type(self vs other) 
* 1274) venv/lib/python3.6/site-packages/pandas/core/indexes/base.py line 2647 - (EA): setops-refactor, clean all this up 
* 1275) venv/lib/python3.6/site-packages/pandas/core/indexes/base.py line 3591 - sort=False here for backwards compat. It may 
* 1276) venv/lib/python3.6/site-packages/pandas/core/indexes/base.py line 3595 - sort=True here for backwards compat. It may 
* 1277) venv/lib/python3.6/site-packages/pandas/core/indexes/base.py line 3925 - (EA): remove index types as they become extension arrays 
* 1278) venv/lib/python3.6/site-packages/pandas/core/indexes/base.py line 4847 - if we are a MultiIndex, we can do better 
* 1279) venv/lib/python3.6/site-packages/pandas/core/indexes/base.py line 5495 - rmod? rdivmod? 
* 1280) venv/lib/python3.6/site-packages/pandas/core/indexes/api.py line 40 - there are many places that rely on these private methods existing in 
* 1281) venv/lib/python3.6/site-packages/pandas/core/indexes/api.py line 129 - handle index names! 
* 1282) venv/lib/python3.6/site-packages/pandas/core/indexes/api.py line 214 - remove once pd.concat sort default changes 
* 1283) venv/lib/python3.6/site-packages/pandas/core/indexes/interval.py line 1116 - integrate with categorical and make generic 
* 1284) venv/lib/python3.6/site-packages/pandas/core/indexes/interval.py line 1294 - arithmetic operations 
* 1285) venv/lib/python3.6/site-packages/pandas/core/indexes/accessors.py line 52 - use to_period_array 
* 1286) venv/lib/python3.6/site-packages/pandas/core/indexes/datetimes.py line 59 - If we knew what was going in to **d, we might be able to 
* 1287) venv/lib/python3.6/site-packages/pandas/core/indexes/datetimes.py line 522 - we shouldn't be setting attributes like this; 
* 1288) venv/lib/python3.6/site-packages/pandas/core/indexes/datetimes.py line 556 - we shouldn't be setting attributes like this; 
* 1289) venv/lib/python3.6/site-packages/pandas/core/indexes/datetimes.py line 622 - consider re-implementing freq._should_cache for fastpath 
* 1290) venv/lib/python3.6/site-packages/pandas/core/indexes/numeric.py line 373 - (jreback); this can change once we have an EA Index type 
* 1291) venv/lib/python3.6/site-packages/pandas/core/indexes/multi.py line 1484 - what if a level contains tuples?? 
* 1292) venv/lib/python3.6/site-packages/pandas/core/indexes/multi.py line 3215 - Index.union returns other when `len(self)` is 0. 
* 1293) venv/lib/python3.6/site-packages/pandas/core/util/hashing.py line 230 - GH 15362 
* 1294) venv/lib/python3.6/site-packages/pandas/core/internals/managers.py line 60 - flexible with index=None and/or items=None 
* 1295) venv/lib/python3.6/site-packages/pandas/core/internals/managers.py line 416 - (EA): may interfere with ExtensionBlock.setitem for blocks 
* 1296) venv/lib/python3.6/site-packages/pandas/core/internals/managers.py line 622 - assert/validate that `d` is always a scalar? 
* 1297) venv/lib/python3.6/site-packages/pandas/core/internals/managers.py line 815 - (Block.get_values): Make DatetimeTZBlock.get_values 
* 1298) venv/lib/python3.6/site-packages/pandas/core/internals/managers.py line 833 - https://github.com/pandas-dev/pandas/issues/22791 
* 1299) venv/lib/python3.6/site-packages/pandas/core/internals/managers.py line 1039 - (EA): Remove an is_extension_ when all extension types satisfy 
* 1300) venv/lib/python3.6/site-packages/pandas/core/internals/managers.py line 1364 - infer dtypes other than float64 from fill_value 
* 1301) venv/lib/python3.6/site-packages/pandas/core/internals/construction.py line 202 - What about re-joining object columns? 
* 1302) venv/lib/python3.6/site-packages/pandas/core/internals/construction.py line 250 - See if we can avoid these copies 
* 1303) venv/lib/python3.6/site-packages/pandas/core/internals/concat.py line 1 - Needs a better name; too many modules are already called "concat" 
* 1304) venv/lib/python3.6/site-packages/pandas/core/internals/concat.py line 404 - should this be ju.block._can_hold_na? 
* 1305) venv/lib/python3.6/site-packages/pandas/core/internals/blocks.py line 645 - (extension) 
* 1306) venv/lib/python3.6/site-packages/pandas/core/internals/blocks.py line 997 - this prob needs some better checking 
* 1307) venv/lib/python3.6/site-packages/pandas/core/internals/blocks.py line 1528 - cleanup this special case. 
* 1308) venv/lib/python3.6/site-packages/pandas/core/internals/blocks.py line 1534 - NonConsolidatableMixin shape 
* 1309) venv/lib/python3.6/site-packages/pandas/core/internals/blocks.py line 1995 - (SparseArray.__setitem__): remove this if condition 
* 1310) venv/lib/python3.6/site-packages/pandas/core/internals/blocks.py line 2627 - remove the np.int64 support once coerce_values and 
* 1311) venv/lib/python3.6/site-packages/pandas/core/internals/blocks.py line 2784 - Refactor when convert_objects is removed since there will be 1 path 
* 1312) venv/lib/python3.6/site-packages/pandas/core/internals/blocks.py line 2816 - allow EA once reshape is supported 
* 1313) venv/lib/python3.6/site-packages/pandas/core/internals/blocks.py line 2863 - (ExtensionArray): remove is_extension_type 
* 1314) venv/lib/python3.6/site-packages/pandas/core/internals/blocks.py line 3168 - (CategoricalBlock.where): 
* 1315) venv/lib/python3.6/site-packages/pandas/core/internals/blocks.py line 3263 - This is no longer hit internally; does it need to be retained 
* 1316) venv/lib/python3.6/site-packages/pandas/core/internals/blocks.py line 3298 - https://github.com/pandas-dev/pandas/issues/23023 
* 1317) venv/lib/python3.6/site-packages/pandas/core/dtypes/cast.py line 190 - (DatetimeArray): merge with previous elif 
* 1318) venv/lib/python3.6/site-packages/pandas/core/dtypes/cast.py line 898 - why not timedelta? 
* 1319) venv/lib/python3.6/site-packages/pandas/core/dtypes/common.py line 636 - Consider making Period an instance of PeriodDtype 
* 1320) venv/lib/python3.6/site-packages/pandas/core/dtypes/common.py line 672 - Consider making Interval an instance of IntervalDtype 
* 1321) venv/lib/python3.6/site-packages/pandas/core/dtypes/common.py line 740 - gh-15585: consider making the checks stricter. 
* 1322) venv/lib/python3.6/site-packages/pandas/core/dtypes/common.py line 1672 - (jreback) 
* 1323) venv/lib/python3.6/site-packages/pandas/core/dtypes/common.py line 1972 - (jreback) 
* 1324) venv/lib/python3.6/site-packages/pandas/core/dtypes/concat.py line 538 - Fix join unit generation so we aren't passed this. 
* 1325) venv/lib/python3.6/site-packages/pandas/core/dtypes/dtypes.py line 23 - (GH26403): Replace with Optional[bool] or bool 
* 1326) venv/lib/python3.6/site-packages/pandas/core/dtypes/dtypes.py line 216 - Document public vs. private API 
* 1327) venv/lib/python3.6/site-packages/pandas/core/dtypes/dtypes.py line 443 - hash_array doesn't handle mixed types. It casts 
* 1328) venv/lib/python3.6/site-packages/pandas/core/dtypes/dtypes.py line 592 - remove if block when ordered=None as default is deprecated 
* 1329) venv/lib/python3.6/site-packages/pandas/core/dtypes/dtypes.py line 742 - (py3): Change this pass to `raise TypeError(msg) from e` 
* 1330) venv/lib/python3.6/site-packages/pandas/core/dtypes/dtypes.py line 758 - update this. 
* 1331) venv/lib/python3.6/site-packages/pandas/core/sparse/frame.py line 213 - figure out how to handle this case, all nan's? 
* 1332) venv/lib/python3.6/site-packages/pandas/core/sparse/frame.py line 575 - be a bit more intelligent here 
* 1333) venv/lib/python3.6/site-packages/pandas/core/sparse/frame.py line 739 - fill value handling 
* 1334) venv/lib/python3.6/site-packages/pandas/core/sparse/frame.py line 1019 - Figure out whether this can be reached. 
* 1335) venv/lib/python3.6/site-packages/pandas/core/sparse/scipy_sparse.py line 36 - how to do this better? cleanly slice nonnull_labels given the 
* 1336) venv/lib/python3.6/site-packages/pandas/core/sparse/scipy_sparse.py line 43 - these two lines can replace the code below but 
* 1337) venv/lib/python3.6/site-packages/pandas/core/sparse/scipy_sparse.py line 145 - (SparseSeries): remove this and the sparse_series keyword. 
* 1338) venv/lib/python3.6/site-packages/pandas/core/sparse/scipy_sparse.py line 148 - specify kind? 
* 1339) venv/lib/python3.6/site-packages/pandas/core/sparse/series.py line 92 - Most of this should be refactored and shared with Series 
* 1340) venv/lib/python3.6/site-packages/pandas/core/sparse/series.py line 145 - See if this can be shared 
* 1341) venv/lib/python3.6/site-packages/pandas/core/sparse/series.py line 336 - Document difference from Series.__getitem__, deprecate, 
* 1342) venv/lib/python3.6/site-packages/pandas/core/sparse/series.py line 506 - https://github.com/pandas-dev/pandas/issues/22314 
* 1343) venv/lib/python3.6/site-packages/pandas/core/sparse/series.py line 522 - remove? 
* 1344) venv/lib/python3.6/site-packages/pandas/core/sparse/series.py line 577 - SparseSeries.isna is Sparse, while Series.isna is dense 
* 1345) venv/lib/python3.6/site-packages/pandas/core/sparse/series.py line 604 - make more efficient 
