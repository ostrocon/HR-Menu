import abc
from enum import Enum
import datetime

class Role(Enum):
    """
    Jack Bellgowan and Connor Ostrowski
    Custom Enumeration class for different roles of employees

    Inhertirs from Enum class

    Enumeration holding variables associating to manager types 1-3 where the ceo has the value
    of 1 and CFO has the value of 2 and CIO has the value of 3
    """
    CEO = 1
    CFO = 2
    CIO = 3

class Department(Enum):
    """
    Jack Bellgowan and Connor Ostrowski
    Custom Emunertaion class for different Departments

    Inherits from Enum class

    Enumeration holding variables associating to department types 1-5 where the department for accounting
    has the value of 1, the Finance has a value of 2, the HR department a value of 3, the R and
    D department has a value of 4, and Machining has a value of 5
    """
    ACCOUNTING = 1
    FINANCE = 2
    HR = 3
    R_AND_D = 4
    MACHINING = 5

class InvalidRoleException(Exception):
    """
    Jack Bellgowan and Connor Ostrowski
    Custom exception type raised when invalid role is given
    Inherits from Exception class
    """
    def __init__(self, message: str):
        """
        Constructor for the InvalidRoleException and has message as a str parameter,
        raises an exception called InvalidRoleException with the message var as a message
        """
        super().__init__(message)

class InvalidDepartmentException(Exception):
    """
    Jack Bellgowan and Connor Ostrowski
    Custom exception type raised when invalid department is given
    Inherits from Exception class
    """
    def __init__(self, message: str):
        """
        Constructor for the InvalidDepartmentException and has message as a str parameter,
        raises an exception called InvalidDepartment Exception with the message var as a message
        """
        super().__init__(message)

class Employee(abc.ABC):
    """
    Jack Bellgowan and Connor Ostrowski
    Abstract Basic class holding info about an object of parent type employee

    Attributes:
        name (str): the name of the employee
        email (str): the email each employee has

    the abstract base class has a static variables CURRENT_ID and IMAGE_PLACEHOLDER
    """
    CURRENT_ID: int = 1
    IMAGE_PLACEHOLDER: str = "./images/placeholder.png"
    def __init__(self, name: str, email: str):
        """
        Jack Bellgowan and Connor Ostrowski
        Constructor for the Employee abstract class

        Each employee will have a name, email, id_number, and image to identify them
        """
        self.name: str = name
        self.email: str = email
        self._id_number: int = Employee.CURRENT_ID
        self.image: str = Employee.IMAGE_PLACEHOLDER
        # adds to CURRENT_ID so next employee has unique ID
        Employee.CURRENT_ID += 1

    @property
    def email(self) -> str:
        """
        Jack Bellgowan and Connor Ostrowski
        getter for self._email

        Returns:
            self._email (str): the email of the individual employee
        """
        return self._email

    @email.setter
    def email(self, email: str) -> None:
        """
        Jack Bellgowan and Connor Ostrowski
        setter for the email of the employee

        Parameters:
            email (str): the email of the individual employee

        Raises:
            ValueError: of the email is not a str or does no contain @acme-machining.com
            in the str
        """
        # Checks content of email
        if not isinstance(email, str) or not email or "@acme-machining.com" not in email:
            raise ValueError("Invalid email")
        # sets email
        self._email: str = email

    @property
    def name(self) -> str:
        """
        Jack Bellgowan and Connor Ostrowski
        getter for self._name

        Returns:
            self._name (str): the name of the individual employee
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Jack Bellgowan and Connor Ostrowski
        setter for the self._name

        Parameters:
            name (str): the name of the individal employee

        Raises:
            ValueError: if the name paramters if blank or is not a string then a error
            will be raised
        """
        # Checks content of name
        if not name or not isinstance(name,str):
            raise ValueError("Invalid name")
        # sets name
        self._name: str = name

    @property
    def image(self) -> str:
        """
        Jack Bellgowan and Connor Ostrowski
        getter for self._image

        Returns:
            self._image (str): the image associated with the individual employee
        """
        return self._image

    @image.setter
    def image(self, image: str) -> None:
        """
        Jack Bellgowan and Connor Ostrowski
        Setter for self._image, checks if image is empty.

        Parameter:
            image (str): the image associated with the individual employee

        Raises:
            ValueError: if the image assocaitated with the employee is black or does not
            have str for a path of the image
        """
        # Checks content of image
        if not image or not isinstance(image,str):
            raise ValueError("Invalid image")
        # sets image
        self._image: str = image

    @property
    def id_number(self) -> int:
        """
        Jack Bellgowan and Connor Ostrowski
        getter for self._id_number

        Returns:
            self._id_number (int): the individual id number of the employee
        """
        return self._id_number

    def __str__(self) -> str:
        """
        Jack Bellgowan and Connor Ostrowski
        returns basic text representation of an object of type
        Employee as type str.

        Returns:
            self._id_number:self.name for the
        """
        return f"{self._id_number}:{self.name}"

    @abc.abstractmethod
    def calc_pay(self) -> float:
        """
        Jack Bellgowan and Connor Ostrowski
        This function calculates the weekly pay for the current employee in our pay report
        """
        pass

    def __repr__(self) -> str:
        """
        Jack Bellgowan and Connor Ostrowski
        returns complex text representation of an object of type
        Employee as type str.

        Returns:
            self.name,self.email,self.IMAGE_PLACEHOLDER
        """
        return f"{self.name},{self.email},{self.IMAGE_PLACEHOLDER}"

class Salaried(Employee):
    """
    Jack Bellgowan and Connor Ostrowski
    Class holding info for all objects of type Salaried and inherits from Employee class

    Attributes:
        name (str): the name of the employee
        email (str): the email each empoyee has
        yearly (float): the amount of money the salaried employee earns per year
    """
    def __init__(self, name: str, email: str, yearly: float):
        """
        Jack Bellgowan and Connor Ostrowski
        constructor for the Salaried type objects with the super() to call the employee constructor

        Parameters:
            name (str): the name of the employee
            email (str): the email each empoyee has
            yearly (float): the amount of money the salaried employee earns per year

        """
        super().__init__(name, email)
        self.yearly: float = yearly

    @property
    def yearly(self) -> float:
        """
        Jack Bellgowan and Connor Ostrowski
        getter for self._yearly

        Returns:
            self._yearly (float): the amount the employee earns in a year
        """
        return self._yearly

    @yearly.setter
    def yearly(self, yearly: float) -> None:
        """
        Jack Bellgowan and Connor Ostrowski
        Setter for self._yearly, checks if yearly is non-negative and
        over 50000.

        Parameters:
            yearly (float): the amount the employee earns in a year

        Raises:
            ValueError: if the yearly income is not a float or is less than 50,000 then
            a exception will be raised
        """
        # Checks value of yearly
        if not isinstance(yearly, float) or yearly <= 50000:
            raise ValueError("Invalid yearly salary")
        # sets yearly
        self._yearly: float = yearly

    def calc_pay(self) -> float:
        """
        Jack Bellgowan and Connor Ostrowski
        This function calculates the weekly pay for the current salaried employee in our pay report

        Returns:
            self.yearly (float): self.yaerly is divided by 52
        """
        return self.yearly / 52

    def __repr__(self) -> str:
        """
        Jack Bellgowan and Connor Ostrowski
        returns complex text representation of an object of type
        Salaried as type str.

        Returns:
            self.name,self.email,self.IMAGE_PLACEHOLDER,self.yearly
        """
        return f"{super().__repr__()},{self.yearly}"

class Hourly(Employee):
    """
    Jack Bellgowan and Connor Ostrowski
    Class holding info for all objects of type Hourly and inherits from Employee class

    Attributes:
        name (str): the name of the employee
        email (str): the email each empoyee has
        hourly (float): the amount the employee earns per hour of work
    """
    def __init__(self, name: str, email: str, hourly: float):
        """
        Jack Bellgowan and Connor Ostrowski
        constructor for the Hourly type object

        Parameters:
            name (str): the name of the employee
            email (str): the email each empoyee has
            hourly (float): the amount the employee earns per hour of work
        """
        super().__init__(name, email)
        self.hourly: float = hourly

    @property
    def hourly(self) -> float:
        """
        Jack Bellgowan and Connor Ostrowski
        getter for self._hourly

        Returns:
            self._hourly (float): the amount the employee earns per hour of work
        """
        return self._hourly

    @hourly.setter
    def hourly(self, hourly: float) -> None:
        """
        Jack Bellgowan and Connor Ostrowski
        Setter for self._hourly,

        Raises:
            Value Error: checks if hourly is between 15 and 99.99 or if hourly is not a float type
        """
        # Checks value of hourly
        if not 15 < hourly < 99.99 or not isinstance(hourly, float):
            raise ValueError("Invalid hourly salary")
        # sets hourly
        self._hourly: float = hourly

    def calc_pay(self) -> float:
        """
        Jack Bellgowan and Connor Ostrowski
        This function calculates the weekly pay
        for the current hourly employee in our pay report

        Returns:
            self.hourly (float): the hourly rate time 40 for a standard work week
        """
        return self.hourly * 40

    def __repr__(self) -> str:
        """
        Jack Bellgowan and Connor Ostrowski
        returns complex text representation of an object of type
        Hourly as type str.

        Returns:
            self.name,self.email,self.IMAGE_PLACEHOLDER,self.hourly
        """
        return f"{super().__repr__()},{self.hourly}"

class Executive(Salaried):
    """
    Jack Bellgowan and Connor Ostrowski
    Class holding info for all objects of type Executive.

    Attributes:
        name (str): the name of the employee
        email (str): the email each empoyee has
        yearly (float): the amount the employee earns per year
        role (Role): what enumeration of the employee has
    """
    def __init__(self, name: str, email: str, yearly: float, role: Role):
        """
        Jack Bellgowan and Connor Ostrowski
        Constructor for the Executive type object with the super() from the Employee class

        Parameters:
        name (str): the name of the employee
        email (str): the email each empoyee has
        yearly (float): the amount the employee earns per year
        role (Role): what enumeration of the employee has
        """
        super().__init__(name, email, yearly)
        self.role: Role = role

    @property
    def role(self) -> Role:
        """
        Jack Bellgowan and Connor Ostrowski
        getter for self._yearly

        Returns:
            self._role (Role): the type of the executive has
        """
        return self._role

    @role.setter
    def role(self, role: Role) -> None:
        """
        Jack Bellgowan and Connor Ostrowski
        Setter for self._role,

        Parameters:
            role (Role): the type of role the executve has

        Raises:
            InvalidRoleException: checks if role is not 1-3 or the role is not of type Role
        """
        # Checks value of role
        if not 1 <= role.value <= 3 or not isinstance(role,Role):
            raise InvalidRoleException("Invalid role")
        # sets role
        self._role: Role = role

    def __repr__(self) -> str:
        """
        Jack Bellgowan and Connor Ostrowski
        returns complex text representation of an object of type Executive as type str.

        Returns:
            self.name,self.email,self.IMAGE_PLACEHOLDER,self.role
        """
        return f"Executive,{super().__repr__()},{self.role}"

class Manager(Salaried):
    """
    Jack Bellgowan and Connor Ostrowski
    Class holding info for all objects of type Manager.

    Attributes:
        name (str): the name of the employee
        email (str): the email each empoyee has
        yearly (float): the amount the employee earns per year
        department (Department): what department the manager is
        """
    def __init__(self, name: str, email: str, yearly: float, department: Department):
        """
        Jack Bellgowan and Connor Ostrowski
        Constructor for the Manager type object and inherits from Salaried

        Parameters:
        name (str): the name of the employee
        email (str): the email each empoyee has
        yearly (float): the amount the employee earns per year
        department (Department): what department the manager is
        """
        super().__init__(name, email, yearly)
        self.department: Department = department

    @property
    def department(self) -> Department:
        """
        Jack Bellgowan and Connor Ostrowski
        getter for self._yearly

        Returns:
            self._department (Department): what department the manager is
        """
        return self._department

    @department.setter
    def department(self, department: Department) -> None:
        """
        Jack Bellgowan and Connor Ostrowski
        Setter for self._department

        Parameters:
            department (Department): what department the mangaer is

        Raises:
            InvalidDepartmentException: checks if role is not 1-5 or if the department parameters is not
            a Department type
        """
        # Checks value of department
        if not 1 <= department.value <= 5 or not isinstance(department, Department):
            raise InvalidDepartmentException("Invalid department")
        # sets department
        self._department: Department = department

    def __repr__(self) -> str:
        """
        Jack Bellgowan and Connor Ostrowski
        returns complex text representation of an object of type
        Manager as type str.

        Returns:
            self.name,self.email,self.IMAGE_PLACEHOLDER,self.department
        """
        return f"Manager,{super().__repr__()},{self.department}"

class Permanent(Hourly):
    """
    Jack Bellgowan and Connor Ostrowski
    Class holding info for all objects of type Permanent.

    Attributes:
        name (str): the name of the employee
        email (str): the email each empoyee has
        yearly (float): the amount the employee earns per year
        hired_date: the date time the employee is hired
    """
    def __init__(self, name: str, email: str, hourly: float, hired_date: datetime.date):
        """
        Jack Bellgowan and Connor Ostrowski
        Constructor for the Permanent class and inherits from Hourly

        Parameters:
            name (str): the name of the employee
            email (str): the email each empoyee has
            yearly (float): the amount the employee earns per year
            hired_date (datetime): the date time the employee is hired
        """
        super().__init__(name, email, hourly)
        self.hired_date: datetime.date = hired_date

    @property
    def hired_date(self) -> datetime.date:
        """
        Jack Bellgowan and Connor Ostrowski
        getter for self._hired_date

        Returns:
            self._hired_date: the date time the employee is hired
        """
        return self._hired_date

    @hired_date.setter
    def hired_date(self, hired_date: datetime.date) -> None:
        """
        Jack Bellgowan and Connor Ostrowski
        Setter for self._hired_date

        Parameters:
            hired_date: the date the employee was hired

        Raises:
            ValueError: check that the hired_date parameter is an datetime.date
        """
        # Checks value of hired date
        if not isinstance(hired_date, datetime.date):
            raise ValueError("Invalid hired date")
        # sets hired date
        self._hired_date: datetime.date = hired_date

    def __repr__(self) -> str:
        """
        Jack Bellgowan and Connor Ostrowski
        returns complex text representation of an object of type
        Permanent as type str.

        Returns:
            Permanent,self.name,self.email,self.IMAGE_PLACEHOLDER,self.hired_date
        """
        return f"Permanent,{super().__repr__()},"+self.hired_date.__repr__().replace(",","!")

class Temporary(Hourly):
    """
    Jack Bellgowan and Connor Ostrowski
    Class holding info for all objects of type Temporary.

    Attributes:
        name (str): the name of the employee
        email (str): the email each empoyee has
        hourly (float): the amount the employee earns per hour
        last_date: the date time the employee is hired
    """
    def __init__(self, name: str, email: str, hourly: float, last_day: datetime.date):
        """
        Jack Bellgowan and Connor Ostrowski
        Constructor for the Temporly type object and inherit from Hourly

        Parameters:
            name (str): the name of the employee
            email (str): the email each empoyee has
            hourly (float): the amount the employee earns per hour
            last_date: the date time the employee is hired
        """
        super().__init__(name, email, hourly)
        self.last_day: datetime.date = last_day

    @property
    def last_day(self) -> datetime.date:
        """
        Jack Bellgowan and Connor Ostrowski
        getter for self._hired_date

        Returns:
            self._last_day: the last day the employee works
        """
        return self._last_day

    @last_day.setter
    def last_day(self, last_day: datetime.date) -> None:
        """
        Jack Bellgowan and Connor Ostrowski
        Setter for self._last_day

        Parameters:
            last_day: the last day the employee works

        Raises:
            ValueError: if the last_day is not a datetime.date then the exception will be raised
        """
        # Checks value of last day
        if not isinstance(last_day, datetime.date):
            raise ValueError("Invalid last day")
        # sets last day
        self._last_day: datetime.date = last_day

    def __repr__(self) -> str:
        """
        Jack Bellgowan and Connor Ostrowski
        returns complex text representation of an object of type
        Temporary as type str.

        Returns:
            Temporary,self.name,self.email,self.IMAGE_PLACEHOLDER,self.last_day
        """
        return f"Temporary,{super().__repr__()},"+self.last_day.__repr__().replace(",","!")

if __name__ == "__main__":
    sample_manager = Manager("Julian","julian@acme-machining.com",50001.0,Department.MACHINING)
    print(sample_manager.__repr__())
    sample_executive = Executive("Jim","jim@acme-machining.com",50001.0,Role.CFO)
    print(sample_executive.__repr__())
    sample_temp = Temporary("Randy","randy@acme-machining.com",16.0,datetime.date.today()+datetime.timedelta(days=90))
    print(sample_temp.__repr__())
    sample_permanent = Permanent("Jim Lahey","lahey@acme-machining.com",99.0,datetime.date.today())
    print(sample_permanent.__repr__())