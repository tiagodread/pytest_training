class TestClass:
    person = {
        "full_name": "Tiago Góes da Silva",
        "age": 26,
        "Country": "Brazil"
    }

    def validate_name(self, name):
        return True if name in self.person['full_name'] else False

    def validate_age(self, age):
        return 'É de maior' if age >= 18 else 'É de menor'

    def test_name(self):
        assert self.validate_name('Tiago') == True

    def test_person_is_older(self):
        assert self.validate_age(25) == 'É de maior'
