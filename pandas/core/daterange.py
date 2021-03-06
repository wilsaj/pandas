# pylint: disable=E1101,E1103

from pandas.core.index import DatetimeIndex, Index
import pandas.core.datetools as datetools


#-----------------------------------------------------------------------------
# DateRange class

class DateRange(Index):

    offset = tzinfo = None

    def __new__(cls, start=None, end=None, periods=None,
                offset=datetools.bday, time_rule=None,
                tzinfo=None, name=None, **kwds):

        import warnings
        warnings.warn("DateRange is deprecated, use DatetimeIndex instead",
                       FutureWarning)

        if time_rule is None:
            time_rule = kwds.get('timeRule')
        if time_rule is not None:
            offset = datetools.get_offset(time_rule)

        return DatetimeIndex(start=start, end=end,
                             periods=periods, freq=offset,
                             tzinfo=tzinfo, name=name, **kwds)

    def __setstate__(self, aug_state):
        """Necessary for making this object picklable"""
        index_state = aug_state[:1]
        offset = aug_state[1]

        # for backwards compatibility
        if len(aug_state) > 2:
            tzinfo = aug_state[2]
        else: # pragma: no cover
            tzinfo = None

        self.offset = offset
        self.tzinfo = tzinfo
        Index.__setstate__(self, *index_state)

def date_range(start=None, end=None, periods=None, freq='D', tz=None,
               normalize=False):
    """
    Return a fixed frequency datetime index, with day (calendar) as the default
    frequency


    Parameters
    ----------
    start :
    end :
    normalize : bool, default False
        Normalize start/end dates to midnight before generating date range

    Returns
    -------

    """
    return DatetimeIndex(start=start, end=end, periods=periods,
                         freq=freq, tz=tz, normalize=normalize)


def bdate_range(start=None, end=None, periods=None, freq='B', tz=None,
                normalize=True):
    """
    Return a fixed frequency datetime index, with business day as the default
    frequency

    Parameters
    ----------

    normalize : bool, default False
        Normalize start/end dates to midnight before generating date
        range. Defaults to True for legacy reasons

    Returns
    -------
    date_range : DatetimeIndex

    """

    return DatetimeIndex(start=start, end=end, periods=periods,
                         freq=freq, tz=tz, normalize=normalize)

def interval_range():
    """
    Return a fixed frequency interval index
    """
