import unittest
from firebase import firebase


class MyTestCase(unittest.TestCase):

    url_appFireBase = 'https://amber-heat-279.firebaseio.com'

    def test_read_firebase(self):
        firebase_cursor = firebase.FirebaseApplication(self.__class__.url_appFireBase, None)
        content = firebase_cursor.get("/users", None)
        print content
        self.assertEqual(True, True)

    def test_create_firebase(self):
        firebase_cursor = firebase.FirebaseApplication(self.__class__.url_appFireBase, None)
        new_user = 'Ozgur Vatansever'
        result = firebase_cursor.post("/users", new_user)
        print result
        self.assertEqual(True, True)

    def test_get_byID(self):
        firebase_cursor = firebase.FirebaseApplication(self.__class__.url_appFireBase, None)
        result = firebase_cursor.get("/users", '-KG8DWT4ekKICBxg9ppU')
        print result
        self.assertEqual(True, True)

    '''
    def test_update_byID(self):
        firebase_cursor = firebase.FirebaseApplication(self.__class__.url_appFireBase, None)
        firebase_cursor.put("/users", {u'-KG8DWT4ekKICBxg9ppU': u'Paul Walker'})
        self.assertEqual(True, True)
        '''

if __name__ == '__main__':
    unittest.main()
