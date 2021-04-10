
from unittest import TestCase
from exercise.main import app

class APITest(TestCase):
    """
    Routes Tests
    """
    @classmethod
    def setUpClass(cls):
        """ Run once before all tests """
        app.debug = True
        app.testing = True

    @classmethod
    def tearDownClass(cls):
        """ Run once after all tests """

    def setUp(self):
        """ Runs before each test """
        self.app = app.test_client()

    def tearDown(self):
        """Runs after each test"""

    ######################################################################
    #  T E S T   C A S E S
    ######################################################################
    def test_root(self):
        """Testing root"""
        resp = self.app.get("/")
        self.assertEqual(resp.status_code, 201)

    def test_create_device(self):
        """Add a device to the pool"""
        obj = {
            "device_id": 12,
            "address": "addr1",
            "device_type": "type1",
            "size": 21
        }
        resp = self.app.post("/device", json=obj, content_type="application/json")
        self.assertEqual(resp.status_code, 201)

        resp = self.app.post("/device", json=obj, content_type="application/json")
        self.assertEqual(resp.status_code, 409)

        obj = {
            "device_id": 22,
            "address": "addr2",
            "device_type": "type2",
            "size": 21
        }
        resp = self.app.post("/device", json=obj, content_type="application/json")
        self.assertEqual(resp.status_code, 201)

        obj = {
            "device_id": "121",
            "address": 655,
            "device_type": 1234,
            "size": 32
        }
        resp = self.app.post("/device", json=obj, content_type="application/json")
        self.assertEqual(resp.status_code, 400)

    def test_remove_device(self):
        """Remove a device from the pool"""
        resp = self.app.delete("/device/{}".format(12))
        self.assertEqual(resp.status_code, 204)

        resp = self.app.delete("/device/{}".format(121))
        self.assertEqual(resp.status_code, 204)

        resp = self.app.delete("/device/{}".format(121))
        self.assertEqual(resp.status_code, 204)

    def test_job_create(self):
        """Add a job into the queue"""
