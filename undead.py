
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
        """Initialise the summon identity, bounded health and power, and starting level."""
        # Identity details are private because subclasses do not change them.
        # Mutable statistics are protected so inherited behaviour can use them.
        self.__unit_identifier = unit_identifier
        self.__name = name
        self._health = self.__limit_health(health)
        self._power = self.__limit_power(power)
        self._level = self.STARTING_LEVEL

    # Task 3.5: Getter methods used by read-only properties.
    def get_unit_identifier(self):
        """Return the unit identifier."""
        return self.__unit_identifier

    def get_name(self):
        """Return the name."""
        return self.__name

    def get_health(self):
        """Return the health."""
        return self._health

    def get_power(self):
        """Return the power."""
        return self._power

    def get_level(self):
        """Return the level."""
        return self._level

    # Task 3.5: Read-only properties using the property() function.
    unit_identifier = property(get_unit_identifier)
    name = property(get_name)
    health = property(get_health)
    power = property(get_power)
    level = property(get_level)

    def level_up(self):
        """Increase the level and bounded stats; return False at the maximum level."""
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
        """Return the summon identity, level, health, and power as formatted text."""
        # Task 3.7: Display the identifier, name, level, health, and power.
        return (
            f"Undead ID: {self.__unit_identifier}\n"
            f"Name: {self.__name}\n"
            f"Level: {self._level}/{self.MAXIMUM_LEVEL}\n"
            f"Health: {self._health}/{self.MAXIMUM_HEALTH}\n"
            f"Power: {self._power}/{self.MAXIMUM_POWER}"
        )

    def __limit_health(self, health):
        """Clamp integer health to its bounds, using the minimum for non-integers."""
        if type(health) is not int:
            return self.MINIMUM_HEALTH

        if health < self.MINIMUM_HEALTH:
            return self.MINIMUM_HEALTH

        if health > self.MAXIMUM_HEALTH:
            return self.MAXIMUM_HEALTH

        return health

    def __limit_power(self, power):
        """Clamp integer power to its bounds, using the minimum for non-integers."""
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
        """Pass the identity and stats to the next constructor in the MRO."""
        super().__init__(unit_identifier, name, health, power)

    def command(self):
        """Return the next MRO command with a weapon-ready response appended."""
        parent_command = super().command()
        return f"{parent_command} It raises its weapon, ready for battle."

    def combat_style(self):
        """Describe the warrior's direct martial combat."""
        return "Fights in direct martial combat with weapons and physical strength."


class CursedUndead(Undead):
    """Represents an undead creature empowered by a curse."""

    def __init__(self, unit_identifier, name, health, power):
        """Pass the identity and stats to the next constructor in the MRO."""
        super().__init__(unit_identifier, name, health, power)

    def command(self):
        """Return the next MRO command with a cursed-energy response appended."""
        parent_command = super().command()
        return f"{parent_command} Cursed energy gathers around it."

    def combat_style(self):
        """Describe combat powered by curses and supernatural energy."""
        return "Fights with curses and supernatural energy."


class DeathKnight(WarriorUndead, CursedUndead):
    """A powerful cursed warrior combining both undead lineages."""

    SUMMON_NAME = "Death Knight"
    MINIMUM_HEALTH = 10
    MAXIMUM_HEALTH = 250
    MINIMUM_POWER = 5
    MAXIMUM_POWER = 200
    STARTING_HEALTH = 80
    STARTING_POWER = 50
    HEALTH_GAINED_PER_LEVEL = 20
    POWER_GAINED_PER_LEVEL = 20

    def __init__(self, unit_identifier):
        """Initialise a Death Knight with the supplied ID and its specialised starting stats."""
        super().__init__(
            unit_identifier,
            self.SUMMON_NAME,
            self.STARTING_HEALTH,
            self.STARTING_POWER,
        )

    def combat_style(self):
        """Use the next combat style implementation in the MRO."""
        return super().combat_style()

    def compare_combat_styles(self):
        """Select each parent's combat style explicitly for comparison."""
        warrior_style = WarriorUndead.combat_style(self)
        cursed_style = CursedUndead.combat_style(self)
        return (
            f"WarriorUndead (explicit call): {warrior_style}\n"
            f"CursedUndead (explicit call): {cursed_style}"
        )


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
        """Initialise a Skeleton Warrior with the supplied ID and its specialised starting stats."""
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
        """Initialise a Vengeful Ghost with the supplied ID and its specialised starting stats."""
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
        """Initialise a Putrid Zombie with the supplied ID and its specialised starting stats."""
        super().__init__(
            unit_identifier,
            self.SUMMON_NAME,
            self.STARTING_HEALTH,
            self.STARTING_POWER,
        )

    def command(self):
        """Return the inherited command with the zombie movement response appended."""
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
        """Initialise a Phantom Guardian with the supplied ID and its specialised starting stats."""
        super().__init__(
            unit_identifier,
            self.SUMMON_NAME,
            self.STARTING_HEALTH,
            self.STARTING_POWER,
        )
