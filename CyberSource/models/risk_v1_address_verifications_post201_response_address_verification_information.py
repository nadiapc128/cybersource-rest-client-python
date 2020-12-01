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


class RiskV1AddressVerificationsPost201ResponseAddressVerificationInformation(object):
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
        'address_type': 'str',
        'bar_code': 'RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationBarCode',
        'applicable_region': 'str',
        'error_code': 'str',
        'status_code': 'str',
        'care_of': 'str',
        'match_score': 'int',
        'standard_address': 'RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationStandardAddress'
    }

    attribute_map = {
        'address_type': 'addressType',
        'bar_code': 'barCode',
        'applicable_region': 'applicableRegion',
        'error_code': 'errorCode',
        'status_code': 'statusCode',
        'care_of': 'careOf',
        'match_score': 'matchScore',
        'standard_address': 'standardAddress'
    }

    def __init__(self, address_type=None, bar_code=None, applicable_region=None, error_code=None, status_code=None, care_of=None, match_score=None, standard_address=None):
        """
        RiskV1AddressVerificationsPost201ResponseAddressVerificationInformation - a model defined in Swagger
        """

        self._address_type = None
        self._bar_code = None
        self._applicable_region = None
        self._error_code = None
        self._status_code = None
        self._care_of = None
        self._match_score = None
        self._standard_address = None

        if address_type is not None:
          self.address_type = address_type
        if bar_code is not None:
          self.bar_code = bar_code
        if applicable_region is not None:
          self.applicable_region = applicable_region
        if error_code is not None:
          self.error_code = error_code
        if status_code is not None:
          self.status_code = status_code
        if care_of is not None:
          self.care_of = care_of
        if match_score is not None:
          self.match_score = match_score
        if standard_address is not None:
          self.standard_address = standard_address

    @property
    def address_type(self):
        """
        Gets the address_type of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformation.
        Contains the record type of the postal code with which the address was matched.  #### U.S. Addresses Depending on the quantity and quality of the address information provided, this field contains one or two characters:  - One character: sufficient correct information was provided to result in accurate matching. - Two characters: standardization would provide a better address if more or better input address information were available. The second character is D (default).  Blank fields are unassigned. When an address cannot be standardized, how the input data was parsed determines the address type. In this case, standardization may indicate a street, rural route, highway contract, general delivery, or PO box. For possible values, see the description for the `dav_address_type` reply field in [CyberSource Verification Services Using the SCMP API](https://apps.cybersource.com/library/documentation/dev_guides/Verification_Svcs_SCMP_API/html/)  #### All Other Countries This field contains one of the following values: - P: Post. - S: Street. - x: Unknown. 

        :return: The address_type of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformation.
        :rtype: str
        """
        return self._address_type

    @address_type.setter
    def address_type(self, address_type):
        """
        Sets the address_type of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformation.
        Contains the record type of the postal code with which the address was matched.  #### U.S. Addresses Depending on the quantity and quality of the address information provided, this field contains one or two characters:  - One character: sufficient correct information was provided to result in accurate matching. - Two characters: standardization would provide a better address if more or better input address information were available. The second character is D (default).  Blank fields are unassigned. When an address cannot be standardized, how the input data was parsed determines the address type. In this case, standardization may indicate a street, rural route, highway contract, general delivery, or PO box. For possible values, see the description for the `dav_address_type` reply field in [CyberSource Verification Services Using the SCMP API](https://apps.cybersource.com/library/documentation/dev_guides/Verification_Svcs_SCMP_API/html/)  #### All Other Countries This field contains one of the following values: - P: Post. - S: Street. - x: Unknown. 

        :param address_type: The address_type of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformation.
        :type: str
        """

        self._address_type = address_type

    @property
    def bar_code(self):
        """
        Gets the bar_code of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformation.

        :return: The bar_code of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformation.
        :rtype: RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationBarCode
        """
        return self._bar_code

    @bar_code.setter
    def bar_code(self, bar_code):
        """
        Sets the bar_code of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformation.

        :param bar_code: The bar_code of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformation.
        :type: RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationBarCode
        """

        self._bar_code = bar_code

    @property
    def applicable_region(self):
        """
        Gets the applicable_region of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformation.
        Value can be - Canada - US - International The values of errorCode and statusCode mean different things depending on the applicable region. Refer to the guide for more info. 

        :return: The applicable_region of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformation.
        :rtype: str
        """
        return self._applicable_region

    @applicable_region.setter
    def applicable_region(self, applicable_region):
        """
        Sets the applicable_region of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformation.
        Value can be - Canada - US - International The values of errorCode and statusCode mean different things depending on the applicable region. Refer to the guide for more info. 

        :param applicable_region: The applicable_region of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformation.
        :type: str
        """

        self._applicable_region = applicable_region

    @property
    def error_code(self):
        """
        Gets the error_code of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformation.
        Four-character error code returned for Canadian, US and international addresses. For possible values, see Verification Services guide. The meaning of the errorCode depends on value of applicableRegion. 

        :return: The error_code of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformation.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """
        Sets the error_code of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformation.
        Four-character error code returned for Canadian, US and international addresses. For possible values, see Verification Services guide. The meaning of the errorCode depends on value of applicableRegion. 

        :param error_code: The error_code of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformation.
        :type: str
        """

        self._error_code = error_code

    @property
    def status_code(self):
        """
        Gets the status_code of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformation.
        Four-to-ten character status code returned for Canadian, US and international addresses. For possible values, see Verification Services guide. The meaning of the errorCode depends on value of applicableRegion. 

        :return: The status_code of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformation.
        :rtype: str
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """
        Sets the status_code of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformation.
        Four-to-ten character status code returned for Canadian, US and international addresses. For possible values, see Verification Services guide. The meaning of the errorCode depends on value of applicableRegion. 

        :param status_code: The status_code of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformation.
        :type: str
        """

        self._status_code = status_code

    @property
    def care_of(self):
        """
        Gets the care_of of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformation.
        Care of data dropped from the standard address.

        :return: The care_of of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformation.
        :rtype: str
        """
        return self._care_of

    @care_of.setter
    def care_of(self, care_of):
        """
        Sets the care_of of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformation.
        Care of data dropped from the standard address.

        :param care_of: The care_of of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformation.
        :type: str
        """

        self._care_of = care_of

    @property
    def match_score(self):
        """
        Gets the match_score of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformation.
        Indicates the probable correctness of the address match. Returned for U.S. and Canadian addresses. Returns a value from 0-9, where 0 is most likely to be correct and 9 is least likely to be correct, or -1 if there is no address match. 

        :return: The match_score of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformation.
        :rtype: int
        """
        return self._match_score

    @match_score.setter
    def match_score(self, match_score):
        """
        Sets the match_score of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformation.
        Indicates the probable correctness of the address match. Returned for U.S. and Canadian addresses. Returns a value from 0-9, where 0 is most likely to be correct and 9 is least likely to be correct, or -1 if there is no address match. 

        :param match_score: The match_score of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformation.
        :type: int
        """

        self._match_score = match_score

    @property
    def standard_address(self):
        """
        Gets the standard_address of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformation.

        :return: The standard_address of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformation.
        :rtype: RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationStandardAddress
        """
        return self._standard_address

    @standard_address.setter
    def standard_address(self, standard_address):
        """
        Sets the standard_address of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformation.

        :param standard_address: The standard_address of this RiskV1AddressVerificationsPost201ResponseAddressVerificationInformation.
        :type: RiskV1AddressVerificationsPost201ResponseAddressVerificationInformationStandardAddress
        """

        self._standard_address = standard_address

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
        if not isinstance(other, RiskV1AddressVerificationsPost201ResponseAddressVerificationInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
