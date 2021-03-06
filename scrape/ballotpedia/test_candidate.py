from collections import namedtuple
from pathlib import Path

import bs4
import pytest

from scrape.ballotpedia.candidate import get_twitters, get_party

TEST_DIR = Path("resources/test/ballotpedia/")

TestCase = namedtuple('TestCase', 'name html party twitters')

candidates = [
    TestCase(
        name='Stacey Abrams',
        party='Democratic',
        html=(TEST_DIR / "Stacey_Abrams.html").read_text(encoding='ISO-8859-1'),
        twitters=[('Personal Twitter', 'staceyabrams')],
    ),
    TestCase(
        name='Mike Pence',
        party='Republican',
        html=(TEST_DIR / "Mike_Pence.html").read_text(encoding='ISO-8859-1'),
        twitters=[('Campaign Twitter', 'TeamTrump'), ('Personal Twitter', 'Mike_Pence')],
    ),
    TestCase(
        name='Hillary Clinton',
        party='Democratic',
        html=(TEST_DIR / "Hillary_Clinton.html").read_text(encoding='ISO-8859-1'),
        twitters=[('Twitter', 'HillaryClinton')],
    ),
    TestCase(
        name='Tim Pawlenty',
        party='Republican',
        html=(TEST_DIR / "Tim_Pawlenty.html").read_text(encoding='ISO-8859-1'),
        twitters=[('Personal Twitter', 'TimPawlenty')],
    ),
]


@pytest.mark.parametrize('candidate', candidates)
def test_scrapes_twitters(candidate: TestCase):
    soup = bs4.BeautifulSoup(candidate.html, features="lxml")

    result = get_twitters(soup)

    assert result == candidate.twitters


@pytest.mark.parametrize('candidate', candidates)
def test_scrapes_party(candidate: TestCase):
    soup = bs4.BeautifulSoup(candidate.html, features="lxml")

    result = get_party(soup)

    assert result == candidate.party
