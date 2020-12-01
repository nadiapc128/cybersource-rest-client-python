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


class Ptsv2paymentsMerchantInformation(object):
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
        'merchant_descriptor': 'Ptsv2paymentsMerchantInformationMerchantDescriptor',
        'sales_organization_id': 'str',
        'category_code': 'int',
        'category_code_domestic': 'int',
        'tax_id': 'str',
        'vat_registration_number': 'str',
        'card_acceptor_reference_number': 'str',
        'transaction_local_date_time': 'str',
        'service_fee_descriptor': 'Ptsv2paymentsMerchantInformationServiceFeeDescriptor',
        'merchant_name': 'str'
    }

    attribute_map = {
        'merchant_descriptor': 'merchantDescriptor',
        'sales_organization_id': 'salesOrganizationId',
        'category_code': 'categoryCode',
        'category_code_domestic': 'categoryCodeDomestic',
        'tax_id': 'taxId',
        'vat_registration_number': 'vatRegistrationNumber',
        'card_acceptor_reference_number': 'cardAcceptorReferenceNumber',
        'transaction_local_date_time': 'transactionLocalDateTime',
        'service_fee_descriptor': 'serviceFeeDescriptor',
        'merchant_name': 'merchantName'
    }

    def __init__(self, merchant_descriptor=None, sales_organization_id=None, category_code=None, category_code_domestic=None, tax_id=None, vat_registration_number=None, card_acceptor_reference_number=None, transaction_local_date_time=None, service_fee_descriptor=None, merchant_name=None):
        """
        Ptsv2paymentsMerchantInformation - a model defined in Swagger
        """

        self._merchant_descriptor = None
        self._sales_organization_id = None
        self._category_code = None
        self._category_code_domestic = None
        self._tax_id = None
        self._vat_registration_number = None
        self._card_acceptor_reference_number = None
        self._transaction_local_date_time = None
        self._service_fee_descriptor = None
        self._merchant_name = None

        if merchant_descriptor is not None:
          self.merchant_descriptor = merchant_descriptor
        if sales_organization_id is not None:
          self.sales_organization_id = sales_organization_id
        if category_code is not None:
          self.category_code = category_code
        if category_code_domestic is not None:
          self.category_code_domestic = category_code_domestic
        if tax_id is not None:
          self.tax_id = tax_id
        if vat_registration_number is not None:
          self.vat_registration_number = vat_registration_number
        if card_acceptor_reference_number is not None:
          self.card_acceptor_reference_number = card_acceptor_reference_number
        if transaction_local_date_time is not None:
          self.transaction_local_date_time = transaction_local_date_time
        if service_fee_descriptor is not None:
          self.service_fee_descriptor = service_fee_descriptor
        if merchant_name is not None:
          self.merchant_name = merchant_name

    @property
    def merchant_descriptor(self):
        """
        Gets the merchant_descriptor of this Ptsv2paymentsMerchantInformation.

        :return: The merchant_descriptor of this Ptsv2paymentsMerchantInformation.
        :rtype: Ptsv2paymentsMerchantInformationMerchantDescriptor
        """
        return self._merchant_descriptor

    @merchant_descriptor.setter
    def merchant_descriptor(self, merchant_descriptor):
        """
        Sets the merchant_descriptor of this Ptsv2paymentsMerchantInformation.

        :param merchant_descriptor: The merchant_descriptor of this Ptsv2paymentsMerchantInformation.
        :type: Ptsv2paymentsMerchantInformationMerchantDescriptor
        """

        self._merchant_descriptor = merchant_descriptor

    @property
    def sales_organization_id(self):
        """
        Gets the sales_organization_id of this Ptsv2paymentsMerchantInformation.
        Company ID assigned to an independent sales organization. Get this value from Mastercard.  #### CyberSource through VisaNet The value for this field corresponds to the following data in the TC 33 capture file: - Record: CP01 TCR6 - Position: 106-116 - Field: Mastercard Independent Sales Organization ID  **Note** The TC 33 Capture file contains information about the purchases and refunds that a merchant submits to CyberSource. CyberSource through VisaNet creates the TC 33 Capture file at the end of the day and sends it to the merchant’s acquirer, who uses this information to facilitate end-of-day clearing processing with payment card companies.  For processor-specific information, see the `sales_organization_ID` field description in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :return: The sales_organization_id of this Ptsv2paymentsMerchantInformation.
        :rtype: str
        """
        return self._sales_organization_id

    @sales_organization_id.setter
    def sales_organization_id(self, sales_organization_id):
        """
        Sets the sales_organization_id of this Ptsv2paymentsMerchantInformation.
        Company ID assigned to an independent sales organization. Get this value from Mastercard.  #### CyberSource through VisaNet The value for this field corresponds to the following data in the TC 33 capture file: - Record: CP01 TCR6 - Position: 106-116 - Field: Mastercard Independent Sales Organization ID  **Note** The TC 33 Capture file contains information about the purchases and refunds that a merchant submits to CyberSource. CyberSource through VisaNet creates the TC 33 Capture file at the end of the day and sends it to the merchant’s acquirer, who uses this information to facilitate end-of-day clearing processing with payment card companies.  For processor-specific information, see the `sales_organization_ID` field description in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :param sales_organization_id: The sales_organization_id of this Ptsv2paymentsMerchantInformation.
        :type: str
        """

        self._sales_organization_id = sales_organization_id

    @property
    def category_code(self):
        """
        Gets the category_code of this Ptsv2paymentsMerchantInformation.
        The value for this field is a four-digit number that the payment card industry uses to classify merchants into market segments. A payment card company assigned one or more of these values to your business when you started accepting the payment card company’s cards. When you do not include this field in your request, CyberSource uses the value in your CyberSource account.  For processor-specific information, see the `merchant_category_code` field description in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html)  #### CyberSource through VisaNet The value for this field corresponds to the following data in the TC 33 capture file5: - Record: CP01 TCR4 - Position: 150-153 - Field: Merchant Category Code 

        :return: The category_code of this Ptsv2paymentsMerchantInformation.
        :rtype: int
        """
        return self._category_code

    @category_code.setter
    def category_code(self, category_code):
        """
        Sets the category_code of this Ptsv2paymentsMerchantInformation.
        The value for this field is a four-digit number that the payment card industry uses to classify merchants into market segments. A payment card company assigned one or more of these values to your business when you started accepting the payment card company’s cards. When you do not include this field in your request, CyberSource uses the value in your CyberSource account.  For processor-specific information, see the `merchant_category_code` field description in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html)  #### CyberSource through VisaNet The value for this field corresponds to the following data in the TC 33 capture file5: - Record: CP01 TCR4 - Position: 150-153 - Field: Merchant Category Code 

        :param category_code: The category_code of this Ptsv2paymentsMerchantInformation.
        :type: int
        """
        if category_code is not None and category_code > 9999:
            raise ValueError("Invalid value for `category_code`, must be a value less than or equal to `9999`")

        self._category_code = category_code

    @property
    def category_code_domestic(self):
        """
        Gets the category_code_domestic of this Ptsv2paymentsMerchantInformation.
        Merchant category code for domestic transactions. The value for this field is a four-digit number that the payment card industry uses to classify merchants into market segments. A payment card company assigned one or more of these values to your business when you started accepting the payment card company’s cards. Including this field in a request for a domestic transaction might reduce interchange fees.  When you include this field in a request: - Do not include the `merchant_category_code` field. - The value for this field overrides the value in your CyberSource account.  This field is supported only for: - Domestic transactions with Mastercard in Spain. Domestic means that you and the cardholder are in the same country. - Merchants enrolled in the OmniPay Direct interchange program. - First Data Merchant Solutions (Europe) on OmniPay Direct. 

        :return: The category_code_domestic of this Ptsv2paymentsMerchantInformation.
        :rtype: int
        """
        return self._category_code_domestic

    @category_code_domestic.setter
    def category_code_domestic(self, category_code_domestic):
        """
        Sets the category_code_domestic of this Ptsv2paymentsMerchantInformation.
        Merchant category code for domestic transactions. The value for this field is a four-digit number that the payment card industry uses to classify merchants into market segments. A payment card company assigned one or more of these values to your business when you started accepting the payment card company’s cards. Including this field in a request for a domestic transaction might reduce interchange fees.  When you include this field in a request: - Do not include the `merchant_category_code` field. - The value for this field overrides the value in your CyberSource account.  This field is supported only for: - Domestic transactions with Mastercard in Spain. Domestic means that you and the cardholder are in the same country. - Merchants enrolled in the OmniPay Direct interchange program. - First Data Merchant Solutions (Europe) on OmniPay Direct. 

        :param category_code_domestic: The category_code_domestic of this Ptsv2paymentsMerchantInformation.
        :type: int
        """
        if category_code_domestic is not None and category_code_domestic > 9999:
            raise ValueError("Invalid value for `category_code_domestic`, must be a value less than or equal to `9999`")

        self._category_code_domestic = category_code_domestic

    @property
    def tax_id(self):
        """
        Gets the tax_id of this Ptsv2paymentsMerchantInformation.
        Your Cadastro Nacional da Pessoa Jurídica (CNPJ) number.  This field is supported only for BNDES transactions on CyberSource through VisaNet.  The value for this field corresponds to the following data in the TC 33 capture file5: - Record: CP07 TCR6 - Position: 40-59 - Field: BNDES Reference Field 1  For details, see `bill_merchant_tax_id` field description in the [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/) 

        :return: The tax_id of this Ptsv2paymentsMerchantInformation.
        :rtype: str
        """
        return self._tax_id

    @tax_id.setter
    def tax_id(self, tax_id):
        """
        Sets the tax_id of this Ptsv2paymentsMerchantInformation.
        Your Cadastro Nacional da Pessoa Jurídica (CNPJ) number.  This field is supported only for BNDES transactions on CyberSource through VisaNet.  The value for this field corresponds to the following data in the TC 33 capture file5: - Record: CP07 TCR6 - Position: 40-59 - Field: BNDES Reference Field 1  For details, see `bill_merchant_tax_id` field description in the [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/) 

        :param tax_id: The tax_id of this Ptsv2paymentsMerchantInformation.
        :type: str
        """

        self._tax_id = tax_id

    @property
    def vat_registration_number(self):
        """
        Gets the vat_registration_number of this Ptsv2paymentsMerchantInformation.
        Your government-assigned tax identification number.  #### Tax Calculation Required field for value added tax only. Not applicable to U.S. and Canadian taxes.  #### CyberSource through VisaNet For CtV processors, the maximum length is 20.  For other processor-specific information, see the `merchant_vat_registration_number` field description in [Level II and Level III Processing Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/Level_2_3_SCMP_API/html) 

        :return: The vat_registration_number of this Ptsv2paymentsMerchantInformation.
        :rtype: str
        """
        return self._vat_registration_number

    @vat_registration_number.setter
    def vat_registration_number(self, vat_registration_number):
        """
        Sets the vat_registration_number of this Ptsv2paymentsMerchantInformation.
        Your government-assigned tax identification number.  #### Tax Calculation Required field for value added tax only. Not applicable to U.S. and Canadian taxes.  #### CyberSource through VisaNet For CtV processors, the maximum length is 20.  For other processor-specific information, see the `merchant_vat_registration_number` field description in [Level II and Level III Processing Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/Level_2_3_SCMP_API/html) 

        :param vat_registration_number: The vat_registration_number of this Ptsv2paymentsMerchantInformation.
        :type: str
        """

        self._vat_registration_number = vat_registration_number

    @property
    def card_acceptor_reference_number(self):
        """
        Gets the card_acceptor_reference_number of this Ptsv2paymentsMerchantInformation.
        Reference number that facilitates card acceptor/corporation communication and record keeping.  For processor-specific information, see the `card_acceptor_ref_number` field description in [Level II and Level III Processing Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/Level_2_3_SCMP_API/html) 

        :return: The card_acceptor_reference_number of this Ptsv2paymentsMerchantInformation.
        :rtype: str
        """
        return self._card_acceptor_reference_number

    @card_acceptor_reference_number.setter
    def card_acceptor_reference_number(self, card_acceptor_reference_number):
        """
        Sets the card_acceptor_reference_number of this Ptsv2paymentsMerchantInformation.
        Reference number that facilitates card acceptor/corporation communication and record keeping.  For processor-specific information, see the `card_acceptor_ref_number` field description in [Level II and Level III Processing Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/Level_2_3_SCMP_API/html) 

        :param card_acceptor_reference_number: The card_acceptor_reference_number of this Ptsv2paymentsMerchantInformation.
        :type: str
        """

        self._card_acceptor_reference_number = card_acceptor_reference_number

    @property
    def transaction_local_date_time(self):
        """
        Gets the transaction_local_date_time of this Ptsv2paymentsMerchantInformation.
        Date and time at your physical location.  Format: `YYYYMMDDhhmmss`, where:  - `YYYY` = year  - `MM` = month  - `DD` = day  - `hh` = hour  - `mm` = minutes  - `ss` = seconds  #### Used by **Authorization** Required for these processors: - American Express Direct                                                                                                                                                                                                                                                                                                                         - American Express Direct - Credit Mutuel-CIC - FDC Nashville Global - SIX  Optional for all other processors. 

        :return: The transaction_local_date_time of this Ptsv2paymentsMerchantInformation.
        :rtype: str
        """
        return self._transaction_local_date_time

    @transaction_local_date_time.setter
    def transaction_local_date_time(self, transaction_local_date_time):
        """
        Sets the transaction_local_date_time of this Ptsv2paymentsMerchantInformation.
        Date and time at your physical location.  Format: `YYYYMMDDhhmmss`, where:  - `YYYY` = year  - `MM` = month  - `DD` = day  - `hh` = hour  - `mm` = minutes  - `ss` = seconds  #### Used by **Authorization** Required for these processors: - American Express Direct                                                                                                                                                                                                                                                                                                                         - American Express Direct - Credit Mutuel-CIC - FDC Nashville Global - SIX  Optional for all other processors. 

        :param transaction_local_date_time: The transaction_local_date_time of this Ptsv2paymentsMerchantInformation.
        :type: str
        """

        self._transaction_local_date_time = transaction_local_date_time

    @property
    def service_fee_descriptor(self):
        """
        Gets the service_fee_descriptor of this Ptsv2paymentsMerchantInformation.

        :return: The service_fee_descriptor of this Ptsv2paymentsMerchantInformation.
        :rtype: Ptsv2paymentsMerchantInformationServiceFeeDescriptor
        """
        return self._service_fee_descriptor

    @service_fee_descriptor.setter
    def service_fee_descriptor(self, service_fee_descriptor):
        """
        Sets the service_fee_descriptor of this Ptsv2paymentsMerchantInformation.

        :param service_fee_descriptor: The service_fee_descriptor of this Ptsv2paymentsMerchantInformation.
        :type: Ptsv2paymentsMerchantInformationServiceFeeDescriptor
        """

        self._service_fee_descriptor = service_fee_descriptor

    @property
    def merchant_name(self):
        """
        Gets the merchant_name of this Ptsv2paymentsMerchantInformation.
        Use this field only if you are requesting payment with Payer Authentication serice together.  Your company’s name as you want it to appear to the customer in the issuing bank’s authentication form. This value overrides the value specified by your merchant bank. 

        :return: The merchant_name of this Ptsv2paymentsMerchantInformation.
        :rtype: str
        """
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, merchant_name):
        """
        Sets the merchant_name of this Ptsv2paymentsMerchantInformation.
        Use this field only if you are requesting payment with Payer Authentication serice together.  Your company’s name as you want it to appear to the customer in the issuing bank’s authentication form. This value overrides the value specified by your merchant bank. 

        :param merchant_name: The merchant_name of this Ptsv2paymentsMerchantInformation.
        :type: str
        """

        self._merchant_name = merchant_name

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
        if not isinstance(other, Ptsv2paymentsMerchantInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
