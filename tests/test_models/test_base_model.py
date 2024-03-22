#!/usr/bin/python3
from datetime import datetime, timedelta
import unittest
from models.base_model import BaseModel
""" This module contain list of tests for
BaseModel class """


class TestBaseModel(unittest.TestCase):
    """ A class to test base Model """

    """ Test model base object """
    def test_baseModelObject(self):
        """ Test whether an object is an instance
        of BaseModel class. Test whether the object
        contains list of attributes of the class.
        Test whether the object contains list of
        instance method of the class.
        Test whether two objects are different """

        base_model1 = BaseModel()
        base_model2 = BaseModel()

        self.assertNotEqual(base_model1, base_model2)
        self.assertIsInstance(base_model1, BaseModel)

        self.assertTrue(hasattr(base_model1, "id"))
        self.assertTrue(hasattr(base_model1, "created_at"))
        self.assertTrue(hasattr(base_model1, "updated_at"))
        self.assertTrue(hasattr(base_model1, "__str__"))
        self.assertTrue(hasattr(base_model1, "save"))
        self.assertTrue(hasattr(base_model1, "to_dict"))

    """ Test attribut id"""
    def test_id(self):
        """ Test whether two objets have different id.
        Tese whether id is an instance of string """

        base_model1 = BaseModel()
        base_model2 = BaseModel()

        self.assertIsInstance(base_model1.id, str)
        self.assertNotEqual(base_model1.id, base_model2.id)

    """ Test attribute created_at"""
    def test_created_at(self):
        """ Test whether the attribute created_at is
        instance of datetime """
        base_model1 = BaseModel()

        self.assertIsInstance(base_model1.created_at, datetime)
        self.assertAlmostEqual(base_model1.created_at, datetime.now(),
                               delta=timedelta(seconds=1))

    """ Test attribute updated_at """
    def test_updated_at(self):
        """ Test whether the attribute updated_at is
        instance of datetime """
        base_model1 = BaseModel()

        self.assertIsInstance(base_model1.updated_at, datetime)
        self.assertAlmostEqual(base_model1.updated_at, datetime.now(),
                               delta=timedelta(seconds=1))

    """ Test __str__ function"""
    def test_str_representation(self):
        """ Test whether printing an object gives
        the expected formatted result """
        base_model1 = BaseModel()

        expected_output = f"[{base_model1.__class__.__name__}] "
        expected_output += f"({base_model1.id}) {base_model1.__dict__}"
        self.assertEqual(str(base_model1), expected_output)

    """ Test save function"""
    def test_save(self):
        """ Test whether save function update the updated_at
        attribute of the class """
        base_model1 = BaseModel()

        base_model1.save()
        self.assertAlmostEqual(base_model1.updated_at, datetime.now(),
                               delta=timedelta(seconds=1))

    """ Test to_dict function """
    def test_to_dict(self):
        """ Test whether the function to_dict returns all
        attributes of the object. Test whether created_at
        and updated_at are instance of string. Test whether
        the dictionary representation contain the key __class__ and its
        value is the class name."""

        base_model1 = BaseModel()

        list_of_attributes = [attr for attr in dir(base_model1) if not
                              (attr.startswith('__') or
                               callable(getattr(base_model1, attr)))]
        base_model_json = base_model1.to_dict()
        self.assertIsInstance(base_model_json, dict)

        for attribute in list_of_attributes:
            self.assertTrue(attribute in base_model_json)

        self.assertTrue("__class__" in base_model_json)
        self.assertIsInstance(base_model_json["created_at"], str)
        self.assertIsInstance(base_model_json["updated_at"], str)
        self.assertEqual(base_model_json["__class__"],
                         base_model1.__class__.__name__)

    """ Test object recreation"""
    def test_object_recreation(self):
        """ Test if object is correctly recreated from the
        the existing dictionary representation of an object"""
        base_model1 = BaseModel()
        model_dict = base_model1.to_dict()
        new_object = BaseModel(**model_dict)
        for key, value in model_dict.items():
            self.assertEqual(getattr(base_model1, key),
                             getattr(new_object, key))
        self.assertNotEqual(base_model1, new_object)


if __name__ == "__main__":
    unittest.main()
