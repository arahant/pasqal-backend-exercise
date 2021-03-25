from exercise.queue import ProcessQueue


def test_queue():
    q = ProcessQueue()

    item1 = {'life': 42}
    item2 = {'pizza': 'yolo'}
    item3 = 'coucou'

    q.push(item1, 10)
    # (-10, 1, item1)
    q.push(item2, 20)
    # (-20, 2, item2), (-10, 1, item1)
    q.push(item3, 20)
    # (-20, 2, item2), (-20, 3, item3), (-10, 1, item1)

    assert q.pop() == item2
    # (-20, 3, item3), (-10, 1, item1)
    assert q.pop() == item3
    # (-10, 1, item1)
    assert q.pop() == item1
