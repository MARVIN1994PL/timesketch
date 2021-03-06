# Copyright 2015 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Tests for the sketch models."""

from timesketch.models.sketch import Sketch
from timesketch.models.sketch import Timeline
from timesketch.models.sketch import SearchIndex
from timesketch.models.sketch import View
from timesketch.models.sketch import Event
from timesketch.lib.testlib import ModelBaseTest


class SketchModelTest(ModelBaseTest):
    """Tests the sketch models."""
    def test_sketch_model(self):
        """
        Test that the test sketch has the expected data stored in the
        database.
        """
        expected_result = frozenset([
            (u'name', 'Test 1'),
            (u'description', 'Test 1'),
            (u'user', self.user1)
        ])
        self._test_db_object(
            expected_result=expected_result, model_cls=Sketch)

    def test_searchindex_model(self):
        """
        Test that the test searchindex has the expected data stored in the
        database.
        """
        expected_result = frozenset([
            (u'name', 'test'),
            (u'description', 'test'),
            (u'index_name', 'test'),
            (u'user', self.user1)
        ])
        self._test_db_object(
            expected_result=expected_result, model_cls=SearchIndex)

    def test_timeline_model(self):
        """
        Test that the test timeline has the expected data stored in the
        database.
        """
        expected_result = frozenset([
            (u'name', 'Timeline 1'),
            (u'description', 'Timeline 1'),
            (u'user', self.user1),
            (u'sketch', self.sketch1),
            (u'searchindex', self.searchindex)
        ])
        self._test_db_object(
            expected_result=expected_result, model_cls=Timeline)

    def test_view_model(self):
        """
        Test that the test view has the expected data stored in the database.
        """
        expected_result = frozenset([
            (u'name', 'View 1'),
            (u'query_string', 'View 1'),
            (u'user', self.user1),
            (u'sketch', self.sketch1)
        ])
        self._test_db_object(
            expected_result=expected_result, model_cls=View)

    def test_event_model(self):
        """
        Test that the test event has the expected data stored in the database.
        """
        expected_result = frozenset([
            (u'searchindex', self.searchindex),
            (u'sketch', self.sketch1),
            (u'document_id', 'test')
        ])
        self._test_db_object(
            expected_result=expected_result, model_cls=Event)
