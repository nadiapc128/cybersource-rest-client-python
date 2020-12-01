# coding: utf-8

"""
    CyberSource Merged Spec

    All CyberSource API specs merged together. These are available at https://developer.cybersource.com/api/reference/api-reference.html

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Ptsv2paymentsTravelInformationAutoRentalRentalAddress(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'city': 'str',
        'state': 'str',
        'country': 'str',
        'location_id': 'str',
        'address1': 'str',
        'address2': 'str',
        'location': 'str'
    }

    attribute_map = {
        'city': 'city',
        'state': 'state',
        'country': 'country',
        'location_id': 'locationId',
        'address1': 'address1',
        'address2': 'address2',
        'location': 'location'
    }

    def __init__(self, city=None, state=None, country=None, location_id=None, address1=None, address2=None, location=None):
        """
        Ptsv2paymentsTravelInformationAutoRentalRentalAddress - a model defined in Swagger
        """

        self._city = None
        self._state = None
        self._country = None
        self._location_id = None
        self._address1 = None
        self._address2 = None
        self._location = None

        if city is not None:
          self.city = city
        if state is not None:
          self.state = state
        if country is not None:
          self.country = country
        if location_id is not None:
          self.location_id = location_id
        if address1 is not None:
          self.address1 = address1
        if address2 is not None:
          self.address2 = address2
        if location is not None:
          self.location = location

    @property
    def city(self):
        """
        Gets the city of this Ptsv2paymentsTravelInformationAutoRentalRentalAddress.
        City in which the auto was rented.  For authorizations, this field is supported for Visa, MasterCard, and American Express.  For captures, this field is supported only for American Express.  For all other card types, this field is ignored. 

        :return: The city of this Ptsv2paymentsTravelInformationAutoRentalRentalAddress.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this Ptsv2paymentsTravelInformationAutoRentalRentalAddress.
        City in which the auto was rented.  For authorizations, this field is supported for Visa, MasterCard, and American Express.  For captures, this field is supported only for American Express.  For all other card types, this field is ignored. 

        :param city: The city of this Ptsv2paymentsTravelInformationAutoRentalRentalAddress.
        :type: str
        """

        self._city = city

    @property
    def state(self):
        """
        Gets the state of this Ptsv2paymentsTravelInformationAutoRentalRentalAddress.
        State in which the auto was rented. Use the [State, Province, and Territory Codes for the United States and Canada](https://developer.cybersource.com/library/documentation/sbc/quickref/states_and_provinces.pdf). 

        :return: The state of this Ptsv2paymentsTravelInformationAutoRentalRentalAddress.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this Ptsv2paymentsTravelInformationAutoRentalRentalAddress.
        State in which the auto was rented. Use the [State, Province, and Territory Codes for the United States and Canada](https://developer.cybersource.com/library/documentation/sbc/quickref/states_and_provinces.pdf). 

        :param state: The state of this Ptsv2paymentsTravelInformationAutoRentalRentalAddress.
        :type: str
        """

        self._state = state

    @property
    def country(self):
        """
        Gets the country of this Ptsv2paymentsTravelInformationAutoRentalRentalAddress.
        Country where the auto was rented. Use the [ISO Standard Country Codes.](https://developer.cybersource.com/library/documentation/sbc/quickref/countries_alpha_list.pdf) This field is supported only for American Express. 

        :return: The country of this Ptsv2paymentsTravelInformationAutoRentalRentalAddress.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this Ptsv2paymentsTravelInformationAutoRentalRentalAddress.
        Country where the auto was rented. Use the [ISO Standard Country Codes.](https://developer.cybersource.com/library/documentation/sbc/quickref/countries_alpha_list.pdf) This field is supported only for American Express. 

        :param country: The country of this Ptsv2paymentsTravelInformationAutoRentalRentalAddress.
        :type: str
        """

        self._country = country

    @property
    def location_id(self):
        """
        Gets the location_id of this Ptsv2paymentsTravelInformationAutoRentalRentalAddress.
        The agency code, address, phone number, etc., used to identify the location where the vehicle was rented. 

        :return: The location_id of this Ptsv2paymentsTravelInformationAutoRentalRentalAddress.
        :rtype: str
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """
        Sets the location_id of this Ptsv2paymentsTravelInformationAutoRentalRentalAddress.
        The agency code, address, phone number, etc., used to identify the location where the vehicle was rented. 

        :param location_id: The location_id of this Ptsv2paymentsTravelInformationAutoRentalRentalAddress.
        :type: str
        """

        self._location_id = location_id

    @property
    def address1(self):
        """
        Gets the address1 of this Ptsv2paymentsTravelInformationAutoRentalRentalAddress.
        Address from where the vehicle was rented. 

        :return: The address1 of this Ptsv2paymentsTravelInformationAutoRentalRentalAddress.
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """
        Sets the address1 of this Ptsv2paymentsTravelInformationAutoRentalRentalAddress.
        Address from where the vehicle was rented. 

        :param address1: The address1 of this Ptsv2paymentsTravelInformationAutoRentalRentalAddress.
        :type: str
        """

        self._address1 = address1

    @property
    def address2(self):
        """
        Gets the address2 of this Ptsv2paymentsTravelInformationAutoRentalRentalAddress.
        Address from where the vehicle was rented. 

        :return: The address2 of this Ptsv2paymentsTravelInformationAutoRentalRentalAddress.
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """
        Sets the address2 of this Ptsv2paymentsTravelInformationAutoRentalRentalAddress.
        Address from where the vehicle was rented. 

        :param address2: The address2 of this Ptsv2paymentsTravelInformationAutoRentalRentalAddress.
        :type: str
        """

        self._address2 = address2

    @property
    def location(self):
        """
        Gets the location of this Ptsv2paymentsTravelInformationAutoRentalRentalAddress.
        This field contains the location where a taxi passenger was picked up or where an auto rental vehicle was picked up. In most cases, this is the rental agency's business name that appears on the storefront and/or customer receipts, commonly referred to as the DBA (Doing Business As) name. However, if the vehicle was picked up at another location (e.g., a hotel,auto dealership, repair shop, etc.), the name of that location should be used. This entry must be easily recognized by the Cardmember to avoid unnecessary inquiries. If the name is more than 38  characters, use proper and meaningful abbreviation, when possible. 

        :return: The location of this Ptsv2paymentsTravelInformationAutoRentalRentalAddress.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """
        Sets the location of this Ptsv2paymentsTravelInformationAutoRentalRentalAddress.
        This field contains the location where a taxi passenger was picked up or where an auto rental vehicle was picked up. In most cases, this is the rental agency's business name that appears on the storefront and/or customer receipts, commonly referred to as the DBA (Doing Business As) name. However, if the vehicle was picked up at another location (e.g., a hotel,auto dealership, repair shop, etc.), the name of that location should be used. This entry must be easily recognized by the Cardmember to avoid unnecessary inquiries. If the name is more than 38  characters, use proper and meaningful abbreviation, when possible. 

        :param location: The location of this Ptsv2paymentsTravelInformationAutoRentalRentalAddress.
        :type: str
        """

        self._location = location

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Ptsv2paymentsTravelInformationAutoRentalRentalAddress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
