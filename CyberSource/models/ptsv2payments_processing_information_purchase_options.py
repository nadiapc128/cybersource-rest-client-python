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


class Ptsv2paymentsProcessingInformationPurchaseOptions(object):
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
        'is_electronic_benefits_transfer': 'bool',
        'type': 'str'
    }

    attribute_map = {
        'is_electronic_benefits_transfer': 'isElectronicBenefitsTransfer',
        'type': 'type'
    }

    def __init__(self, is_electronic_benefits_transfer=None, type=None):
        """
        Ptsv2paymentsProcessingInformationPurchaseOptions - a model defined in Swagger
        """

        self._is_electronic_benefits_transfer = None
        self._type = None

        if is_electronic_benefits_transfer is not None:
          self.is_electronic_benefits_transfer = is_electronic_benefits_transfer
        if type is not None:
          self.type = type

    @property
    def is_electronic_benefits_transfer(self):
        """
        Gets the is_electronic_benefits_transfer of this Ptsv2paymentsProcessingInformationPurchaseOptions.
        Flag that indicates whether this transaction is an EBT transaction. Possible values: - `true` - `false`  #### PIN debit Required field for EBT and EBT voucher transactions that use PIN debit credit or PIN debit purchase; otherwise, not used. 

        :return: The is_electronic_benefits_transfer of this Ptsv2paymentsProcessingInformationPurchaseOptions.
        :rtype: bool
        """
        return self._is_electronic_benefits_transfer

    @is_electronic_benefits_transfer.setter
    def is_electronic_benefits_transfer(self, is_electronic_benefits_transfer):
        """
        Sets the is_electronic_benefits_transfer of this Ptsv2paymentsProcessingInformationPurchaseOptions.
        Flag that indicates whether this transaction is an EBT transaction. Possible values: - `true` - `false`  #### PIN debit Required field for EBT and EBT voucher transactions that use PIN debit credit or PIN debit purchase; otherwise, not used. 

        :param is_electronic_benefits_transfer: The is_electronic_benefits_transfer of this Ptsv2paymentsProcessingInformationPurchaseOptions.
        :type: bool
        """

        self._is_electronic_benefits_transfer = is_electronic_benefits_transfer

    @property
    def type(self):
        """
        Gets the type of this Ptsv2paymentsProcessingInformationPurchaseOptions.
        Flag that indicates an EBT voucher transaction. Possible value: - `EBT_VOUCHER`: Indicates the PIN debit transaction is an EBT voucher.  #### PIN debit Required field for EBT voucher transactions that use PIN debit purchase; otherwise, not used. 

        :return: The type of this Ptsv2paymentsProcessingInformationPurchaseOptions.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Ptsv2paymentsProcessingInformationPurchaseOptions.
        Flag that indicates an EBT voucher transaction. Possible value: - `EBT_VOUCHER`: Indicates the PIN debit transaction is an EBT voucher.  #### PIN debit Required field for EBT voucher transactions that use PIN debit purchase; otherwise, not used. 

        :param type: The type of this Ptsv2paymentsProcessingInformationPurchaseOptions.
        :type: str
        """

        self._type = type

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
        if not isinstance(other, Ptsv2paymentsProcessingInformationPurchaseOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
