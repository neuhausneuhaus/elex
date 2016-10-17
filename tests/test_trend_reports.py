import tests
from elex.api import USGovernorTrendReport, USSenateTrendReport, USHouseTrendReport


class TestDelegateReports(tests.TrendReportTestCase):

    def test_us_governor(self):
        tr = USGovernorTrendReport()
        [o.serialize() for o in tr.parties]

    def test_us_senate(self):
        tr = USSenateTrendReport()
        [o.serialize() for o in tr.parties]

    def test_us_house(self):
        tr = USHouseTrendReport()
        [o.serialize() for o in tr.parties]
