from seasons import findMinuteGap
from seasons import findMinuteGap
from datetime import date


def testCorrectOutput():
    today = date.today()
    testDate = today.replace(year=(today.year - 2))
    assert (
        findMinuteGap(testDate).strip()
        == "One million, fifty-one thousand, two hundred minutes"
    )
    testDate = today.replace(year=(today.year - 1))
    assert (
        findMinuteGap(testDate).strip()
        == "Five hundred twenty-five thousand, six hundred minutes"
    )
