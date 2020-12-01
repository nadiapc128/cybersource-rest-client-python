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


class Ptsv2paymentsPromotionInformation(object):
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
        'additional_code': 'str',
        'code': 'str'
    }

    attribute_map = {
        'additional_code': 'additionalCode',
        'code': 'code'
    }

    def __init__(self, additional_code=None, code=None):
        """
        Ptsv2paymentsPromotionInformation - a model defined in Swagger
        """

        self._additional_code = None
        self._code = None

        if additional_code is not None:
          self.additional_code = additional_code
        if code is not None:
          self.code = code

    @property
    def additional_code(self):
        """
        Gets the additional_code of this Ptsv2paymentsPromotionInformation.
        Additional rental agency marketed coupons for consumers to discount the rate of the vehicle rental agreement. 

        :return: The additional_code of this Ptsv2paymentsPromotionInformation.
        :rtype: str
        """
        return self._additional_code

    @additional_code.setter
    def additional_code(self, additional_code):
        """
        Sets the additional_code of this Ptsv2paymentsPromotionInformation.
        Additional rental agency marketed coupons for consumers to discount the rate of the vehicle rental agreement. 

        :param additional_code: The additional_code of this Ptsv2paymentsPromotionInformation.
        :type: str
        """

        self._additional_code = additional_code

    @property
    def code(self):
        """
        Gets the code of this Ptsv2paymentsPromotionInformation.
        Code for a promotion or discount. 

        :return: The code of this Ptsv2paymentsPromotionInformation.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this Ptsv2paymentsPromotionInformation.
        Code for a promotion or discount. 

        :param code: The code of this Ptsv2paymentsPromotionInformation.
        :type: str
        """

        self._code = code

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
        if not isinstance(other, Ptsv2paymentsPromotionInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
