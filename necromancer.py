from resource_system import ResourceSystem
from summoning_ritual import SummoningRitual


class Necromancer:
    """Coordinates resources, rituals, and controlled undead summons."""

    # Task 1.3: Constant representing the maximum number of controlled undead.
    MAXIMUM_CONTROLLED_UNDEAD = 5

    FIRST_SUMMON_IDENTIFIER = 1

    def __init__(
        self,
        name,
        necrotic_runes=ResourceSystem.MINIMUM_VALID_RESOURCE_QUANTITY,
        spirit_runes=ResourceSystem.MINIMUM_VALID_RESOURCE_QUANTITY,
        bone_runes=ResourceSystem.MINIMUM_VALID_RESOURCE_QUANTITY,
        flesh_runes=ResourceSystem.MINIMUM_VALID_RESOURCE_QUANTITY,
        ectoplasm=ResourceSystem.MINIMUM_VALID_RESOURCE_QUANTITY,
    ):
        # Task 1.1 and 1.2: The Necromancer creates and owns its resources.
        self.__name = name
        self.__resources = ResourceSystem(
            necrotic_runes,
            spirit_runes,
            bone_runes,
            flesh_runes,
            ectoplasm,
        )
        self.__controlled_undead = []
        self.__next_unit_identifier = self.FIRST_SUMMON_IDENTIFIER

    # Task 1.2: Getter methods used by read-only properties.
    def get_name(self):
        return self.__name

    def get_resources(self):
        return self.__resources

    def get_controlled_undead(self):
        return self.__controlled_undead

    def get_next_unit_identifier(self):
        return self.__next_unit_identifier

    name = property(get_name)
    resources = property(get_resources)
    controlled_undead = property(get_controlled_undead)
    next_unit_identifier = property(get_next_unit_identifier)

    def collect_resources(
        self,
        necrotic_runes,
        spirit_runes,
        bone_runes,
        flesh_runes,
        ectoplasm,
    ):
        # Task 1.2: Delegate resource changes to the ResourceSystem object.
        return self.__resources.collect_resources(
            necrotic_runes,
            spirit_runes,
            bone_runes,
            flesh_runes,
            ectoplasm,
        )

    def summon_undead(self, ritual):
        # Task 1.4: Require a SummoningRitual and enough resources.
        if not isinstance(ritual, SummoningRitual):
            return None

        if len(self.__controlled_undead) >= self.MAXIMUM_CONTROLLED_UNDEAD:
            return None

        if not ritual.can_perform(self.__resources):
            return None

        if not ritual.consume_required_resources(self.__resources):
            return None

        # The necromancer supplies the identifier, while the ritual decides
        # which specialised Undead subclass to instantiate.
        undead = ritual.create_summon(self.__next_unit_identifier)
        self.__next_unit_identifier += 1
        self.__controlled_undead.append(undead)

        return undead

    def dismiss_undead(self, unit_identifier):
        # Task 1.5 and 1.6: Use the helper to find and remove a summon.
        undead = self.__find_controlled_summon(unit_identifier)

        if undead is None:
            return False

        self.__controlled_undead.remove(undead)
        return True

    def level_controlled_undead(self, unit_identifier):
        # Task 1.7: Find a summon, then delegate levelling to the undead object.
        undead = self.__find_controlled_summon(unit_identifier)

        if undead is None:
            return False

        return undead.level_up()

    def __str__(self):
        controlled_count = len(self.__controlled_undead)

        return (
            f"Necromancer: {self.__name}\n"
            f"Controlled Undead: {controlled_count}/{self.MAXIMUM_CONTROLLED_UNDEAD}\n"
            f"Next Summon ID: {self.__next_unit_identifier}\n"
            f"Resources:\n{self.__resources}"
        )

    def __find_controlled_summon(self, unit_identifier):
        # Task 1.6: Private helper for locating controlled undead by ID.
        for undead in self.__controlled_undead:
            if undead.unit_identifier == unit_identifier:
                return undead

        return None
