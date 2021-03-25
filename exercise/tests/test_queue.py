from exercise.queue import PriorityQueue

def test_queue():
    q = PriorityQueue()

    item1 = {'life': 42}
    item2 = {'pizza': 'yolo'}
    item3 = 'coucou'

    q.push(item1, 10)
    q.push(item2, 20)
    q.push(item3, 20)

    assert q.pop() == item2
    assert q.pop() == item3
    assert q.pop() == item1
