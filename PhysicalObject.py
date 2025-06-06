class PhysicalObject:
    """This class is meant to represent
    a physical object that is falling. """

    def __init__(self, acceleration: float or None, time: float or None,
                 velocity: float or None, height: float or None) -> None:
        """For creating instances of the object. """

        """For initializing private fields of the 
        object that serve as attributes"""
        self.acceleration: float or None = acceleration
        self.time: float or None = time
        self.velocity: float or None = velocity
        self.height: float or None = height

        self.type_error_message: str = "Error: One or more of the values used is not a valid number"

    def compute_velocity(self, acceleration: float or None, time: float or None,
                         use_attribute: bool, set_velocity_to_object: bool) -> float or None:
        """For computing the velocity of the object using provided
        parameters, in the form of acceleration and time."""

        try:
            """Attempt to compute the velocity of the object"""

            computed_results: None = None # initialize the variable to be returned as null

            if use_attribute is True:
                """For checking if the values to be used
                in the computation are attribute values of
                the object itself. If not, non-attribute values
                can be used if the attribute values are null. """
                velocity: float = self.acceleration * self.time # compute velocity using attribute values
                computed_results: float = velocity # store the velocity as the computed result

                if set_velocity_to_object is True: # will only work if it should be stored as attribute
                    """For checking if the computed results should be stored
                     as the velocity of the object. If so, the object's velocity 
                     will be set to the computed results. (as an attribute)"""
                    self.velocity: float = computed_results # store in object's private field for velocity

            elif use_attribute is False: # will only work if non-attribute values are to be used in computing
                """For checking if the computed results should be
                calculated using non-attribute values"""
                computed_results: float = acceleration * time # stored as computed result

                if set_velocity_to_object is True: # will only work if it should be stored as attribute
                    """Checks if the computed result is to be stored
                    in the private field of the object. """
                    self.velocity: float = computed_results # store computed results in object attribute

            return computed_results # return the value of the velocity computed

        except TypeError: # if a non-number is used in computing

            print(self.type_error_message) # print error message found in the __init__ method
            return None

    def compute_height(self, acceleration: float or None, time: float or None,
                       use_attribute: bool, set_to_attribute: bool) -> float or None:
        """For computing the height of the object using provided
        parameters, in the form of acceleration and time."""

        try:
            """Attempt to compute the height of the object"""

            computed_result: None = None # initialize as the variable to be returned

            if use_attribute is True: # will run if attributes are to be used in calculating
                """For checking if the values to be used
                in the computation are attribute values of
                the object itself. If not, non-attribute values
                can be used if the attribute values are null. """
                computed_result: float = (self.acceleration * (self.time ** 2)) / 2 # store as computed result

            elif use_attribute is False:
                """For checking if the computed results should be calculated using non-attribute values"""
                computed_result: float = (acceleration * (time **2)) / 2 # store as computed result

                if set_to_attribute is True: # check if computed result should be stored as object's height
                    self.height: float = computed_result # store as object height

            return computed_result

        except TypeError:
            print(self.type_error_message)
            return None

    def compute_time(self, height: float or None, acceleration: float or None,
                     use_attribute: bool, set_to_attribute: bool) -> float or None:
        """For computing the time of the object using provided
        parameters, in the form of height and acceleration."""

        try: # attempt to get time

            computed_result = None # initialize as result to be returned

            if use_attribute is True:
                """For checking if the values to be used
                in the computation are attribute values of
                the object itself. If not, non-attribute values
                can be used if the attribute values are null. """
                computed_result = ((2 * self.height) / self.acceleration) ** 0.5 # store as computed result

                if set_to_attribute is True:
                    """Checks if the computed result is to be stored in the private field of the object. """
                    self.time = computed_result # store as object time

            elif use_attribute is False:
                """Checks if the values to be used in the computation
                are not attribute values of the object."""
                computed_result = ((2 * height) / acceleration) ** 0.5 # store as computed results

                if set_to_attribute is True: # checks if computed result is to be stored as the object's time
                    self.time = computed_result # store as object time

            return computed_result

        except TypeError: # if a non-number is used in computing
            print(self.type_error_message) # display error message found in the __init__ method
            return None

        except ZeroDivisionError: # if the acceleration is zero
            print("Error: Acceleration cannot be zero")
            return None
