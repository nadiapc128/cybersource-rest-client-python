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


class PtsV2PaymentsPost201ResponseRiskInformationProfile(object):
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
        'name': 'str',
        'desination_queue': 'str',
        'selector_rule': 'str'
    }

    attribute_map = {
        'name': 'name',
        'desination_queue': 'desinationQueue',
        'selector_rule': 'selectorRule'
    }

    def __init__(self, name=None, desination_queue=None, selector_rule=None):
        """
        PtsV2PaymentsPost201ResponseRiskInformationProfile - a model defined in Swagger
        """

        self._name = None
        self._desination_queue = None
        self._selector_rule = None

        if name is not None:
          self.name = name
        if desination_queue is not None:
          self.desination_queue = desination_queue
        if selector_rule is not None:
          self.selector_rule = selector_rule

    @property
    def name(self):
        """
        Gets the name of this PtsV2PaymentsPost201ResponseRiskInformationProfile.
        Name of the active profile chosen by the profile selector. If no profile selector exists, the default active profile is chosen.  **Note** By default, your default profile is the active profile, or the Profile Selector chooses the active profile. Use this field only if you want to specify the name of a different profile. The passed-in profile will then become the active profile. 

        :return: The name of this PtsV2PaymentsPost201ResponseRiskInformationProfile.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PtsV2PaymentsPost201ResponseRiskInformationProfile.
        Name of the active profile chosen by the profile selector. If no profile selector exists, the default active profile is chosen.  **Note** By default, your default profile is the active profile, or the Profile Selector chooses the active profile. Use this field only if you want to specify the name of a different profile. The passed-in profile will then become the active profile. 

        :param name: The name of this PtsV2PaymentsPost201ResponseRiskInformationProfile.
        :type: str
        """

        self._name = name

    @property
    def desination_queue(self):
        """
        Gets the desination_queue of this PtsV2PaymentsPost201ResponseRiskInformationProfile.
        Name of the queue where orders that are not automatically accepted are sent. 

        :return: The desination_queue of this PtsV2PaymentsPost201ResponseRiskInformationProfile.
        :rtype: str
        """
        return self._desination_queue

    @desination_queue.setter
    def desination_queue(self, desination_queue):
        """
        Sets the desination_queue of this PtsV2PaymentsPost201ResponseRiskInformationProfile.
        Name of the queue where orders that are not automatically accepted are sent. 

        :param desination_queue: The desination_queue of this PtsV2PaymentsPost201ResponseRiskInformationProfile.
        :type: str
        """

        self._desination_queue = desination_queue

    @property
    def selector_rule(self):
        """
        Gets the selector_rule of this PtsV2PaymentsPost201ResponseRiskInformationProfile.
        Name of the profile selector rule that chooses the profile to use for the transaction. If no profile selector exists, the value is Default Active Profile. 

        :return: The selector_rule of this PtsV2PaymentsPost201ResponseRiskInformationProfile.
        :rtype: str
        """
        return self._selector_rule

    @selector_rule.setter
    def selector_rule(self, selector_rule):
        """
        Sets the selector_rule of this PtsV2PaymentsPost201ResponseRiskInformationProfile.
        Name of the profile selector rule that chooses the profile to use for the transaction. If no profile selector exists, the value is Default Active Profile. 

        :param selector_rule: The selector_rule of this PtsV2PaymentsPost201ResponseRiskInformationProfile.
        :type: str
        """

        self._selector_rule = selector_rule

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
        if not isinstance(other, PtsV2PaymentsPost201ResponseRiskInformationProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
