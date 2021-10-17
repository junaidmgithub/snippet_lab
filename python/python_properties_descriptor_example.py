def dynamic_property(instance_name, name):
    def _get(self):
        obj = getattr(self, instance_name)
        return getattr(obj, name)
    def _set(self, value):
        obj = getattr(self, instance_name)
        setattr(obj, name, value)
    return property(_get, _set)

class DynamicProperty:

    def __init__(self, instance_name, attr_name):
        self._instance_name = instance_name
        self._attr_name = attr_name
    def __get__(self, instance, owner):
        obj = getattr(instance, self._instance_name)
        return getattr(obj, self._attr_name)
    def __set__(self, instance, value):
        obj = getattr(instance, self._instance_name)
        setattr(obj, self._attr_name, value)


class Person:

    def __init__(self):
        self.name = ''
        self.age = 0
        self.place = ''

class Student(Person):
    pass

class Teacher(Person):
    pass

class SampleStudent:

    def __init__(self):
        self._student = Student()
        self._teacher = Teacher()

    name = dynamic_property('_student', 'name')
    age = dynamic_property('_student', 'age')
    place = dynamic_property('_student', 'place')

    teacher_name = DynamicProperty('_teacher', 'name')
    teacher_age = DynamicProperty('_teacher', 'age')
    teacher_place = DynamicProperty('_teacher', 'place')


s = SampleStudent()
s.name = 'Junaid'
s.age = 24
s.place = 'Palakkal'

s.teacher_name = 'Ramesh'
s.teacher_age = 29
s.teacher_place = 'Kotakkal'

print(s)
print(s.name)
print(s.age)
print(s.place)

print(s.teacher_name)
print(s.teacher_age)
print(s.teacher_place)
