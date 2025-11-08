class ClassRoom:
    """Represents a classroom with an ID, name, capacity, location, and creation timestamp."""


# Initializes an object with attributes for id, name, capacity, location, and creation date.
# - id: Unique identifier for the object (default: None).
# - name: Name of the classroom (default: empty string).
# - capacity: Maximum number of students (default: 30).
# - location: Location or address (default: empty string).
# - created_at: Timestamp of creation (default: None).
    def __init__(self, id=None, name="", capacity=30, location="", created_at=None):
        self._id = id
        self._name = name
        self._capacity = capacity
        self._location = location
        self._created_at = created_at


# Property getter for the private _id attribute.
# Allows read-only access to the object's unique identifier.
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



# Property getter for the private _name attribute.
# Allows read-only access to the name of the object.
    @property
    def name(self):
        return self._name


# Property setter for the private _name attribute.
# - Validates that the value is not empty or whitespace.
# - Raises a ValueError if the validation fails.
    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Name cannot be empty or whitespace.")
        self._name = value



# Property getter for the private _capacity attribute.
# Allows read-only access to the capacity of the object.
    @property
    def capacity(self):
        return self._capacity



# Property setter for the private _capacity attribute.
# - Validates that the value is a non-negative integer.
# - Raises a ValueError if the validation fails.
    @capacity.setter
    def capacity(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Capacity must be a non-negative integer.")
        self._capacity = value



# Property getter for the private _location attribute.
# Allows read-only access to the location of the object.
    @property
    def location(self):
        return self._location


# Property setter for the private _location attribute.
# - Validates that the value is not empty or whitespace.
# - Raises a ValueError if the validation fails.
    @location.setter
    def location(self, value):
        if not value.strip():
            raise ValueError("Location cannot be empty or whitespace.")
        self._location = value


# Property getter for the private _created_at attribute.
# Allows read-only access to the object's creation timestamp.
    @property
    def created_at(self):
        return self._created_at


# Property setter for the private _created_at attribute.
# - Assigns a new value to the created_at attribute.
# - Assumes validation or conversion is handled elsewhere.
    @created_at.setter
    def created_at(self, value):
        self._created_at = value  # Assume validation/conversion is handled elsewhere
