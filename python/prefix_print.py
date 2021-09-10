import sys, textwrap

def prefix_print(prefix, max_lines=None, file=sys.stdout):
    def wrapper_fn(*args, **kwargs):
        print(textwrap.fill(*args, **kwargs,
            max_lines=max_lines, initial_indent=prefix,
            subsequent_indent=prefix + ' ' * 2), file=file)
    return wrapper_fn

log_wrapped_print = prefix_print('[Test 1]')
log_wrapped_print_max_line_3 = prefix_print('[Test 2]')

TEXT = "Lorem Ipsum dolor sit amet, consectetur adipiscing elit," +\
    " sed do eiusmod tempor incididunt ut labore et dolore magna aliqua." +\
    " Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris" +\
    " nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in" +\
    " reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla " +\
    "pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa" +\
    " qui officia deserunt mollit anim id est laborum"

log_wrapped_print(TEXT)
log_wrapped_print_max_line_3(TEXT)

# [Test 1]Lorem Ipsum dolor sit amet, consectetur adipiscing elit, sed
# [Test 1]  do eiusmod tempor incididunt ut labore et dolore magna
# [Test 1]  aliqua. Ut enim ad minim veniam, quis nostrud exercitation
# [Test 1]  ullamco laboris nisi ut aliquip ex ea commodo consequat.
# [Test 1]  Duis aute irure dolor in reprehenderit in voluptate velit
# [Test 1]  esse cillum dolore eu fugiat nulla pariatur. Excepteur sint
# [Test 1]  occaecat cupidatat non proident, sunt in culpa qui officia
# [Test 1]  deserunt mollit anim id est laborum
# [Test 2]Lorem Ipsum dolor sit amet, consectetur adipiscing elit, sed
# [Test 2]  do eiusmod tempor incididunt ut labore et dolore magna
# [Test 2]  aliqua. Ut enim ad minim veniam, quis nostrud exercitation
# [Test 2]  ullamco laboris nisi ut aliquip ex ea commodo consequat.
# [Test 2]  Duis aute irure dolor in reprehenderit in voluptate velit
# [Test 2]  esse cillum dolore eu fugiat nulla pariatur. Excepteur sint
# [Test 2]  occaecat cupidatat non proident, sunt in culpa qui officia
# [Test 2]  deserunt mollit anim id est laborum
