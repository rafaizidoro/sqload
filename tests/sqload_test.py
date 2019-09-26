import pytest
from sqload import load


@pytest.fixture
def q():
    return load('tests/queries.sql')

def test_load_all_queries(q):
    assert len(q.keys()) == 3

def test_get_query_by_key(q):
    assert q['find-all-by-name'] == 'SELECT * FROM users WHERE name = :name'

def test_clean_multiple_lines(q):
    sql = 'SELECT * FROM users u INNER JOIN products p ON u.id = p.user_id WHERE u.id = 1 LIMIT 1'

    assert q['find-users-join-products'] == sql