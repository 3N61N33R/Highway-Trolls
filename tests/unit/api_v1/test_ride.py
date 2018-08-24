import unittest
import json

from app import app

class TestRide(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def create_ride_offer(self):
        ride_info ={
            "pick_up":"Nairobi CBD",
            "dropoff":"Roysambu",
            "time":"06:00p.m"


        }
        response = self.app.post('/api/v1/rides',
            data= json.dumps(ride_info),
            content_type = 'application/json')
        return response

    def test_create_ride(self):
        response = self.create_ride_offer()
	self.assertEqual(response.status_code, 201)

    def test_get_rides(self):
        """test to fetch all ride offers"""
        response = self.app.get('/api/v1/rides')
        self.assertEqual(response.status_code, 200)

    def test_get_one_ride(self):
        """test to fetch one ride"""
        response = self.app.get('api/v1/rides/1')
        self.assertEqual(response.status_code, 200)

    def test_delete_ride_offer(self):
        """test to delete a ride offer"""
        response = self.app.delete('/api/v1/rides/1')
        self.assertEqual(response.status_code, 200)

    def update_ride_offer(self):
        ride_info = {
            "pick_up": "Nairobi CBD",
            "dropoff": "Roysambu",
            "time": "06:00p.m"


        }
        response = self.app.post('/api/v1/rides/6',
                                 data=json.dumps(ride_info),
                                 content_type='application/json')
        return response

    def test_update_ride(self):
        response= self.update_ride_offer()
        self.assertEqual(response.status_code, 201)

if __name__ == "__main__":
	unittest.main()
	