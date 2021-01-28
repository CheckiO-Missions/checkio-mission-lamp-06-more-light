"""
CheckiOReferee is a base referee for checking you code.
    arguments:
        tests -- the dict contains tests in the specific structure.
            You can find an example in tests.py.
        cover_code -- is a wrapper for the user function and additional operations before give data
            in the user function. You can use some predefined codes from checkio.referee.cover_codes
        checker -- is replacement for the default checking of an user function result. If given, then
            instead simple "==" will be using the checker function which return tuple with result
            (false or true) and some additional info (some message).
            You can use some predefined codes from checkio.referee.checkers
        add_allowed_modules -- additional module which will be allowed for your task.
        add_close_builtins -- some closed builtin words, as example, if you want, you can close "eval"
        remove_allowed_modules -- close standard library modules, as example "math"

checkio.referee.checkers
    checkers.float_comparison -- Checking function fabric for check result with float numbers.
        Syntax: checkers.float_comparison(digits) -- where "digits" is a quantity of significant
            digits after coma.

checkio.referee.cover_codes
    cover_codes.unwrap_args -- Your "input" from test can be given as a list. if you want unwrap this
        before user function calling, then using this function. For example: if your test's input
        is [2, 2] and you use this cover_code, then user function will be called as checkio(2, 2)
    cover_codes.unwrap_kwargs -- the same as unwrap_kwargs, but unwrap dict.

"""

from checkio.signals import ON_CONNECT
from checkio import api
from checkio.referees.io import CheckiOReferee
from checkio.referees import cover_codes

from tests import TESTS

all_datetime_py = '''
def cover(func, in_data):
    from datetime import datetime, timedelta
    els = [((datetime(*el[0]), el[1]) if len(el) == 2 else datetime(*el)) for el in in_data[0]]
    kwargs = {}
    if len(in_data) > 1 and in_data[1] is not None:
        kwargs['start_watching'] = datetime(*in_data[1])
    if len(in_data) > 2 and in_data[2] is not None:
        kwargs['end_watching'] = datetime(*in_data[2])
    if len(in_data) > 3 and in_data[3] is not None:
        kwargs['operating'] = timedelta(seconds=in_data[3])
    if len(in_data) > 4 and in_data[4] is not None:
        kwargs['req'] = in_data[4]
    return func(els, **kwargs)
'''

all_datetime_js = '''
function cover(func, in_data) {
    var els = in_data[0].map(function(ee) {
        if (ee.length === 2) {
            return [new Date(ee[0][0], ee[0][1], ee[0][2], ee[0][3], ee[0][4], ee[0][5]), ee[1]];
        } else {
            return new Date(ee[0], ee[1], ee[2], ee[3], ee[4], ee[5]);
        }
    });
    var start_watching, end_watching, operating, req;
    if (in_data.length > 1 && in_data[1]) {
        start_watching = new Date(in_data[1][0], in_data[1][1], in_data[1][2], in_data[1][3], in_data[1][4], in_data[1][5]);
    }
    if (in_data.length > 2 && in_data[2]) {
        end_watching = new Date(in_data[2][0], in_data[2][1], in_data[2][2], in_data[2][3], in_data[2][4], in_data[2][5]);
    }
    if (in_data.length > 3 && in_data[3]) {
        operating = in_data[3];
    }
    if (in_data.length > 4 && in_data[4]) {
        req = in_data[4];
    }
    return func(els, start_watching, end_watching, operating, req);
}
'''

api.add_listener(
    ON_CONNECT,
    CheckiOReferee(
        tests=TESTS,
        function_name={
            "python": "sum_light",
            "js": "sumLight"
        },
        cover_code={
            'python-3': all_datetime_py,
            'js-node': all_datetime_js
        }
    ).on_ready)
