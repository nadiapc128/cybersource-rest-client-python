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


class PtsV2PaymentsPost201ResponsePaymentInformationAccountFeaturesBalances(object):
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
        'account_type': 'str',
        'amount': 'str',
        'amount_type': 'str',
        'currency': 'str'
    }

    attribute_map = {
        'account_type': 'accountType',
        'amount': 'amount',
        'amount_type': 'amountType',
        'currency': 'currency'
    }

    def __init__(self, account_type=None, amount=None, amount_type=None, currency=None):
        """
        PtsV2PaymentsPost201ResponsePaymentInformationAccountFeaturesBalances - a model defined in Swagger
        """

        self._account_type = None
        self._amount = None
        self._amount_type = None
        self._currency = None

        if account_type is not None:
          self.account_type = account_type
        if amount is not None:
          self.amount = amount
        if amount_type is not None:
          self.amount_type = amount_type
        if currency is not None:
          self.currency = currency

    @property
    def account_type(self):
        """
        Gets the account_type of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeaturesBalances.
        Type of account.  This value is returned only if you request a balance inquiry.  Possible values:   - `00`: Not applicable or not specified  - `10`: Savings account  - `20`: Checking account  - `30`: Credit card account  - `40`: Universal account  Balance Account Types returned on EBT Debit card transactions:   - `96`: Cash Benefits Account (PIN Debit Gateway EBT only)  - `98`: Food Stamp Account (PIN Debit Gateway EBT only) 

        :return: The account_type of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeaturesBalances.
        :rtype: str
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        """
        Sets the account_type of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeaturesBalances.
        Type of account.  This value is returned only if you request a balance inquiry.  Possible values:   - `00`: Not applicable or not specified  - `10`: Savings account  - `20`: Checking account  - `30`: Credit card account  - `40`: Universal account  Balance Account Types returned on EBT Debit card transactions:   - `96`: Cash Benefits Account (PIN Debit Gateway EBT only)  - `98`: Food Stamp Account (PIN Debit Gateway EBT only) 

        :param account_type: The account_type of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeaturesBalances.
        :type: str
        """

        self._account_type = account_type

    @property
    def amount(self):
        """
        Gets the amount of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeaturesBalances.
        Remaining balance on the account. If the processor returns the sign, positive or negative, this sign is prefixed to the amount value as (+/-). 

        :return: The amount of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeaturesBalances.
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """
        Sets the amount of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeaturesBalances.
        Remaining balance on the account. If the processor returns the sign, positive or negative, this sign is prefixed to the amount value as (+/-). 

        :param amount: The amount of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeaturesBalances.
        :type: str
        """

        self._amount = amount

    @property
    def amount_type(self):
        """
        Gets the amount_type of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeaturesBalances.
        Type of amount. This value is returned only if you request a balance inquiry. The issuer determines the value that is returned.  Possible values for deposit accounts:   - `01`: Current ledger (posted) balance.  - `02`: Current available balance, which is typically the ledger balance minus outstanding authorizations. Some  depository institutions also include pending deposits and the credit or overdraft line associated with the account.  Possible values for credit card accounts:   - `01`: Credit amount remaining for customer (open to buy).  - `02`: Credit limit. 

        :return: The amount_type of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeaturesBalances.
        :rtype: str
        """
        return self._amount_type

    @amount_type.setter
    def amount_type(self, amount_type):
        """
        Sets the amount_type of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeaturesBalances.
        Type of amount. This value is returned only if you request a balance inquiry. The issuer determines the value that is returned.  Possible values for deposit accounts:   - `01`: Current ledger (posted) balance.  - `02`: Current available balance, which is typically the ledger balance minus outstanding authorizations. Some  depository institutions also include pending deposits and the credit or overdraft line associated with the account.  Possible values for credit card accounts:   - `01`: Credit amount remaining for customer (open to buy).  - `02`: Credit limit. 

        :param amount_type: The amount_type of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeaturesBalances.
        :type: str
        """

        self._amount_type = amount_type

    @property
    def currency(self):
        """
        Gets the currency of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeaturesBalances.
        Currency of the remaining balance on the account. 

        :return: The currency of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeaturesBalances.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """
        Sets the currency of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeaturesBalances.
        Currency of the remaining balance on the account. 

        :param currency: The currency of this PtsV2PaymentsPost201ResponsePaymentInformationAccountFeaturesBalances.
        :type: str
        """

        self._currency = currency

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
        if not isinstance(other, PtsV2PaymentsPost201ResponsePaymentInformationAccountFeaturesBalances):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
