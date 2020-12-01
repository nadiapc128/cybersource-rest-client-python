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


class Ptsv2paymentsProcessingInformationLoanOptions(object):
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
        'type': 'str',
        'asset_type': 'str'
    }

    attribute_map = {
        'type': 'type',
        'asset_type': 'assetType'
    }

    def __init__(self, type=None, asset_type=None):
        """
        Ptsv2paymentsProcessingInformationLoanOptions - a model defined in Swagger
        """

        self._type = None
        self._asset_type = None

        if type is not None:
          self.type = type
        if asset_type is not None:
          self.asset_type = asset_type

    @property
    def type(self):
        """
        Gets the type of this Ptsv2paymentsProcessingInformationLoanOptions.
        Type of loan based on an agreement between you and the issuer. Examples: AGROCUSTEIO, AGRO-INVEST, BNDES-Type1, CBN, FINAME. This field is supported only for these kinds of payments: - BNDES transactions on CyberSource through VisaNet. - Installment payments with Mastercard on CyberSource through VisaNet in Brazil.  See \"\"Installment Payments on CyberSource through VisaNet,\"\" in the SCMP/SO guide  For BNDES transactions, the value for this field corresponds to the following data in the TC 33 capture file: - Record: CP07 TCR2, Position: 27-46, Field: Loan Type  For installment payments with Mastercard in Brazil, the value for this field corresponds to the following data in the TC 33 capture file: - Record: CP07 TCR4, Position: 5-24,Field: Financing Type 

        :return: The type of this Ptsv2paymentsProcessingInformationLoanOptions.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Ptsv2paymentsProcessingInformationLoanOptions.
        Type of loan based on an agreement between you and the issuer. Examples: AGROCUSTEIO, AGRO-INVEST, BNDES-Type1, CBN, FINAME. This field is supported only for these kinds of payments: - BNDES transactions on CyberSource through VisaNet. - Installment payments with Mastercard on CyberSource through VisaNet in Brazil.  See \"\"Installment Payments on CyberSource through VisaNet,\"\" in the SCMP/SO guide  For BNDES transactions, the value for this field corresponds to the following data in the TC 33 capture file: - Record: CP07 TCR2, Position: 27-46, Field: Loan Type  For installment payments with Mastercard in Brazil, the value for this field corresponds to the following data in the TC 33 capture file: - Record: CP07 TCR4, Position: 5-24,Field: Financing Type 

        :param type: The type of this Ptsv2paymentsProcessingInformationLoanOptions.
        :type: str
        """

        self._type = type

    @property
    def asset_type(self):
        """
        Gets the asset_type of this Ptsv2paymentsProcessingInformationLoanOptions.
        Indicates whether a loan is for a recoverable item or a non-recoverable item. Possible values: - `N`: non-recoverable item - `R`: recoverable item This field is supported only for BNDES transactions on CyberSource through VisaNet. The value for this field corresponds to the following data in the TC 33 capture file5:  Record: CP07 TCR2, Position: 26, Field: Asset Indicator 

        :return: The asset_type of this Ptsv2paymentsProcessingInformationLoanOptions.
        :rtype: str
        """
        return self._asset_type

    @asset_type.setter
    def asset_type(self, asset_type):
        """
        Sets the asset_type of this Ptsv2paymentsProcessingInformationLoanOptions.
        Indicates whether a loan is for a recoverable item or a non-recoverable item. Possible values: - `N`: non-recoverable item - `R`: recoverable item This field is supported only for BNDES transactions on CyberSource through VisaNet. The value for this field corresponds to the following data in the TC 33 capture file5:  Record: CP07 TCR2, Position: 26, Field: Asset Indicator 

        :param asset_type: The asset_type of this Ptsv2paymentsProcessingInformationLoanOptions.
        :type: str
        """

        self._asset_type = asset_type

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
        if not isinstance(other, Ptsv2paymentsProcessingInformationLoanOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
