# Copyright 2018 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Utility methods to perform actions in consitent ways across the app."""

import calendar


def datetime_to_unix(timestamp, milliseconds=False):
  """Converts a datetime object to a unix timestamp.

  Args:
    timestamp: A datetime object.
    milliseconds: Bool, default False, return result in milliseconds instead.

  Returns:
    An integer of unit timestamp in seconds.
  """
  if milliseconds:
    return int(calendar.timegm(timestamp.timetuple()) * 1000)
  else:
    return int(calendar.timegm(timestamp.timetuple()))


def is_weekend_or_monday(date):
  """Checks if the current date is a weekend or Monday.

  Args:
    date: datetime.datetime obj, the date to check.

  Returns:
    Bool indicating if it is a weekend or Monday.
  """
  return date.weekday() in (0, 5, 6)