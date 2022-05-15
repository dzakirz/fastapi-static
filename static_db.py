from typing import List
from uuid import UUID

from models import Gender, Role, User

class Database:
  static :List[User] = [
    User(
      id = UUID("07427c4b-879e-45af-97bd-87398130cf09"),
      first_name = "Dzaki",
      last_name = "Rozaan",
      gender = Gender.male,
      roles = [Role.student,Role.admin]
    ),
    User(
      id = UUID("84a76d08-0d50-447c-92ca-6b033daf2c45"),
      first_name = "Nathan",
      middle_name = "Anandala",
      last_name = "Panjaitan",
      gender = Gender.male,
      roles = [Role.student]
    )
]