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


class PtsV2PaymentsPost201ResponseRiskInformationTravelFirstDestination(object):
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
        'country': 'str',
        'locality': 'str',
        'latitude': 'str',
        'longitude': 'str'
    }

    attribute_map = {
        'country': 'country',
        'locality': 'locality',
        'latitude': 'latitude',
        'longitude': 'longitude'
    }

    def __init__(self, country=None, locality=None, latitude=None, longitude=None):
        """
        PtsV2PaymentsPost201ResponseRiskInformationTravelFirstDestination - a model defined in Swagger
        """

        self._country = None
        self._locality = None
        self._latitude = None
        self._longitude = None

        if country is not None:
          self.country = country
        if locality is not None:
          self.locality = locality
        if latitude is not None:
          self.latitude = latitude
        if longitude is not None:
          self.longitude = longitude

    @property
    def country(self):
        """
        Gets the country of this PtsV2PaymentsPost201ResponseRiskInformationTravelFirstDestination.
        Country of first destination on the route.

        :return: The country of this PtsV2PaymentsPost201ResponseRiskInformationTravelFirstDestination.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this PtsV2PaymentsPost201ResponseRiskInformationTravelFirstDestination.
        Country of first destination on the route.

        :param country: The country of this PtsV2PaymentsPost201ResponseRiskInformationTravelFirstDestination.
        :type: str
        """

        self._country = country

    @property
    def locality(self):
        """
        Gets the locality of this PtsV2PaymentsPost201ResponseRiskInformationTravelFirstDestination.
        City of first destination on the route.

        :return: The locality of this PtsV2PaymentsPost201ResponseRiskInformationTravelFirstDestination.
        :rtype: str
        """
        return self._locality

    @locality.setter
    def locality(self, locality):
        """
        Sets the locality of this PtsV2PaymentsPost201ResponseRiskInformationTravelFirstDestination.
        City of first destination on the route.

        :param locality: The locality of this PtsV2PaymentsPost201ResponseRiskInformationTravelFirstDestination.
        :type: str
        """

        self._locality = locality

    @property
    def latitude(self):
        """
        Gets the latitude of this PtsV2PaymentsPost201ResponseRiskInformationTravelFirstDestination.
        Latitude of first destination on the route.

        :return: The latitude of this PtsV2PaymentsPost201ResponseRiskInformationTravelFirstDestination.
        :rtype: str
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """
        Sets the latitude of this PtsV2PaymentsPost201ResponseRiskInformationTravelFirstDestination.
        Latitude of first destination on the route.

        :param latitude: The latitude of this PtsV2PaymentsPost201ResponseRiskInformationTravelFirstDestination.
        :type: str
        """

        self._latitude = latitude

    @property
    def longitude(self):
        """
        Gets the longitude of this PtsV2PaymentsPost201ResponseRiskInformationTravelFirstDestination.
        Longitude of first destination on the route.

        :return: The longitude of this PtsV2PaymentsPost201ResponseRiskInformationTravelFirstDestination.
        :rtype: str
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """
        Sets the longitude of this PtsV2PaymentsPost201ResponseRiskInformationTravelFirstDestination.
        Longitude of first destination on the route.

        :param longitude: The longitude of this PtsV2PaymentsPost201ResponseRiskInformationTravelFirstDestination.
        :type: str
        """

        self._longitude = longitude

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
        if not isinstance(other, PtsV2PaymentsPost201ResponseRiskInformationTravelFirstDestination):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
