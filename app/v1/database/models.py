class DbCharacter:
    def __init__(
        self,
        titles: str,
        first_name: str,
        last_name: str,
        suffix: str | None,
        dob: str,
        birthplace: str,
        dod: str | None,
        house: str | None,
        organisation: str | None,
        created_at: str,
        updated_at: str,
    ) -> None:
        ...
