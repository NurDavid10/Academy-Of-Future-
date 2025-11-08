# Represents a payment entry with details including ID, parent ID, amount, payment date, and description.
# - Initializes the payment object with an optional ID, parent ID, amount, payment date, and description.
# - Default values are provided for attributes like amount (0.0) and description (empty string).
# - Encapsulates payment information for processing and storage.
class Payment:
    """Represents a payment entry with an ID, parent ID, amount, payment date, and description."""

    def __init__(self, id=None, parent_id=None, amount=0.0, payment_date=None, description=""):
        self._id = id
        self._parent_id = parent_id
        self._amount = amount
        self._payment_date = payment_date
        self._description = description



# Property getter for the private _id attribute.
# Allows read-only access to the unique identifier of the payment entry.
    @property
    def id(self):
        return self._id



# Property setter for the private _id attribute.
# - Validates that the value is an integer or None.
# - Raises a ValueError if the validation fails.
    @id.setter
    def id(self, value):
        if value is not None and not isinstance(value, int):
            raise ValueError("ID must be an integer or None.")
        self._id = value



# Property getter for the private _parent_id attribute.
# Allows read-only access to the parent ID associated with the payment.
    @property
    def parent_id(self):
        return self._parent_id



# Property setter for the private _parent_id attribute.
# - Validates that the value is an integer or None.
# - Raises a ValueError if the validation fails.
    @parent_id.setter
    def parent_id(self, value):
        if value is not None and not isinstance(value, int):
            raise ValueError("Parent ID must be an integer or None.")
        self._parent_id = value



# Property getter for the private _amount attribute.
# Allows read-only access to the amount of the payment.
    @property
    def amount(self):
        return self._amount



# Property setter for the private _amount attribute.
# - Validates that the value is a non-negative number (either int or float).
# - Raises a ValueError if the validation fails.
    @amount.setter
    def amount(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Amount must be a non-negative number.")
        self._amount = value



# Property getter for the private _payment_date attribute.
# Allows read-only access to the date of the payment.
    @property
    def payment_date(self):
        return self._payment_date



# Property setter for the private _payment_date attribute.
# - Validates that the value is a string in the format 'YYYY-MM-DD' or None.
# - Raises a ValueError if the validation fails.
    @payment_date.setter
    def payment_date(self, value):
        if value is not None and not isinstance(value, str):
            raise ValueError("Payment date must be a string in the format 'YYYY-MM-DD' or None.")
        self._payment_date = value



# Property getter for the private _description attribute.
# Allows read-only access to the description of the payment.
    @property
    def description(self):
        return self._description



# Property setter for the private _description attribute.
# - Strips leading and trailing spaces from the description value if provided.
# - Sets the description to an empty string if the value is None or empty.
    @description.setter
    def description(self, value):
        self._description = value.strip() if value else ""
