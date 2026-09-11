
class Undead:
    """Represents an undead creature summoned by the necromancer."""

    # Task 3.3: Constants defining the current stat boundaries.
    MINIMUM_HEALTH = 1
    MAXIMUM_HEALTH = 100
    MINIMUM_POWER = 1
    MAXIMUM_POWER = 100
    MAXIMUM_LEVEL = 10

    # Task 3.4: Constants defining stat growth when levelling.
    HEALTH_GAINED_PER_LEVEL = 10
    POWER_GAINED_PER_LEVEL = 10

    # Task 3.2: Every undead creature begins at Level 1.
    STARTING_LEVEL = 1

    def __init__(self, unit_identifier, name, health, power):
        # Identity details are private because subclasses do not change them.
        # Mutable statistics are protected so inherited behaviour can use them.
        self.__unit_identifier = unit_identifier
        self.__name = name
        self._health = self.__limit_health(health)
        self._power = self.__limit_power(power)
        self._level = self.STARTING_LEVEL

    # Task 3.5: Getter methods used by read-only properties.
    def get_unit_identifier(self):
        return self.__unit_identifier

    def get_name(self):
        return self.__name

    def get_health(self):
        return self._health

    def get_power(self):
        return self._power

    def get_level(self):
        return self._level

    # Task 3.5: Read-only properties using the property() function.
    unit_identifier = property(get_unit_identifier)
    name = property(get_name)
    health = property(get_health)
    power = property(get_power)
    level = property(get_level)

    def level_up(self):
        # Task 3.6: Prevent the undead from exceeding the maximum level.
        if self._level >= self.MAXIMUM_LEVEL:
            return False

        # Task 3.6: Increase level, health, and power.
        self._level += 1
        self._health += self.HEALTH_GAINED_PER_LEVEL
        self._power += self.POWER_GAINED_PER_LEVEL

        # Task 3.6: Prevent health and power from exceeding maximum values.
        self._health = self.__limit_health(self._health)
        self._power = self.__limit_power(self._power)

        return True

    def command(self):
        """Return behaviour shared by every undead summon."""
        return f"{self.__name} awaits its necromancer's command."

    def __str__(self):
        # Task 3.7: Display the identifier, name, level, health, and power.
        return (
            f"Undead ID: {self.__unit_identifier}\n"
            f"Name: {self.__name}\n"
            f"Level: {self._level}/{self.MAXIMUM_LEVEL}\n"
            f"Health: {self._health}/{self.MAXIMUM_HEALTH}\n"
            f"Power: {self._power}/{self.MAXIMUM_POWER}"
        )

    def __limit_health(self, health):
        if type(health) is not int:
            return self.MINIMUM_HEALTH

        if health < self.MINIMUM_HEALTH:
            return self.MINIMUM_HEALTH

        if health > self.MAXIMUM_HEALTH:
            return self.MAXIMUM_HEALTH

        return health

    def __limit_power(self, power):
        if type(power) is not int:
            return self.MINIMUM_POWER

        if power < self.MINIMUM_POWER:
            return self.MINIMUM_POWER

        if power > self.MAXIMUM_POWER:
            return self.MAXIMUM_POWER

        return power


class WarriorUndead(Undead):
    """Represents an undead creature specialised for battle."""

    def __init__(self, unit_identifier, name, health, power):
        super().__init__(unit_identifier, name, health, power)

    def command(self):
        parent_command = super().command()
        return f"{parent_command} It raises its weapon, ready for battle."


class CursedUndead(Undead):
    """Represents an undead creature empowered by a curse."""

    def __init__(self, unit_identifier, name, health, power):
        super().__init__(unit_identifier, name, health, power)

    def command(self):
        parent_command = super().command()
        return f"{parent_command} Cursed energy gathers around it."


class SkeletonWarrior(WarriorUndead):
    """A lightly armoured warrior raised from bones."""

    SUMMON_NAME = "Skeleton Warrior"
    MINIMUM_HEALTH = Undead.MINIMUM_HEALTH
    MAXIMUM_HEALTH = Undead.MAXIMUM_HEALTH
    MINIMUM_POWER = Undead.MINIMUM_POWER
    MAXIMUM_POWER = Undead.MAXIMUM_POWER
    STARTING_HEALTH = 30
    STARTING_POWER = 15

    def __init__(self, unit_identifier):
        super().__init__(
            unit_identifier,
            self.SUMMON_NAME,
            self.STARTING_HEALTH,
            self.STARTING_POWER,
        )


class VengefulGhost(CursedUndead):
    """A spirit bound to the world by vengeance."""

    SUMMON_NAME = "Vengeful Ghost"
    MINIMUM_HEALTH = Undead.MINIMUM_HEALTH
    MAXIMUM_HEALTH = Undead.MAXIMUM_HEALTH
    MINIMUM_POWER = Undead.MINIMUM_POWER
    MAXIMUM_POWER = Undead.MAXIMUM_POWER
    STARTING_HEALTH = 20
    STARTING_POWER = 30

    def __init__(self, unit_identifier):
        super().__init__(
            unit_identifier,
            self.SUMMON_NAME,
            self.STARTING_HEALTH,
            self.STARTING_POWER,
        )


class PutridZombie(Undead):
    """A resilient corpse animated by necromancy."""

    SUMMON_NAME = "Putrid Zombie"
    MINIMUM_HEALTH = Undead.MINIMUM_HEALTH
    MAXIMUM_HEALTH = Undead.MAXIMUM_HEALTH
    MINIMUM_POWER = Undead.MINIMUM_POWER
    MAXIMUM_POWER = Undead.MAXIMUM_POWER
    STARTING_HEALTH = 45
    STARTING_POWER = 10

    def __init__(self, unit_identifier):
        super().__init__(
            unit_identifier,
            self.SUMMON_NAME,
            self.STARTING_HEALTH,
            self.STARTING_POWER,
        )

    def command(self):
        parent_command = super().command()
        return f"{parent_command} It shambles forward relentlessly."


class PhantomGuardian(WarriorUndead):
    """A powerful spectral warrior summoned to guard its master."""

    SUMMON_NAME = "Phantom Guardian"
    MINIMUM_HEALTH = Undead.MINIMUM_HEALTH
    MAXIMUM_HEALTH = Undead.MAXIMUM_HEALTH
    MINIMUM_POWER = Undead.MINIMUM_POWER
    MAXIMUM_POWER = Undead.MAXIMUM_POWER
    STARTING_HEALTH = 60
    STARTING_POWER = 35

    def __init__(self, unit_identifier):
        super().__init__(
            unit_identifier,
            self.SUMMON_NAME,
            self.STARTING_HEALTH,
            self.STARTING_POWER,
        )
