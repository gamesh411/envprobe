from . import EnvVar, register_type


class NumericEnvVar(EnvVar):
    """
    Environmental variable which holds a numeric value. This type can be used
    to wrap casting to integer or float all the time in Python code.
    """

    def __init__(self, name, env_string):
        super().__init__(name, env_string)
        self.value = env_string

    @property
    def value(self):
        """
        Get the current value of the numeric environment variable.

        :returns: Either a :type:`int` or a :type:`float`, the current value.
        """
        return self._value

    @value.setter
    def value(self, new_value):
        """
        Set the value of the environment variable to the given new value.
        """

        try:
            self._value = float(new_value)
            self._kind = float
        except ValueError:
            # If ValueError is raised, the value is not a float. Raise this
            # error and refuse loading.
            raise

        if self._value.is_integer():
            self._value = int(self._value)
            self._kind = int

    @property
    def is_integer(self):
        return self._kind == int

    def to_raw_var(self):
        return str(self.value)


register_type('number', NumericEnvVar)
