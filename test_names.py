from check_names import check_name
import unittest
from ddt import ddt, data

@ddt
class TestNameChecker(unittest.TestCase):
    @data('Jun Wang', 'Nishant Dahad','Alison Cheung','Naomi Nguyen ')
    def test_person_name(self, name):
        self.assertTrue(check_name(name))
        
    @data('Preembarrass Hippogryph', 'Fustellatrici Pazze Perugia e dintorni', 'Undercloth Reclothe', 'Chinese New Year', 'Thames River')
    def test_non_person_name(self, name):
        self.assertFalse(check_name(name))

if __name__ == '__main__':
    unittest.main(exit=False)
