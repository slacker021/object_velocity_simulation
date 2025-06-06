class PhysicalObject:
    """This class is meant to represent
    a physical object that is falling. """

    def __init__(self, acceleration: float or None, time: float or None,
                 velocity: float or None, height: float or None) -> None:
        """For creating instances of the object. """

        """For initializing private fields of the 
        object that serve as attributes"""
        self.acceleration = acceleration
        self.time = time
        self.velocity = velocity
        self.height = height

        self.type_error_message: str = "One or more of the values used is not a valid number"

    def compute_velocity(self, acceleration: float, time: float,
                         use_attribute: bool, set_velocity_to_object: bool) -> float or None:
        """For computing the velocity of the object using provided
        parameters, in the form of acceleration and time."""

        try:

            computed_results = None

            if use_attribute is True:
                self.velocity = self.acceleration * self.time
                computed_results = self.velocity

                if set_velocity_to_object is True:
                    self.velocity = computed_results

            elif use_attribute is False:
                computed_results = acceleration * time

                if set_velocity_to_object is True:
                    self.velocity = computed_results

            return computed_results

        except TypeError:

            print(self.type_error_message)
            return None

    def compute_height(self, acceleration: float, time: float,
                       use_attribute: bool, set_to_attribute: bool):
        """For computing the height of the object using provided
        parameters, in the form of acceleration and time."""

        try:

            computed_result = None

            if use_attribute is True:
                self.height = (self.acceleration * (self.time ** 2)) / 2
                computed_result = self.height

            elif use_attribute is False:
                computed_result = (acceleration * (time **2)) / 2

                if set_to_attribute is True:
                    self.height = computed_result

        except TypeError:
            print(self.type_error_message)

    def compute_time(self, height: float, acceleration: float,
                     use_attribute: bool, set_to_attribute: bool):
        """For computing the time of the object using provided
        parameters, in the form of height and acceleration."""

        try:

            computed_result = None

            if use_attribute is True:
                self.time = ((2 * self.height) / self.acceleration) ** 0.5
                computed_result = self.time

                if set_to_attribute is True:
                    self.time = computed_result

            elif use_attribute is False:
                computed_result = ((2 * height) / acceleration) ** 0.5

                if set_to_attribute is True:
                    self.time = computed_result

            return computed_result

        except TypeError:
            print(self.type_error_message)
            return None

        except ZeroDivisionError:
            print("Error: Acceleration cannot be zero")
            return None
