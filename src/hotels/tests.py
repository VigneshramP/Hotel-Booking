from django.test import TestCase
from models import *

# Create your tests here.


class LocationTestCase(TestCase):
    def setUp(self):
        Location.objects.create(country = 'India', city= 'Chennai', province = 'Asia')
        Location.objects.create(country = 'India', city= 'Madurai', province = 'Asia')

    def test_overall_defects(self):
        location1 = Location.objects.create(country = 'India', city= 'Madurai', province = 'Asia')
        location2 = Location.objects.create(country = 'India', city= 'Chennai', province = 'Asia')

        
# Country Field Test Cases
	    self.assertEqual(location1.country(),  "India")
        self.assertEqual(location2.country(),  "India")
	    self.assertNotEqual(location1.country(),  "Asia")
        self.assertNotEqual(location2.country(),  "Chennai")
	    self.assertTrue(location1.country(),  "India"))
        self.assertTrue(location2.country(),  "India")
	    self.assertFalse(location1.country(),  "Asia")
        self.assertFalse(location2.country(),  "Asia")
	
# Observations Field Test Cases
	    self.assertEqual(location1.city(),  "Madurai")
        self.assertEqual(location2.city(),  "Chennai")
	    self.assertNotEqual(location1.city(),  "Asia")
        self.assertNotEqual(location2.city(),  "Chennai")
	    self.assertTrue(location1.city(),  "Madurai"))
        self.assertTrue(location2.city(),  "Chennai")
	    self.assertFalse(location1.city(),  "Asia")
        self.assertFalse(location2.city(),  "Asia")

class HotelTestCase(TestCase):
    def setUp(self):
        Hotel.objects.create(name='OYO',star=4, address='Kovilampakkam', description='Good Cleaning and Compact Room Avilable', located = 'Chennai')
        Hotel.objects.create(name='OYO',star=3, address='Thirumangalam', description='Good Cleaning and Compact Room Avilable', located = 'Madurai')

    def test_hotel(self):
        hotel1= Hotel.objects.create(name='OYO',star=4, address='Kovilampakkam', description='Good Cleaning and Compact Room Avilable', located = 'Chennai')

        self.assertEqual(hotel1.name(),  "OYO")
	    self.assertNotEqual(hotel1.name(),  "Pandian")
	    self.assertTrue(hotel1.name(),  "OYO")
	    self.assertFalse(hotel1.name(),  "Pandian")

        self.assertEqual(hotel1.star(),  4)
	    self.assertNotEqual(hotel1.star(),  3)
	    self.assertTrue(hotel1.star(),  4)
	    self.assertFalse(hotel1.star(),  3)


class RoomTestCase(TestCase):
    def setUp(self):
        Room.objects.create(adult=2,children=2,belongto='OYO',price=1500.0,roomNumber=1)
        Room.objects.create(adult=2,children=2,belongto='OYO',price=1000.0,roomNumber=2)

    def test_room(self):
        room1 = Room.objects.create(adult=2,children=2,belongto='OYO',price=1500.0,roomNumber=1)

        self.assertEqual(room1.adult(),  2)
	    self.assertNotEqual(room1.adult(),  1)
	    self.assertTrue(room1.adult(),  2)
	    self.assertFalse(room1.adult(),  1)
        
        self.assertEqual(room1.price(),  1500.0)
	    self.assertNotEqual(room1.price(),  1500)
	    self.assertTrue(room1.price(),  1500.0)
	    self.assertFalse(room1.price(),  1534)

class ClientTest(TestCase):
    def setUp(self):
        Client.objects.create(firstname='Vignesh',lastname='Perumal',requirement='Need Extra Bed')
        Client.objects.create(firstname='Deva',lastname='Raj',requirement='Need Extra Bed')

    def test_client(self):
        client1=Client.objects.create(firstname='Vignesh',lastname='Perumal',requirement='Need Extra Bed')

        self.assertEqual(client1.firstname(), 'Vignesh')
	    self.assertNotEqual(client1.firstname(), 'Perumal')
	    self.assertTrue(client1.firstname(), 'Vignesh')
	    self.assertFalse(client1.firstname(), 'Perumal')
        
        self.assertEqual(room1.lastname(), 'Perumal')
	    self.assertNotEqual(room1.lastname(), 'Vignesh')
	    self.assertTrue(room1.lastname(), 'Perumal')
	    self.assertFalse(room1.lastname(), 'Vignesh')  