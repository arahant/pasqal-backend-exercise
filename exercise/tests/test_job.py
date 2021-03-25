
from exercise.job import Job

def test_job():
    job1 = Job(12, "uid1", "prog11", "type1", 21)
    assert job1.id == 12

    job2 = Job(22, "uid4", "prog141", "type2", 21)
    assert job2.id == 22

    job3 = Job(121, "uid3", "prog9", "type3", 32)
    assert job3.id == 121
